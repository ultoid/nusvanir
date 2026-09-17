"""Verify batch preservation, JSON parsing, local links and reference inventory.

Writes only 07_Bestiary/_audit/verification.json and REFERENCES.md.
Existing broken wiki links are reported, never repaired by guesswork.
"""
import collections
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
from bestiary_audit import ROOT, BEST, REPORT, read, digest, inspect


def main():
    errors = []
    old = read(REPORT / 'pre_batch_hashes.json')
    allowed = {p.relative_to(ROOT).as_posix() for p in (BEST / '01_Alam_Liar').glob('*')}
    allowed |= {'07_Bestiary/' + name for name in ['BESTIARY_REWORK_AUDIT.md','BESTIARY_STANDARD_V2.md','CREATURE_TAXONOMY.md','BESTIARY_REWORK_CHANGELOG.md']}
    allowed.add('06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md')
    # Jenggala has its own pre-batch snapshot and strict preservation verifier.
    if (REPORT / 'pre_jenggala_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '02_Jenggala').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_thalantira_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '03_Thalantira').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_avalerion_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '04_Guardians_of_Avalerion_Outpost').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_agnitra_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '05_Dragons_of_Agnitra_Nest').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_arkananta_chiefs_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '06_Chiefs_of_Arkananta').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_sayendra_sentinels_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '07_Sentinels_of_Nusa_Sayendra').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_raksamala_commanders_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '08_Commanders_of_Raksamala_Fortress').glob('*') if p.suffix in ('.md', '.json')}
    if (REPORT / 'pre_rangkaruna_narrative.json').exists():
        allowed |= {p.relative_to(ROOT).as_posix() for p in (BEST / '09_Laut_Rangkaruna').glob('*') if p.suffix in ('.md', '.json')}
    changed = []
    for name, sha in old.items():
        path = ROOT / name
        if not path.exists() or digest(path) != sha:
            changed.append(name)
            if name not in allowed and name != 'tools/bestiary_audit.py':
                errors.append('unexpected pre-existing file change: ' + name)
    parsed = 0
    for p in ROOT.rglob('*.json'):
        if '.git' in p.parts:
            continue
        try:
            read(p)
            parsed += 1
        except (ValueError, UnicodeError) as exc:
            errors.append(f'JSON parse: {p.relative_to(ROOT)}: {exc}')
    snapshot = read(REPORT / 'pre_batch_2026-09-17.json')
    preserved = 0
    for p in (BEST / '01_Alam_Liar').glob('*.json'):
        original = json.loads(snapshot[p.relative_to(ROOT).as_posix()])
        current = read(p)
        for key, value in original.items():
            if key not in ['stat_status','balance_status','source_status'] and current.get(key) != value:
                errors.append(f'legacy field altered: {p.stem}/{key}')
        if original['id'] != current['v2']['identity']['id']:
            errors.append(f'ID changed: {p.stem}')
        preserved += 1
    checked = inspect()
    errors.extend(checked['errors'])
    docs = list(BEST.glob('*.md')) + list((BEST/'01_Alam_Liar').glob('*.md')) + [ROOT/'06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md']
    for p in docs:
        text = p.read_text(encoding='utf-8-sig')
        if '<!-- BESTIARY V2 START -->' in text:
            if text.count('\n## Bestiary V2 — catatan implementasi\n') != 1:
                errors.append('V2 heading must appear exactly once: ' + str(p.relative_to(ROOT)))
            if text.count('<details>') != 1 or text.count('</details>') != 1:
                errors.append('invalid V2 details block: ' + str(p.relative_to(ROOT)))
        if sum(line.startswith('```') for line in text.splitlines()) % 2:
            errors.append('unclosed Markdown code fence: ' + str(p.relative_to(ROOT)))
        for link in re.findall(r'\]\(([^)]+)\)', text):
            link = unquote(link.strip('<>').split('#')[0])
            if link and not re.match(r'[a-z]+://',link) and not (p.parent/link).exists():
                errors.append(f'broken Markdown link: {p.relative_to(ROOT)} -> {link}')
    # Reviewable repository-wide references; exclude our audit copies and tools.
    textfiles = [p for p in ROOT.rglob('*') if p.is_file() and p.suffix in ['.md','.json','.js','.txt','.html','.py','.ps1']
                 and '.git' not in p.parts and '_audit' not in p.parts and 'tools' not in p.parts]
    creatures = [read(p) for p in (BEST/'01_Alam_Liar').glob('*.json')]
    refs = {o['id']: [] for o in creatures}
    for p in textfiles:
        text = p.read_text(encoding='utf-8-sig',errors='replace')
        for obj in creatures:
            if obj['id'] in text or obj['title'] in text:
                refs[obj['id']].append(p.relative_to(ROOT).as_posix())
    report = ['# Referensi Wildlife', '', 'Pencarian repository-wide literal ID/nama; tidak mengganti ID, nama, atau path. Agregat hanya dibaca.', '']
    for key, paths in sorted(refs.items()):
        report += ['## ' + key, ''] + ['- `' + path + '`' for path in paths] + ['']
    (REPORT/'REFERENCES.md').write_text('\n'.join(report),encoding='utf-8')
    result = {'errors':errors,'json_files_parsed':parsed,'legacy_records_preserved':preserved,'changed_pre_existing_files':changed,
              'strict_v2_validation':checked['errors'],'repository_inventory_warnings':len(checked['warnings']),
              'runtime_and_unrelated_files_preserved':not any('unexpected' in e for e in errors),
              'limitations':['No balance simulation or playtest','No general legacy wiki-link resolution',
                             'Aggregate generator unavailable; aggregates preserved, not synchronized',
                             'Runtime snapshot validity is not calibration; known canon and implementation blockers remain']}
    (REPORT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=True))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
