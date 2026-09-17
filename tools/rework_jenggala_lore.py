"""One-time, archived Jenggala lore batch. No runtime writes or new balance numbers."""
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BEST = ROOT / '07_Bestiary'
FOLDER = BEST / '02_Jenggala'
REPORT = BEST / '_audit'
GAME = ROOT / '10_Game Project/Tales of The Dark Time'

ARK = '03_Region/05_Arkananta/Threat.md'
AST = '03_Region/02_Astradipa/Threat.md'
VAL = '03_Region/01_Mandala Kingdom/Cities & Town/Valkindra.md'
HER = '03_Region/01_Mandala Kingdom/Cities & Town/Hermindar.md'
ART = '03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md'
RAK = '02_World/Raksamala.md'
PRO = '08_Story/02_Prologue/03_Teror_di_Pesisir_Timur.md'

# Description, appearance, behavior, habitat, story title, story, sources, unresolved.
ENTRIES = {
'Ahool': (
 'Kelelawar purba raksasa yang membuat mulut gua terasa sempit ketika sayapnya terbentang. Ahool dikenal sebagai pembawa wabah; tempat bertengger yang ditinggalkannya tetap diperlakukan dengan waspada oleh penjelajah. Suara kepakannya dapat terdengar sebelum tubuhnya keluar dari kegelapan, tetapi gema gua menyulitkan orang memperkirakan arah kedatangannya.',
 'Tubuhnya berat pada dada dan bahu, dengan selaput sayap membentang di antara jemari yang panjang. Bulu gelap menutupi punggung serta tengkuk, sedangkan selaputnya tampak tipis dan berurat jika diterangi dari belakang. Kepala bermoncong pendek, telinga lebar, dan cakar melengkung memberinya siluet yang berbeda dari burung pemangsa. Ketika menggantung, sayap terlipat mengurung tubuh seperti mantel kusut. Rincian visual ini mengembangkan wujud kelelawar purba yang sudah tercatat.',
 'Buas ketika memburu dan sangat defensif di tempat bertengger. Cahaya yang mendadak diarahkan ke sarangnya atau suara benturan berulang dapat memancing terjangan keluar. Ia menggunakan ruang gelap dan ketinggian untuk mendekat, lalu mundur ke langit-langit bila jalur depannya tertutup. Sifat pembawa wabah tidak berarti setiap sentuhan pasti menularkan penyakit; cara penularannya belum dijelaskan dalam lore.',
 'Gua Arkananta merupakan habitat existing. Mulut gua besar, lorong tinggi, dan celah tebing di lereng luar cocok sebagai tempat bertengger yang diusulkan. Kehadirannya perlu dibedakan dari penduduk gua Butoraksa, Troliogoro, dan Rakshorien; tidak ada bukti bahwa mereka semua memelihara atau menguasai Ahool.',
 'Atap yang Bergerak',
 'Seorang pencari mineral mengira langit-langit gua Arkananta tertutup kain hitam yang ditinggalkan rombongan terdahulu. Rekannya melihat goresan cakar pada batu dan menghentikan langkahnya sebelum obor diangkat lebih tinggi.\n\nKetika angin bergerak dari dalam, kain itu membuka diri menjadi sepasang sayap. Mereka mundur meninggalkan karung batu di dekat pintu. Dari lereng, pencari mineral menyaksikan sesuatu yang terlalu besar untuk lorong tadi melintas di atasnya. Ia baru memahami bahwa gua tersebut tidak kosong; pemiliknya hanya sedang tidur.',
 [ARK], ['Mekanisme wabah belum ditentukan; tidak menambah state penyakit.']),
'Banshee': (
 'Hantu wanita yang dikenal pula dengan sebutan Kuntilanak. Jerit Banshee bukan sekadar suara untuk menakut-nakuti: getarannya dapat mengguncang pertahanan dan memecah ketenangan orang yang menghadapinya. Sosoknya sering lebih dahulu dikenali dari arah tangisan yang tidak sesuai dengan tempat tubuhnya terlihat.',
 'Wujudnya menyerupai perempuan berambut panjang, dengan wajah pucat yang sebagian tertutup helaian gelap. Kain lusuh menggantung dari bahu dan bergerak seolah tertarik angin yang tidak menyentuh daun di sekitarnya. Saat menjerit, rahang terbuka lebar dan garis wajah yang semula samar menjadi tajam. Rupa ini tidak menambahkan sayap atau tubuh burung; ancamannya tetap terletak pada manifestasi hantu dan kekuatan suara.',
 'Berbahaya dan tidak dapat dinilai seperti satwa yang sedang mencari makan. Dalam pengembangan perilaku ini, ia mengawasi pendatang dari dekat pohon tempat kemunculannya sebelum mengeluarkan tangisan. Orang yang terus mendekat dapat memancing jeritan yang lebih keras. Tindakan tampak mengundang atau menyerupai kesedihan tidak membuktikan bahwa ia meminta pertolongan, maupun bahwa setiap Banshee berasal dari kisah kematian yang sama.',
 'Pohon beringin raksasa adalah lokasi sumber tanpa region pasti. Tepian hutan tua di sekitar Hermindar diusulkan sebagai penempatan yang cocok. Tidak semua pohon beringin ditetapkan berhantu, dan bentuk roh tidak otomatis memastikan bahwa Banshee termasuk Dhemit.',
 'Tangis di Balik Batang',
 'Seorang pembawa kayu dari luar Hermindar mendengar perempuan menangis di balik pohon besar. Ia meletakkan bebannya, tetapi orang yang berjalan bersamanya justru memperhatikan daun: tidak satu pun bergerak meskipun kain putih di dekat batang berkibar.\n\nMereka mundur. Tangisan itu berubah menjadi jeritan, membuat ikatan pada tumpukan kayu bergetar. Setelah mencapai jalan terbuka, pembawa kayu menyadari bahwa sejak awal tidak pernah terdengar suara napas di sela tangisan tersebut.',
 [HER], ['Hubungan Banshee/Kuntilanak dengan Dhemit belum diputuskan.']),
'Direboar': (
 'Babi siluman raksasa yang juga disebut Celeng Ngepet. Lapisan hitam menyerupai baja membuat tubuhnya tampak seperti bongkah logam bergerak di antara pepohonan. Berbeda dari Babi Hutan yang menyerbu untuk membuka jalan keluar, Direboar dalam catatan serangan Jenggala dapat terus menerjang ke arah kerumunan.',
 'Bahu menjulang di atas kepala rendah, dengan moncong lebar dan taring besar melengkung di kedua sisi rahang. Punggungnya berlapis kulit hitam keras yang memantulkan cahaya dalam bidang-bidang kusam. Bulu kasar menonjol di sela lipatan leher dan sepanjang tengkuk. Kaki pendek serta tebal menahan tubuh yang sangat berat. Istilah kulit baja dipertahankan dari sumber, tanpa menetapkan bahwa tubuhnya merupakan bijih yang dapat ditambang.',
 'Sangat agresif ketika menerobos atau mengejar. Ia menggesekkan taring, menghentakkan kaki, dan merendahkan kepala sebelum serbuan terbuka, tetapi tutupan hutan dapat menyembunyikan tanda tersebut. Setelah terhalang, ia berusaha mencari celah untuk menerjang lagi. Sebutan Celeng Ngepet tidak otomatis membuktikan bahwa setiap individu merupakan manusia yang berubah demi mencuri kekayaan; mekanisme asal itu belum ada dalam canon Nusvanir.',
 'Hutan Bayangan adalah habitat lama yang belum terpetakan. Kawasan berhutan Raksamala diusulkan sebagai penempatan, sedangkan kemunculannya melalui portal di pesisir Aqualis sudah tercatat dalam Prologue. Lokasi penyerbuan tidak harus menjadi habitat alaminya.',
 'Di Belakang Gerobak',
 'Dalam kisah tambahan tentang dampak serbuan di pesisir Mandala, seorang pengangkut memilih berlindung di balik gerobak kosong. Derap berat mendekat dari antara rumah. Ketika moncong hitam muncul, ia meninggalkan perlindungannya dan berlari ke celah dinding.\n\nGerobak itu terangkat oleh taring sebelum jatuh dalam serpihan. Ia selamat bukan karena membawa senjata lebih kuat, melainkan karena berhenti menganggap kayu tipis sebagai tembok. Kisah ini tidak menambahkan peran baru pada tokoh utama Prologue.',
 [RAK, PRO], ['Hutan Bayangan belum terpetakan; asal transformasi Celeng Ngepet belum ditetapkan.']),
'Goblin': (
 'Penghuni gua bertubuh pendek yang dikenal sebagai Ebu Gogo. Goblin menjadi jauh lebih berani ketika bergerombol: suara dari depan dapat menutupi gerakan anggota lain di sisi jalan. Mereka tidak perlu mengalahkan rombongan sekaligus untuk membahayakannya; cukup membuat seorang pengelana tertinggal.',
 'Tubuhnya pendek dengan bahu membungkuk, lengan relatif panjang, dan jemari yang kuat untuk mencengkeram batu. Wajah lebar, alis menonjol, serta rambut kasar yang tidak rata memperkuat kesan penghuni lorong lembap. Kulit berwarna tanah kusam dan kuku kotor melengkapi rancangan rupanya. Ia tidak diberi telinga atau ciri ras Asrivana hanya karena namanya menggunakan istilah Goblin; Ebu Gogo tetap menjadi acuan identitas yang tercatat.',
 'Beringas dalam kelompok tetapi lebih berhati-hati ketika sendirian. Mereka mengintai jalur sempit, saling memanggil, lalu mendekat setelah lawan kehilangan arah. Individu yang terluka dapat mundur ke celah sementara anggota lain mengalihkan perhatian. Pola ini menggambarkan koordinasi kawanan, bukan bukti bahwa mereka memiliki kerajaan, kasta, atau kebudayaan yang belum ditulis.',
 'Sistem gua merupakan habitat existing. Gua pada lereng luar Arkananta diusulkan sebagai penempatan regional yang sesuai. Prologue juga mencatat Goblin keluar dari portal yang dibuka Wight di pesisir Aqualis; ini merupakan rute invasi, bukan alasan menjadikan Goblin fauna pantai.',
 'Suara dari Lorong Kiri',
 'Pemandu rombongan di lereng Arkananta mendengar teriakan dari lorong kiri, tetapi melihat debu jatuh dari celah kanan. Ia meminta semua orang tetap berjalan rapat. Seorang pengangkut hampir memisahkan diri untuk mengejar sosok kecil yang memperlihatkan kantong bekalnya.\n\nBaru setelah obor kedua diarahkan ke kanan, tampak beberapa tangan menggenggam tepian batu. Rombongan itu mundur bersama. Teriakan berhenti begitu tidak ada lagi orang yang mau masuk sendirian.',
 [ARK, PRO], ['Gua regional adalah usulan; Ebu Gogo dipertahankan sebagai alias, bukan ras baru.']),
'Gondarwa': (
 'Raksasa hutan berbulu tebal yang kehadirannya dapat dikenali dari jalur tumbuhan yang patah pada ketinggian tidak biasa. Gondarwa mengandalkan kekuatan tubuh, bukan rupa senjata yang dibawanya. Kesunyian sesaat sebelum ia bergerak lebih berbahaya daripada suara langkahnya yang sudah menjauh.',
 'Tubuhnya tinggi dan lebar, dengan lengan berat yang menggantung di sisi paha. Bulu kusut menutupi bahu, dada, serta punggung; serpihan kulit kayu dan daun dapat tersangkut di dalamnya. Wajah sebagian tenggelam di balik rambut, menyisakan mata dalam dan rahang besar. Warna cokelat gelap serta hitam tanah dipilih untuk menyatu dengan batang tua. Wujud berbulu tidak menjadikannya Hanorok atau kerabat yang sudah dipastikan.',
 'Teritorial dan mudah menjadi ganas ketika jalur atau tempat berdiamnya diganggu. Ia dapat merobohkan semak, menghantam batang, atau mengentakkan kaki sebagai tanda kehadiran sebelum mendekat. Pendatang yang terus menekan dapat memancing serangan langsung. Diet dan susunan kelompoknya belum cukup jelas untuk menyatakan bahwa ia selalu memangsa manusia atau hidup sebagai penjaga hutan yang baik hati.',
 'Catatan Jenggala Dalam menjelaskan habitat yang rapat tetapi bukan region administratif. Lantai hutan Astradipa yang jauh dari jalur aman diusulkan sebagai lokasi kemunculan. Ancaman Jenggala terhadap Akar-Dipa mendukung konteks perjumpaan tersebut, tanpa menjadikan seluruh hutan sebagai wilayah Gondarwa.',
 'Batang yang Tidak Ditebang',
 'Sebuah patroli Asrivana menemukan pohon muda patah di tengah jalur bawah Astradipa. Tidak ada bekas kapak. Serat batang terpelintir seolah diremas dari kedua arah. Penjaga terdepan hendak melewatinya ketika tanah bergetar dari sisi rimbun.\n\nMereka mengubah jalur dan menandai lokasi itu untuk patroli berikutnya. Di belakang, terdengar satu hantaman berat pada kayu. Tidak ada pengejaran, tetapi mereka tidak kembali untuk memastikan apakah peringatan kedua akan tetap berupa suara.',
 [AST], ['Asal spesies, diet, dan hubungan dengan Hanorok belum ditetapkan.']),
'Gremlin': (
 'Makhluk kecil gesit yang dikenal sebagai Tuyul, pengincar koin dan barang bawaan. Gremlin menyukai saat orang sibuk memperhatikan sesuatu yang lain. Bunyi uang jatuh dapat menjadi jejak kehadirannya, tetapi barang yang hilang tidak selalu berada pada arah suara terakhir.',
 'Tubuhnya kecil dengan kepala tampak besar, bahu sempit, dan lengan yang berakhir pada jemari panjang. Kulit pucat kelabu, rambut tipis, serta mata gelap memberi rupa yang samar-samar menyerupai boneka hidup ketika dilihat dari jauh. Kaki ramping memudahkannya menyelinap di bawah gerobak. Rancangan ini tidak memberinya sayap atau menjadikannya anak dari ras fana tertentu; sebutan Tuyul digunakan sesuai entri lama.',
 'Licik dan oportunistis, lebih sering mencuri daripada menghadapi lawan secara terbuka. Ia menunggu kantong terbuka, mengambil benda kecil, lalu berlari menuju tempat sempit. Ketika tertangkap atau terpojok, ia dapat menggigit dan mencakar. Tindakan yang tampak bermain-main tetap merugikan korbannya; tidak ada aturan canon bahwa ia harus dipelihara atau dikendalikan seorang majikan.',
 'Jalan setapak pada malam hari adalah habitat perjumpaan existing. Jalur pengangkutan di luar Hermindar diusulkan sebagai penempatan karena banyak barang melewati batas hutan dan permukiman. Tidak perlu menjadikannya penyebab semua pencurian di Cakrawala, yang ancaman utamanya sudah dijelaskan sebagai kriminalitas fana.',
 'Koin untuk Jalan Pulang',
 'Seorang pembawa perkakas dari Hermindar mendengar koin berdenting di belakang gerobak. Ia hampir meninggalkan kendali untuk mengejarnya, tetapi melihat jemari pucat masih menyelip di bawah penutup muatan. Ia segera menghentikan gerobak dan memanggil rekannya.\n\nSosok kecil melompat turun sambil membawa kantong kosong. Koin yang tercecer dikumpulkan bersama sebelum perjalanan dilanjutkan. Malam itu, kehilangan terbesar ternyata bukan uang, melainkan waktu yang mereka habiskan memeriksa setiap simpul.',
 [HER], ['Majikan, asal, dan mekanisme pencurian supernatural belum ditetapkan.']),
'Homunculus': (
 'Boneka kuno parasit yang juga disebut Jenglot. Homunculus dapat disangka benda temuan sampai ia menempel pada makhluk hidup dan perlahan mengisap daya hidupnya. Bahayanya terletak pada kedekatan: tubuh kecil membuatnya mudah dibawa keluar dari reruntuhan oleh orang yang merasa telah menemukan pusaka.',
 'Wujudnya kecil dan kaku, menyerupai figur yang mengering bersama usia. Rambut panjang tidak sebanding dengan ukuran kepala, jemari tipis melengkung ke dalam, dan kuku tampak menonjol pada tangan serta kaki. Permukaan tubuh menyerupai kulit tua yang berkerut, bukan batu pahatan. Mata yang nyaris tertutup serta mulut sempit menyulitkan orang membedakannya dari benda mati. Tidak ditetapkan siapa pembuatnya atau bahan ritual yang melahirkannya.',
 'Tidak menunjukkan keganasan melalui serbuan terbuka. Ia menunggu kontak atau kesempatan menempel, sehingga ketenangannya justru menipu. Korban yang menganggapnya jimat dapat terlambat menyadari bahwa rasa lemah datang setelah benda itu dibawa. Jika ditemukan pada tubuh atau barang bawaan, bentuknya yang kecil tidak boleh dianggap bukti ia aman. Jalur pemurnian dan efek parasit spesifik masih memerlukan sumber tersendiri.',
 'Reruntuhan kuil merupakan lokasi lama. Kompleks kuno di sekitar Valkindra cocok sebagai usulan penempatan karena lore wilayah tersebut sudah memuat penyelidikan sihir terlarang dan reruntuhan. Ini bukan pernyataan bahwa kuil aktif atau seluruh pemujaan di Mandala menciptakan Homunculus.',
 'Temuan dalam Lipatan Kain',
 'Seorang pembantu ekspedisi dari Valkindra menyelipkan figur kecil ke dalam kain, berharap menjualnya setelah pulang. Sepanjang perjalanan ia terus meminta rombongan berhenti, padahal bawaannya paling ringan.\n\nKetika kainnya dibuka untuk mencari perbekalan, figur itu tidak lagi berada di tempat semula. Jari-jari keringnya mencengkeram bagian dalam lengan baju. Pemimpin ekspedisi menghentikan perjalanan menuju pasar dan membawa temuan itu beserta pembawanya untuk diperiksa. Tidak seorang pun menyebutnya cendera mata lagi.',
 [VAL], ['Asal penciptaan, ritual, dan metode pemurnian belum dipastikan.']),
'Leyak': (
 'Penyihir iblis dengan tubuh yang mengalami mutasi hewani dan serangan berupa kutukan. Leyak berbahaya karena lawan dapat terlalu sibuk mengamati perubahan rupanya hingga mengabaikan gerakan merapal. Bentuk hewan yang tampak pada tubuhnya tidak cukup untuk menentukan dari ras mana ia berasal.',
 'Siluet dasarnya menyerupai sosok tegak, tetapi proporsi anggota tubuh tidak lagi serasi. Dalam rancangan ini, jari memanjang menjadi cakar, punggung membungkuk, dan bagian wajah bercampur dengan rahang atau gigi hewani. Rambut kusut serta kain koyak menutup sebagian perubahan sehingga bentuknya sulit dikenali dalam gelap. Mutasinya tidak ditetapkan selalu sama pada setiap individu dan tidak disamakan dengan kepala terbang Strigoi.',
 'Agresif dengan cara mengintimidasi dan mengutuk, bukan sekadar menerkam. Ia dapat mempertahankan jarak, mencari penghalang, atau memanfaatkan kepanikan untuk melanjutkan rapalan. Sosok yang mundur belum tentu menyerah. Meski disebut penyihir dalam entri lama, kemampuan merapal tidak digunakan untuk memutuskan konflik tentang kesadaran Dhemit atau membuktikan bahwa semua Leyak berasal dari golongan tersebut.',
 'Lokasi lama Pulau Asrivana belum memiliki padanan wilayah yang terverifikasi. Tepi hutan Astradipa yang mengalami gangguan sihir gelap merupakan usulan penempatan berdasarkan ancaman regional. Usulan ini tidak menyatakan Astradipa adalah pulau maupun bahwa Asrivana berubah menjadi Leyak.',
 'Bayangan di Akar Pohon',
 'Seorang penjaga Akar-Dipa melihat bayangan manusia membungkuk di antara akar, tetapi tangan yang keluar darinya berakhir dengan cakar. Ia tidak segera mengejar. Dari balik pohon lain, rekannya melihat bibir sosok itu terus bergerak meskipun tubuhnya tampak sedang bersembunyi.\n\nMereka memanggil bantuan dan menutup jalur warga sebelum mendekat. Ketika bayangan itu berpindah, yang ditinggalkannya bukan korban yang berhasil dipancing keluar, melainkan jalan yang sudah kosong.',
 [AST], ['Pulau Asrivana belum terpetakan; hubungan Leyak dengan ras/Dhemit tidak diputuskan.']),
'Lycan': (
 'Manusia harimau beraura petir yang dikenal sebagai Cindaku. Lycan Nusvanir dikenali dari perpaduan tubuh humanoid, ciri harimau, dan kilatan listrik di sekitar gerakannya. Namanya tidak menjadikannya manusia serigala atau makhluk yang harus berubah ketika bulan purnama.',
 'Tubuhnya tegak dan berotot dengan bahu lebar, tangan bercakar, serta tungkai yang dapat merendah ketika bersiap melompat. Rancangan bulu belang memadukan kuning tua dan hitam, sementara wajah mempertahankan perpaduan tatapan manusia dengan moncong serta kumis harimau. Bulu tengkuk terangkat ketika aura petir menguat; kilatan pendek tampak menyusuri garis tubuh, bukan perhiasan logam yang dikenakannya.',
 'Waspada, teritorial, dan sangat berbahaya ketika memilih menyerang. Ia dapat mengamati pendatang sebelum menunjukkan gigi atau merendahkan tubuh. Serangannya mengandalkan lompatan dan cakar, sementara aura petir mempertegas ancaman yang sudah tercatat. Perilaku ini tidak menetapkan bahwa ia selalu jahat, dapat dijinakkan, atau mempunyai aturan perubahan bentuk yang sama pada setiap individu.',
 'Lereng Gunung Emas adalah habitat sumber yang belum ditemukan pemetaan pastinya. Lereng berhutan Arkananta diusulkan sebagai penempatan regional sementara, tanpa mengganti nama lama dalam arsip. Gunung Emas tidak disamakan dengan Puncak Emas Swargaloka, yang merupakan habitat melayang bangsa Garuda.',
 'Belang dalam Hujan',
 'Rombongan pembawa obat di lereng Arkananta melihat kilatan di bawah pepohonan meskipun suara guntur sudah menjauh. Pada cahaya berikutnya, tampak sosok tegak dengan belang harimau berdiri di jalur sempit.\n\nPemandu meminta semua orang menurunkan bungkusan yang menutupi pandangan dan mundur bersama. Sosok itu tidak mengikuti mereka ke jalan berbatu. Mereka memilih menginap sebelum melanjutkan perjalanan, tanpa menganggap pertemuan singkat tersebut sebagai izin untuk kembali melewati wilayah yang sama.',
 [ARK, '03_Region/07_Nusa Sayendra/Cities & Town/Puncak Emas Swargaloka.md'], ['Letak Gunung Emas, asal manusia-harimau dan aturan transformasi belum ditetapkan.']),
'Ogre': (
 'Raksasa hijau pemakan daging mentah yang juga dikenal sebagai Buto Ijo. Ogre menggunakan tubuh besarnya untuk memaksa jalan melalui penghalang dan dapat membuat perlindungan kayu terasa rapuh. Kemunculannya bersama Goblin dalam serbuan tidak berarti keduanya merupakan satu spesies atau memiliki hubungan keluarga.',
 'Badannya sangat besar dengan dada lebar, perut berat, dan lengan tebal yang menggantung rendah. Kulit hijau kusam berlipat pada leher serta siku, sementara kepala tampak kecil dibandingkan bahunya. Rahang lebar, gigi kasar, dan hidung pipih memperkuat rupa yang sudah disebut Buto Ijo. Tangan besarnya mampu menggenggam benda yang bagi manusia harus diangkat bersama. Ciri ini tidak digunakan untuk menyamakannya dengan Butoraksa atau Troliogoro.',
 'Buas dan berbahaya di dekat sumber makanan. Ia dapat mendekati bau daging, menyingkirkan penghalang, dan menyerang makhluk yang mencoba merebut atau mempertahankan makanan itu. Ketika terluka, gerakannya semakin kasar dan sulit diperkirakan. Rancangan ini tidak menganggap setiap Ogre bodoh atau tidak mampu belajar; tingkat kecerdasan serta susunan kelompoknya belum ditetapkan.',
 'Gunung Bebatuan adalah habitat lama tanpa region jelas. Lereng berbatu Arkananta yang berdekatan dengan jalur portal liar menjadi usulan yang sesuai. Prologue mencatat Ogre muncul di pesisir Aqualis melalui portal, sehingga pantai merupakan lokasi serangan yang terbukti, bukan habitat asal yang dipaksakan.',
 'Pintu yang Terlalu Kecil',
 'Seorang pengangkut berlindung di pondok jalan lereng Arkananta ketika mendengar langkah berat. Ia sempat lega karena pintunya terlalu kecil untuk sosok hijau yang muncul di luar. Lalu tangan besar meraih kusen dan membuat seluruh dinding berderak.\n\nPengangkut itu keluar lewat celah belakang sebelum atap merosot. Dari kejauhan ia melihat makhluk itu membongkar kantong daging yang tertinggal. Pintu yang kuat baginya ternyata hanya benda lain yang dapat ditarik dari tempatnya.',
 [ARK, PRO], ['Gunung Bebatuan belum terpetakan; Ogre tidak disatukan dengan Butoraksa/Troliogoro.']),
'Pyrowisp': (
 'Bola api melayang menyerupai Banaspati yang mampu melepaskan ledakan mematikan. Pyrowisp lebih tepat dikenali dari panas dan lontaran apinya daripada diikuti sebagai penunjuk jalan. Meski namanya mirip Wisp, catatan keduanya menekankan ancaman yang berbeda: serangan api terbuka dan penyesatan.',
 'Wujudnya berupa gumpalan api dengan pusat terang dan lidah-lidah nyala yang terus melengkung mengitari inti. Dalam rancangan rupa ini, batas tubuh tampak membesar saat api berkumpul, lalu berkerut sesudah lontaran dilepaskan. Asap tipis dan bara mengikuti gerakannya tanpa membentuk tubuh berkaki atau bersayap. Bayangan wajah yang sesekali terbaca pada nyala merupakan kesan visual, bukan penetapan roh seseorang di dalamnya.',
 'Agresif dan berbahaya untuk didekati. Ia dapat melayang menghadapi gangguan, menahan posisi, lalu melontarkan api ke arah yang menarik perhatiannya. Menjauh dari satu nyala tidak selalu berarti keluar dari jangkauan panas di sekitarnya. Belum ada dasar untuk menyatakan bahwa ia lahir dari Wisp, merupakan tahap pertumbuhan tertentu, atau dapat dipelihara hanya dengan menyediakan bahan bakar.',
 'Rawa Kering adalah lokasi lama yang belum terpetakan. Cekungan rawa yang mengering di pinggiran hutan Mandala diusulkan sebagai habitat tanpa memberi nama wilayah baru. Kesamaan nama dengan Pyrowisp Caldera tidak membuktikan bahwa makhluk ini berasal dari ibu kota Nagarasven di Agnitra.',
 'Api yang Menunggu',
 'Dua pengelana menyangka cahaya di cekungan kering sebagai api unggun rombongan lain. Yang lebih muda hendak turun meminta tempat bermalam, tetapi rekannya melihat nyala itu melayang tanpa kayu di bawahnya.\n\nMereka baru berbalik ketika cahaya membesar dan lontaran api menyambar tanah tempat mereka semula berdiri. Dari lereng yang lebih tinggi, keduanya menyaksikan bara berputar di atas cekungan. Malam itu mereka memilih gelap yang mereka kenal daripada cahaya yang tidak mempunyai penjaga.',
 ['02_World/Mandala.md', '03_Region/04_Agnitra/Cities & Town/Pyrowisp Caldera.md'], ['Rawa Kering belum terpetakan; asal dan hubungan dengan Wisp belum ditetapkan.']),
'Strigoi': (
 'Undead terbang yang dikenal sebagai Kuyang dan mengisap daya hidup korbannya. Strigoi lebih mudah mencapai tepian rumah atau tempat singgah daripada pemangsa yang harus berjalan melalui pintu. Suara di atas atap dapat membuat orang menengadah tepat ketika ancaman bergerak mendekati sisi lain bangunan.',
 'Mengikuti sebutan Kuyang, rancangan ini menampilkan kepala terbang dengan rambut panjang dan sisa tubuh yang menggantung di bawahnya. Wajahnya pucat, matanya cekung, dan gerak rambut dapat menyamarkan arah terbang dalam cahaya redup. Tidak ada sayap kelelawar yang diperlukan untuk menjelaskan wujudnya. Detail ini merupakan pengembangan visual; cara tubuh terpisah, asal manusia, dan ritual pembentukannya belum menjadi fakta canon.',
 'Memangsa dan mengintai korban yang terpisah dari rombongan. Ia dapat berputar di luar jangkauan, menunggu celah, lalu mendekat untuk mengisap daya hidup. Jika dihalau, ia mencari sudut lain alih-alih selalu bertahan dalam serangan frontal. Tidak ditambahkan aturan bahwa hanya kelompok korban tertentu yang dapat diserang atau bahwa ia harus pulang ke tubuh asal sebelum fajar.',
 'Pinggiran desa adalah habitat perjumpaan existing tanpa desa bernama. Permukiman luar di kawasan utara Mandala diusulkan sebagai penempatan yang selaras dengan ancaman gaib sekitar Valkindra. Ini bukan klaim bahwa seluruh desa Mandala mengalami serangan rutin atau bahwa Strigoi otomatis anggota Dhemit.',
 'Bayangan di Cucuran Atap',
 'Seorang penjaga penginapan luar kota mendengar sesuatu menyeret di atas atap dan menyuruh tamunya tetap di dalam. Ketika lentera diarahkan ke cucuran, rambut panjang jatuh melewati balok, disusul wajah yang tidak mempunyai pijakan.\n\nIa menutup celah jendela dan membangunkan seluruh penghuni agar tidak ada yang pergi memeriksa sendirian. Bayangan itu mengitari rumah sampai langkah patroli terdengar dari jalan. Tidak seorang pun keluar untuk memastikan ke mana ia terbang.',
 [VAL], ['Asal Kuyang, rincian transformasi dan hubungan dengan Dhemit belum diputuskan.']),
'Wendigo': (
 'Raksasa ramping menjulang yang dikenal sebagai Begu Ganjang. Wendigo Nusvanir mengancam dengan kemampuan mencekik dari jauh, sehingga ruang kosong di antara tubuhnya dan korban bukan jaminan aman. Rupanya tidak mengikuti gambaran bertanduk rusa; identitas lokal dalam sumber adalah raksasa tinggi yang menyesakkan napas.',
 'Tubuhnya memanjang tidak wajar, dengan bahu sempit, dada cekung, dan lengan yang menggantung jauh ke bawah. Kepala kecil di ujung leher panjang membuat jarak tubuhnya sulit diperkirakan pada lereng berkabut. Kulit gelap pucat, jari-jari kurus, serta rambut jarang melengkapi rancangan yang menyerupai bayangan pohon mati. Ia tidak diberi tanduk, tengkorak hewan, atau ciri dingin yang tidak didukung entri Nusvanir.',
 'Mengancam dan tidak perlu berlari untuk membuat pendatang merasa terpojok. Dalam pengembangan ini, ia berdiri mengawasi jalur sebelum mengangkat tangan ke arah korban. Orang yang merasakan cekikan dapat salah mengira bahaya berasal dari seseorang di belakangnya. Jangkauan, penyebab, dan cara pasti memutus pengaruh itu belum ditetapkan sebagai aturan; kisah tidak memberikan jarak aman atau ritual penawar baru.',
 'Puncak bukit Raksamala merupakan habitat existing. Jalur menanjak, tonjolan batu, dan punggung bukit terbuka cocok untuk siluetnya yang menjulang. Tidak ada benteng dosa tertentu yang ditetapkan sebagai pemilik atau wilayah kekuasaannya.',
 'Orang Ketiga di Punggung Bukit',
 'Dalam kisah perjalanan di Raksamala, dua pelintas berhenti ketika menghitung bayangan pada punggung bukit. Mereka hanya berdua, tetapi ada sosok ketiga yang jauh lebih tinggi. Salah seorang mulai menarik kerahnya, mengira pakaiannya tersangkut.\n\nRekannya tidak melihat tangan yang menyentuh leher itu. Ia menariknya mundur ke jalur tempat mereka datang, tanpa menunggu sosok tinggi tersebut melangkah. Setelah napas kembali, keduanya meninggalkan barang yang jatuh. Tidak ada yang mau naik lagi hanya untuk membuktikan ukuran bayangan tadi.',
 [RAK], ['Mekanisme cekikan dan komando/faksi khusus belum dipastikan.']),
'Wight': (
 'Mayat terbungkus kain kafan yang bergerak dengan lentingan kuat dan membawa miasma beracun; sebutan lokalnya adalah Pocong. Ikatan pada tubuhnya tidak membuatnya lamban. Dalam Prologue, seorang Dhemit Wight menjadi utusan Sangrahal dan membuka portal yang mengeluarkan kawanan Jenggala di pesisir Aqualis.',
 'Tubuh tegak terbalut kain kusam yang terikat pada bagian atas dan bawah, menahan anggota tubuh dalam siluet sempit. Wajah pucat terlihat di sela kain, sementara lipatan lembap serta noda tanah menegaskan rupa mayat yang telah lama terbungkus. Saat bergerak, seluruh tubuh melenting dan mendarat sebagai satu kesatuan. Mulutnya dapat memuntahkan miasma; bentuknya tidak dilengkapi cakar panjang atau sayap yang bertentangan dengan koreografi cerita.',
 'Bermusuhan ketika menjalankan perintah kegelapan. Ia menutup jarak melalui lompatan dan menekan lawan dengan miasma, bukan melalui kepakan atau cakaran. Wight dalam cerita juga menyampaikan titah dan memimpin serangan. Hal tersebut dicatat sebagai tindakan utusan yang benar-benar terjadi, tanpa menyimpulkan bahwa seluruh Dhemit memiliki kehendak bebas; sumber ras menyebut mereka sepenuhnya berada di bawah kendali Sangrahal.',
 'Kuburan tua merupakan habitat dalam entri Bestiary. Pesisir Aqualis merupakan lokasi kemunculan yang dibuktikan Prologue, sedangkan penyebaran dari Raksamala mengikuti konteks utusan dan portal. Kuburan tidak ditetapkan sebagai satu-satunya tempat asal setiap Wight.',
 'Utusan di Pesisir Timur',
 'Kisah ini merangkum peristiwa Prologue yang sudah ada. Di dekat gubuk Rama, Wight membuka portal berwujud pusaran akar berduri. Goblin, Ogre, dan Direboar keluar darinya ketika sang utusan mengincar bayi yang dilindungi nelayan itu.\n\nJane menghadapi kawanan, sementara Hector, Cassian, dan petualang lain menekan pemimpinnya. Lompatan Wight menghantam pertahanan mereka, tetapi ikatan sihir menahan bagian bawah kafannya. Cahaya Cassian melemahkannya sebelum Hector mengakhiri perlawanan. Ketika Wight gugur, portal kehilangan pengikatnya dan menutup.',
 [PRO, '08_Story/02_Prologue/06_Kutukan_dan_Pengorbanan.md', '04_Ras/04_Drahkthar/Dhemit.md'], ['Folder Jenggala dipertahankan sebagai kategori arsip; bukan redefinisi Wight sebagai ras Jenggala.']),
'Wisp': (
 'Api hantu penyesat jalan yang dikenal sebagai Kemamang. Wisp tampak seperti cahaya kecil yang dapat dijangkau dalam beberapa langkah, lalu menjauh ketika didekati. Bahayanya sering terungkap setelah pengelana tidak lagi mengenali jalan pulang, bukan ketika nyalanya pertama kali terlihat.',
 'Wujudnya kecil dan tidak padat, dengan inti cahaya pucat dikelilingi nyala yang berubah bentuk. Tepian apinya terurai seperti serabut, kemudian menyatu kembali ketika melayang. Dalam kabut, lingkaran cahaya dapat tampak lebih besar daripada sumbernya sehingga jaraknya sulit dinilai. Ia tidak diberi kaki, wajah tetap, atau pakaian untuk menjelaskan gerakannya; identitasnya tetap api hantu yang tercatat.',
 'Tidak menunjukkan keganasan seperti hewan bertaring. Ia menarik perhatian dengan bergerak di batas pandangan, berhenti, lalu melanjutkan perjalanan ketika diikuti. Cahaya yang tampak memandu belum tentu membawa niat menolong. Belum dipastikan apakah penyesatan itu selalu dilakukan secara sadar atau bagaimana ia memilih korban. Wisp juga tidak otomatis menjadi bentuk muda Pyrowisp hanya karena keduanya berwujud api.',
 'Rawa berkabut merupakan habitat existing yang belum memiliki region. Lahan basah berkabut di luar kawasan Valkindra diusulkan sebagai penempatan karena wilayah utara itu sudah mempunyai kabut mistis. Keberadaan rawa spesifik adalah pengembangan habitat, bukan pengubahan seluruh dataran Valkindra menjadi rawa.',
 'Lampu yang Tidak Pulang',
 'Seorang pengelana di luar Valkindra kehilangan pandangan terhadap rekannya dan melihat cahaya bergerak di depan. Ia mengikutinya sambil memanggil. Cahaya itu tidak menjawab, tetapi selalu berhenti ketika ia berhenti.\n\nIa baru sadar setelah pijakannya berubah menjadi lumpur dan tidak lagi menemukan bekas langkah rombongan. Dari kejauhan, panggilan rekannya datang dari arah berbeda. Pengelana itu bertahan di tanah yang masih keras sampai dijemput. Cahaya kecil tadi tetap menunggu di atas rawa, seolah perjalanan mereka belum selesai.',
 [VAL], ['Region rawa dan asal Wisp belum pasti; hubungan pertumbuhan dengan Pyrowisp tidak ditetapkan.'])
}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def write(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def main():
    archive = REPORT / 'pre_jenggala_narrative.json'
    if archive.exists():
        raise SystemExit('Batch already archived; edit current Markdown directly.')
    paths = sorted(FOLDER.glob('*.json'))
    assert {p.stem for p in paths} == set(ENTRIES)
    old = {p.relative_to(ROOT).as_posix(): p.read_text(encoding='utf-8-sig') for p in FOLDER.iterdir() if p.suffix in ('.md','.json')}
    write(archive, old)
    # Baseline covers user edits and the entire runtime before this controlled batch.
    hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.parts and '_audit' not in p.parts and '__pycache__' not in p.parts}
    write(REPORT/'pre_jenggala_hashes.json', hashes)
    db = {n:load(GAME/'data'/(n+'.json')) for n in ['Enemies','Skills','Items','Weapons','Armors']}
    for p in paths:
        obj = load(p)
        desc, form, behavior, habitat, story_title, story, sources, unresolved = ENTRIES[p.stem]
        matches = [e for e in db['Enemies'] if e and e['name'] == obj['title']]
        assert len(matches) == 1, p
        enemy = matches[0]
        header = f'---\ntitle: {obj["title"]}\ntags:\n  - Bestiary\n---\n\n# {obj["title"]}\n'
        for heading, content in [('Deskripsi',desc),('Bentuk',form),('Tingkah Laku',behavior),('Habitat',habitat),('Kisah — '+story_title,story)]:
            header += f'\n## {heading}\n\n{content}\n'
        links = []
        for source in sources:
            assert (ROOT/source).is_file(), source
            links.append('[' + Path(source).stem.replace('_',' ') + '](../../' + quote(source, safe='/') + ')')
        note = ('Rincian visual tambahan adalah usulan; kisah merangkum Prologue yang sudah tercatat.' if p.stem=='Wight' else
                'Rincian rupa, perilaku tambahan, penempatan regional baru, dan kisah merupakan pengembangan usulan; identitas serta kemampuan dasar mengikuti entri sebelumnya.')
        header += '\n> Catatan penulisan: ' + note + ' Acuan: ' + '; '.join(links) + '.\n'
        p.with_suffix('.md').write_text(header, encoding='utf-8')
        previous_status = {k:obj.get(k) for k in ['stat_status','balance_status','source_status']}
        obj['stat_status'] = obj['balance_status'] = 'BLOCKED'
        obj['source_status'] = 'legacy_with_runtime_observation'
        obj['presentation'] = {'markdown_role':'lore_only', 'lore_source':p.with_suffix('.md').relative_to(ROOT).as_posix(),
                               'game_data_source':p.relative_to(ROOT).as_posix(),
                               'narrative_status':'PROPOSED_ADDITIONS', 'approval':None,
                               'scope':'New Jenggala additions; Wildlife approval is not extended to this batch.',
                               'sync_policy':'Author lore in Markdown; game data stays in JSON.'}
        obj['lore_review'] = {'source_archive':archive.relative_to(ROOT).as_posix(),'sources':sources,
                              'unresolved':unresolved,'category_note':'Jenggala is the retained folder category; no universal species/origin inferred.',
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
    print('Jenggala narrative batch: 15 Markdown entries; legacy data and runtime snapshots in JSON.')


if __name__ == '__main__':
    main()
