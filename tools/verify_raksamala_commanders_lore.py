"""Validate Raksamala commanders narrative/data separation and preservation."""
import hashlib
import json
import re
import sys
from urllib.parse import unquote
from bestiary_audit import ROOT, BEST, GAME, REPORT, read, valid_id

FOLDER = BEST/'08_Commanders_of_Raksamala_Fortress'
RACES = {'Asmodea':'Dhemit','Beelzebub':'Bhuta','Belphegor':'Bhuta','Leviathanus':'Bhuta','Luciferus':'Bhuta','Mamon':'Bhuta','Vraka_The_Wrathful':'Bhuta'}

def main():
    errors = []
    snapshot = read(REPORT/'pre_raksamala_commanders_narrative.json')
    hashes = read(REPORT/'pre_raksamala_commanders_hashes.json')
    allowed = {'07_Bestiary/BESTIARY_REWORK_CHANGELOG.md','07_Bestiary/BESTIARY_STANDARD_V2.md',
               '07_Bestiary/BESTIARY_REWORK_AUDIT.md','tools/bestiary_audit.py','tools/verify_bestiary_workspace.py',
               'tools/rework_raksamala_commanders_lore.py','tools/verify_raksamala_commanders_lore.py'}
    allowed |= {'tools/verify_agnitra_lore.py','tools/verify_arkananta_chiefs_lore.py',
                'tools/verify_sayendra_sentinels_lore.py'}
    changed = []
    for name, old_hash in hashes.items():
        p = ROOT/name
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != old_hash:
            changed.append(name)
            approved_scope = name.startswith(('07_Bestiary/05_Dragons_of_Agnitra_Nest/',
                                               '07_Bestiary/06_Chiefs_of_Arkananta/',
                                               '07_Bestiary/07_Sentinels_of_Nusa_Sayendra/',
                                               '07_Bestiary/08_Commanders_of_Raksamala_Fortress/',
                                               '07_Bestiary/09_Laut_Rangkaruna/'))
            if not approved_scope and name not in allowed:
                errors.append('Unexpected change outside batch: '+name)
    db = {n:read(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','States','Items','Weapons','Armors','System']}
    entries, runtime_ids = [], set()
    for p in sorted(FOLDER.glob('*.json')):
        obj = read(p)
        old = json.loads(snapshot[p.relative_to(ROOT).as_posix()])
        for key, value in old.items():
            if key not in ('stat_status','balance_status','source_status') and obj.get(key) != value:
                errors.append(f'{p.stem}: changed legacy field {key}')
        if obj.get('race') != RACES[p.stem]:
            errors.append(f'{p.stem}: incorrect race')
        md = p.with_suffix('.md')
        text = md.read_text(encoding='utf-8')
        for heading in ['## Deskripsi','## Bentuk','## Kepribadian dan Sikap','## Kedudukan dan Benteng','## Kisah']:
            if text.count(heading) != 1:
                errors.append(f'{p.stem}: missing/duplicate {heading}')
        if '# '+obj['title']+'\n' not in text:
            errors.append(f'{p.stem}: title mismatch')
        if any(t in text for t in ['**HP:**','**MP:**','```json','stat_status','runtime_values','**Elemen:**','**Tier:**']):
            errors.append(f'{p.stem}: technical data in lore')
        for href in re.findall(r'\]\(([^)]+)\)',text):
            if not (md.parent/unquote(href)).resolve().is_file():
                errors.append(f'{p.stem}: broken source link {href}')
        for source in obj['lore_review']['sources']:
            if not (ROOT/source).is_file():
                errors.append(f'{p.stem}: missing source {source}')
        presentation = obj['presentation']
        if presentation['lore_source'] != md.relative_to(ROOT).as_posix() or presentation['game_data_source'] != p.relative_to(ROOT).as_posix():
            errors.append(f'{p.stem}: pair references mismatch')
        approval_path = REPORT/'raksamala_commanders_lore_approval.json'
        if approval_path.exists():
            record = read(approval_path)
            expected = {**record['approval'], 'source':md.relative_to(ROOT).as_posix()}
            if presentation['approval'] != expected or presentation['narrative_status'] != 'APPROVED':
                errors.append(f'{p.stem}: approval record mismatch')
            if hashlib.sha256(md.read_bytes()).hexdigest() != record['approved_markdown_sha256'].get(md.relative_to(ROOT).as_posix()):
                errors.append(f'{p.stem}: narrative changed since owner approval')
        elif presentation['approval'] is not None or presentation['narrative_status'] != 'PROPOSED_ADDITIONS':
            errors.append(f'{p.stem}: unsupported approval')
        if obj['stat_status'] != 'BLOCKED' or obj['balance_status'] != 'BLOCKED':
            errors.append(f'{p.stem}: unsupported calibration status')
        observation = obj['runtime_observation']
        enemy = observation['enemy']
        if enemy['id'] in runtime_ids or enemy != db['Enemies'][enemy['id']] or enemy['name'] != obj['title']:
            errors.append(f'{p.stem}: duplicate/stale runtime match')
        runtime_ids.add(enemy['id'])
        if [s['id'] for s in observation['skills']] != [a['skillId'] for a in enemy['actions']]:
            errors.append(f'{p.stem}: action skill mapping mismatch')
        for skill in observation['skills']:
            if skill != db['Skills'][skill['id']]:
                errors.append(f'{p.stem}: stale skill')
            eid = skill['damage']['elementId']
            if not -1 <= eid < len(db['System']['elements']):
                errors.append(f'{p.stem}: unknown element ID')
            for effect in skill['effects']:
                if effect['code'] in (21,22) and effect['dataId'] and not valid_id(db['States'],effect['dataId']):
                    errors.append(f'{p.stem}: unknown state ID')
        for drop in observation['drop_records']:
            if drop['record'] != db[drop['database']][drop['record']['id']]:
                errors.append(f'{p.stem}: stale item reference')
        entries.append({'id':obj['id'],'race':obj['race'],'words':len(text.split()),'runtime_id':enemy['id']})
    if len(entries) != 7:
        errors.append('Expected 7 Raksamala commander pairs')
    result = {'errors':errors,'entries':entries,'changed_baseline_files':changed,
              'scope':'7 narrative/data pairs; identities, original fields, sources, runtime references, and outside-batch preservation',
              'balance_simulation':None,'playtest':None,
              'new_narrative_approval':read(REPORT/'raksamala_commanders_lore_approval.json')['approval'] if (REPORT/'raksamala_commanders_lore_approval.json').exists() else None}
    (REPORT/'raksamala_commanders_verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'pairs':len(entries),'errors':errors,'game_runtime_changed':any(n.startswith('10_Game Project/') for n in changed)}))
    return bool(errors)

if __name__ == '__main__':
    sys.exit(main())
