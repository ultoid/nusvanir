"""Record the owner's approval of the fifteen Wildlife narrative drafts."""
import json
import re
from bestiary_audit import BEST, ROOT, read

HABITATS = {
 'Ayam_Hutan': 'Hutan ringan di Mandala, terutama tepian hutan di sekitar lahan pertanian Arthiska. Ruang terbuka menyediakan tempat mencari makan, sementara semak di batas kebun menjadi perlindungan dan tempat bersarang.',
 'Babi_Hutan': 'Semak dan tanah lembap pada hutan perbatasan Hermindar, di luar jalur permukiman. Akar, umbi, dan tutupan tumbuhan yang rapat menyediakan makanan sekaligus perlindungan. Kawasan ini memperjelas habitat yang dahulu hanya disebut Pinggiran Jenggala.',
 'Bebek_Danau': 'Danau Mandala serta perairan tenang di kawasan agraris Arthiska, terutama tepian sungai yang terlindung dan berdekatan dengan persawahan. Kawanan mencari makan di tepian dangkal dan kembali ke air ketika terganggu.',
 'Beruang_Madu_Raksasa': 'Gua-gua hutan dan pepohonan besar di lereng luar Arkananta. Pertemuan kawasan berbatu dan hutan menyediakan tempat berlindung serta makanan. Persebaran ini tidak menetapkan keberadaannya di inti pegunungan yang masih belum dijelajahi.',
 'Buaya_Rawa': 'Rawa dan genangan liar di luar kawasan sungai pertanian Arthiska, terutama tepian berlumpur tempat hewan mendekati air. Catatan lama juga menyebut Rawa Beracun, tetapi letak wilayah bernama itu masih belum terpetakan. Tidak semua rawa yang dihuni buaya merupakan perairan beracun.',
 'Burung_Puyuh_Hutan': 'Semak hutan serta batas kebun dan hutan ringan di kawasan Arthiska. Biji, serasah, dan penutup tanah mendukung kehidupannya dekat permukaan tanah; ia tidak bergantung pada kanopi tinggi.',
 'Ikan_Sisik_Perak': 'Sungai dan danau air tawar, dengan jaringan sungai tenang Arthiska sebagai salah satu habitat utamanya. Ikan ini juga dapat dijumpai pada bagian sungai yang sesuai di sekitar Lingkar Samodra, meskipun kanal bongkar muat yang sibuk bukan tempat pemijahan utamanya.',
 'Kambing_Arkananta': 'Lereng berbatu Pegunungan Arkananta, terutama tepian yang masih ditumbuhi rumput dan semak. Pendatang lebih sering menjumpainya di lereng luar. Keberadaannya tidak menjadi bukti bahwa jalur menuju inti pegunungan aman dilalui.',
 'Kelinci_Padang': 'Kebun dan lahan terbuka dekat pinggiran ibu kota Mandala. Catatan penampakannya di Lingkar Bumi juga mencakup kelinci yang dibawa ke Pasar Agung Bumi. Distrik pasar yang padat itu merupakan tempat perdagangan hewan, bukan padang luas tempat seluruh populasinya hidup liar.',
 'Kura_Kura_Sungai': 'Tepian sungai tenang di kawasan Arthiska yang menyediakan lumpur, akar, dan tempat berjemur. Ia menyukai bagian aliran yang jauh dari lalu lintas perahu dan dapat segera kembali ke air dari tempat istirahatnya.',
 'Macan_Kumbang': 'Pepohonan besar Astradipa dengan cabang kuat dan lantai hutan yang teduh. Habitat ini memperjelas catatan lama tentang pohon-pohon tinggi Jenggala, tanpa menjadikannya anggota Jenggala atau penghuni tetap permukiman kanopi Asrivana.',
 'Rusa_Tanduk_Cabang': 'Lantai Hutan Astradipa dan ruang terbuka di antara akar raksasa. Cabang rendah yang terlalu rapat membatasi gerak tanduknya, sehingga rusa memilih jalur yang cukup lapang. Ia merupakan penghuni ekosistem bawah, bukan hewan yang berlari di jembatan kota kanopi.',
 'Sapi_Perah_Mandala': 'Padang rumput dan peternakan Mandala, terutama kawasan agraris sekitar Arthiska yang memiliki air serta jaringan pasokan pangan. Padang penggembalaan terpisah dari terasering padi agar kawanan tidak merusak tanaman.',
 'Serigala_Kelabu': 'Hutan rimbun di luar Valkindra, pada kawasan utara Mandala yang lebih dingin dan berkabut. Kawanan memanfaatkan tutupan pepohonan di sekitar jalur liar. Kehadirannya dekat reruntuhan tidak menjadikannya makhluk kutukan.',
 'Ular_Piton_Pohon': 'Cabang dan ranting besar pada lapisan bawah kanopi Astradipa, dekat jalur satwa di antara akar dan dahan. Tidak setiap cabang dekat permukiman Asrivana dihuni ular; ia memilih tempat yang memberi tumpuan tubuh dan perlindungan untuk menyergap.'
}

for path in sorted((BEST / '01_Alam_Liar').glob('*.md')):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'## Habitat\n\n.*?(?=\n## Kisah)', '## Habitat\n\n' + HABITATS[path.stem] + '\n', text, flags=re.S)
    text = text.replace('diusulkan ', '').replace('Rancangan bulunya', 'Bulunya').replace('Rancangan bulu', 'Bulu').replace('Rancangan sisiknya', 'Sisiknya')
    text = text.replace('Dalam rancangan kisah di pinggiran Arthiska,', 'Di pinggiran Arthiska,')
    text = text.replace('Diet madu, serangga, dan buah untuk melengkapi identitasnya; kisah lama yang menekankan penyergapan tidak cukup untuk menetapkannya sebagai pemakan daging semata.', 'Ia memakan madu, serangga, dan buah, sehingga tidak bergantung pada daging semata.')
    text = text.replace('Bulu kelabu berlapis cokelat arang lebih tebal', 'Bulu kelabu berlapis cokelat arang lebih tebal')
    text = re.sub(r'> Catatan penulisan:.*?(?=(?:Acuan[^:]*:))', '> ', text)
    text = text.replace('Tidak ditambahkan tanduk, sayap, atau tanda korupsi yang belum didukung lore.', 'Tubuhnya tidak memiliki tanduk, sayap, atau tanda korupsi.')
    text = text.replace('meskipun catatan game lama memberinya serangan gigitan', 'meskipun ia dapat menggigit untuk membela diri')
    path.write_text(text, encoding='utf-8')
    jp = path.with_suffix('.json')
    obj = read(jp)
    obj['v2']['presentation']['lore_approval'] = {
        'status': 'APPROVED', 'date': '2026-09-17', 'authority': 'project_owner',
        'request': 'usulan aku setujui semua',
        'scope': 'Deskripsi, bentuk, tingkah laku, habitat dan kisah pada batch narasi 15 Alam Liar.',
        'source': path.relative_to(ROOT).as_posix(),
        'exclusions': 'Tidak menetapkan kalibrasi stat, spawn map runtime, atau usulan combat/crafting lama.'
    }
    jp.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Approved narrative records: 15; game values unchanged.')
