"""Initial archived Agnitra narrative batch; later material revisions live in current files."""
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BEST = ROOT / '07_Bestiary'
FOLDER = BEST / '05_Dragons_of_Agnitra_Nest'
REPORT = BEST / '_audit'
GAME = ROOT / '10_Game Project/Tales of The Dark Time'
WORLD = '02_World/Agnitra.md'
RACE = '04_Ras/02_Wuru Loka/Nagarasven_(Naga).md'
POST = '03_Region/04_Agnitra/Cities & Town/'
COUNCIL = '03_Region/04_Agnitra/Faksi & Institusi/Dewan Keseimbangan Agnitra.md'

ENTRIES = {
'Blackhorn': (
 'Naga berlapis baja hitam yang menyemburkan magma murni. Saat berdiam di lereng Mahasvara, tubuhnya menyerupai bongkah vulkanik yang belum kehilangan panas. Ia merupakan penjaga yang mampu menimbang maksud pendatang; keheningannya memberi waktu untuk menjelaskan tujuan, tetapi bukan izin untuk melewati batas sarang.',
 'Tubuhnya berat pada dada dan bahu, ditopang empat kaki bercakar lebar. Lempeng sisik hitam saling menindih sepanjang punggung, sementara sambungan di leher memungkinkan kepalanya bergerak tanpa membuka banyak celah. Sepasang tanduk gelap mengarah ke belakang, dengan permukaan kasar seperti batu yang berkali-kali mendingin. Sayap terlipat rapat pada sisi tubuh. Cahaya jingga tampak di sela rahang ketika magma terkumpul, kemudian memantul pada bagian bawah tanduk. Ekor tebal menyapu debu saat ia mengubah tumpuan.',
 'Blackhorn pendiam dan berhati-hati dalam memberi kepercayaan. Ia lebih menghargai jawaban yang terus terang daripada pujian terhadap kekuatannya. Pendatang yang mengakui keterbatasan akan didengarkan, sedangkan orang yang terus mendesak dapat mendapati percakapan berakhir tanpa peringatan kedua. Kesabarannya disertai kekakuan: ia kadang terlalu lama mempertahankan keputusan awal meskipun keadaan sudah berubah. Namun, tanggung jawab terhadap sarang membuatnya bersedia mendengar penjelasan baru sebelum memilih tindakan yang tidak dapat ditarik kembali.',
 'Lereng bawah Gunung Mahasvara merupakan lokasi lama Blackhorn. Ceruk luas pada batu vulkanik diusulkan sebagai ruang istirahat, dengan teras terbuka untuk mengawasi jalan naik. Adamantine Nest memang berada di dasar lereng barat dan memiliki penjaga berzirah alami, tetapi belum ada sumber yang memastikan Blackhorn sebagai pemimpin atau anggota klan tersebut. Penempatan sarangnya tetap pada lereng bawah tanpa menetapkan arah baru.',
 'Jawaban di Bawah Tanduk',
 'Seorang pembawa pesan berhenti di depan sosok hitam yang menutupi jalan. Ia telah menyiapkan banyak pujian, tetapi lupa kalimat pertama ketika mata Blackhorn terbuka. Naga itu hanya menanyakan keperluannya.\n\nPembawa pesan mengakui bahwa ia tidak mengetahui jalan berikutnya dan takut salah memasuki sarang. Blackhorn lama tidak menjawab. Lalu kepalanya bergeser, memperlihatkan jalan yang semula tertutup bayangan tanduk. Ia memberi petunjuk menuju tempat pemeriksaan dan meminta orang itu menunggu pengawalan. Pesan tersebut akhirnya dapat diteruskan karena pembawanya berani mengaku tidak tahu, bukan karena berhasil membuat sang penjaga terkesan.',
 [WORLD, RACE, POST+'Adamantine Nest.md', POST+'Pyrowisp Caldera.md'], ['Klan dan status pemimpin belum dipastikan; kemiripan zirah bukan bukti Adamantine. Mikrohabitat, bentuk rinci, kepribadian, dan kisah usulan. Elemen legacy Api/Besi berbeda dengan runtime Earth/Fire; tidak direkonsiliasi sepihak.']),
'Goldenscale': (
 'Naga keemasan yang melepaskan berkas cahaya suci dengan panas luar biasa, digambarkan dalam catatan lama seperti suhu matahari. Kilau sisiknya dapat terlihat sebelum tubuhnya terpisah dari terang puncak Mahasvara. Kekuatan itu tidak selalu dilepaskan; kemampuannya menahan serangan menjadi bagian penting dari kewibawaan seorang penjaga berakal.',
 'Sisik emas menutupi leher panjang dan dada, dengan bidang lebih besar pada bahu serta punggung. Tepian sisik memantulkan cahaya dengan warna kemerahan ketika kepala bergerak. Sayap lebar memiliki selaput lebih pucat, sehingga tulang penyangganya terlihat sebagai garis gelap saat diterangi dari belakang. Tanduk melengkung membingkai kepala, dan mata terang tampak di bawah tonjolan alis. Sebelum berkas dilepaskan, cahaya mengumpul di rahang hingga bayangan pada bebatuan sekitarnya menjadi tajam. Warna emas tersebut tidak memastikan bahan logam penyusun sisiknya.',
 'Goldenscale menjaga tutur kata dan mengharapkan kesungguhan yang sama dari tamunya. Ia senang mendengar pertanyaan yang dipikirkan baik-baik, tetapi tidak mudah terkesan oleh gelar atau keberanian yang dipamerkan. Harga dirinya membuat koreksi terasa sulit diterima pada awalnya; ia memilih diam sebelum menilai kembali alasan lawan bicara. Terhadap orang yang ceroboh, sikapnya dingin dan tegas. Ia lebih menghormati kesediaan memperbaiki kesalahan daripada permintaan maaf yang diulang tanpa perubahan tindakan.',
 'Puncak timur Gunung Mahasvara adalah lokasi yang tercatat. Sebuah teras batu menghadap cahaya pagi diusulkan sebagai tempat berdiamnya. Kawasan timur juga memuat Mithril Nest, sementara Orichalcum Nest berada di selatan kawah utama. Kilau emas dan kekuatan sihir Goldenscale belum menjadi dasar untuk memindahkan sarangnya ke selatan atau menetapkannya sebagai pemimpin Orichalcum.',
 'Cahaya yang Ditahan',
 'Seorang pengunjung yang memperoleh pengawalan tiba di teras puncak dan meminta melihat semburan sang naga. Ia menyebutnya bukti keagungan, seolah permintaan itu merupakan penghormatan. Goldenscale mengarahkan pandangan ke lereng di bawah mereka.\n\nDi sana, rombongan lain masih berjalan melintasi batu. Sang pengunjung akhirnya memahami apa yang tidak ia perhitungkan. Ia menarik permintaannya dan menunggu sampai seluruh rombongan mencapai perlindungan. Goldenscale tetap tidak menyemburkan cahaya. Percakapan mereka baru dimulai setelah tamunya berhenti menganggap kekuatan penjaga sebagai pertunjukan yang dapat diminta sesuka hati.',
 [WORLD, RACE, POST+'Mithril Nest.md', POST+'Orichalcum Nest.md'], ['Afiliasi klan belum ditetapkan; lokasi timur dipertahankan. Suhu matahari adalah gambaran lore, bukan angka fisika/rumus damage. Serangan lore berkas cahaya berbeda dari label runtime Melee; kedua catatan dipertahankan.']),
'Moonfang': (
 'Naga penyergap senyap yang menyemburkan api dingin hingga membekukan. Ketiadaan suara membuat kehadirannya sulit diperkirakan dalam gua Agnitra. Julukan pembunuh dalam catatan lama menggambarkan cara serangannya, tetapi tidak menjelaskan seluruh wataknya atau membuktikan bahwa ia telah kehilangan akal budi menjadi naga Feral.',
 'Tubuhnya memanjang dengan dada lebih ramping dan kaki yang dapat ditekuk rendah. Sisik kelabu gelap mengurangi kilau di lorong, sementara warna pucat mengikuti rahang hingga ujung taring. Sayap dilipat dekat punggung agar tepian tidak menyeret dinding. Tanduk pendek mengikuti lengkung kepala, menyisakan siluet yang tidak mudah tersangkut pada batu. Ketika bernapas, uap tipis keluar sebelum nyala pucat muncul di sela gigi. Embun beku yang tertinggal pada batu membuat jalur lewatnya tampak berbeda dari dinding gua yang masih hangat.',
 'Moonfang tertutup dan peka terhadap cara orang menghormati ruang pribadinya. Ia mendengarkan lebih lama daripada berbicara, lalu mengajukan pertanyaan singkat yang langsung menyentuh maksud kunjungan. Sikap tenangnya dapat terasa mengintimidasi bagi tamu yang terbiasa mendapat sambutan ramah. Ia tidak menyukai tipu daya, tetapi juga enggan mengungkapkan banyak tentang dirinya. Kepercayaan tumbuh melalui janji kecil yang ditepati. Saat marah, ia semakin hemat kata; keputusan untuk mengakhiri pertemuan lebih mungkin disampaikan dengan menutup jalan daripada berdebat panjang.',
 'Gua Gelap Agnitra merupakan lokasi lama, tanpa koordinat atau nama nest regional yang sudah dipastikan. Ruang dalam dengan celah udara dan jalur masuk sempit diusulkan sebagai bagian sarangnya. Silver Nest berada di lembah bersalju utara, namun kesamaan unsur dingin belum memastikan Moonfang tinggal di sana. Ia juga tidak otomatis menjadi penjaga Adamantine hanya karena memilih gua.',
 'Janji di Mulut Gua',
 'Seorang utusan meninggalkan penanda di mulut gua dan menunggu seperti yang telah dijanjikan. Lama tidak ada jawaban. Ketika udara mulai dingin, ia tergoda melangkah masuk untuk memastikan bahwa penanda itu terlihat.\n\nIa tetap di tempat. Dari kegelapan, Moonfang menanyakan mengapa ia belum pergi. Utusan itu menjawab bahwa ia telah berjanji menunggu sampai diminta kembali. Kepala pucat muncul melewati batas bayangan. Pertemuan berlangsung singkat, tetapi pada kunjungan berikutnya sang utusan tidak lagi harus menjelaskan siapa dirinya. Moonfang mengingat orang yang tidak mengubah janji hanya karena tidak ada yang tampak mengawasi.',
 [WORLD, RACE, POST+'Silver Nest.md', POST+'Adamantine Nest.md'], ['Gua Gelap belum dipetakan; afiliasi Silver/Adamantine dan status Feral tidak diasumsikan. Api dingin tidak menambah state pembekuan atau durasi baru. Bentuk, kepribadian, dan kisah usulan.']),
'Silverwing': (
 'Naga penguasa badai api yang beroperasi di langit kawah Mahasvara. Sayapnya membawa terang melintasi abu, sementara hembusan di sekeliling tubuh mengubah arah bara. Ia melihat jalur udara sebagai ruang yang harus dipahami sebelum dikuasai; kemampuan bergerak cepat tidak menghilangkan kewajiban memperhatikan mereka yang terbang di belakangnya.',
 'Sepasang sayap lebar berkilau perak menjadi ciri paling menonjol. Selaputnya memperlihatkan garis kemerahan ketika diterangi magma dari bawah, berbeda dari sisi atas yang memantulkan langit. Tubuhnya ramping dengan leher melengkung dan ekor panjang sebagai penyeimbang. Cakar belakang terlipat dekat perut saat meluncur, sedangkan sisik di bahu menebal pada pangkal sayap. Bara berputar mengikuti hembusan ketika ia mengerahkan badai api. Kilau perak pada sayap tidak dengan sendirinya menunjukkan bahwa tubuhnya tersusun dari Mithril atau perak murni.',
 'Silverwing terbuka dalam percakapan dan mudah tertarik pada tantangan yang menuntut keterampilan. Ia senang membandingkan pengalaman penerbangan, tetapi kadang terlalu cepat mengira orang lain mampu mengikuti kecepatannya. Ketika menyadari kekeliruan itu, ia berusaha menyesuaikan langkah tanpa mempermalukan yang tertinggal. Dalam keadaan genting, pembawaannya menjadi singkat dan terarah. Kebanggaannya sebagai penerbang harus berhadapan dengan tanggung jawab menjaga jalur: ia bersedia membatalkan lintasan yang mengesankan bila risikonya membahayakan orang lain.',
 'Langit kawah Mahasvara adalah wilayah jelajah yang tercatat. Bibir kawah dengan pelataran lebar diusulkan sebagai tempat mendarat dan beristirahat. Lokasi ini berdekatan dengan kehidupan Pyrowisp Caldera, tanpa menjadikannya anggota Dewan Keseimbangan. Mithril Nest memang berperan dalam pertahanan udara, tetapi belum ada penetapan klan Silverwing. Silver Nest di lembah utara juga tidak disamakan dengan sarangnya berdasarkan nama.',
 'Putaran yang Dibatalkan',
 'Silverwing memimpin penerbangan melintasi sisi kawah ketika abu naik lebih tinggi dari biasanya. Seekor naga muda mencoba mengikuti putarannya, lalu kehilangan jarak dan mulai turun terlalu dekat dengan arus panas.\n\nSilverwing membatalkan lintasan, berbalik lebar, dan mengarahkan penerbangan menuju tempat mendarat. Naga muda itu meminta maaf karena memperlambat perjalanan. Sang penjaga mengakui bahwa ia telah memilih kecepatan tanpa memeriksa kemampuan pengikutnya. Mereka menunggu abu mereda sebelum mencoba lagi. Kali ini Silverwing terus menoleh, memastikan keberhasilan perjalanan dihitung dari siapa yang tiba bersama, bukan siapa yang paling dahulu mencapai ujungnya.',
 [WORLD, RACE, POST+'Pyrowisp Caldera.md', POST+'Mithril Nest.md', POST+'Silver Nest.md', COUNCIL], ['Klan Mithril/Silver dan keanggotaan dewan belum ditetapkan. Pelataran istirahat, bentuk, kepribadian, serta kisah usulan. Tidak menambah kemampuan transformasi atau material drop.'])
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    archive = REPORT / 'pre_agnitra_narrative.json'
    if archive.exists():
        raise SystemExit('Batch already archived; edit current Markdown directly.')
    paths = sorted(FOLDER.glob('*.json'))
    assert {p.stem for p in paths} == set(ENTRIES)
    old = {p.relative_to(ROOT).as_posix(): p.read_text(encoding='utf-8-sig') for p in FOLDER.iterdir() if p.suffix in ('.md','.json')}
    write(archive, old)
    # Baseline covers user edits and the entire runtime before this controlled batch.
    hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.parts and '_audit' not in p.parts and '__pycache__' not in p.parts}
    write(REPORT/'pre_agnitra_hashes.json', hashes)
    db = {n:load(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','Items','Weapons','Armors']}
    for p in paths:
        obj = load(p)
        desc, form, behavior, habitat, story_title, story, sources, unresolved = ENTRIES[p.stem]
        matches = [e for e in db['Enemies'] if e and e['name'] == obj['title']]
        assert len(matches) == 1, p
        enemy = matches[0]
        header = f'---\ntitle: {obj["title"]}\ntags:\n  - Bestiary\n  - Boss\n---\n\n# {obj["title"]}\n'
        for heading, content in [('Deskripsi',desc),('Bentuk',form),('Kepribadian dan Sikap',behavior),('Lokasi Nest',habitat),('Kisah — '+story_title,story)]:
            header += f'\n## {heading}\n\n{content}\n'
        links = []
        for source in sources:
            assert (ROOT/source).is_file(), source
            links.append('[' + Path(source).stem.replace('_',' ') + '](../../' + quote(source, safe='/') + ')')
        note = 'Rincian bentuk, kepribadian dan sikap, mikrohabitat nest, serta kisah merupakan usulan. Lokasi lama dipertahankan; afiliasi klan dan jabatan belum ditetapkan.'
        header += '\n> Catatan penulisan: ' + note + ' Acuan: ' + '; '.join(links) + '.\n'
        p.with_suffix('.md').write_text(header, encoding='utf-8')
        previous_status = {k:obj.get(k) for k in ['stat_status','balance_status','source_status']}
        obj['stat_status'] = obj['balance_status'] = 'BLOCKED'
        obj['source_status'] = 'legacy_with_runtime_observation'
        obj['presentation'] = {'markdown_role':'lore_only', 'lore_source':p.with_suffix('.md').relative_to(ROOT).as_posix(),
                               'game_data_source':p.relative_to(ROOT).as_posix(),
                               'narrative_status':'PROPOSED_ADDITIONS', 'approval':None,
                               'scope':'New Agnitra additions; Previous category approvals do not extend to this batch; Thalantira proposal status remains unchanged.',
                               'sync_policy':'Author lore in Markdown; game data stays in JSON.'}
        obj['lore_review'] = {'source_archive':archive.relative_to(ROOT).as_posix(),'sources':sources,
                              'unresolved':unresolved,'category_note':'Nagarasven berakal di Agnitra; klan, status pemimpin nest, dan status Feral tidak diasumsikan dari nama atau warna.',
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
    print('Agnitra narrative batch: 4 Markdown entries; legacy data and runtime snapshots in JSON.')


if __name__ == '__main__':
    main()
