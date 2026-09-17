"""Record explicit owner approval of the Jenggala narrative batch."""
import hashlib
import json
import re
from bestiary_audit import BEST, ROOT, REPORT, read

replacements = {
    'merupakan habitat existing': 'merupakan habitat yang tercatat',
    'adalah habitat perjumpaan existing': 'adalah tempat kemunculan yang tercatat',
    'cocok sebagai tempat bertengger yang diusulkan': 'menjadi tempat bertenggernya',
    'diusulkan sebagai penempatan yang cocok': 'menjadi salah satu tempat kemunculannya',
    'diusulkan sebagai penempatan regional yang sesuai': 'menjadi bagian dari persebarannya',
    'diusulkan sebagai lokasi kemunculan': 'menjadi salah satu lokasi kemunculannya',
    'diusulkan sebagai penempatan regional sementara, tanpa mengganti nama lama dalam arsip': 'menjadi persebaran regionalnya; pemetaan nama Gunung Emas tetap belum dipastikan',
    'diusulkan sebagai penempatan': 'menjadi tempat kemunculannya',
    'cocok sebagai usulan penempatan': 'menjadi tempat kemunculannya',
    'merupakan usulan penempatan berdasarkan ancaman regional': 'menjadi salah satu tempat kemunculannya',
    'Usulan ini tidak menyatakan': 'Penempatan ini tidak menyatakan',
    'menjadi usulan yang sesuai': 'menjadi bagian dari persebarannya',
    'diusulkan sebagai habitat tanpa memberi nama wilayah baru': 'menjadi habitatnya',
    'Dalam rancangan rupa ini, batas': 'Batas',
    'Dalam rancangan ini, jari': 'Jari',
    'Dalam pengembangan perilaku ini, ia': 'Ia',
    'Dalam pengembangan ini, ia': 'Ia',
    'Mengikuti sebutan Kuyang, rancangan ini menampilkan': 'Sebagaimana sebutannya, Kuyang, Strigoi berwujud',
    'Rancangan bulu belang': 'Bulu belang',
    'melengkapi rancangan rupanya': 'melengkapi rupanya',
    'melengkapi rancangan yang menyerupai': 'membentuk rupa yang menyerupai',
    'Rancangan ini tidak memberinya sayap atau menjadikannya anak dari ras fana tertentu': 'Ia tidak bersayap, dan asalnya tidak ditetapkan sebagai anak dari ras fana tertentu',
    'Rancangan ini tidak menganggap setiap Ogre bodoh atau tidak mampu belajar;': 'Tidak semua Ogre dapat dianggap bodoh atau tidak mampu belajar;',
    'Rancangan ini tidak menetapkan': 'Hal ini tidak menetapkan',
    'Rincian visual ini mengembangkan wujud kelelawar purba yang sudah tercatat.': '',
    'Detail ini merupakan pengembangan visual; cara tubuh terpisah, asal manusia, dan ritual pembentukannya belum menjadi fakta canon.': 'Cara tubuhnya terpisah, asal manusia, dan ritual pembentukannya belum diketahui.',
}

manifest = REPORT/'jenggala_lore_approval.json'
if manifest.exists():
    raise SystemExit('Approval already recorded; edit current lore directly.')
approval = {'status':'APPROVED','date':'2026-09-17','authority':'project_owner',
            'request':'aku setuju semua usulannya',
            'scope':'Seluruh deskripsi, bentuk, tingkah laku, penempatan habitat dan kisah dalam batch narasi 15 Jenggala.',
            'exclusions':'Kalibrasi game dan jawaban atas pertanyaan yang tidak pernah diusulkan tetap terpisah.'}
hashes = {}
for md in sorted((BEST/'02_Jenggala').glob('*.md')):
    text = md.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old,new)
    text = re.sub(r'> Catatan penulisan:.*? Acuan:', '> Acuan:', text)
    text = '\n'.join(line.rstrip() for line in text.splitlines())+'\n'
    md.write_text(text,encoding='utf-8')
    p = md.with_suffix('.json')
    obj = read(p)
    obj['presentation']['narrative_status'] = 'APPROVED'
    obj['presentation']['approval'] = {**approval,'source':md.relative_to(ROOT).as_posix()}
    obj['presentation']['scope'] = approval['scope']
    obj['lore_review']['approval_record'] = manifest.relative_to(ROOT).as_posix()
    obj['lore_review']['unresolved'] = [s.replace('Gua regional adalah usulan;', 'Penempatan gua Arkananta disetujui;') for s in obj['lore_review']['unresolved']]
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    hashes[md.relative_to(ROOT).as_posix()] = hashlib.sha256(md.read_bytes()).hexdigest()
manifest.write_text(json.dumps({'approval':approval,'approved_markdown_sha256':hashes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Recorded approval for 15 Jenggala narratives.')
