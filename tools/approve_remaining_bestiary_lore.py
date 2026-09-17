"""Record the project owner's approval for every remaining Bestiary narrative batch."""
import hashlib
import json
import re

from bestiary_audit import BEST, ROOT, REPORT, read


BATCHES = [
    ('05_Dragons_of_Agnitra_Nest', 'agnitra_lore_approval.json',
     'Seluruh deskripsi, bentuk, kepribadian dan sikap, lokasi nest, serta kisah empat naga Agnitra.'),
    ('06_Chiefs_of_Arkananta', 'arkananta_chiefs_lore_approval.json',
     'Seluruh deskripsi, bentuk, kepribadian dan sikap, kedudukan dan wilayah, serta kisah tiga kepala suku Arkananta.'),
    ('07_Sentinels_of_Nusa_Sayendra', 'sayendra_sentinels_lore_approval.json',
     'Seluruh deskripsi, bentuk, kepribadian dan sikap, kedudukan dan wilayah, serta kisah empat Sentinel Nusa Sayendra.'),
    ('08_Commanders_of_Raksamala_Fortress', 'raksamala_commanders_lore_approval.json',
     'Seluruh deskripsi, bentuk, kepribadian dan sikap, kedudukan dan benteng, serta kisah tujuh komandan Raksamala.'),
    ('09_Laut_Rangkaruna', 'rangkaruna_lore_approval.json',
     'Seluruh deskripsi, bentuk, tingkah laku, habitat, serta kisah sepuluh fauna Laut Rangkaruna.'),
]

REQUEST = 'cek ulang semua yang ada di 07_Bestiary, aku menyetujui semua usulanmu'
EXCLUSIONS = ('Kalibrasi game serta pertanyaan canon, taksonomi, dan mekanika yang belum '
              'pernah dijawab tetap terpisah.')


def approved_unresolved(value):
    value = value.replace('menunggu persetujuan pemilik', 'telah disetujui pemilik')
    value = value.replace('menunggu persetujuan', 'telah disetujui pemilik')
    value = value.replace('masih merupakan usulan', 'telah disetujui pemilik')
    value = value.replace('merupakan usulan', 'telah disetujui pemilik')
    return value


def main():
    total = 0
    for folder_name, manifest_name, scope in BATCHES:
        manifest = REPORT / manifest_name
        if manifest.exists():
            raise SystemExit(f'Approval already recorded: {manifest.relative_to(ROOT)}')
        approval = {
            'status': 'APPROVED',
            'date': '2026-09-17',
            'authority': 'project_owner',
            'request': REQUEST,
            'scope': scope,
            'exclusions': EXCLUSIONS,
        }
        hashes = {}
        for md in sorted((BEST / folder_name).glob('*.md')):
            text = md.read_text(encoding='utf-8')
            text = re.sub(r'> Catatan penulisan:.*? Acuan:', '> Acuan:', text)
            text = '\n'.join(line.rstrip() for line in text.splitlines()) + '\n'
            md.write_text(text, encoding='utf-8')

            data_path = md.with_suffix('.json')
            obj = read(data_path)
            obj['presentation']['narrative_status'] = 'APPROVED'
            obj['presentation']['approval'] = {
                **approval,
                'source': md.relative_to(ROOT).as_posix(),
            }
            obj['presentation']['scope'] = scope
            obj['lore_review']['approval_record'] = manifest.relative_to(ROOT).as_posix()
            obj['lore_review']['unresolved'] = [
                approved_unresolved(item) for item in obj['lore_review']['unresolved']
            ]
            data_path.write_text(
                json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
            )
            hashes[md.relative_to(ROOT).as_posix()] = hashlib.sha256(md.read_bytes()).hexdigest()
            total += 1

        manifest.write_text(
            json.dumps({'approval': approval, 'approved_markdown_sha256': hashes},
                       ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
        )
    print(f'Recorded owner approval for {total} remaining Bestiary narratives.')


if __name__ == '__main__':
    main()
