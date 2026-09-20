# Bestiary Rework Changelog

## 2026-09-17 | Persetujuan menyeluruh Bestiary

Pemilik proyek menyetujui seluruh usulan narasi yang tersisa pada batch Agnitra, Arkananta, Nusa Sayendra, Raksamala, dan Laut Rangkaruna. Sebanyak 28 entri pada lima batch tersebut kini berstatus `APPROVED`; bersama persetujuan batch sebelumnya, seluruh 80 entri Bestiary telah disetujui. Keterangan usulan pada catatan batch di bawah merupakan riwayat keadaan sebelum persetujuan ini.

Persetujuan mencakup deskripsi, rupa, kepribadian atau tingkah laku, lokasi, dan kisah. Konflik sumber serta pertanyaan canon, taksonomi, dan mekanika yang belum dijawab tetap dicatat sebagai hal terbuka. Angka, runtime, dan kalibrasi game tidak diubah; status balance tetap `BLOCKED`.

## 2026-09-17 | Batch 09 — Laut Rangkaruna

Sepuluh fauna laut diperluas dengan Deskripsi, Bentuk, Tingkah Laku, Habitat, dan Kisah. Lintah Palung, Pari Kematian Besi, Sirenia Kegelapan, Ubur-Ubur Pijar Kematian, dan Krakentis memakai peristiwa pelayaran Prologue; Kepiting Batu Karang memakai reputasi Rama. Empat entri lain menggunakan vignette ekologis usulan.

JSON legacy yang sebelumnya tidak memiliki ID/title kini menyimpan identitas pasangan, deskripsi naratif ringkas, seluruh objek awal dalam `legacy_values`, sumber, serta snapshot runtime. Tidak ada angka atau runtime yang diubah. Hydra Rangkaruna tidak disamakan dengan Hydra Jurang; Krakentis tidak disamakan dengan Kraken Tentacle Thalantira; Hiu Phantom/undead tidak otomatis Dhemit. Balance BLOCKED.

## 2026-09-17 | Batch 08 — komandan benteng Raksamala

Tujuh pasangan komandan diperluas dengan Deskripsi, Bentuk, Kepribadian dan Sikap, Kedudukan dan Benteng, serta Kisah. Profil tokoh dan tujuh Fortress of Sins menjadi sumber utama. Kisah Mamon merangkum penyerangan gereja Aqualis dalam Prologue; enam vignette lain masih usulan.

Race JSON mengikuti profil: Asmodea `Dhemit`, enam lainnya `Bhuta`; Vraka juga dicatat berasal dari Hanorok dalam narasi. Konflik Asmodea antara profil Dhemit dan dokumen benteng yang menyebut bos Bhuta tetap terbuka. Kronologi membedakan masa benteng aktif dari reruntuhan setelah Hector menghancurkan Raksamala.

Seluruh angka, kelas, lokasi, dan field legacy dipertahankan; runtime tidak diubah. Arsip dan verifikasi: `_audit/pre_raksamala_commanders_narrative.json`, `_audit/pre_raksamala_commanders_hashes.json`, `_audit/raksamala_commanders_verification.json`. Balance BLOCKED tanpa simulasi atau playtest.

## 2026-09-17 | Batch 07 — Sentinel Nusa Sayendra

Empat pasangan Jenderal Jatayu, Paksi, Sempati, dan Suparna diperluas dengan Deskripsi, Bentuk, Kepribadian dan Sikap, Kedudukan dan Kuil Penjagaan, serta Kisah. Seluruh JSON mencatat ras Garuda. Jatayu mengikuti profil tokoh sebagai komandan armada, veteran, pengganti operasional ketika Swarnapatra terkena kutukan Feral, dan sahabat Ksatria Vayu. Tiga Sentinel lain dikembangkan dari identitas kemampuan dan pos lama.

Kuil selatan, timur, utara, dan barat dipertahankan sebagai pos tugas tanpa menambahkan permukiman atau hierarki pemerintahan baru. Puncak Emas Swargaloka tetap pusat kehidupan Garuda. Narasi baru berstatus PROPOSED_ADDITIONS; angka, kelas, lokasi, ID, dan field legacy dipertahankan. Tidak ada perubahan runtime, skill, drop, atau spawn.

Delapan teks awal dan hash workspace diarsipkan. Alat: `tools/rework_sayendra_sentinels_lore.py`, `tools/verify_sayendra_sentinels_lore.py`; laporan: `_audit/sayendra_sentinels_verification.json`. Balance tetap BLOCKED tanpa simulasi atau playtest.

## 2026-09-17 | Batch 06 — kepala suku Arkananta

Tiga pasangan Grok Tulang-Besi, Krom Batugilang, dan Nyai Larasati diperluas dengan Deskripsi, Bentuk, Kepribadian dan Sikap, Kedudukan dan Wilayah, serta Kisah. Identitas mengikuti profil tokoh: Grok adalah Troliogoro shaman pemimpin cairn; Krom adalah Butoraksa petarung dan negosiator barter; Larasati adalah Rakshorien buangan yang memimpin komunitas damai serta botani spora.

JSON mencatat race dan sumber karakter, mempertahankan seluruh angka/field legacy, serta menambahkan snapshot runtime tanpa mengubah game. VERIFIED Nyai Larasati menjadi BLOCKED. Konflik kelas Grok (MD Shaman Tier 5, JSON Berserker Tier 4), lokasi tanpa dokumen tersendiri, dan rincian mekanis kemampuan tidak diputuskan. Narasi baru masih PROPOSED_ADDITIONS.

Enam teks awal serta hash workspace diarsipkan. Alat: `tools/rework_arkananta_chiefs_lore.py`, `tools/verify_arkananta_chiefs_lore.py`; laporan: `_audit/arkananta_chiefs_verification.json`. Tidak ada simulasi balance, playtest, commit, atau perubahan runtime.

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

## 2026-09-17 | Batch 04 — penjaga pos Avalerion

Empat pasangan Aqua, Solarius, Terra, dan Vayu diperluas menjadi lima bagian lore, masing-masing dengan kisah tugas penjagaan. Penempatan Aqua–Tirta, Solarius–Agni, Terra–Bumi, dan Vayu–Bayu diusulkan berdasarkan peran serta geografi pos existing. Para ksatria diperlakukan sebagai penjaga berakal, bukan fauna agresif; identitas komandan tidak diasumsikan. Tambahan masih PROPOSED_ADDITIONS. Status proposal Thalantira tidak berubah.

Seluruh angka, ID, dan kelas JSON dipertahankan. Perbedaan Vayu (Dragoon Tier 4 di MD, Windrunner Tier 3 di JSON) disimpan dalam arsip serta lore_review. Status VERIFIED Aqua diganti BLOCKED; snapshot runtime bukan kalibrasi. Delapan teks awal serta hash workspace diarsipkan. Runtime, batch sebelumnya, dan kategori berikutnya tidak diubah.

Pemeriksaan: `python tools/verify_avalerion_lore.py`, `python tools/bestiary_audit.py --write-report`, `python tools/verify_bestiary_workspace.py`, serta `git diff --check`. Laporan khusus: `_audit/avalerion_verification.json`. Tidak dilakukan simulasi balance atau playtest.

## 2026-09-17 | Batch 03 — narasi Thalantira

- Memperluas 18 Markdown dengan deskripsi bergaya ensiklopedia makhluk, bentuk rinci, tingkah laku, habitat berdasarkan geografi pulau, dan kisah. Treant, Golem, serta tiga penjaga memakai ringkasan Prologue; 13 kisah lainnya merupakan pengembangan ekologis usulan.
- Menjaga konteks ilusi, pengaruh Uru, hubungan para penjaga, dan perbedaan masa Kuil Api. Bentuk Behemoth memakai koreksi bab 8; Void Wyrm memakai wujud naga dan ksatria perak. Tambahan batch belum disetujui; persetujuan batch terdahulu tidak diperluas otomatis.
- Mengarsipkan 36 teks awal dan hash workspace. JSON mempertahankan angka/ID/key lama, menambahkan sumber lore, snapshot enemy/skill/drop, serta catatan balance BLOCKED. Data runtime tidak diubah.
- Menambahkan `tools/rework_thalantira_lore.py` dan `tools/verify_thalantira_lore.py`, serta memperbarui verifier workspace, standard, audit, dan inventaris. Verifikasi meliputi pasangan, lima bagian, tautan lokal, pelestarian field lama, ID runtime, referensi skill/state/element/drop, serta hash di luar batch.
- Perintah pemeriksaan: `python tools/verify_thalantira_lore.py`, `python tools/bestiary_audit.py --write-report`, `python tools/verify_bestiary_workspace.py`, `git diff --check`. Tidak ada simulasi, playtest, commit, atau push.

## 2026-09-17 | Persetujuan seluruh narasi Jenggala

Pemilik menyatakan “aku setuju semua usulannya”. Seluruh deskripsi, bentuk, tingkah laku, penempatan habitat, dan kisah pada 15 entri Jenggala ditetapkan sebagai lore yang disetujui. Penanda usulan dihapus; acuan sumber tetap dipertahankan. Persetujuan dicatat di JSON pasangan dan `_audit/jenggala_lore_approval.json`, beserta hash Markdown yang disetujui. Validator disesuaikan untuk memeriksa bukti persetujuan tersebut.

Nama geografis lama yang belum dipetakan, asal transformasi, serta pertanyaan taxonomy yang belum diberi jawaban tetap terbuka; persetujuan tidak mengisi detail yang belum pernah diusulkan. Angka, ID, runtime dan status kalibrasi BLOCKED tidak diubah. Catatan usulan pada log sebelumnya adalah riwayat sebelum persetujuan.

## 2026-09-17 | Batch 02 — narasi Jenggala

- Memperluas **15 pasangan / 30 file**: Ahool, Banshee, Direboar, Goblin, Gondarwa, Gremlin, Homunculus, Leyak, Lycan, Ogre, Pyrowisp, Strigoi, Wendigo, Wight, Wisp. Setiap Markdown sekitar 300 kata, dengan Deskripsi, Bentuk, Tingkah Laku, Habitat, dan Kisah; data tempur tidak ditampilkan di Markdown.
- Memakai wilayah dan faksi existing sebagai acuan. Lycan tetap manusia harimau/Cindaku; Wendigo tetap Begu Ganjang tanpa tanduk rusa; Wight tetap Pocong yang melenting dan memuntahkan miasma. Kisah Wight merangkum Prologue; 14 kisah lain adalah tambahan usulan.
- Menyimpan seluruh teks sebelum batch dan hash workspace; seluruh key data existing dipertahankan kecuali label stat/source status. Menambahkan referensi runtime enemy/skill/drop dan catatan lore pada JSON. Runtime, Wildlife yang sudah disetujui, ID, filename, angka, dan agregat tidak diubah.
- Mengganti status VERIFIED Goblin/Wendigo menjadi BLOCKED; seluruh 15 angka legacy tidak diklaim terkalibrasi. Tidak ada stat, item, state, recipe, faksi, atau aturan cosmology baru dibuat. Tidak ada duplicate entry dihapus.
- Membuat `tools/rework_jenggala_lore.py`, `tools/verify_jenggala_lore.py`, `_audit/pre_jenggala_narrative.json`, `_audit/pre_jenggala_hashes.json`, `_audit/jenggala_verification.json`; memperbarui standard, audit, inventaris dan alat verifikasi pasangan.
- Verifikasi: pasangan, lima bagian narasi, tautan sumber, ID unik, original field preservation, enemy/skill/item snapshot, element/state IDs dan hash di luar batch. Perintah: `python tools/verify_jenggala_lore.py`, `python tools/bestiary_audit.py --write-report`, `python tools/verify_bestiary_workspace.py`, `git diff --check`.
- Batas: narasi baru belum disetujui; lokasi ambigu dan taxonomy tidak diputuskan sepihak. Belum ada simulasi, playtest, atau perubahan perilaku game. Tidak ada commit/push. Langkah berikut: review tambahan Jenggala dan keputusan habitat; setelah itu batch Thalantira dapat diaudit sesuai konteks era/ilusi Prologue.

## 2026-09-17 | Persetujuan pemilik atas narasi Alam Liar

Pemilik menyatakan “usulan aku setujui semua” untuk batch narasi terakhir. Deskripsi, bentuk, tingkah laku, habitat, dan 15 kisah kini disetujui sebagai lore. Penanda usulan di Markdown dihapus dan habitat ditulis sebagai persebaran yang ditetapkan. Acuan world-building tetap dicantumkan. Detail yang memang belum dijelaskan, seperti asal racun piton dan lokasi bernama Rawa Beracun, tidak diisi dengan keputusan baru.

Persetujuan dicatat pada `v2.presentation.lore_approval` di 15 JSON. Ini tidak mengubah status BLOCKED untuk kalibrasi game atau menyetujui proposal combat/crafting historis. ID, angka, dan runtime tetap. Catatan usulan pada log sebelumnya merupakan riwayat sebelum persetujuan ini.

## 2026-09-17 | Pengayaan narasi 15 fauna Alam Liar

- Memperluas semua 15 Markdown Alam Liar menjadi Deskripsi bergaya ensiklopedia fauna, Bentuk, Tingkah Laku, Habitat, dan Kisah pendek. Bagian Ciri-ciri diganti dengan Tingkah Laku yang menjelaskan agresi, penghindaran, pertahanan diri dan perlindungan anak.
- Membaca geografi Mandala/Astradipa/Arkananta serta profil Arthiska, Hermindar, Valkindra, Aqualis, ibu kota, Wana Prasetya dan Akar-Dipa. Habitat dipilih berdasarkan kesesuaian lingkungan; rekomendasi persebaran baru ditandai sebagai usulan.
- Memperjelas Lingkar Bumi sebagai distrik perkotaan, bukan padang luas; Rawa Beracun tetap lokasi yang belum terpetakan. Kisah mengambil konteks pertanian/tekstil Arthiska, industri Hermindar, logistik Lingkar Samodra, patroli Asrivana, dan perjalanan lereng Arkananta tanpa menambah faksi atau tokoh penting baru.
- Bentuk terperinci, perilaku tambahan, dan vignette baru diberi catatan usulan dan sumber. Racun Ular Piton dipertahankan sesuai entri lama tanpa menciptakan asal kutukan; hewan berelemen game tidak otomatis menjadi roh/elemental dalam narasi.
- Game JSON, angka, ID, skill, reward, dan runtime tidak diubah. Standard narasi diperbarui; validator pasangan dan tautan dijalankan kembali.

## 2026-09-17 | Penyederhanaan sesuai arahan pemilik

- Menyederhanakan 15 Markdown Alam Liar menjadi deskripsi, bentuk, ciri-ciri, habitat, dan lore. Bagian tanpa informasi pendukung dihilangkan. Tidak menambahkan asal-usul baru.
- Menghapus tampilan stat, skill, drop, snapshot JSON, dan laporan teknis dari halaman lore. Seluruh data game tetap di JSON tanpa perubahan nilai, ID, atau status balance.
- Menambahkan `v2.presentation` pada 15 JSON untuk mencatat sumber narasi dan pemisahan tanggung jawab. Markdown sebelumnya tersimpan dalam `_audit/pre_lore_split_markdown.json`.
- Memperbarui standard, audit, serta validator/renderer agar hanya memeriksa pasangan identitas dan tidak memasukkan game data kembali ke Markdown. Menambahkan migrator sekali-jalan `tools/simplify_wildlife_lore.py`.
- Format berlaku untuk kategori berikutnya; kategori di luar Alam Liar tidak diubah pada batch ini. Tidak ada perubahan runtime, commit, atau push.

## 2026-09-17 | Batch 01a/01b — audit ulang runtime dan migrasi Wildlife V2

Bagian ini mencatat eksekusi terbaru, terpisah dari batch awal yang sudah ada saat pekerjaan dimulai. **Migrasi dokumentasi sudah diterapkan; balance, canon gap, dan gameplay implementation tetap BLOCKED.** Tidak mengklaim Wildlife siap rilis atau seluruh Bestiary selesai.

### File dan cakupan

- Dimodifikasi: kelima dokumen existing `BESTIARY_REWORK_AUDIT.md`, `BESTIARY_STANDARD_V2.md`, `CREATURE_TAXONOMY.md`, `BESTIARY_REWORK_CHANGELOG.md`, dan `06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md`. Isi lama dipertahankan sebagai arsip dengan koreksi prioritas di bagian awal. Pedoman milik pemilik tidak diedit.
- Dimodifikasi: 30 file pasangan Wildlife. Batch 01a: Babi Hutan, Beruang Madu Raksasa, Macan Kumbang, Sapi Perah Mandala, Serigala Kelabu. Setelah pemeriksaan 01a lolos, batch 01b: Ayam Hutan, Bebek Danau, Buaya Rawa, Burung Puyuh Hutan, Ikan Sisik Perak, Kambing Arkananta, Kelinci Padang, Kura-Kura Sungai, Rusa Tanduk-Cabang, Ular Piton Pohon.
- Dibuat: `WILDLIFE_INTEGRATION_NOTES.md`; `tools/bestiary_audit.py`, `tools/migrate_wildlife_v2.py`, `tools/verify_bestiary_workspace.py`, `tools/.gitignore`; artefak `_audit/pre_batch_2026-09-17.json`, `pre_batch_hashes.json`, `pre_batch_git_status.txt`, `inventory.json`, `INVENTORY.md`, `REFERENCES.md`, `verification.json`.
- Diaudit: 80 creature pairs pada sembilan kategori, termasuk referensi runtime dan overlap karakter; 15 Wildlife dimigrasi. Tidak ada pasangan hilang; 10 JSON Rangkaruna memakai field lokal tanpa ID/title eksplisit, bukan sepuluh duplicate IDs. Ada 19 overlap filename dengan tokoh; tidak ada entri duplikat dihapus atau ID diganti.

### Isi perubahan

V2 memisahkan identity, species/family, origin/faction/region, encounter/threat/rarity, progression/role, balance, combat/AI, spawn, reward, worldbuilding, runtime observation dan legacy. Wildlife tetap kategori fauna yang mencakup ternak; habitat bukan region. Alias element dibedakan secara eksplisit, khususnya Air Indonesia vs Air runtime (Udara). Null tidak diisi dengan tebakan. Usulan ecology/counterplay/quest diberi label proposal; tidak mengubah cosmology atau penempatan canon regional.

Runtime ternyata tersedia; audit dan framework diperbarui. Formula, curves, equipment dan state tidak dilaporkan hilang. Blocker sebenarnya adalah baseline per encounter, gear availability, target durasi/pressure/reward, efek skill tertunda, konflik matchup dan bukti validasi. Taxonomy Drahkthar diperjelas dari profil Bhuta/Dhemit/Sangrahal; definisi universal/reproduksi Jenggala tetap keputusan pemilik.

Reuse enam item existing: Beast Bone 99, Beast Fang 100, Deer Hide 60, Arkananta Horn 102, Clear Crystal 74, Spirit Dust 282. Snapshot mencatat chain ke equipment dan catalyst existing. **Item baru dibuat: tidak ada; item baru diusulkan: tidak ada.** Resep yang hanya berupa catatan tidak diklaim executable; konflik unggas/Spirit Dust, satwa air/Crystal dan region Deer Hide dicatat. Occultist/Cultist/Necromancer dipetakan ke class learnings, skill/catalyst existing, serta gap pemanggilan/consumption.

Semua nilai legacy dipertahankan dalam snapshot dan metadata arsip, termasuk nilai sebelum perubahan pengguna pada lima Wildlife. Angka runtime disalin sebagai observasi tanpa perubahan ke game. Delapan parameter kalibrasi dan EXP/Saka V2 null; seluruh 15 `stat_status` dan `balance_status` BLOCKED. Babi Markdown VERIFIED dikoreksi menjadi BLOCKED; runtime-match tidak disamakan dengan CALIBRATED. Tidak ada PROVISIONAL/CALIBRATED/VALIDATED diberikan.

### Verifikasi dan batas hasil

Perintah reproduksi:

```text
python tools/bestiary_audit.py --write-report
python tools/verify_bestiary_workspace.py
git diff --check
```

Untuk pembaruan JSON V2 di masa depan, render hanya bagian Markdown bertanda dengan `python tools/bestiary_audit.py --render-wildlife --write-report`. Migrator sekali-jalan sengaja menolak overwrite V2 existing.

Pemeriksaan batch mencakup parse JSON repository, ID Wildlife tetap, seluruh field legacy tetap (kecuali label status), parity seluruh objek V2, hash dependensi, enemy/skill snapshot, element/state/drop IDs, rarity, output crafting IDs, source paths, code fences/struktur Markdown, tautan Markdown dokumentasi yang disentuh, dan hash file sebelum/sesudah. Pencarian literal ID/nama repository-wide disimpan dalam REFERENCES. Git diff ditinjau; skrip sync/mass lama tidak dijalankan. Runtime, agregat, dan perubahan pengguna di luar batch tidak disentuh.

Pemeriksaan ketat V2 lulus setelah perbaikan renderer. Temuan review sempat menangkap pengulangan heading pada hasil render; diperbaiki lalu seluruh 15 bagian di-render ulang dan dicek independen. Verifier juga diperketat agar teks penjelasan marker di Standard tidak keliru dianggap record creature.

Inventaris masih mencatat peringatan legacy/implementation (lihat angka terbaru `verification.json`), termasuk boss tanpa phase/counterplay, Tier >5 yang tidak dipetakan ke class, Void tidak terdaftar, status VERIFIED di kategori lain, dan placeholder effects. Ini **bukan** klaim semua checks repository lolos. Resolusi semua wikilink lore lama dan konsistensi agregat belum diselesaikan; generator belum ditemukan. Wiki tetap menggunakan snapshot lama.

Simulasi balance: tidak dijalankan karena input wajib belum dipilih. Playtest: tidak ada bukti yang terhubung. Markdown/JSON V2 Wildlife: sama; metadata arsip yang bertentangan tetap ditandai, tidak dipaksakan menjadi canon.

### Keputusan dan next batch

Pilih roster/progression/gear dan target encounter; putuskan chart elemen vs runtime; tentukan satwa/ternak yang noncombat; selesaikan konflik asal drop. Batch berikut yang disarankan: **Jenggala 15 entri**, mulai dari source mapping Goblin/Wendigo/Wight dan batas Dhemit/undead serta alias folklore. Tunda redefinisi taxonomy, origin universal, reproduksi, dan penulisan balance sampai keputusan yang tercatat di taxonomy tersedia. Boss, commander dan Thalantira tetap backlog, bukan rewrite otomatis.

Tidak ada commit/push atau perpindahan branch; seluruh perubahan tetap reviewable di workspace.

## Arsip batch sebelumnya

## 2026-09-17 | Batch 01 — Audit + Wildlife standardization

### Files created

- `07_Bestiary/BESTIARY_REWORK_AUDIT.md`
- `07_Bestiary/BESTIARY_STANDARD_V2.md`
- `07_Bestiary/CREATURE_TAXONOMY.md`
- `06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md`
- `07_Bestiary/BESTIARY_REWORK_CHANGELOG.md`

### Files modified

- `07_Bestiary/01_Alam_Liar/Babi_Hutan.md`
- `07_Bestiary/01_Alam_Liar/Babi_Hutan.json`
- `07_Bestiary/01_Alam_Liar/Serigala_Kelabu.md`
- `07_Bestiary/01_Alam_Liar/Serigala_Kelabu.json`
- `07_Bestiary/01_Alam_Liar/Beruang_Madu_Raksasa.md`
- `07_Bestiary/01_Alam_Liar/Beruang_Madu_Raksasa.json`
- `07_Bestiary/01_Alam_Liar/Macan_Kumbang.md`
- `07_Bestiary/01_Alam_Liar/Macan_Kumbang.json`
- `07_Bestiary/01_Alam_Liar/Sapi_Perah_Mandala.md`
- `07_Bestiary/01_Alam_Liar/Sapi_Perah_Mandala.json`

### Creatures audited

- Babi Hutan
- Serigala Kelabu
- Beruang Madu Raksasa
- Macan Kumbang
- Sapi Perah Mandala

### Canon decisions recorded

- Wildlife remains separate from Jenggala and Drahkthar taxonomy.
- No final numerical balance is assigned without runtime formulas and progression baselines.
- Legacy values remain traceable but blocked from final status.

### Legacy values retained or marked blocked

- Babi Hutan HP 150 retained as legacy candidate, not final.
- Serigala Kelabu HP 250 retained as legacy candidate, not final.
- Beruang Madu Raksasa HP 850 retained as legacy candidate, not final.
- Macan Kumbang HP 400 retained as legacy candidate, not final.
- Sapi Perah Mandala HP 120 retained as legacy candidate, not final.

### Stat status changes

- All wildlife batch entries changed from unstructured legacy metadata to `BLOCKED` status with explicit legacy notes.

### Blockers

- Missing runtime database
- Missing progression baseline
- Missing party reference and formulas
- No playtest evidence available

### Owner decisions required

- Confirm final taxonomy boundaries for Jenggala and Drahkthar
- Confirm whether Void becomes a formal element or remains a lore entity
- Authorize completion of full numerical balance framework after runtime data is provided
