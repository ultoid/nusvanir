"""Read-only Bestiary checks; --write-report refreshes only audit artifacts.

No game database, legacy source, or aggregate is rewritten by this tool.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BEST = ROOT / '07_Bestiary'
GAME = ROOT / '10_Game Project/Tales of The Dark Time'
REPORT = BEST / '_audit'
START = '<!-- BESTIARY V2 START -->'
END = '<!-- BESTIARY V2 END -->'


def read(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def normalized(value):
    return re.sub(r'[^a-z0-9]', '', value.lower())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def render(v):
    """The entire structured V2 record is mirrored, without lossy field mapping."""
    if v.get('presentation', {}).get('markdown_role') == 'lore_only':
        raise ValueError('Lore Markdown is authored directly; game data must stay in JSON.')
    enemy = v['runtime_observation']['enemy']
    overview = ['### Identitas, ekologi, dan encounter', '',
                f'- **ID:** {v["identity"]["id"]}; runtime enemy {enemy["id"]}. **Balance: BLOCKED.**',
                f'- **Habitat sumber:** {v["spawn"]["source_habitat"]}. **Region:** {v["identity"]["region"] or "belum dipastikan"}.',
                f'- **Tipe:** {v["classification"]["creature_type"]}. **Encounter runtime:** {v["classification"]["encounter_type"]}. **Role usulan:** {v["gameplay"]["combat_role"] or "belum ditetapkan"}.',
                '', '**Usulan ekologi / peradaban (belum canon):** ' + v['worldbuilding']['proposal'],
                '', '**Counterplay / batas implementasi:** ' + v['gameplay']['intended_counterplay'],
                '', '### Skill dan reward yang sudah dirujuk', '']
    overview += ['- Skill ' + str(s['id']) + ': ' + s['name'] + (' — efek masih placeholder.' if s['id'] in v['combat']['pending_effect_skill_ids'] else ' — lihat formula/effects runtime pada record.') for s in v['runtime_observation']['skills']]
    for d in v['rewards']['drops']:
        use = '; '.join(f'{u["database"]} {u["id"]}: {u["name"]}' for u in d['uses']) or 'belum ada recipe terhubung'
        overview.append(f'- {d["database"]} {d["id"]}: **{d["name"]}** ({d["rarity"]}) → {use}. Resep tercatat, belum executable.')
        if d['canon_review']:
            overview.append('  Konflik sumber: ' + d['canon_review'])
    overview += ['', '### Gerbang yang belum terpenuhi', '']
    overview += ['- ' + b for b in v['balance']['unresolved_blockers']]
    overview += ['', '### Record lengkap (identik dengan JSON V2)', '', '<details>', '<summary>Data, sumber, observasi runtime dan arsip angka</summary>', '']
    return (START + '\n## Bestiary V2 — catatan implementasi\n\n'
            'Bagian ini adalah sumber pembacaan terkini. Teks sebelum bagian ini '
            'dipertahankan sebagai arsip draf, bukan keputusan canon baru atau bukti kalibrasi. '
            'Angka di `runtime_observation` adalah salinan database, bukan stat yang disetujui. '
            'Usulan desain ditandai `proposal`; null berarti belum ditetapkan.\n\n'
            + '\n'.join(overview) + '\n```json\n' + json.dumps(v, ensure_ascii=False, indent=2) + '\n```\n\n</details>\n' + END)


def inspect():
    db = {n: read(GAME / 'data' / (n + '.json')) for n in
          ['System', 'Enemies', 'Skills', 'States', 'Items', 'Weapons', 'Armors', 'Actors', 'Classes', 'Troops']}
    plugins = json.loads((GAME / 'js/plugins.js').read_text(encoding='utf-8-sig').split('=', 1)[1].strip().rstrip(';'))
    enemies = collections.defaultdict(list)
    for e in db['Enemies']:
        if e and e.get('name'):
            enemies[normalized(e['name'])].append(e)
    characters = collections.defaultdict(list)
    for p in (ROOT / '05_Karakter & Tokoh Penting').rglob('*.md'):
        characters[normalized(p.stem)].append(p.relative_to(ROOT).as_posix())
    entries, errors, warnings = [], [], []
    for p in sorted(BEST.glob('[0-9]*/*.json')):
        try:
            obj = read(p)
        except (ValueError, UnicodeError) as exc:
            errors.append(f'{p.relative_to(ROOT)}: {exc}')
            continue
        md = p.with_suffix('.md')
        text = md.read_text(encoding='utf-8-sig') if md.exists() else ''
        matches = enemies[normalized(obj.get('title', p.stem))]
        findings = []
        if not obj.get('id') or not obj.get('title'):
            findings.append('legacy localized schema: missing explicit id/title; filename used for matching only')
        if not md.exists():
            findings.append('missing Markdown')
        if len(matches) != 1:
            findings.append('runtime match missing/ambiguous')
        if len(matches) == 1:
            enemy = matches[0]
            element = re.search(r'<NUSV Element:\s*(.*?)>', enemy['note'])
            allowed = set(db['System']['elements']) | {'Wind','Lightning','Light'}
            if element and element.group(1) not in allowed:
                findings.append('unmapped runtime element label: ' + element.group(1))
            pending = [str(a['skillId']) for a in enemy['actions'] if valid_id(db['Skills'], a['skillId']) and
                       any(token in db['Skills'][a['skillId']]['note'] for token in ['[CUSTOM SKILL EFFECT]', '[PENDING', '[CUSTOM FORMULA/EFFECT]'])]
            if pending:
                findings.append('pending skill behavior: ' + ','.join(pending))
            for action in enemy['actions']:
                if not valid_id(db['Skills'], action['skillId']):
                    findings.append('unknown runtime skill ID: ' + str(action['skillId']))
            for drop in enemy['dropItems']:
                if drop['kind']:
                    table = {1:'Items',2:'Weapons',3:'Armors'}.get(drop['kind'])
                    if not table or not valid_id(db[table], drop['dataId']):
                        findings.append('unknown runtime drop ID: ' + str(drop['dataId']))
            if re.search(r'<NUSV Enemy Rank:.*(?:Boss|Commander)', enemy['note']) and not re.search(r'phase|fase|telegraph|counterplay', text, re.I):
                findings.append('boss phase/counterplay documentation absent')
            tier = re.search(r'<NUSV Tier:\s*T(\d+)>', enemy['note'])
            if tier and int(tier.group(1)) > 5:
                findings.append('enemy Tier exceeds lore class T5; mapping unresolved')
        if 'VERIFIED' in text or obj.get('stat_status') == 'VERIFIED':
            findings.append('VERIFIED is not a calibration status')
        if len(re.findall(r'\*\*HP:\*\*', text)) > 1:
            findings.append('multiple HP blocks')
        if 'v2' not in obj and obj.get('presentation', {}).get('markdown_role') == 'lore_only':
            if '# ' + obj['title'] + '\n' not in text or obj['presentation']['lore_source'] != md.relative_to(ROOT).as_posix():
                errors.append(f'{p.stem}: narrative pair mismatch')
            if any(token in text for token in ['```json', '**HP:**', '**MP:**']):
                errors.append(f'{p.stem}: game data in lore')
            observation = obj.get('runtime_observation', {})
            if len(matches) != 1 or observation.get('enemy') != matches[0]:
                errors.append(f'{p.stem}: stale runtime observation')
            findings.append('narrative split; lore ' + obj['presentation']['narrative_status'] + '; balance BLOCKED')
        elif 'v2' not in obj:
            findings.append('legacy: no V2 evidence gate')
            for key, label in [('hp', 'HP'), ('mp', 'MP'), ('element', 'Elemen'), ('weakness', 'Kelemahan')]:
                vals = re.findall(r'\*\*' + label + r':\*\*\s*([^\r\n]+)', text)
                if key in obj and vals and str(obj[key]) not in vals:
                    findings.append('Markdown/JSON mismatch: ' + key)
        else:
            v = obj['v2']
            if v.get('presentation', {}).get('markdown_role') == 'lore_only':
                if v['presentation']['lore_source'] != md.relative_to(ROOT).as_posix():
                    errors.append(f'{p.stem}: incorrect lore source')
                if '# ' + obj['title'] + '\n' not in text:
                    errors.append(f'{p.stem}: lore title mismatch')
                if any(token in text for token in [START, '```json', '**HP:**', '**MP:**', 'runtime_observation', 'stat_status']):
                    errors.append(f'{p.stem}: game data leaked into lore Markdown')
            elif START not in text or END not in text or text.split(START, 1)[1].split(END, 1)[0] != render(v).split(START, 1)[1].split(END, 1)[0]:
                errors.append(f'{p.stem}: V2 Markdown/JSON mismatch')
            if v['identity']['id'] != obj['id']:
                errors.append(f'{p.stem}: changed identity')
            if v['balance']['stat_status'] != 'BLOCKED' or any(x is not None for x in v['balance']['stats'].values()):
                errors.append(f'{p.stem}: unsupported calibration')
            for source in v['balance']['source_dependencies']:
                if not (ROOT / source).is_file():
                    errors.append(f'{p.stem}: missing source {source}')
                elif digest(ROOT / source) != v['balance']['source_sha256'].get(source):
                    errors.append(f'{p.stem}: changed dependency {source}')
            for source in v['worldbuilding']['regional_sources']:
                if not (ROOT / source).is_file():
                    errors.append(f'{p.stem}: missing regional source {source}')
            observation = v['runtime_observation']
            if len(matches) != 1 or observation['enemy'] != matches[0]:
                errors.append(f'{p.stem}: stale runtime enemy snapshot')
            for skill in observation['skills']:
                if skill != db['Skills'][skill['id']]:
                    errors.append(f'{p.stem}: stale skill {skill["id"]}')
                eid = skill['damage']['elementId']
                if eid < -1 or eid >= len(db['System']['elements']):
                    errors.append(f'{p.stem}: unknown element ID {eid}')
                for effect in skill['effects']:
                    if effect['code'] in (21, 22) and effect['dataId'] and not valid_id(db['States'], effect['dataId']):
                        errors.append(f'{p.stem}: unknown state {effect["dataId"]}')
            for drop in v['rewards']['drops']:
                if drop['rarity'] not in ['Common','Uncommon','Rare','Epic','Legendary','Mythic']:
                    errors.append(f'{p.stem}: unknown item rarity')
                if not valid_id(db[drop['database']], drop['id']):
                    errors.append(f'{p.stem}: unknown drop {drop["id"]}')
                elif drop['name'] != db[drop['database']][drop['id']]['name']:
                    errors.append(f'{p.stem}: drop name mismatch')
                for use in drop['uses']:
                    if not valid_id(db[use['database']], use['id']):
                        errors.append(f'{p.stem}: unknown recipe output')
            for trait in observation['enemy']['traits']:
                if trait['code'] in (13, 14, 32) and not valid_id(db['States'], trait['dataId']):
                    errors.append(f'{p.stem}: unknown state trait')
            if obj.get('stat_status') != v['balance']['stat_status']:
                errors.append(f'{p.stem}: top-level status mismatch')
            findings.extend('BLOCKED: ' + b for b in v['balance']['unresolved_blockers'] if 'Spirit Dust' in b)
        overlap = characters[normalized(p.stem)]
        if overlap:
            findings.append('character overlap (not automatic duplicate deletion)')
        entries.append({'path': p.relative_to(ROOT).as_posix(), 'id': obj.get('id'),
                        'name': obj.get('title'), 'runtime_ids': [e['id'] for e in matches],
                        'character_sources': overlap, 'findings': findings})
        warnings.extend(f'{p.stem}: {x}' for x in findings)
    for key in ['id', 'name']:
        values = collections.Counter(e[key] for e in entries if e[key] is not None)
        for value, count in values.items():
            if count > 1:
                warnings.append(f'duplicate {key}: {value} ({count})')
    for p in BEST.glob('[0-9]*/*.md'):
        if not p.with_suffix('.json').exists():
            warnings.append(f'orphan Markdown: {p.relative_to(ROOT)}')
    missing_plugins = [x['name'] for x in plugins if x['status'] and not (GAME / 'js/plugins' / (x['name'] + '.js')).exists()]
    warnings.extend('enabled plugin missing: ' + n for n in missing_plugins)
    return {'scope': 'All Bestiary inventory; strict V2 checks only on migrated entries; no calibration simulation',
            'entries': entries, 'errors': errors, 'warnings': warnings,
            'runtime': {'counts': {n: len([x for x in a if x]) for n, a in db.items() if isinstance(a, list)},
                        'elements': db['System']['elements'], 'party_members': db['System']['partyMembers'],
                        'plugins': [x for x in plugins if x['status']],
                        'sha256': {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted((GAME / 'data').glob('*.json'))}}}


def valid_id(array, index):
    return isinstance(index, int) and 0 < index < len(array) and bool(array[index])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-report', action='store_true')
    parser.add_argument('--render-wildlife', action='store_true', help='Render only marked Markdown sections from existing Wildlife JSON V2')
    args = parser.parse_args()
    if args.render_wildlife:
        for p in sorted((BEST / '01_Alam_Liar').glob('*.json')):
            obj = read(p)
            if 'v2' not in obj:
                continue
            if obj['v2'].get('presentation', {}).get('markdown_role') == 'lore_only':
                continue
            md = p.with_suffix('.md')
            text = md.read_text(encoding='utf-8-sig')
            if text.count(START) != 1 or text.count(END) != 1:
                raise ValueError(f'Unsafe Markdown markers: {md}')
            before, marked = text.split(START, 1)
            _, after = marked.split(END, 1)
            md.write_text(before + render(obj['v2']) + after, encoding='utf-8')
    result = inspect()
    if args.write_report:
        REPORT.mkdir(exist_ok=True)
        (REPORT / 'inventory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        rows = ['# Inventaris Bestiary', '', 'Dihasilkan oleh `python tools/bestiary_audit.py --write-report`. Angka runtime bukan bukti kalibrasi.', '',
                '| Entri | ID runtime | Temuan |', '|---|---|---|']
        for e in result['entries']:
            rows.append(f'| {e["path"]} | {", ".join(map(str,e["runtime_ids"]))} | {"; ".join(e["findings"]) or "V2 parity checked; balance BLOCKED"} |')
        rows += ['', '## Batas verifikasi', '', result['scope'], '', '## Kegagalan pemeriksaan V2', '']
        rows += ['- ' + x for x in result['errors']] or ['Tidak ada.']
        (REPORT / 'INVENTORY.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
    print(json.dumps({'entries': len(result['entries']), 'errors': result['errors'], 'legacy_warnings': len(result['warnings'])}, ensure_ascii=True))
    return bool(result['errors'])


if __name__ == '__main__':
    sys.exit(main())
