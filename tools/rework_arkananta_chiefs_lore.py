"""One-time archived narrative batch for the three Arkananta chiefs."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BEST = ROOT / '07_Bestiary'
FOLDER = BEST / '06_Chiefs_of_Arkananta'
REPORT = BEST / '_audit'
GAME = ROOT / '10_Game Project/Tales of The Dark Time'
REGION = '03_Region/05_Arkananta/Pegunungan Arkananta.md'
RELIGION = '03_Region/05_Arkananta/Religion.md'
ECONOMY = '03_Region/05_Arkananta/Economy.md'

# description, appearance, personality, position, story title, story, race, sources, unresolved
ENTRIES = {
'Grok_Tulang_Besi': (
 'Kepala Suku Troliogoro sekaligus shaman Animisme Batu. Grok memimpin ritual penyusunan cairn untuk menenangkan roh Gunung Arkananta dan menjaga keselamatan kaumnya. Julukan Tulang-Besi merujuk pada tubuh Troliogoro yang telah menyatu dengan logam serta kekokohan pemimpin yang memilih mempertahankan gua daripada mencari perang di luar wilayahnya.',
 'Grok bertubuh raksasa dengan punggung yang dipenuhi pertumbuhan kristal gua. Kulit tebalnya menyimpan lapisan logam hasil evolusi buatan Troliogoro, sedangkan kedua tangan dibalut potongan logam dari reruntuhan kuno. Susunannya tidak sepenuhnya simetris: beberapa lempeng menutup buku jari, sementara bagian lain mengikuti lengan seperti bekas tempaan yang tumbuh bersama tubuh. Ia membawa tongkat ritual berat untuk memukul batu dan membangunkan gema pemujaan. Ketika berdiri diam di antara cairn, siluetnya menyerupai bagian dari dinding kristal.',
 'Grok keras, curiga kepada orang luar, dan sangat menjaga tata ruang sakral. Kemarahannya mudah muncul ketika cairn dipindahkan atau dirusak, sebab tindakan itu ia anggap membahayakan seluruh suku. Meski dikenal brutal, ia tidak mencari pertempuran terbuka tanpa alasan. Ia lebih suka menutup akses, mengamati niat pendatang, lalu menuntut mereka memperbaiki kerusakan yang dibuat. Sebagai shaman, ia sabar saat memimpin ritual dan mampu menunggu lama demi membaca perubahan gunung. Kesetiaannya kepada tradisi dapat membuatnya menolak gagasan baru sebelum memahami manfaatnya.',
 'Grok memimpin Suku Troliogoro dari Gua Troliogoro yang terletak tinggi pada tebing curam Arkananta. Lorong besarnya menampung tubuh para troll, bengkel logam, serta susunan cairn yang digunakan dalam ritual. Lokasi Bestiary lama menyebut Lembah Batu Arkananta; lembah tersebut dipertahankan sebagai bagian wilayah patroli dan pengumpulan batu, sedangkan pusat kekuasaannya berada di gua sukunya. Hubungannya dengan Krom tegang karena sengketa batas dan perbedaan cara hidup.',
 'Batu yang Harus Dikembalikan',
 'Seorang pedagang yang tersesat mengambil batu pipih dari sebuah cairn untuk menahan roda gerobaknya. Ketika Grok menemukannya, ia mengangkat tongkat ritual dan meminta seluruh rombongan menjauh. Pedagang itu mengira emas dapat menyelesaikan masalah, tetapi tawarannya justru membuat wajah sang shaman semakin keras.\n\nGrok menyuruhnya mengembalikan batu ke susunan semula. Pedagang itu tidak mengingat posisinya, sehingga para Troliogoro membimbingnya menyusun ulang cairn dari dasar. Pekerjaan berlangsung sampai gema pukulan batu kembali terdengar benar. Grok akhirnya membuka jalan keluar. Ia tidak menerima koin; bagi pemimpin itu, pelajaran untuk menghormati batu jauh lebih berharga daripada pembayaran yang dibawa orang asing.',
 'Troliogoro',
 ['05_Karakter & Tokoh Penting/05_Arkananta/Grok Tulang-Besi.md','04_Ras/02_Wuru Loka/Troliogoro_(Troll).md','03_Region/05_Arkananta/Cities & Town/Gua Troliogoro.md',RELIGION,ECONOMY,REGION],
 ['MD Bestiary lama menyebut Shaman Tier 5, sedangkan JSON lama Berserker Tier 4; konflik kelas tidak diputuskan. Lembah Batu belum memiliki dokumen lokasi tersendiri.']),
'Krom_Batugilang': (
 'Kepala Suku Butoraksa dan petarung yang menguasai pertambangan luar Arkananta. Krom Batugilang dikenal ganas di medan laga, tetapi kecerdikannya dalam barter membuatnya lebih berbahaya daripada pemimpin yang hanya mengandalkan kekuatan. Ia menilai mineral, senjata, dan pasokan berdasarkan kegunaan nyata bagi sukunya, bukan berdasarkan kemilau koin.',
 'Krom adalah Butoraksa purba berukuran sangat besar dengan kulit hijau gelap yang tertutup bekas luka. Darah monster dilukiskan pada dada, bahu, dan lengan membentuk pola spiral Akar Darah. Senjatanya berupa palu raksasa dari tulang paha Behemoth; gagangnya dibungkus kulit agar tidak terlepas saat ia melompat di antara batu. Bahu lebar dan kaki kuat membantunya menahan benturan ketika mendarat. Catatan lama menyebut gada angin puting beliung, tetapi profil tokoh menetapkan palu tulang sebagai senjata visual utamanya.',
 'Krom berani, dominan, dan menikmati negosiasi yang membuat lawan mengungkap kebutuhan mereka lebih dahulu. Ia tidak menyamakan keramahan dengan kemurahan hati: setiap pertukaran harus memberi manfaat jelas bagi Butoraksa. Dalam pertempuran ia agresif serta menganggap luka sebagai bagian dari kehormatan, tetapi ia tidak membuang prajurit demi kemenangan yang tidak berguna. Orang yang meremehkannya sebagai sosok biadab mudah kehilangan posisi tawar. Ia juga menyimpan dendam terhadap Troliogoro karena sengketa batas gua, meski kebutuhan sukunya dapat memaksanya menahan permusuhan sementara.',
 'Krom memimpin Gua Butoraksa, pemukiman paling dangkal dan terbuka yang menjadi benteng pertama menghadapi monster luar. Suku di bawahnya menguasai area pertambangan luar dan memperdagangkan bijih kasar dengan pihak yang membawa senjata atau pasokan berguna. Jembatan Tebing Arkananta pada lokasi Bestiary lama menjadi jalur patroli serta titik pengawasan menuju tambang, bukan pusat pemukiman. Ornamen tulang, daging bakar, dan kulit samak memenuhi wilayah kekuasaannya.',
 'Harga Sebuah Mata Palu',
 'Seorang penempa dari luar membawa mata palu baja dan meminta bijih Arkananta sebagai gantinya. Krom memeriksa logam itu, lalu menjatuhkannya ke batu sampai salah satu sisi retak. Sang penempa memprotes bahwa ujian tersebut merusak barang dagangannya.\n\nKrom menjawab bahwa alat yang patah di gua dapat membunuh penambang yang menggunakannya. Ia menawarkan bijih lebih sedikit untuk baja yang tersisa. Sang penempa meminta kesempatan memperbaiki mata palu di tempat dan menunjukkan cara tempa yang lebih kuat. Krom menerima usulan itu. Saat pertukaran selesai, keduanya mendapat lebih dari benda: Butoraksa memperoleh pengetahuan, dan sang penempa pulang memahami bahwa kepala suku itu menguji nilai melalui keselamatan kaumnya.',
 'Butoraksa',
 ['05_Karakter & Tokoh Penting/05_Arkananta/Krom Batugilang.md','04_Ras/02_Wuru Loka/Butoraksa_(Orc).md','03_Region/05_Arkananta/Cities & Town/Gua Butoraksa.md',RELIGION,ECONOMY,REGION],
 ['Hubungan mekanis palu tulang dengan label angin Bestiary belum ditentukan. Jembatan Tebing belum memiliki dokumen lokasi tersendiri.']),
'Nyai_Larasati': (
 'Pemimpin Rakshorien buangan yang memilih kehidupan damai di gua tersembunyi Arkananta. Nyai Larasati mengembangkan botani bawah tanah, Pemujaan Spora, serta ramuan penetral gas beracun. Sihir air dan getaran alam membantunya merawat kebun jamur sekaligus melindungi komunitas yang menolak jalan kekerasan Rakshorien lain.',
 'Larasati adalah Dark Elf yang sangat sepuh dengan tubuh ramping dan kulit pucat gelap. Kedua matanya berwarna ungu terang sepenuhnya, hasil kehidupan panjang dalam kegelapan gua. Telinganya meruncing, sedangkan kuku hitam yang diwarisi fisiologi Rakshorien dijaga tetap pendek agar tidak merusak tanaman obat. Ia mengenakan jubah dari tenunan serat dan jamur yang berpendar lembut. Botol ramuan tergantung pada sabuknya, dan sebuah tongkat bercabang membantu mengarahkan aliran air serta getaran melalui lantai batu.',
 'Larasati tenang, penuh pertimbangan, dan protektif kepada para pelarian yang mempercayakan hidup kepadanya. Ia tidak mudah menerima orang luar ke kebun spora, tetapi memilih bertanya sebelum menghakimi. Pengalaman panjang membuat tutur katanya lembut sekaligus sulit dibantah. Ia membenci kekerasan yang dilakukan hanya demi kesenangan, sehingga menjaga jarak dari faksi Rakshorien yang memilih jalan bandit. Dalam barter ia berhati-hati dan merahasiakan hubungan dagangnya dengan Krom. Ketika komunitasnya terancam, kelembutan itu berubah menjadi ketegasan seorang pemimpin yang memahami racun, penyembuhan, dan medan guanya.',
 'Larasati memimpin komunitas Rakshorien damai di Gua Rakshorien, wilayah lembap dan tersembunyi yang diterangi jamur bioluminesen. Kebun spora beracun serta jamur penyembuh menjadi sumber pangan, obat, ritual, dan barter. Gua Air Mata Air Arkananta pada catatan lama ditempatkan sebagai ruang mata air di dalam kompleks gua, tempat Larasati mengumpulkan air untuk ramuan dan melatih sihirnya. Penempatan ini menyelaraskan lokasi lama tanpa menciptakan permukiman Rakshorien kedua.',
 'Barter di Bawah Cahaya Jamur',
 'Krom datang melalui jalur tersembunyi dengan bungkusan daging monster. Larasati telah menyiapkan jamur obat, tetapi menemukan noda busuk pada salah satu potongan. Pengawal Rakshorien meraih senjata, mengira Butoraksa mencoba menipu mereka.\n\nLarasati meminta semua orang menunggu. Ia memperlihatkan perubahan warna pada serat daging dan menjelaskan racun gas yang terserap selama perjalanan. Krom memerintahkan bagian itu dibuang, lalu menambah kulit samak sebagai pengganti. Barter selesai tanpa pertumpahan darah. Sebelum berpisah, Larasati memberinya sedikit ramuan untuk jalur pulang. Hubungan mereka tetap rahasia dan penuh kewaspadaan, tetapi malam itu pengetahuan sang Nyai mencegah kedua suku mengubah kesalahan menjadi perang.',
 'Rakshorien',
 ['05_Karakter & Tokoh Penting/05_Arkananta/Nyai Larasati.md','04_Ras/02_Wuru Loka/Rakshorien_(Dark_Elf).md','03_Region/05_Arkananta/Cities & Town/Gua Rakshorien.md',RELIGION,ECONOMY,REGION],
 ['Gua Air Mata Air ditafsirkan sebagai ruang dalam kompleks Gua Rakshorien; belum ada dokumen lokasi terpisah. Detail tongkat dan mata air adalah usulan.'])
}

def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def main():
    archive = REPORT/'pre_arkananta_chiefs_narrative.json'
    if archive.exists():
        raise SystemExit('Batch already archived; edit current files directly.')
    paths = sorted(FOLDER.glob('*.json'))
    assert {p.stem for p in paths} == set(ENTRIES)
    old = {p.relative_to(ROOT).as_posix():p.read_text(encoding='utf-8-sig') for p in FOLDER.iterdir() if p.suffix in ('.md','.json')}
    write(archive, old)
    hashes = {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.parts and '_audit' not in p.parts and '__pycache__' not in p.parts}
    write(REPORT/'pre_arkananta_chiefs_hashes.json', hashes)
    db = {n:load(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','Items','Weapons','Armors']}
    for p in paths:
        obj = load(p)
        desc, form, personality, position, story_title, story, race, sources, unresolved = ENTRIES[p.stem]
        matches = [e for e in db['Enemies'] if e and e['name'] == obj['title']]
        assert len(matches) == 1, p
        enemy = matches[0]
        text = f'---\ntitle: {obj["title"]}\ntags:\n  - Bestiary\n  - Boss\n---\n\n# {obj["title"]}\n'
        for heading, content in [('Deskripsi',desc),('Bentuk',form),('Kepribadian dan Sikap',personality),('Kedudukan dan Wilayah',position),('Kisah - '+story_title,story)]:
            text += f'\n## {heading}\n\n{content}\n'
        links = ['['+Path(s).stem.replace('_',' ')+'](../../'+quote(s,safe='/')+')' for s in sources]
        for source in sources:
            assert (ROOT/source).is_file(), source
        text += '\n> Catatan penulisan: Identitas, kedudukan, dan fakta utama mengikuti profil karakter serta wilayah. Rincian rupa tambahan dan kisah merupakan usulan. Acuan: '+'; '.join(links)+'.\n'
        p.with_suffix('.md').write_text(text, encoding='utf-8')
        previous = {k:obj.get(k) for k in ['stat_status','balance_status','source_status']}
        obj['stat_status'] = obj['balance_status'] = 'BLOCKED'
        obj['source_status'] = 'legacy_with_runtime_observation'
        obj['race'] = race
        obj['presentation'] = {'markdown_role':'lore_only','lore_source':p.with_suffix('.md').relative_to(ROOT).as_posix(),
            'game_data_source':p.relative_to(ROOT).as_posix(),'narrative_status':'PROPOSED_ADDITIONS','approval':None,
            'scope':'Three Arkananta chiefs; prior category approvals do not extend to this batch.',
            'sync_policy':'Author lore in Markdown; game data stays in JSON.'}
        obj['lore_review'] = {'source_archive':archive.relative_to(ROOT).as_posix(),'sources':sources,'unresolved':unresolved,
            'category_note':'Named sapient chiefs: Grok–Troliogoro, Krom–Butoraksa, Larasati–Rakshorien.',
            'historical_description':obj['description']}
        obj['runtime_observation'] = {'status':'OBSERVED_ONLY','source':(GAME/'data/Enemies.json').relative_to(ROOT).as_posix(),
            'enemy':enemy,'skills':[db['Skills'][a['skillId']] for a in enemy['actions']],
            'drop_records':[{'database':{1:'Items',2:'Weapons',3:'Armors'}[d['kind']],
                'record':db[{1:'Items',2:'Weapons',3:'Armors'}[d['kind']]][d['dataId']]}
                for d in enemy['dropItems'] if d['kind']],
            'meaning':'Snapshot only; does not establish calibrated balance.'}
        obj['balance_review'] = {'stat_status':'BLOCKED','previous_status':previous,
            'legacy_note':'Existing top-level numbers preserved for traceability; not recalibrated.',
            'authority':'06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md','simulation_result':None,'playtest_evidence':None,
            'unresolved':['Approved party/gear/progression and encounter targets absent.',
                          'Runtime placeholders and modifiers require implementation review before calibration.']}
        write(p,obj)
    print('Arkananta chiefs narrative batch: 3 Markdown entries; legacy data and runtime snapshots in JSON.')

if __name__ == '__main__':
    main()
