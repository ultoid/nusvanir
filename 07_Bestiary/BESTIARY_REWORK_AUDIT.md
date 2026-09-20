# Audit Rework Bestiary Nusvanir

## Persetujuan menyeluruh — 2026-09-17

Pemilik proyek menyetujui semua usulan narasi di `07_Bestiary`. Dua puluh delapan entri yang sebelumnya masih berstatus usulan pada batch 05–09 kini `APPROVED`, sehingga seluruh 80 pasangan Markdown–JSON memiliki persetujuan narasi. Manifest persetujuan per batch menyimpan ruang lingkup dan hash Markdown yang disetujui. Penyebutan status usulan pada bagian historis di bawah merujuk pada keadaan saat audit batch itu dibuat.

Persetujuan tidak menutup konflik canon atau taksonomi yang memang belum memperoleh jawaban dan tidak mengubah data runtime. Kalibrasi game, simulasi, dan playtest tetap di luar persetujuan narasi; balance tetap `BLOCKED`.

## Batch narasi Laut Rangkaruna — 2026-09-17

Sepuluh pasangan / dua puluh file telah diperluas berdasarkan World/Region Rangkaruna dan Prologue bab 1, 3, serta 5. Arsip: `_audit/pre_rangkaruna_narrative.json`; baseline: `_audit/pre_rangkaruna_hashes.json`; hasil: `_audit/rangkaruna_verification.json`.

Hydra lokal tetap spesies berkepala delapan yang berbeda dari penjaga Thalantira. Krakentis adalah individu gurita pemutar arus dalam Prologue dan tidak disatukan dengan Kraken Tentacle. Hiu Purba Tulang belum dipastikan sebagai Dhemit. Istilah perut tanpa dasar pada Paus diperlakukan sebagai hiperbola. Efek racun, kelumpuhan, sonar, penyembuhan kerangka, dan serangan mental belum dikalibrasi menjadi mekanik game.

Narasi baru masih PROPOSED_ADDITIONS. Seluruh nilai lama, runtime, skill, dan drop dipertahankan; tidak dilakukan simulasi atau playtest.

## Batch narasi komandan Raksamala — 2026-09-17

Tujuh pasangan / empat belas file telah dipisahkan menjadi lore Markdown dan data JSON. Seluruh komandan memiliki profil karakter dan dokumen benteng. Mamon memakai kejadian Prologue bab 10; komandan lain menggunakan vignette baru. Arsip: `_audit/pre_raksamala_commanders_narrative.json`; baseline: `_audit/pre_raksamala_commanders_hashes.json`; hasil: `_audit/raksamala_commanders_verification.json`.

- Asmodea tercatat sebagai Dhemit dalam profil, tetapi Fortress of Lust menyebut bos Bhuta Succubus/Incubus. JSON mengikuti profil dan konflik taxonomy tidak ditutup.
- Beelzebub memiliki perbedaan istilah hasil transformasi korban antara Dhemit dan Jenggala; tidak dibuat aturan transformasi baru.
- Leviathanus berwujud ular laut bertentakel dalam profil, sedangkan dokumen benteng menyebut kembar siam cacat. Keduanya dicatat sebagai konflik visual.
- Vraka adalah Bhuta yang dibentuk ulang dari mantan jenderal Hanorok. Api neraka dan Bloodlust tidak diterjemahkan menjadi immunity atau state terkalibrasi.
- Tujuh benteng diceritakan pada masa aktif. Untold Story menyatakan Hector kemudian menghancurkan peradaban dan para komandannya; tidak ada klaim bahwa benteng masih utuh pada era sesudahnya.

Narasi baru masih PROPOSED_ADDITIONS. Tidak ada perubahan runtime, stat numerik, skill, drop, spawn, profil tokoh, atau dokumen wilayah.

## Batch narasi Sentinel Nusa Sayendra — 2026-09-17

Empat pasangan / delapan file telah dipisahkan menjadi lore Markdown dan data JSON. Sumber meliputi profil Jenderal Jatayu, profil Ksatria Vayu, ras Garuda, Puncak Emas Swargaloka, Pasukan Ksatria Sayap Garuda, Sumpah Penjaga Langit, ancaman regional, dan World Nusa Sayendra. Arsip: `_audit/pre_sayendra_sentinels_narrative.json`; baseline: `_audit/pre_sayendra_sentinels_hashes.json`; hasil: `_audit/sayendra_sentinels_verification.json`.

- Jatayu adalah satu-satunya Sentinel dengan profil tokoh terpisah. Komando operasional, kesetiaan kepada Swarnapatra, pencarian obat kutukan Feral, luka sayap, dan hubungannya dengan Vayu mengikuti sumber existing.
- Sempati sebagai saudara Jatayu serta kemampuan Paksi dan Suparna mengikuti entri Bestiary lama. Rupa rinci, kepribadian, dan vignette mereka adalah usulan.
- Empat Kuil Angin belum memiliki dokumen lokasi mandiri. Batch mempertahankannya sebagai pos kardinal, tanpa menentukan arsitektur, jarak, populasi, atau pemerintahan baru.
- Klaim ras mengenai kecepatan dan pertahanan mutlak tidak dipindahkan menjadi mekanik game. Angka legacy tetap arsip dan seluruh balance BLOCKED.

Tidak ada perubahan runtime, profil karakter, geografi regional, skill, drop, atau spawn. Batch belum disetujui pemilik.

## Batch narasi kepala suku Arkananta — 2026-09-17

Tiga pasangan / enam file telah dipisahkan menjadi lore Markdown dan data JSON. Sumber utama adalah profil tokoh pada `05_Karakter & Tokoh Penting/05_Arkananta`, dokumen tiga ras, pemukiman gua, agama, ekonomi, dan geografi Arkananta. Arsip awal: `_audit/pre_arkananta_chiefs_narrative.json`; baseline: `_audit/pre_arkananta_chiefs_hashes.json`; hasil: `_audit/arkananta_chiefs_verification.json`.

- Grok merupakan Troliogoro, shaman Animisme Batu, pemimpin isolasionis yang menjaga cairn. Lembah Batu diperlakukan sebagai wilayah kegiatannya; pusat kekuasaan tetap Gua Troliogoro. Konflik Shaman Tier 5 versus Berserker Tier 4 tetap terbuka.
- Krom merupakan Butoraksa, pemimpin tambang luar, penganut Akar Darah, petarung ganas, dan negosiator barter cerdik. Jembatan Tebing menjadi jalur patroli; pusat suku tetap Gua Butoraksa. Palu tulang Behemoth mengikuti profil tokoh, sementara mekanisme gada angin lama belum dijelaskan.
- Larasati merupakan Rakshorien buangan yang memimpin faksi damai, botani bawah tanah, Pemujaan Spora, dan pembuatan penawar gas. Gua Air Mata Air ditempatkan sebagai ruang dalam kompleks Gua Rakshorien. Barter rahasia dengan Krom mengikuti profil tokoh.

Narasi baru masih usulan. Tidak ada perubahan stat numerik, kelas legacy, runtime, skill, drop, spawn, atau dokumen profil karakter. Balance seluruh batch BLOCKED.

## Penguatan material nest Agnitra ? 2026-09-17

Atas arahan pemilik, setiap naga kini mewakili satu nest/material: Blackhorn?Adamantine (zirah dan peredaman sihir, barat), Orichalor?Orichalcum (konduktivitas sihir, selatan kawah), Argentfang?Silver (dingin dan pemurnian, utara), Mithralis?Mithril (ringan dan kuat, timur). Bentuk, kepribadian, ujian, lokasi, serta kisah diselaraskan. Argentfang menjadi penjaga pemurnian, bukan pembunuh yang menguji dengan kematian.

Pemetaan ini menggantikan kehati-hatian afiliasi pada catatan sebelumnya. JSON `lore_identity` menyimpan identitas terkini; field legacy dan snapshot runtime tetap utuh untuk jejak historis. Lokasi Orichalor berpindah dari puncak timur ke Orichalcum selatan; Argentfang dari gua tanpa koordinat ke Silver utara; Mithralis bersarang di Mithril timur dengan jelajah kawah. Tidak ada perubahan stat, drop, recipe, atau runtime. Rincian narasi tetap PROPOSED_ADDITIONS sampai disetujui.

## Batch narasi Agnitra ? 2026-09-17

Empat pasangan Blackhorn, Orichalor, Argentfang, dan Mithralis memakai Deskripsi, Bentuk, Kepribadian dan Sikap, Lokasi Nest, serta Kisah. Narasi baru berstatus PROPOSED_ADDITIONS. Lokasi legacy dipertahankan; klan dan jabatan pemimpin tidak disimpulkan dari warna, nama, atau kemampuan. Kisah baru menampilkan naga berakal sesuai Nagarasven, bukan menetapkan mereka Feral.

Blackhorn tetap di lereng bawah Mahasvara, Orichalor di puncak timur, Argentfang di Gua Gelap Agnitra yang belum dipetakan, dan Mithralis di langit kawah. Mikrohabitat istirahat merupakan usulan. Sarang regional dipakai sebagai konteks, bukan pemetaan otomatis: Orichalcum berada di selatan, Mithril di timur, Silver di utara, Adamantine di dasar lereng barat.

Angka, ID, kelas, dan field legacy dipertahankan. VERIFIED Blackhorn/Orichalor diganti BLOCKED; perbedaan elemen Blackhorn dan label serangan Orichalor terhadap runtime dicatat tanpa rekonsiliasi sepihak. Snapshot runtime hanya observasi. Tidak ada perubahan runtime, item, skill, spawn, atau batch sebelumnya. Arsip: `_audit/pre_agnitra_narrative.json` dan `_audit/pre_agnitra_hashes.json`; hasil: `_audit/agnitra_verification.json`. Pemeriksaan: `python tools/verify_agnitra_lore.py`, audit inventaris, verifier workspace, dan `git diff --check`. Tidak dilakukan simulasi balance atau playtest.

## Persetujuan seluruh narasi Thalantira ? 2026-09-17

Pemilik menegaskan persetujuan seluruh usulan 18 entri Thalantira. Narasi, rincian visual/perilaku, habitat tambahan, dan kisah kini APPROVED. Penanda usulan dihapus; sumber dipertahankan. Bukti persetujuan dan hash Markdown tersimpan di `_audit/thalantira_lore_approval.json`. Pernyataan usulan atau status Thalantira belum berubah pada catatan terdahulu merupakan riwayat sebelum konfirmasi ini. Pertanyaan canon yang belum dijawab tetap terbuka; angka, runtime, serta status balance BLOCKED tidak berubah.

## Persetujuan penjaga Avalerion ? 2026-09-17

Pemilik menyetujui seluruh usulan empat penjaga Avalerion, termasuk kepribadian dan sikap, lokasi benteng, serta kisah. Penanda usulan dihapus dari narasi; sumber dipertahankan. JSON berstatus APPROVED dengan bukti dan hash Markdown di `_audit/avalerion_lore_approval.json`. Race tetap Asevari sesuai permintaan. Konflik kelas Vayu, identitas komandan, dan pemetaan arah yang belum dijawab tetap terbuka; balance tetap BLOCKED dan runtime tidak berubah. Pernyataan usulan Avalerion di bagian terdahulu merupakan riwayat sebelum persetujuan. Status Thalantira tidak berubah.

## Batch narasi penjaga Avalerion — 2026-09-17

Empat pasangan / delapan file telah diperluas. Sumber utama ialah empat dokumen Outpost, Senopati Prabha, dan World Avalerion. Arsip awal: `_audit/pre_avalerion_narrative.json`; hash baseline: `_audit/pre_avalerion_hashes.json`; verifikasi: `_audit/avalerion_verification.json`. Kisah dan rincian baru masih usulan; kategori sebelumnya dipertahankan utuh.

- Aqua diusulkan bertugas di Tirta (pesisir menuju Rangkaruna), Solarius di Agni (dataran tinggi perbatasan Arkananta), Terra di Bumi (perbatasan Mandala), dan Vayu di Bayu (tebing dekat kanopi Astradipa). Lokasi pos bersumber; penugasan tiap entri belum dikonfirmasi sebagai canon. Tidak mengidentifikasi mereka otomatis sebagai komandan yang disebut dokumen pos.
- Arah barat/timur/utara/selatan pada entri legacy belum dipetakan terhadap pos bernama; metadata lama tetap disimpan. Deskripsi JSON lama tetap arsip, Markdown sumber narasi terkini.
- Vayu memiliki konflik kelas: MD Dragoon Tier 4, JSON Windrunner Tier 3. Nilai JSON dipertahankan dan teks MD lama diarsipkan, tanpa keputusan kelas baru. Ciri kulit batu Terra tidak menentukan asal biologis atau immunity gameplay.
- Aqua memuat nilai runtime dan legacy yang berbeda; keduanya dipertahankan. VERIFIED tidak membuktikan kalibrasi sehingga seluruh batch BLOCKED. Tidak ada perubahan stat numerik, skill, drop, spawn, runtime, atau aturan ras berdasarkan gambaran naratif.

## Batch narasi Thalantira — 2026-09-17

18 pasangan / 36 file telah dipisahkan menjadi lore Markdown dan data JSON. Teks sebelum batch tersimpan di `_audit/pre_thalantira_narrative.json`; hash workspace di `_audit/pre_thalantira_hashes.json`; hasil pemeriksaan di `_audit/thalantira_verification.json`. Tambahan narasi masih usulan. Wildlife dan Jenggala yang telah disetujui tidak diubah.

Acuan utama: Threat Thalantira, World Thalantira, Gunung Ungu, profil Uru, Prologue bab 6–9, dan Penjaga Kuil Api Neraka. Bentuk Behemoth mengikuti koreksi eksplisit bab 8: banteng/reptil purba, tanduk ungu, cakar emas, ekor berduri; tafsiran gajah dari peta bab 7 bukan anatomi sebenarnya. Void Wyrm mengikuti warna serta wujud ksatria perak dalam bab 8. Hydra tidak otomatis diberi banyak kepala.

Keputusan dan batas yang tetap terbuka:

- Catatan wilayah tanpa jejak peradaban bertentangan dengan kuil dan gerbang buatan dalam Prologue. Entri memakai lokasi kuil yang diceritakan tanpa menciptakan kerajaan, pembangun, atau sejarah pemukiman baru. Dokumen wilayah tidak diubah.
- Keramahan Hydra/Behemoth, serangan setelah pengaruh kristal, dan penampilan sadar saat berlutut kepada Uru dicatat sesuai urutan. Mutasi paksa yang disebut Untold Story tidak dijadikan bukti bahwa kesadaran para penjaga hilang permanen. Sebutan Ayah/saudara tidak menetapkan silsilah biologis.
- Golem kecil yang takut pada pengunjung tidak otomatis disamakan dengan individu besar sesudah pengungkapan. Treant yang menyerang Rama sambil melindungi Shinta tidak menjadi aturan keramahan universal. Penampakan Shinta menjelang kematian Rama bukan mekanisme kebangkitan baru.
- Manta Ray Void dan Gargoyle tidak disebut khusus pada daftar kemunculan bab 9. Kisah keduanya merupakan usulan ekologis, bukan tambahan peran dalam adegan tersebut. Kraken Tentacle tetap bagian tubuh; Phantom tidak berarti otomatis Dhemit; fauna pulau tidak ditetapkan seluruhnya Voidborn.
- Mikrohabitat baru diturunkan dari karang, laut dalam, hutan, padang batu barat, dan lereng gunung yang sudah ada. Tidak ada kota/pelaut menetap atau saksi ekspedisi baru diciptakan. Kuil Api selatan milik masa Hector dibedakan dari Kuil Udara utara.
- Angka Void Wyrm serta `legacy_values`/`runtime_values` dipertahankan. Label VERIFIED menjadi BLOCKED. Label historis Endgame Final Boss tidak menetapkan urutan akhir cerita; Void tidak didaftarkan sebagai elemen System baru. Ketahanan absolut dan pembekuan permanen belum memiliki spesifikasi gameplay terkalibrasi.

Tidak ada perubahan runtime, stat numerik, ID, drop, skill, spawn, aggregate/wiki, atau kategori berikutnya. Tidak dilakukan simulasi balance maupun playtest karena batch ini mengubah dokumentasi narasi dan pencatatan sumber.

> **Pembaruan persetujuan Jenggala:** pada 2026-09-17 pemilik menyetujui seluruh tambahan narasi 15 entri. Habitat regional dan kisah yang sebelumnya ditandai usulan kini disetujui; catatan sumber dan pertanyaan tanpa jawaban tetap berlaku. Bukti: `_audit/jenggala_lore_approval.json`. Status game tetap BLOCKED.

## Batch narasi Jenggala — 2026-09-17

Seluruh 15 entri `02_Jenggala` kini mempunyai Markdown naratif dan JSON yang mempertahankan data game. Sumber sebelum batch diarsipkan dalam `_audit/pre_jenggala_narrative.json`; `_audit/pre_jenggala_hashes.json` memungkinkan pemeriksaan bahwa Wildlife, runtime, dan perubahan pengguna lain tidak tersentuh. Hasil pemeriksaan khusus berada di `_audit/jenggala_verification.json`.

Fakta yang dipertahankan: Ahool kelelawar pembawa wabah; Banshee/Kuntilanak; Direboar/Celeng Ngepet; Goblin/Ebu Gogo; Gondarwa raksasa berbulu; Gremlin/Tuyul; Homunculus/Jenglot; Leyak penyihir bermutasi; Lycan manusia harimau/Cindaku; Ogre/Buto Ijo; Pyrowisp/Banaspati; Strigoi/Kuyang undead terbang; Wendigo/Begu Ganjang; Wight/Pocong; Wisp/Kemamang. Alias dipertahankan, tidak didefinisikan menjadi ras baru.

Konflik/keputusan yang tetap terbuka:

- Wight merupakan Dhemit utusan Sangrahal dalam Prologue, sementara folder Bestiary adalah Jenggala. Folder tidak diubah dan tidak dipakai membuktikan semua isinya satu ras. Tindakan berbicara/memimpin pada Prologue tidak dipakai mengubah ketentuan Dhemit tanpa kehendak bebas.
- Pulau Asrivana pada Leyak belum ditemukan padanan geografisnya; penempatan Astradipa adalah usulan, bukan perubahan Astradipa menjadi pulau.
- Gunung Emas pada Lycan tidak disamakan dengan Puncak Emas Swargaloka yang melayang. Penempatan lereng Arkananta masih usulan.
- Hutan Bayangan, Gunung Bebatuan, Rawa Kering, dan rawa Wisp belum terpetakan pasti; penempatan regional naratif tidak mengubah spawn database.
- Pyrowisp tidak dinyatakan berasal dari Balairung Kaldera Mahasvara hanya karena nama sama; tidak ditetapkan berevolusi dari Wisp.
- Semua detail baru dan vignette ditandai usulan. Kisah Wight merangkum kejadian Prologue existing. Reproduksi, asal korupsi universal, ritual, dan subtype Dhemit lain tidak diciptakan.

Goblin/Wendigo tidak lagi memakai VERIFIED sebagai status kalibrasi JSON. Seluruh Jenggala memakai BLOCKED tanpa mengganti angka lama. Runtime 15 enemy, skill dan drop direferensikan melalui snapshot; belum ada simulasi atau playtest, dan batch ini tidak mengklaim rework combat/boss selesai.

> Pembaruan pemilik 2026-09-17: Markdown Wildlife kini khusus narasi; data game tetap dalam JSON. Aturan mirror penuh di audit historis berikut sudah digantikan oleh bagian **Format sederhana** pada BESTIARY_STANDARD_V2.md. Pasangan dicek melalui identitas dan referensi, bukan kesamaan seluruh isi.

## Audit ulang workspace — 2026-09-17, batch 01a/01b

**Bagian ini menggantikan kesimpulan audit awal di bawah.** Audit awal dipertahankan sebagai riwayat; pernyataan bahwa runtime belum tersedia sudah kedaluwarsa. Status kerja: dokumentasi dan migrasi Wildlife, **bukan kalibrasi atau rilis game**.

### Fakta terkonfirmasi

- Tidak ditemukan AGENTS.md dalam repository maupun direktori induk yang diperiksa. Branch `main`; tidak dibuat commit, perpindahan branch, atau push. Sebelum kerja sudah ada perubahan pada Wildlife, Goblin, Wendigo, Void Wyrm, guardian, naga, chiefs, dokumentasi, skrip sinkronisasi, dan seluruh project game yang untracked. Arsip teks sebelum perubahan: `_audit/pre_batch_2026-09-17.json`; status dan hash awal disimpan di direktori yang sama.
- Workspace memuat project MV `10_Game Project/Tales of The Dark Time`, termasuk database, engine, konfigurasi dan seluruh plugin yang diaktifkan. Ini sumber observasi implementasi lokal; keberadaan file tidak membuktikan build rilis atau kelulusan balance.
- Inventaris lengkap: [_audit/INVENTORY.md](_audit/INVENTORY.md), dengan sumber mesin `_audit/inventory.json`: **80 pasangan**. Wildlife 15, Jenggala 15, Thalantira 18, Avalerion 4, Agnitra 4, Arkananta 3, Sayendra 4, Raksamala 7, Rangkaruna 10. Inventaris mencatat pasangan, ID runtime, overlap karakter, status, dan mismatch metadata.
- `Pedoman_Pemberian_Stat.md` tersedia dan tetap otoritas governance; catatan historisnya tentang ketiadaan runtime tidak lagi menggambarkan workspace. Dokumen pemilik tersebut tidak diubah.
- Lore primer berada di direktori 00–05 dan 08. `Mekanik_Class_Job.md` menetapkan lima Tier class; runtime class curves berada di `Classes.json`. Tier musuh seperti T9 pada Void Wyrm bukan bukti Tier class sembilan.
- Elemen: `Mekanik_Efektivitas_Elemen.md`; implementasi: `System.json`, skill elementId, traits, `YEP_ElementCore`. State: `States.json`, `YEP_BuffsStatesCore`, passive plugins. Formula: `Skills.json`, `rpg_objects.js`, `NUSV_DamageCore`, critical/extra/special parameter plugins.
- Equipment, relic/accessory, rarity, item, upgrade, socket, forge: `Weapons.json`, `Armors.json`, `Items.json`, `NUSV_ItemUpgrade`, `NUSV_SocketCore`, `NUSV_ItemSynthesis`. Ekonomi lore: `Sistem_Ekonomi_&_Crafting.md`, `Sistem_Mata_Uang.md`, dan Economy regional. Item rarity runtime: Common, Uncommon, Rare, Epic, Legendary, Mythic; ini bukan spawn rarity.

### Source-of-truth dan kompatibilitas

Wiki membaca `nusvanirDB` dari `Nusvanir_Wiki_App/database.js`, berisi salinan Markdown; ia tidak membaca JSON V2 langsung. `combined_lore.txt` dan `all_lore_combined.txt` mempunyai penanda FILE. Generator agregat tidak ditemukan. `Nusvanir_Database.json` memuat versi genesis berbeda; jangan menganggapnya lebih baru daripada sumber terpisah. `Kitab_Nusvanir_Kodex_Semesta.md` adalah kompendium editorial menurut README, bukan bukti runtime. Semua agregat dipertahankan; Wiki belum mencerminkan V2.

Skrip `sync_bestiary_from_game.py` menimpa data melalui nama yang dinormalisasi, mengganti legacy snapshot, dan memberi status `VERIFIED`; `temp_mass_bestiary_update.py` menebak tipe dari folder. Keduanya **tidak dijalankan**. Belum ada konvensi sinkronisasi aman. Konvensi batch yang didokumentasikan sebelum migrasi: pertahankan semua ID/nama/path dan key lama, tambahkan objek `v2` sebagai sumber structured record, render objek itu identik ke bagian Markdown bertanda. Metadata lama adalah arsip. Tidak ada ekspor V2 ke MV, sehingga null kalibrasi tidak masuk Enemies.json. Perubahan bentuk record dibatasi field tambahan; consumer eksternal yang tidak tersedia belum dapat dijamin kompatibel.

### Inkonsistensi yang dibuktikan

- Babi Hutan: Markdown sebelum batch memakai runtime HP 126/MP 8 dan VERIFIED; JSON masih BLOCKED dengan legacy HP 150/MP 0. Status VERIFIED hanya membuktikan salinan, bukan status yang diizinkan pedoman.
- Wendigo dan Void Wyrm memiliki blok HP ganda. Void diberi notetag tetapi tidak ada dalam daftar elemen System. Tidak dibuat multiplier Void.
- Wildlife menyimpan weakness Fire 1.5 pada traits, sedangkan chart lore memakai 2x untuk matchup efektif. Catatan All pada Kelinci belum menjadi traits. Primary element tidak menjelaskan semua skill: Shadow Pounce memakai Dark; Death Roll memakai Dark.
- Honey Rage (373), Scatter Flight (380), Shell Bash (390), Withdraw (391), Pack Howl (403): damage type 0, effects kosong, hanya petunjuk CUSTOM SKILL EFFECT. Nama skill tidak membuktikan buff bekerja.
- Catatan chance 50% pada Wildlife diganti kondisi turn di database; rating adalah bobot pemilihan, bukan peluang 50% atau rotasi pasti.
- Troop 2 bernama Slime tetapi mengacu enemy 2 Babi Hutan; troop 3 Orc mengacu Bebek; troop 4 Minotaur mengacu Beruang. Jangan menyimpulkan progression dari nama troop yang tertinggal.
- Spirit Dust (282) dideskripsikan berasal dari Wisp, tetapi menjadi drop Ayam/Puyuh. Deer Hide (60) menulis Mandala sedangkan habitat rusa menulis Astradipa. Clear Crystal pada fauna air butuh penjelasan ekologi. Semua dipertahankan sebagai konflik, bukan dikanonkan otomatis.
- Entri karakter dan boss dengan nama sama bukan otomatis duplikat yang boleh dihapus. Varian Raksamala/Raksmala dan Rangkaruna/Laut_Rangkaruna masih ada. Daftar per creature ada dalam inventaris.

### Missing information dan numerical blockers

Ada formula, curves, equipment, states dan konfigurasi party; yang belum ada adalah **baseline encounter yang dipilih dan disetujui**, availability gear per chapter, target ronde/pressure/reward, implementasi efek tertunda, serta simulasi/playtest. Jangan melaporkan semua formula hilang. Runtime menetapkan party awal 1/2/3 dan maksimum battle members 4, tetapi ini bukan keputusan bahwa semua encounter memakai empat anggota. Level maksimum actor berbeda-beda, bukan satu level cap global.

### Perbaikan aman dan keputusan pemilik

Perbaikan batch: arsip legacy, status BLOCKED, pemisahan taxonomy/habitat/region, snapshot skill/traits/drop runtime, reuse item IDs, parity deterministik, dan kerangka kalibrasi. Tidak ada item, state, angka combat, atau lore dasar baru.

Keputusan pemilik: (1) pilih konteks Wildlife: prologue party atau progression baru, roster/gear dan target encounter; (2) pilih kebijakan matchup runtime vs chart; (3) tentukan wildlife pasif/ternak sebagai combat atau interaksi; (4) selesaikan asal drop Spirit Dust/Clear Crystal serta habitat Deer Hide; (5) putuskan definisi/reproduksi Jenggala dan pemetaan folklor sebelum batch Jenggala. Tidak diperlukan izin tambahan untuk membaca atau memperbaiki traceability, tetapi konflik tersebut tidak diselesaikan diam-diam.

---

## Arsip audit awal (kesimpulan runtime digantikan audit ulang di atas)

## Status ringkas

Repositori Nusvanir saat ini terdiri dari dokumentasi lore dan pengaturan sistem, bukan database runtime RPG Maker MV aktif. Berdasarkan audit awal pada 17 September 2026, data berikut berstatus valid dan dapat dipakai sebagai sumber otoritas:

- `06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md` hadir dan menyatakan bahwa angka final harus dihitung dari progression, party baseline, formula skill, equipment, dan hasil simulasi/playtest.
- `06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md` hadir dan memetakan 10 elemen Nusvanir dengan multiplier `2x`, `1x`, `0.5x`, dan `0x`.
- `07_Bestiary/01_Alam_Liar/**` berisi entri fauna liar yang masih menggunakan format legacy ringkas.
- `07_Bestiary/02_Jenggala/**`, `07_Bestiary/03_Thalantira/**`, dan kategori boss lainnya berisi banyak materi lore dan beberapa nilai numerik yang perlu ditinjau ulang.
- Tidak ditemukan `AGENTS.md` di akar maupun subdirektori yang relevan.

## 1. Sumber aktif yang teridentifikasi

### Confirmed facts

1. Sumber canon dunia:
   - `00_Kosmologi & Sejarah/**`
   - `01_Hukum Sihir/**`
   - `02_World/**`
   - `03_Region/**`
   - `04_Ras/**`
   - `05_Karakter & Tokoh Penting/**`
   - `08_Story/**`
   - `Kitab_Nusvanir_Kodex_Semesta.md`
   - `Nusvanir_Database.json`

2. Sumber sistem permainan:
   - `06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md`
   - `06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md`
   - `06_Sistem Game & Ekonomi/Sistem_Ekonomi_&_Crafting.md`
   - `06_Sistem Game & Ekonomi/Mekanik_Class_Job.md`

3. Sumber bestiary dan ekologi:
   - `07_Bestiary/01_Alam_Liar/**`
   - `07_Bestiary/02_Jenggala/**`
   - `07_Bestiary/03_Thalantira/**`
   - `07_Bestiary/...` kategori boss dan regional entries

4. Data runtime RPG Maker MV aktif:
   - Belum terdeteksi di workspace.
   - Tidak ada `data/System.json`, `data/Enemies.json`, `data/Classes.json`, `data/Skills.json`, `data/Weapons.json`, `data/Armors.json`, atau `data/States.json` yang dapat dipakai sebagai baseline.

## 2. Audit current Bestiary

### 2.1 Struktur data yang ada

- Mayoritas entri Bestiary memiliki pasangan file `.md` + `.json`.
- Format `.md` masih menggunakan gaya yang sangat ringkas, seperti `Kategori`, `Elemen`, `Kelemahan`, `Tipe Serangan`, `HP`, `MP`, `Spawn Location`, dan satu paragraf deskripsi.
- Format `.json` berisi metadata yang lebih ringkas dan sering tidak mencerminkan skema perencanaan baru.

### 2.2 Contoh masalah yang ditemukan

- `Babi_Hutan.md` dan `Babi_Hutan.json` menyimpan `HP: 150` dan `weakness: Api`, namun belum ada bukti bahwa angka tersebut berasal dari progression atau formula game yang valid.
- `Beruang_Madu_Raksasa.md` menyimpan `HP: 850`, namun `Pedoman_Pemberian_Stat.md` secara eksplisit menolak angka seperti itu sebagai final tanpa baseline party dan formula yang benar.
- `Argentfang` memiliki angka besar dalam catatan lore/legacy, tetapi tidak punya bukti sumber runtime atau hasil playtest.
- `Thalantira` memiliki entri dengan nilai HP dan variabel yang tidak terukur dari sistem yang sedang dipakai.
- Terdapat duplikasi nama pada lokasi/region: `Raksamala` dan `Raksmala` (varian nama yang berpotensi menimbulkan kebingungan).
- Beberapa file seperti `Pulau_Kegelapan_Raksamala.json` dan `Pulau_Kegelapan_Raksmala.json` tampak sebagai duplikasi nama yang sama dengan varian ejaan berbeda.

### 2.3 Masalah terminologi

- Campuran istilah Indonesian/English masih jelas, terutama di kategori boss dan beberapa bestiary entries.
- `Creature Type` dan `Faction/Region` sering tercampur dalam satu label, misalnya `location` atau `category` yang memuat informasi ekologi dan wilayah sekaligus.
- Label `element` sering hanya berisi `Netral` atau `Api` tanpa menghubungkan ke matchup sistem 10 elemen yang resmi.
- Banyak `weakness` tidak dibedakan dengan `elemental vulnerability`, `status weakness`, atau `mechanic counter`.

## 3. Missing information and blockers

### Missing information

- Tidak ada database runtime RPG Maker MV aktif.
- Tidak ada `data/Enemies.json`, `data/Skills.json`, `data/States.json`, dan seterusnya.
- Tidak ada level cap, chapter progression, party size, equipment baseline, atau formula skill yang dipakai oleh build game.
- Tidak ada hasil simulasi/playtest yang dapat menopang peringkat `VALIDATED`.
- Belum ada struktur lengkap untuk `BESTIARY_REWORK_AUDIT.md`, `BESTIARY_STANDARD_V2.md`, `CREATURE_TAXONOMY.md`, dan `MONSTER_BALANCE_FRAMEWORK.md`.

### Numerical balance blockers

Setiap angka bestiary yang masih bersifat legacy harus diperlakukan sebagai `LEGACY_CANDIDATE` sampai memenuhi kriteria `Pedoman_Pemberian_Stat.md`. Status yang diperbolehkan saat ini adalah:

- `BLOCKED`: tidak ada data yang cukup untuk menghitung
- `PROVISIONAL`: hanya untuk model eksperimen dengan asumsi yang jelas
- `CALIBRATED`: hanya bila database runtime dan simulasi tersedia
- `VALIDATED`: hanya bila playtest valid tersedia

## 4. Safe automatic fixes

Yang aman untuk diterapkan tanpa mengubah canon inti:

- menambahkan dokumen audit dan skema standar rework;
- membagi taxonomy antara fauna liar, Jenggala, Drahkthar, Thalantira, dan divinity;
- menandai semua nilai numerik yang ada sebagai `legacy candidate` atau `BLOCKED`;
- menormalkan nama kategori agar mengikuti struktur `01_Alam_Liar`, `02_Jenggala`, `03_Thalantira`, dll.;
- memperjelas bahwa `Mekanik_Efektivitas_Elemen.md` adalah satu-satunya otoritas matchup elemen yang saat ini valid;
- mengecek keselarasan `.md` dan `.json` untuk entri yang akan dirework batch-by-batch.

## 5. Decisions requiring owner approval

- apakah `Jenggala` harus dipahami sebagai ras, korupsi ekologis, atau kondisi mutasi terpadu;
- apakah `Drahkthar` adalah istilah umum untuk entitas demonic/warborn atau identitas etnis/civilizational yang mapan;
- apakah `Void` akan dijadikan elemen resmi atau tetap dikelola sebagai entitas kosmik tanpa rating 10-elemen;
- level cap, party size, class curves, dan progression baseline yang valid untuk semua stat final;
- apakah `Argentfang` dan boss Thalantira akan diturunkan dari legacy value atau tetap di-backlog sampai data game saat ini tersedia.

## 6. Conclusion

Repo saat ini memiliki canon yang cukup kuat untuk dokumentasi, taxonomi, dan ekologi, tetapi belum cukup untuk memberikan angka final atau mengklaim balance yang valid. Oleh karena itu, batch pertama harus fokus pada struktur, audit, pencegahan overclaiming, dan rework non-numerik pada fauna liar tanpa mengarang stat baru.

## 7. Status akhir audit

- Confirmed facts: yes
- Inconsistencies found: yes
- Missing data: yes
- Safe fixes identified: yes
- Owner approval required: yes
- Numerical balance blockers: yes
