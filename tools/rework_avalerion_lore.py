"""Archived Avalerion guardian narrative batch; preserves numerical game data."""
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BEST = ROOT / '07_Bestiary'
FOLDER = BEST / '04_Guardians_of_Avalerion_Outpost'
REPORT = BEST / '_audit'
GAME = ROOT / '10_Game Project/Tales of The Dark Time'
POST = '03_Region/03_Avalerion/Cities & Town/'
COMMAND = '03_Region/03_Avalerion/Faksi & Institusi/Senopati_Prabha.md'
WORLD = '02_World/Avalerion.md'

ENTRIES = {
'Ksatria_Aqua': (
 'Penjaga Avalerion yang menggunakan air suci untuk merawat luka di tengah pertempuran. Kehadirannya dikenali dari aliran bening yang tetap terarah meskipun geladak berguncang. Ia menjaga agar prajurit yang terluka dapat meninggalkan garis serang; pertahanan yang dibangunnya tidak selalu berupa tembok, melainkan kesempatan bagi orang lain untuk bertahan.',
 'Sosoknya tegak dalam zirah berlapis yang memberi ruang pada bahu dan siku untuk bergerak. Kain biru pucat terikat rapat pada pinggang agar tidak terseret air, sementara pelindung lengan memiliki alur menyerupai riak. Tangan yang dibuka saat merawat luka dikelilingi air bercahaya lembut. Pada rancangan ini, permukaan zirah tampak basah ketika sihir mengalir, tetapi tidak terus menetes setelah aliran berhenti. Wajahnya tetap terlihat melalui ketopong terbuka sehingga orang yang ditolong dapat mengikuti isyarat serta arah pandangannya.',
 'Aqua sabar dan penuh perhatian, terutama kepada orang yang berusaha menyembunyikan rasa sakit. Ia berbicara dengan tenang, menjelaskan apa yang hendak dilakukan sebelum menyentuh luka, dan memberi kesempatan bagi orang yang ditolong untuk menenangkan diri. Kepada rekannya ia bersikap hangat, tetapi dapat menegur keras prajurit yang memaksakan diri kembali bertempur. Ia mudah merasa bertanggung jawab atas keselamatan orang lain, sehingga kadang sulit menyerahkan perawatan kepada rekannya. Dalam keadaan genting, ia berusaha tetap jujur tentang batas pertolongannya tanpa mematahkan harapan orang yang sedang bergantung kepadanya.',
 'Outpost Tirta di pesisir Avalerion merupakan usulan penempatan yang sesuai dengan peran air suci. Pos ini menghadap perairan yang bermuara ke Laut Rangkaruna dan menampung pasukan maritim dengan kapal bersayap cahaya. Dermaga, geladak kapal patroli, serta tempat penerimaan prajurit terluka menjadi lingkungan tugasnya. Catatan lama menyebut pos barat; hubungan arah tersebut dengan Tirta belum dipastikan oleh peta regional.',
 'Air yang Tetap Tenang',
 'Sebuah kapal patroli kembali ke Tirta dengan geladak licin dan seorang prajurit yang sulit berdiri. Rekannya mencoba mengangkatnya ketika gelombang menghantam lambung. Aqua meminta mereka berhenti, mengatur pegangan, lalu berlutut di antara peti yang telah diikat.\n\nAir suci bergerak mengikuti tangannya, tidak mengikuti oleng kapal. Setelah luka cukup tertangani untuk pemindahan, ia memberi isyarat kepada pembawa tandu. Prajurit itu dibawa melewati dermaga tanpa harus memaksakan langkah. Aqua baru bangkit ketika tandu mencapai pijakan yang kokoh; baginya, pertolongan belum selesai hanya karena darah berhenti mengalir.',
 [POST+'Outpost_Tirta.md', COMMAND, WORLD], ['Penempatan Aqua di Tirta adalah usulan, bukan identifikasi otomatis sebagai komandan pos. Pos barat legacy belum dipetakan. Angka runtime dan legacy tetap terpisah.']),
'Ksatria_Solarius': (
 'Ksatria Avalerion yang menghadang kegelapan dengan perisai api suci. Nyala di hadapannya menjadi tanda bagi rekan di belakang untuk merapat, bukan alasan untuk maju tanpa perlindungan. Ia dikenal sebagai penjaga yang sanggup menerima tekanan di garis depan sambil membuka ruang bagi barisan lain untuk mengatur kembali langkah.',
 'Zirahnya menutup dada dan bahu dalam bidang lebar, dengan tepian keemasan yang menangkap cahaya api. Ketopong membingkai wajah seperti garis sinar yang menyebar dari dahi, sedangkan kain pelindung di belakang tubuh terikat agar tidak menyapu nyala. Perisainya tampak padat di bagian tengah dan dikelilingi lidah api terang pada pinggirannya. Ketika diangkat, pantulan pada lengan membuat batas antara logam dan cahaya sulit dibedakan. Api suci menjadi ciri utamanya, tanpa menetapkan bahwa semua perlengkapan yang dikenakan selalu terbakar.',
 'Solarius disiplin dan terus terang. Ia menghargai kesiapan, ketepatan janji, serta keberanian mengakui kesalahan. Cara bicaranya tegas dan kadang terdengar kaku bagi orang yang baru mengenalnya, tetapi ia bersedia menjelaskan alasan di balik perintahnya. Ia menuntut banyak dari para prajurit karena menuntut hal yang sama dari dirinya sendiri. Ketika seorang rekan gagal, dorongan pertamanya adalah memberi teguran; ia harus menahan ketidaksabarannya agar tetap mendengar penjelasan mereka. Di hadapan ancaman ia memilih berdiri bersama barisan, sebab baginya tanggung jawab seorang penjaga harus terlihat melalui tindakan.',
 'Outpost Agni di dataran tinggi perbatasan Arkananta cocok sebagai usulan tempat tugas Solarius. Pos api ini berada dalam kesiagaan tinggi dan mengawasi pergerakan monster batu, Troliogoro, serta Rakshorien. Pelataran benteng dan jalan masuk berbatu mendukung perannya sebagai penahan serangan. Identitasnya belum dipastikan sebagai komandan Agni; sebutan pos timur dalam entri lama juga belum dihubungkan dengan arah geografis pos tersebut.',
 'Nyala di Mulut Jalan',
 'Patroli dari lereng Arkananta tiba di depan Agni ketika suara batu berguling menyusul dari belakang. Seorang prajurit tertinggal karena ikatan perlengkapannya tersangkut. Solarius bergerak ke mulut jalan dan mengangkat perisai; cahaya api memperlihatkan jalur di antara debu.\n\nIa menahan posisi sementara dua rekannya menarik prajurit itu ke pelataran. Ketika semua telah melewati pintu, barisan kembali rapat. Tidak ada sorak kemenangan. Solarius masih menghadap lereng, menunggu debu turun agar pasukan dapat membedakan bahaya yang sungguh mendekat dari bayangan yang dibesarkan kepanikan.',
 [POST+'Outpost_Agni.md', COMMAND, WORLD], ['Solarius–Agni dan rincian rupa/kisah adalah usulan. Komandan serta arah timur belum dikonfirmasi. Api suci tidak ditafsirkan sebagai aturan damage universal.']),
'Ksatria_Terra': (
 'Penjaga Avalerion dengan kulit menyerupai bebatuan bercahaya, terkenal karena kemampuannya bertahan di tempat yang harus tetap tertutup. Kehadirannya membuat sebuah celah dalam barisan terasa seperti gerbang yang kembali terkunci. Ia menjaga batas sekaligus orang-orang di belakangnya, sehingga keteguhannya berguna bahkan ketika tidak ada pertempuran.',
 'Tubuhnya lebar dan kokoh, dengan lapisan batu bercahaya yang mengikuti lengan, leher, serta bagian wajah yang tidak tertutup zirah. Permukaannya bersekat seperti lempeng mineral; cahaya lembut terlihat di sela-selanya ketika tubuh bergerak. Pelindung bahu dan dada menambah kesan benteng, sementara perisai besar menutup sebagian besar tubuh saat ditegakkan. Kaki diletakkan berjauhan untuk menjaga tumpuan. Lapisan batu ini mengembangkan ciri kulit dalam entri lama, tanpa memastikan apakah terbentuk sejak lahir atau muncul melalui sihir.',
 'Terra pendiam, sabar, dan lebih suka mendengarkan sampai seseorang selesai berbicara. Ia memperlakukan pengunjung yang gugup dengan tenang, menjelaskan aturan gerbang tanpa mempermalukan mereka di depan kerumunan. Rekannya mengenalnya sebagai orang yang dapat diandalkan untuk menepati janji, termasuk urusan kecil yang mudah dilupakan setelah pergantian jaga. Keteguhannya kadang berubah menjadi keras kepala: ia sulit menerima perubahan rencana sebelum memahami alasannya. Namun, ia bersedia mengalah ketika keselamatan orang lain menuntutnya. Saat keadaan kacau, ia berusaha memberi orang-orang satu arahan yang jelas untuk diikuti.',
 'Outpost Bumi di perbatasan darat Avalerion dan Mandala menjadi usulan penempatan yang sesuai. Pos ini merupakan gerbang diplomatik sekaligus pertahanan utama dengan infanteri berat dan perisai suci besar. Ambang gerbang serta jalur pemeriksaan merupakan lingkungan tugas yang masuk akal bagi Terra. Catatan pos utara dipertahankan sebagai lokasi historis yang arah pastinya belum dicocokkan; penempatan ini tidak menjadikannya penguasa gerbang atau komandan tanpa sumber.',
 'Ruang untuk Satu Gerobak',
 'Roda sebuah gerobak patah di jalur pemeriksaan Bumi. Orang-orang di belakang mulai mendesak, sementara kusir berusaha menahan muatan agar tidak jatuh mengenai rekannya. Terra menegakkan perisai di sisi jalan dan meminta barisan berhenti.\n\nDengan ruang yang kini kosong, para pengangkut dapat memindahkan peti satu per satu. Seorang pelintas mengeluh bahwa penjaga batu itu hanya memperlambat perjalanan. Lalu ikatan terakhir terlepas dan peti jatuh tepat di tempat kerumunan tadi berdiri. Terra menunggu serpihan disingkirkan sebelum membuka jalan kembali. Tidak ada musuh yang dikalahkan hari itu, tetapi tak seorang pun tertindih.',
 [POST+'Outpost_Bumi.md', COMMAND, WORLD], ['Asal kulit batu belum ditetapkan. Terra–Bumi adalah penempatan usulan; status komandan dan arah utara belum dipastikan. Tidak membuat immunity baru.']),
'Ksatria_Vayu': (
 'Ksatria Avalerion yang membelah formasi dengan badai bercahaya dan perubahan arah yang cepat. Ia dikenal dari hembusan yang datang sebelum sosoknya melintas. Gerakannya membantu menghubungkan bagian medan yang terpisah, membawa tekanan ke titik yang terbuka atau memberi ruang bagi rekan yang harus bergerak mundur.',
 'Siluetnya lebih ramping daripada penjaga berperisai besar. Zirah berlapis mengikuti dada dan paha, dengan sambungan lentur pada pinggang serta lutut. Kain pendek terikat di belakang bahu, memperlihatkan arah angin ketika tubuh berhenti. Cahaya tipis berpilin di sekitar lengan dan kaki saat hembusan dikumpulkan. Ketika melesat, garis cahaya tertinggal sesaat seperti pita yang ditarik dari udara. Rancangan ini menekankan mobilitas tanpa menetapkan senjata khas atau bentuk sayap yang belum dijelaskan dalam entri sumber.',
 'Vayu sigap dan waspada, dengan kebiasaan berbicara singkat saat bertugas. Ia memperhatikan perubahan suasana dan cepat menyadari ketika seorang rekan tertinggal atau enggan meminta bantuan. Kesabarannya mudah diuji oleh perdebatan yang berlarut, terutama ketika ada pesan penting yang harus disampaikan. Meski begitu, ia berusaha memastikan orang lain memahami arahannya sebelum bergerak. Di luar keadaan genting, ia lebih santai dan senang mendengar kabar dari petugas yang baru kembali. Ia bangga pada kecepatannya, tetapi lebih mengutamakan keselamatan rekan daripada kesempatan membuktikan diri melalui pengejaran yang berisiko.',
 'Outpost Bayu di tebing dekat kanopi Astradipa sesuai sebagai usulan tempat tugas Vayu. Pos ini berfokus pada mobilitas udara, serangan cepat, dan dukungan logistik, kadang dibantu Garuda dari Nusa Sayendra. Tepian pelataran serta jalur penghubung di tebing cocok untuk kegiatan pengawasan. Nama Vayu tidak memastikan bahwa ia komandan Bayu, dan catatan lama tentang pos selatan belum mendapatkan pemetaan arah yang pasti.',
 'Pesan Sebelum Badai',
 'Angin berubah saat seorang pembawa pesan mencapai pelataran Bayu. Kain penandanya menegang ke arah berbeda dari awan, dan petugas di tepi tebing menghentikan keberangkatan rombongan. Vayu menunggu satu hembusan lewat sambil memperhatikan pucuk-pucuk kanopi.\n\nIa kemudian bergerak menuju pelataran penghubung, membawa pesan agar rombongan berikutnya bertahan di tempat terlindung. Cahaya melintas pendek di antara batu, lalu hilang di balik dinding pos. Ketika badai menutup pandangan, tidak ada orang yang masih berdiri menunggu di tepian terbuka. Hari itu kecepatannya berguna untuk menyampaikan peringatan sebelum orang lain harus berlari.',
 [POST+'Outpost_Bayu.md', COMMAND, WORLD], ['MD lama menyebut Dragoon Tier 4; JSON menyebut Windrunner Tier 3. Konflik diarsipkan, kelas tidak dipilih ulang. Vayu–Bayu adalah usulan penempatan, bukan penetapan komandan atau arah selatan.'])
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    archive = REPORT / 'pre_avalerion_narrative.json'
    if archive.exists():
        raise SystemExit('Batch already archived; edit current Markdown directly.')
    paths = sorted(FOLDER.glob('*.json'))
    assert {p.stem for p in paths} == set(ENTRIES)
    old = {p.relative_to(ROOT).as_posix(): p.read_text(encoding='utf-8-sig') for p in FOLDER.iterdir() if p.suffix in ('.md','.json')}
    write(archive, old)
    # Baseline covers user edits and the entire runtime before this controlled batch.
    hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.parts and '_audit' not in p.parts and '__pycache__' not in p.parts}
    write(REPORT/'pre_avalerion_hashes.json', hashes)
    db = {n:load(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','Items','Weapons','Armors']}
    for p in paths:
        obj = load(p)
        desc, form, behavior, habitat, story_title, story, sources, unresolved = ENTRIES[p.stem]
        matches = [e for e in db['Enemies'] if e and e['name'] == obj['title']]
        assert len(matches) == 1, p
        enemy = matches[0]
        header = f'---\ntitle: {obj["title"]}\ntags:\n  - Bestiary\n  - Boss\n---\n\n# {obj["title"]}\n'
        for heading, content in [('Deskripsi',desc),('Bentuk',form),('Kepribadian dan Sikap',behavior),('Lokasi Benteng',habitat),('Kisah — '+story_title,story)]:
            header += f'\n## {heading}\n\n{content}\n'
        links = []
        for source in sources:
            assert (ROOT/source).is_file(), source
            links.append('[' + Path(source).stem.replace('_',' ') + '](../../' + quote(source, safe='/') + ')')
        note = 'Rincian rupa, kepribadian dan sikap, penempatan pada pos bernama, dan kisah merupakan pengembangan usulan. Peran dasar mengikuti entri lama; geografi dan fungsi pos mengikuti sumber wilayah.'
        header += '\n> Catatan penulisan: ' + note + ' Acuan: ' + '; '.join(links) + '.\n'
        p.with_suffix('.md').write_text(header, encoding='utf-8')
        previous_status = {k:obj.get(k) for k in ['stat_status','balance_status','source_status']}
        obj['stat_status'] = obj['balance_status'] = 'BLOCKED'
        obj['source_status'] = 'legacy_with_runtime_observation'
        obj['presentation'] = {'markdown_role':'lore_only', 'lore_source':p.with_suffix('.md').relative_to(ROOT).as_posix(),
                               'game_data_source':p.relative_to(ROOT).as_posix(),
                               'narrative_status':'PROPOSED_ADDITIONS', 'approval':None,
                               'scope':'New Avalerion additions; Previous category approvals do not extend to this batch; Thalantira proposal status remains unchanged.',
                               'sync_policy':'Author lore in Markdown; game data stays in JSON.'}
        obj['lore_review'] = {'source_archive':archive.relative_to(ROOT).as_posix(),'sources':sources,
                              'unresolved':unresolved,'category_note':'Civilized Avalerion guardians, not wildlife. Named-post assignments proposed; no automatic commander identity or new military rank.',
                              'historical_description':obj['description']}
        obj['runtime_observation'] = {'status':'OBSERVED_ONLY','source':(GAME/'data/Enemies.json').relative_to(ROOT).as_posix(),
                                     'enemy':enemy,'skills':[db['Skills'][a['skillId']] for a in enemy['actions']],
                                     'drop_records':[{'database':{1:'Items',2:'Weapons',3:'Armors'}[d['kind']],
                                                      'record':db[{1:'Items',2:'Weapons',3:'Armors'}[d['kind']]][d['dataId']]}
                                                     for d in enemy['dropItems'] if d['kind']],
                                     'meaning':'Snapshot only; does not establish calibrated balance.'}
        obj['balance_review'] = {'stat_status':'BLOCKED','previous_status':previous_status,
                                'legacy_note':'Existing top-level numbers preserved for traceability; not recalibrated.',
                                'authority':'06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md',
                                'simulation_result':None,'playtest_evidence':None,
                                'unresolved':['Approved party/gear/progression and encounter targets absent.',
                                              'Runtime placeholders and modifiers require implementation review before calibration.']}
        write(p,obj)
    print('Avalerion narrative batch: 4 Markdown entries; legacy data and runtime snapshots in JSON.')


if __name__ == '__main__':
    main()
