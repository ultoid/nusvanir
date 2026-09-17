"""Controlled, additive Wildlife migration. Requires an explicit --batch.

Preserves all prior prose and legacy JSON fields. V2 is authored in JSON and
rendered identically into Markdown. Refuses to overwrite an existing V2 record.
"""
import argparse
import json
from pathlib import Path
import re
from bestiary_audit import ROOT, BEST, GAME, read, digest, normalized, render

FIRST = {'Babi_Hutan', 'Beruang_Madu_Raksasa', 'Macan_Kumbang', 'Sapi_Perah_Mandala', 'Serigala_Kelabu'}
# These are proposals grounded in the existing habitat/description, not new canon.
# biome, region (only explicit named regions), role, ecology/civilization proposal, counterplay
BRIEFS = {
 'Ayam_Hutan': ('Hutan ringan', None, None, 'Penjaga sarang; usulan encounter defensif ketika sarang didekati, bukan agresor patroli. Hubungan rantai makanan dan panen unggas perlu keputusan.', 'Beri kesempatan menghindari sarang; jangan mewajibkan pertempuran untuk melintas.'),
 'Babi_Hutan': ('Tepi hutan dan semak', None, 'Bruiser', 'Draf menghubungkan gangguan ladang dengan ekonomi agraris Mandala; penempatan Mandala masih usulan karena lokasi sumber hanya Pinggiran Jenggala. Jalur makan dan mundur menjelaskan konflik dengan petani.', 'Kenalkan ancaman serbuan melalui isyarat map; guard saat serbuan disiapkan adalah usulan, telegraph belum diimplementasikan.'),
 'Bebek_Danau': ('Danau', 'Mandala', None, 'Pergerakan beriringan menjadi dasar usulan kawanan tepi danau; pisahkan pengamatan fauna dari encounter bermusuhan. Panen dan diet belum ditetapkan.', 'Sediakan rute melewati kawanan tanpa bertarung; ini rancangan map, bukan perilaku AI saat ini.'),
 'Beruang_Madu_Raksasa': ('Hutan dan gua', None, 'Bruiser', 'Pertahankan gua sebagai habitat. Draf menyebut penyergapan dan gangguan ekspedisi; diet madu/omnivora serta batas wilayah belum menjadi canon. Ukuran raksasa tidak membuktikan asal Magical Beast.', 'Honey Rage memerlukan efek dan telegraph nyata; beri kesempatan guard sebelum Crushing Maul, tanpa mengarang buff.'),
 'Buaya_Rawa': ('Rawa dan perairan dangkal', None, 'Tank', 'Pemangsa dangkal membuat titik penyeberangan lebih berbahaya daripada jalan kering; usulan quest pengamanan lintasan perlu map dan permukiman yang disetujui.', 'Tunjukkan tanda keberadaan sebelum menyeberang; jangan mengandalkan positioning di battle MV tanpa sistem pendukung.'),
 'Burung_Puyuh_Hutan': ('Semak hutan', None, 'Sniper', 'Unggas bersayap pendek tetap fauna semak. Serangan Feather Dart dan atribut Wind runtime perlu penjelasan sebelum dijadikan bukti spesies magis.', 'Scatter Flight masih placeholder; counterplay terhadap pelarian/buff menunggu implementasi.'),
 'Ikan_Sisik_Perak': ('Sungai dan danau air tawar', None, None, 'Sumber menyebut mudah ditangkap; usulan perikanan dan panen non-tempur lebih sesuai untuk ditinjau sebelum combat wajib. Jangan menetapkan laut sebagai habitat.', 'Pisahkan aktivitas menangkap ikan dari akses traversal; School Rush belum membuktikan troop kawanan.'),
 'Kambing_Arkananta': ('Tebing pegunungan', 'Pegunungan Arkananta', 'Bruiser', 'Kelincahan tebing menjelaskan keterbatasan akses panen tanduk. Arkananta Horn sudah terhubung ke forge; perdagangan harus memperhatikan barter lokal dan pengecualian Troliogoro.', 'Tampilkan wilayah kambing sebelum lintasan sempit; Horn Ram memiliki state nyata yang perlu diuji terhadap party.'),
 'Kelinci_Padang': ('Padang', 'Mandala', None, 'Lokasi Lingkar Bumi menghubungkannya ke wilayah pangan Mandala. Label pasif bertentangan dengan kit Assassin runtime; usulan aktivitas buruan opsional menunggu keputusan.', 'Jangan menganggap Escape Dash sebagai perintah kabur: runtime adalah serangan damage.'),
 'Kura_Kura_Sungai': ('Tepian sungai', None, 'Tank', 'Tempurung tebal mendukung pertahanan relatif, bukan multiplier stat. Usulan gangguan defensif di tepian sungai perlu dibedakan dari predator air.', 'Shell Bash dan Withdraw belum memiliki efek defensif executable; jangan menjanjikan mekanik break tempurung.'),
 'Macan_Kumbang': ('Hutan dengan tajuk tinggi', None, 'Assassin', 'Habitat pohon tinggi dan draf nokturnal mendukung pengintaian. Kata Jenggala pada habitat bukan bukti ras atau region administratif. Ancaman rute pemburu adalah usulan kontekstual.', 'Usulkan tanda pengintaian di map sebelum encounter; Shadow Pounce beratribut Dark runtime tidak otomatis menjadikannya Voidborn.'),
 'Rusa_Tanduk_Cabang': ('Hutan', 'Astradipa', 'Bruiser', 'Herbivora Astradipa menghubungkan fauna dengan hutan Asrivana/Hanorok. Perdagangan kulit tidak berarti izin berburu bebas: perdagangan Astradipa dibatasi di suaka perbatasan.', 'Usulkan kesempatan menghindari teritori; jangan mengubah herbivora menjadi pemburu karena kit charge.'),
 'Sapi_Perah_Mandala': ('Padang rumput dan peternakan', 'Mandala', None, 'Ternak penghasil susu merupakan aset ekonomi agraris. Usulan quest perlindungan ternak sesuai draf; tidak ada item susu terhubung yang boleh diciptakan hanya untuk mengisi drop.', 'Putuskan apakah herd adalah objek perlindungan atau musuh opsional sebelum mengaktifkan Stampede; Support bukan bukti skill healing.'),
 'Serigala_Kelabu': ('Hutan rimbun', None, 'Skirmisher', 'Draf pemburu berkelompok mendukung tekanan kawanan, tetapi komposisi troop belum ada. Gangguan ternak/rute adalah usulan; jangan menyimpulkan invasi dari hadirnya satwa.', 'Prioritas target kawanan perlu troop nyata; Pack Howl belum memberi buff meskipun namanya menyiratkan itu.'),
 'Ular_Piton_Pohon': ('Ranting besar dan tajuk', None, 'Controller', 'Pertahankan lore lilitan dan Poison yang memang tercatat; jangan menghapus racun atas dasar zoologi dunia nyata. Sumber belum menjelaskan adaptasi atau asal magis.', 'Tinjau penangkal Poison dan Root yang tersedia pada progression; jangan menebak immunity atau durasi.'),
}


def tag(note, key):
    match = re.search(r'<' + re.escape(key) + r':\s*(.*?)>', note)
    return match.group(1) if match else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', choices=['01a', '01b'], required=True)
    args = parser.parse_args()
    db = {n: read(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','Items','Weapons','Armors','Troops','System','States']}
    by_name = {normalized(e['name']): e for e in db['Enemies'] if e}
    deps = ['06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md', '06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md',
            '06_Sistem Game & Ekonomi/Sistem_Ekonomi_&_Crafting.md']
    deps += [(GAME/'data'/(n+'.json')).relative_to(ROOT).as_posix() for n in ['System','Enemies','Actors','Classes','Skills','States','Items','Weapons','Armors','Troops']]
    deps += [(GAME/'js/plugins.js').relative_to(ROOT).as_posix(), (GAME/'js/rpg_objects.js').relative_to(ROOT).as_posix()]
    hashes = {p: digest(ROOT/p) for p in deps}
    aliases = {'Neutral': None, 'Fire':'Api', 'Water':'Air', 'Earth':'Tanah', 'Air':'Udara', 'Electric':'Listrik',
               'Ice':'Es', 'Steel':'Besi', 'Sound':'Suara', 'Holy':'Cahaya', 'Dark':'Kegelapan'}
    for p in sorted((BEST/'01_Alam_Liar').glob('*.json')):
        if (p.stem in FIRST) != (args.batch == '01a'):
            continue
        obj = read(p)
        if 'v2' in obj:
            raise SystemExit(f'Refusing to overwrite V2: {p}')
        enemy = by_name[normalized(obj['title'])]
        biome, region, role, ecology, counterplay = BRIEFS[p.stem]
        skills = [db['Skills'][a['skillId']] for a in enemy['actions']]
        drops = []
        for d in enemy['dropItems']:
            if not d['kind']:
                continue
            database = {1:'Items',2:'Weapons',3:'Armors'}[d['kind']]
            item = db[database][d['dataId']]
            uses = [{'database':n, 'id':x['id'], 'name':x['name'], 'evidence':x['note'],
                     'implementation':'documented recipe only; no Synthesis Recipe tag'}
                    for n in ['Items','Weapons','Armors'] for x in db[n] if x and item['name'] in x.get('note','')]
            drops.append({'database':database, 'id':item['id'], 'name':item['name'],
                          'rarity':tag(item['note'], 'NUSV Rarity'), 'runtime_denominator':d['denominator'],
                          'description':item['description'], 'source_note':item['note'], 'uses':uses,
                          'canon_review':'Spirit Dust source names Wisp, not birds; owner decision required' if item['id']==282 else None})
        blockers = ['Titik progression, rentang level, dan gear legal LOW/EXPECTED/HIGH belum dipilih.',
                    'Target durasi, tekanan, komposisi troop, dan target EXP/Saka belum disetujui.',
                    'Runtime snapshot bukan bukti simulasi atau playtest.',
                    'Kondisi turn runtime tidak sama dengan peluang random dalam catatan AI.',
                    'Matchup runtime dan dokumen elemen berbeda; jangan ubah formula otomatis.',
                    'Resep material berbentuk catatan, belum tag executable NUSV_ItemSynthesis.']
        placeholders = [s['id'] for s in skills if '[CUSTOM SKILL EFFECT]' in s['note']]
        if placeholders:
            blockers.append('Efek skill belum executable: ' + ', '.join(map(str, placeholders)))
        if any(d['canon_review'] for d in drops):
            blockers.append('Drop Spirit Dust pada unggas tidak selaras dengan sumber Wisp.')
        states = {t['dataId'] for t in enemy['traits'] if t['code'] in (13,14,32)}
        states |= {e['dataId'] for s in skills for e in s['effects'] if e['code'] in (21,22) and e['dataId']}
        attack_elements = [t['dataId'] for t in enemy['traits'] if t['code']==31]
        v = {
          'schema_version':'2.1', 'batch':'2026-09-17/'+args.batch,
          'identity':{'id':obj['id'],'name':obj['title'],'alternative_names':[], 'canonical_slug':p.stem,
                      'species':None,'creature_family':None,'origin':None,'faction':None,'region':region,'biome':biome,'sub_area':None},
          'classification':{'creature_type':'Wildlife','basis':'kategori sumber Alam Liar; bukan klaim biologi baru',
                            'encounter_type':tag(enemy['note'],'NUSV Enemy Rank'),'encounter_type_basis':'runtime label, not calibrated',
                            'threat_rank':None,'spawn_rarity':None,'sentience_level':None,
                            'civilization_status':'Domesticated' if p.stem=='Sapi_Perah_Mandala' else None},
          'gameplay':{'progression_point':None,'recommended_level':None,'combat_role':role,'design_status':'proposal',
                      'attack_type':tag(enemy['note'],'NUSV Attack Type'),
                      'primary_element':aliases.get(db['System']['elements'][attack_elements[0]]) if attack_elements else None,
                      'secondary_element':None,'element_basis':'runtime attack-element trait; neutral is absence of cosmological affinity',
                      'ai_archetype':tag(enemy['note'],'NUSV Archetype'), 'intended_counterplay':counterplay,
                      'troop_context':[{'id':t['id'],'name':t['name'],'members':t['members']} for t in db['Troops'] if t and any(m['enemyId']==enemy['id'] for m in t['members'])],
                      'balance_status':'BLOCKED'},
          'balance':{'stat_status':'BLOCKED','balance_version':'2026-09-17-evidence-only',
                     'stats':dict.fromkeys(['mhp','mmp','atk','def','mat','mdf','agi','luk']),
                     'source_dependencies':deps,'source_sha256':hashes,
                     'party_reference':{'size':None,'level_range':None,'equipment_tier':None,'LOW':None,'EXPECTED':None,'HIGH':None},
                     'target_encounter_duration':None,'target_pressure':None,'assumptions':[],
                     'calculation_summary':None,'simulation_result':None,'playtest_evidence':None,'unresolved_blockers':blockers},
          'combat':{'basic_attack_skill_id':skills[0]['id'], 'active_skill_ids':[s['id'] for s in skills[1:]],
                    'passive':None,'special_mechanic':None, 'ai_conditions':enemy['actions'],
                    'action_priority':'Runtime rating is weighted selection among eligible actions, not a guaranteed sequence.',
                    'target_selection':'Resolve each Skills.json scope and runtime target selection; no custom smart targeting assumed.',
                    'resource_use':[{'skill_id':s['id'],'mp_cost':s['mpCost'],'tp_cost':s['tpCost']} for s in skills],
                    'enrage_behavior':None,'elemental_affinity':[t for t in enemy['traits'] if t['code']==11],
                    'status_resistances':[t for t in enemy['traits'] if t['code'] in (13,14)],
                    'state_registry':[{'id':n,'name':db['States'][n]['name']} for n in sorted(states)],
                    'pending_effect_skill_ids':placeholders},
          'spawn':{'region':region,'biome':biome,'sub_area':None,'source_habitat':tag(enemy['note'],'NUSV Region'),
                   'time':None,'weather':None,'spawn_weight':None,'pack_size':None,'aggression':None,
                   'encounter_conditions':None,'diet':None,'predators':[],'prey':[],'migration_or_territory':None,
                   'status':'habitat retained; map/time/weather/food-web links unresolved'},
          'rewards':{'status':'BLOCKED','exp':None,'saka':None,'common_drop':None,'uncommon_drop':None,
                     'rare_drop':None,'unique_drop':None,'quest_drop':None,'drops':drops,
                     'drop_slot_note':'MV slots have no common/rare semantics; rarity belongs to Items metadata.',
                     'economy_risk':'Respawn, encounter access, sale proceeds, recipe sinks and summon farming need measurement before rewards are calibrated.'},
          'worldbuilding':{'description':obj['description'],'lore':None,'origin':None,'ecology':None,'behavior':None,
                           'diet':None,'predators':[],'prey':[],'relationship_with_civilization':None,
                           'cultural_significance':None,'economic_value':None,'known_uses':[d['name'] for d in drops],
                           'historical_notes':None,'quest_relevance':None,'story_relevance':None,
                           'proposal':ecology,'proposal_status':'owner review; not inserted into regional canon',
                           'source':p.relative_to(ROOT).as_posix(),'regional_sources':['02_World/Mandala.md','02_World/Astradipa.md','02_World/Arkananta.md',
                              '03_Region/01_Mandala Kingdom/Economy.md','03_Region/02_Astradipa/Economy.md','03_Region/05_Arkananta/Economy.md']},
          'runtime_observation':{'status':'OBSERVED_ONLY','source':(GAME/'data/Enemies.json').relative_to(ROOT).as_posix(),
                                 'enemy':enemy,'skills':skills,'meaning':'Unchanged runtime data, not proposed or calibrated stat values.'},
          'legacy':{'source':'07_Bestiary/_audit/pre_batch_2026-09-17.json',
                    'values':obj.get('legacy_values', {k:obj[k] for k in ['hp','mp','element','weakness','location'] if k in obj}),
                    'status':'legacy_candidate','prior_stat_status':obj.get('stat_status'),
                    'compatibility':'All prior top-level fields retained as historical metadata; V2 takes precedence for this documentation batch.'}
        }
        obj['v2'] = v
        obj['stat_status'] = obj['balance_status'] = 'BLOCKED'
        obj['source_status'] = 'legacy_with_v2_evidence'
        p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        md = p.with_suffix('.md')
        text = md.read_text(encoding='utf-8-sig')
        text = re.sub(r'\*\*Status:\*\* VERIFIED[^\r\n]*', '**Status:** BLOCKED (runtime match does not establish calibration)', text)
        text = text.replace('**Stat Status:** VERIFIED','**Stat Status:** BLOCKED')
        title_end = re.search(r'^# .+$',text,re.M).end()
        notice = '\n\n> **V2: BLOCKED.** Metadata dan narasi draf di bawah dipertahankan sebagai arsip. Baca bagian Bestiary V2 untuk data terkini, sumber runtime, konflik, dan usulan yang belum disetujui.\n'
        text = text[:title_end] + notice + text[title_end:]
        md.write_text(text.rstrip()+'\n\n'+render(v)+'\n',encoding='utf-8')
        print(p.stem)


if __name__ == '__main__':
    main()
