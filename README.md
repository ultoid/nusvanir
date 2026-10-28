# Nusvanir Vault

[![Engine](https://img.shields.io/badge/Engine-RPG%20Maker%20MV-red.svg)](https://www.rpgmakerweb.com/)
[![Genre](https://img.shields.io/badge/Genre-Dark%20Fantasy%20%7C%20Turn--Based%20JRPG-purple.svg)](#)
[![Format](https://img.shields.io/badge/Format-Obsidian%20Vault%20%7C%20Markdown-blue.svg)](#)
[![Status](https://img.shields.io/badge/Database-100%25%20Calibrated-brightgreen.svg)](#)

Pusat data, dokumentasi *worldbuilding*, kanon cerita, dan basis data teknis RPG turn-based untuk semesta **Nusvanir**. 

Repositori ini dirancang sebagai *single source of truth* (SSOT) yang memadukan kedalaman narasi epik fantasi gelap bernuansa kepulauan dengan spesifikasi implementasi langsung ke dalam engine **RPG Maker MV** (didukung ekosistem plugin Yanfly Engine Plugins / YEP).

---

## 📑 Daftar Isi

- [Sinopsis Semesta Nusvanir](#-sinopsis-semesta-nusvanir)
  - [Kosmologi Primordial & Rahasia Ilusi](#1-kosmologi-primordial--rahasia-ilusi)
  - [Garis Waktu & Alur Cerita](#2-garis-waktu--alur-cerita)
  - [Atlas 11 Wilayah](#3-atlas-11-wilayah)
  - [Taksonomi 8 Ras Utama](#4-taksonomi-8-ras-utama)
  - [Ekonomi Koin Saka & Mata Uang](#5-ekonomi-koin-saka--mata-uang)
- [Spesifikasi Sistem RPG Turn-Based](#-spesifikasi-sistem-rpg-turn-based)
  - [Standar Database RPG Maker MV](#1-standar-database-rpg-maker-mv)
  - [Formula Tempur & Resolusi Kerusakan](#2-formula-tempur--resolusi-kerusakan)
  - [Hierarki 35 Kelas Petualang](#3-hierarki-35-kelas-petualang)
  - [Basis Data Perlengkapan & Item](#4-basis-data-perlengkapan--item)
  - [Kamus Status Efek & State Codex](#5-kamus-status-efek--state-codex)
  - [80 Bestiary & Kalibrasi AI Yanfly](#6-80-bestiary--kalibrasi-ai-yanfly)
- [Struktur Direktori Vault](#-struktur-direktori-vault)
- [Panduan Penggunaan & Integrasi](#-panduan-penggunaan--integrasi)
- [Kontributor & Lisensi](#-kontributor--lisensi)

---

## 🌌 Sinopsis Semesta Nusvanir

### 1. Kosmologi Primordial & Rahasia Ilusi

Semesta Nusvanir dibangun di atas ketegangan antara dogma resmi yang diajarkan di kuil-kuil fana dengan kenyataan kosmik tersembunyi:

* **Mitos Resmi (Doktrin Agama Surya):**  
  Sebelum waktu bermula, Sang Hyang Cahaya bertahta dalam kesendirian hampa. Dari air matanya memadat daratan dan samudra Nusvanir, sementara napas pertamanya meniupkan kehidupan ke dalam makhluk fana. Sang Hyang membelah kekuatannya menjadi Kala Laksana untuk menjaga sangkala (waktu) dan bayang-bayang.
* **Kenyataan Tersembunyi (*The Old Tale*):**  
  Jauh sebelum ras fana ada, pengelana kosmik raksasa bernama **Uru** (manifestasi absolut kehampaan / *Void*) singgah di Nusvanir. Benturan medan energi Uru dengan Sang Hyang Cahaya memusnahkan kehidupan purba dan melahirkan aspek **Kegelapan**.  
  Menyadari Uru tidak dapat dibunuh, Sang Hyang merajut ilusi surga tropis abadi bernama **Pulau Thalantira** (*Śaptadvīpa*) untuk memikat kesadaran Uru agar tertidur lelap di dalam kristal purba (*Void Crystal*). Demi melindungi tidur ilusi tersebut dari gangguan makhluk luar, Sang Hyang mendirikan benua kegelapan **Raksamala** sebagai dinding sipir dan memagarinya dengan **Laut Rangkaruna** yang dipenuhi badai petir abadi serta leviathan samudra.

---

### 2. Garis Waktu & Alur Cerita

Alur narasi Nusvanir terbagi ke dalam tiga babak besar:

1. **Prologue (*Tales of The Dark Time*):**  
   Ekspedisi berdarah dua sahabat ksatria Avalerion—**Hector** (Paladin suci) dan **Cassian** (Priest pengasingan)—bersama nelayan **Rama** menembus badai Rangkaruna menuju Thalantira. Ekspedisi ini tanpa sengaja mengguncang segel kristal purba, membangunkan sebagian kesadaran Uru, dan memicu manifestasi teror iblis Mamon di Kota Pelabuhan Aqualis. Tragedi ini berujung pada gugurnya Rama, jatuhnya vonis buang dari Kerajaan Avalerion, serta terpisahnya bayi kembar: **Hiro** (dibesarkan dalam tradisi Cahaya) dan **Damian** (diadopsi oleh Hector).
2. **Prequel / Timeskip (*The Untold Story* - 5 Tahun Pasca-Prologue):**  
   Meluapnya anomali sihir Cahaya memicu ketidakseimbangan global dan mutasi fauna liar. Demi membebaskan Damian dari kutukan jiwa Sangrahal, Hector menginvasi benteng Raksamala seorang diri, membantai seluruh jajaran komandan Bhuta iblis, dan menyerap energi kegelapan mutlak hingga bertransformasi menjadi **Death Knight**. Bersama Damian, Hector mendirikan altar terlarang di reruntuhan Thalantira dan menciptakan doktrin sihir mutlak *Hellfire* (Api Neraka).
3. **Kisah Utama (*The Dual Paths* & Invasi Void):**  
   Retakan dimensi Void terbuka di seantero Nusvanir, menenggelamkan kota-kota utama ke dalam anarki. Cerita terbelah menjadi dua perspektif moral:
   * **The Light Path:** Perjalanan Hiro bersama Aran Sylvar dan Adhiva menyatukan aliansi fana, mencari pencerahan spiritual (*Transcendence*), dan memulihkan segel kosmik.
   * **The Dark Path:** Ambisi Hector dan Damian meruntuhkan tatanan lama kerajaan teokrasi yang munafik dan memusnahkan sumber korupsi dunia dengan kekuatan absolut Api Neraka.

---

### 3. Atlas 11 Wilayah

Bentang alam Nusvanir terbagi menjadi 11 zona administratif dan teritorial berkekuatan unik:

| Wilayah | Karakteristik Utama | Penguasa / Penghuni Dominan |
| :--- | :--- | :--- |
| **Kerajaan Mandala** | Pusat peradaban 5 lingkar konsentris di poros benua. Mengendalikan kota satelit Aqualis, Valkindra, Arthiska, dan Hermindar. | Ras Pribumi & Wahanarsa (Prabu Mandalapati & Dewan Candra Nawa) |
| **Kerajaan Suci Avalerion** | Dataran tinggi teokrasi dengan dinding marmer putih raksasa. Menjunjung supremasi doktrin suci Cahaya. | Manusia Langit & Ordo Holy Knight / Paladin |
| **Hutan Keramat Astradipa** | Hutan hujan mistis berkabut kanopi raksasa yang menyembunyikan retakan dimensi purba. | Bangsa Peri Asrivana & Kera Petarung Hanorok |
| **Pulau Naga Agnitra** | Gugusan kepulauan vulkanik aktif, sungai magma obsidian, dan sarang logam *Adamantite Nest*. | Ras Naga Berzirah Nagarasven |
| **Pegunungan Arkananta** | Rantai pegunungan es vertikal yang dipercaya menopang kubah langit (*Langit Pertiwi*). Tambang mineral terbesar. | Suku Perkasa Butoraksa (Orc), Troliogoro (Troll), & Rakshorien (Dark Elf) |
| **Kota Bebas Cakrawala** | Metropolis gurun pasir di sekitar oasis ajaib. Surga pasar gelap, tentara bayaran, dan artefak terlarang. | Sindikat Cakrawala (Tuan Midas) |
| **Nusa Sayendra** | Kepulauan pulau karang melayang di angkasa barat daya yang ditopang anomali angin magnetik. | Ras Suci Garuda (Puncak Emas Swargaloka) |
| **Kota Suci Tirta Amarta** | Lembah air terjun abadi bertingkat sembilan; mata air pemurnian racun dan penawar kutukan. | Monastisisme Rahib & Peziarah Doktrin Cahaya |
| **Laut Rangkaruna** | Samudra taring karang dan pusaran air pemisah daratan fana dengan domain kegelapan. | Fauna Abyssal, Leviathan, & Monster Purba |
| **Pulau Raksamala** | Benteng karang hitam tanpa fajar; bekas domain kekaisaran iblis (*Drahkthar*) yang kini menjadi padang abu. | Komandan Bhuta (Telah ditumbangkan oleh Hector) |
| **Pulau Misterius Thalantira** | Pulau vulkanik terisolasi; penjara ilusi tempat kesadaran kosmik Uru tertidur dan deposit tunggal *Void Crystal*. | Uru (Tertidur), Proyeksi Ilusi, & Kuil Hellfire |

---

### 4. Taksonomi 8 Ras Utama

1. **Pribumi (*Human*):** Penduduk mayoritas Mandala; adaptif, serbabisa dalam ilmu sains dan magis, serta mendominasi profesi petualang.
2. **Manusia Langit Avalerion (*High Human*):** Memiliki resonansi alami terhadap elemen Cahaya; kaku, berdisiplin militer tinggi, dan berpusat di institusi monastik.
3. **Garuda (*Avesari Celestial*):** Bangsa unggas mulia bersayap emas dari Nusa Sayendra. Memiliki kekebalan biologis dan spiritual mutlak terhadap racun miasma kegelapan.
4. **Nagarasven (*Dragonkin*):** Ras naga kuno penghuni Agnitra dengan ketahanan fisik luar biasa, mampu memanipulasi api bumi, dan menjunjung hierarki kehormatan.
5. **Wahanarsa (*Simian Beastfolk*):** Bangsa kera bertubuh lincah dan berintelektual tinggi di Mandala serta Astradipa; unggul dalam perdagangan, eksplorasi, dan pertahanan gerilya.
6. **Asrivana (*Wood Elf / Sylph*):** Penjaga keharmonisan hutan lebat Astradipa; ahli sihir alam, panahan jarak jauh, dan komunikasi flora-fauna.
7. **Butoraksa & Troliogoro (*Earth Giants*):** Penghuni Arkananta berdaya tahan fisik masif; pengrajin tempa besi dan ksatria benteng garda depan.
8. **Drahkthar (*Shadowkin / Demon*):** Ras entitas kegelapan Raksamala yang terlahir dari resonansi emosi negatif dan energi ketiadaan.

---

### 5. Ekonomi Koin Saka & Mata Uang

Sistem perdagangan Nusvanir bersandar pada mata uang logam standar **Saka** dengan rasio pertukaran desimal yang ketat:

$$\text{1 Saka Kencana (Gold)} = 100\text{ Saka Perak (Silver)} = 10.000\text{ Saka Tembaga (Copper)}$$

* **Saka Tembaga (ID 1):** Alat tukar harian rakyat jelata untuk kebutuhan pangan, sewa kamar, dan ransum petualang.
* **Saka Perak (ID 2):** Transaksi standar perlengkapan senjata, zirah baja, dan pembayaran kontrak tentara bayaran.
* **Saka Kencana (ID 3):** Mata uang elit bangsawan, pembelian properti, bahan tempa langka (*Mithril*, *Adamantite*), dan artefak berkekuatan tinggi.
* **Void Crystal (ID 4):** Komoditas pasar gelap terlarang. Dihargai ribuan Saka Kencana di kalangan alkemis hitam dan kultis karena menyimpan daya magis ketiadaan tanpa batas.

---

## ⚔️ Spesifikasi Sistem RPG Turn-Based

Seluruh sistem mekanik permainan dirancang dengan ketelitian matematis dan kompatibel penuh dengan **RPG Maker MV** serta arsitektur **Yanfly Engine Plugins (YEP)**.

### 1. Standar Database RPG Maker MV

*Dokumen Sumber: [STANDAR_DATABASE_TYPES_RPG_MAKER.md](06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md)*

* **5 Skill Types Resmi:**  
  `01 White Magic` (Penyembuhan/Buff Suci), `02 Black Magic` (Elemen Kehancuran/Status Merusak), `03 Skill` (Teknik Fisik/Senjata/Taktis), `04 Summon` (Pemanggilan Roh Alam/Entitas), `05 Ultimate` (Jurus Pamungkas TP 100).
* **11 Elemen Kanonikal:**  
  `01 Neutral/Fisik`, `02 Api`, `03 Es`, `04 Petir`, `05 Air`, `06 Bumi`, `07 Angin`, `08 Logam`, `09 Suara`, `10 Light/Kudus`, `11 Dark/Void`.
* **10 Tipe Senjata (WType):**  
  Pedang, Belati, Busur, Tongkat Sihir, Kapak, Tombak, Cakar/Fist, Senjata Api, Palu Tempur, Senjata Khusus.
* **6 Tipe Armor (AType):**  
  Kain/Jubah, Kulit Ringan, Zirah Sedang, Zirah Berat, Tameng Ringan, Perisai Besar.
* **7 Slot Perlengkapan (Equip Slots):**  
  `Slot 1: Senjata Utama`, `Slot 2: Senjata Kedua / Perisai`, `Slot 3: Helm / Pelindung Kepala`, `Slot 4: Zirah Badan`, `Slot 5: Sepatu / Boots`, `Slot 6: Aksesoris`, `Slot 7: Relik Purba`.

---

### 2. Formula Tempur & Resolusi Kerusakan

*Dokumen Sumber: [Sistem_Resolusi_Combat_&_AI.md](06_Sistem%20Game%20&%20Ekonomi/Sistem_Resolusi_Combat_&_AI.md)*

Semua formula serangan menggunakan perlindungan proteksi *zero/negative damage* dengan pembungkus standar `Math.max(1, ...)`:

* **Formula Kerusakan Fisik Standar:**
  ```javascript
  Math.max(1, (a.atk * 4 - b.def * 2))
  ```
* **Formula Kerusakan Sihir Standar:**
  ```javascript
  Math.max(1, (a.mat * 4 - b.mdf * 2))
  ```
* **Formula Pemulihan Suci (Healing):**
  ```javascript
  Math.max(1, (a.mat * 3 + a.mdf * 1.5))
  ```
* **Sistem Kecepatan Giliran (ATB Speed Brackets):**  
  Distribusi nilai Agility (AGI) menentukan interval pengisian *gauge* giliran dalam Active Turn-Based System:
  * *Tank Lambat / Monster Raksasa:* AGI 10–25
  * *Ksatria / Prajurit Tempur:* AGI 30–50
  * *Penyihir / Pelindung Suci:* AGI 40–60
  * *Scout / Assassin / Monster Udara:* AGI 75–120+
* **Matriks Target Rate (TGR) & Taunt:**  
  Menjamin peran *aggro management* bekerja deterministik di mana Paladin/Knight memiliki TGR 200–300%, sedangkan Mage/Priest memiliki TGR 50–70%.

---

### 3. Hierarki 35 Kelas Petualang

*Direktori Dokumen: [06_Sistem Game & Ekonomi/Class/](06_Sistem%20Game%20&%20Ekonomi/Class/)*

Tersedia **35 Class** lengkap dengan kurva pertumbuhan stat, restriksi equipment, daftar *Skill Progression* bertingkat (Tier 1 hingga Tier 3 / Master), dan pasif unik:

* **Jalur Fisik (11 Kelas):**  
  Fighter, Warrior, Squire, Brawler, Mercenary, Knight, Martial Artist, Champion, Dragoon, Paladin, Monk.
* **Jalur Sihir (17 Kelas):**  
  Apprentice, Magician, Acolyte, Occultist, Mage, Cleric, Cultist, Priest, Necromancer, Pyromancer, Hydromancer, Geomancer, Aeromancer, Electromancer, Cryomancer, Ferromancer, Echomancer.
* **Jalur Lincah (7 Kelas):**  
  Scout, Archer, Thief, Ranger, Rogue, Sniper, Assassin.

---

### 4. Basis Data Perlengkapan & Item

*Direktori Dokumen: [06_Sistem Game & Ekonomi/Equipment/](06_Sistem%20Game%20&%20Ekonomi/Equipment/) & [Items/](06_Sistem%20Game%20&%20Ekonomi/Items/)*

* **[66 Senjata (Weapons)](06_Sistem%20Game%20&%20Ekonomi/Equipment/01_Weapons.md):** Tersebar merata pada 10 tipe senjata dari tier Kayu/Besi hingga Relik Kuno (Pedang Surya Avalerion, Tombak Petir Garuda, Busur Angin Sylph). Dilengkapi harga beli/jual Saka, recipe tempa, dan deskripsi lore.
* **[123 Zirah & Aksesoris (Armors)](06_Sistem%20Game%20&%20Ekonomi/Equipment/02_Armors.md):** Meliputi 6 tipe proteksi zirah, 20 Aksesoris tematik faksi, 12 Relik Purba bersyarat khusus, serta sistem *Set Bonus* (e.g., Set Zirah Paladin Avalerion, Set Gaib Necromancer).
* **[398 Item Master Index](06_Sistem%20Game%20&%20Ekonomi/Items/README.md):** 50 Consumables, 100 Crafting Materials, 100 Forge Ingots, 100 Valuables/Trade Goods, dan 48 Key Items alur cerita.

---

### 5. Kamus Status Efek & State Codex

*Dokumen Sumber: [Kamus_State_&_Status_Efek.md](06_Sistem%20Game%20&%20Ekonomi/Kamus_State_&_Status_Efek.md)*

Menstandarisasi total **203 State** RPG Maker MV:
* **26 Canonical States (ID 201–226):** Status pertempuran umum seperti *Stun, Poison, Bleed, Burn, Freeze, Shock, Silence, Blind, Confusion, Sleep, Taunt, Invincibility, Doom*, dll.
* **177 Skill Buff / Debuff / Passive States (ID 301–477):** State unik turunan bakat 35 kelas dan monster boss (e.g., *Hellfire Aura, Dragon Scales, Holy Barrier, Shadow Cloak*).

---

### 6. 80 Bestiary & Kalibrasi AI Yanfly

*Direktori Dokumen: [07_Bestiary/](07_Bestiary/)*

Seluruh 80 entitas monster dan boss telah terverifikasi, bebas dari file usang, dan dilengkapi blok konfigurasi AI siap-pakai untuk plugin `YEP_BattleAICore`:

* **Distribusi Ekosistem:**
  * 15 Fauna Alam Liar Nusantara (Hutan Mandala, Sungai, Lembah)
  * 16 Entitas Jenggala (Siluman, Monster Kegelapan Liar, Mitologi Lokal)
  * 17 Predator & Mutasi Void Thalantira
  * 4 Outpost Guardian Avalerion (Ksatria Elemen Penjaga Garis Depan)
  * 4 Naga Penjaga Agnitra (*Argentfang, Blackhorn, Mithralis, Orichalor*)
  * 3 Kepala Suku Arkananta (*Grok, Krom, Nyai Larasati*)
  * 4 Jenderal Garuda Nusa Sayendra (*Jatayu, Paksi, Sempati, Suparna*)
  * 7 Komandan Benteng Raksamala (*Asmodea, Beelzebub, Belphegor, Leviathanus, Luciferus, Mamon, Vraka*)
  * 10 Teror Kedalaman Laut Rangkaruna
* **Standar Blok AI Taktis:**  
  Setiap monster memiliki prioritas keputusan cerdas (kondisi HP threshold, deteksi party member yang terlemah, rotasi giliran pembuka, pemulihan darurat, dan serangan pamungkas).

---

## 📂 Struktur Direktori Vault

```text
Nusvanir_Vault/
├── 02_World/                    # Atlas overview dan kosmologi dasar
├── 03_Region/                   # Profil mendalam 11 wilayah teritorial
├── 04_Ras/                      # Fisiologi, budaya, dan atribut 8 bangsa
├── 05_Karakter & Tokoh Penting/ # Lembar karakter biografi tokoh kanonikal
├── 06_Sistem Game & Ekonomi/    # Arsitektur teknis turn-based RPG Maker MV
│   ├── Class/                   # 35 Kelas petualang (Fisik, Sihir, Lincah)
│   ├── Equipment/               # 66 Senjata & 123 Armor, Aksesoris, Relik
│   ├── Items/                   # 398 Item consumables, material, dan kunci
│   ├── Kamus_State_&_Status_Efek.md # Kamus 203 state (ID 201-477)
│   ├── STANDAR_DATABASE_TYPES_RPG_MAKER.md # Standar tipe database MV
│   ├── Sistem_Mata_Uang.md      # Nilai kurs Saka & ekonomi komparatif
│   ├── Sistem_Resolusi_Combat_&_AI.md      # Formula damage & algoritma AI
│   └── Sistem_Stat_&_Formula_Turn_Based.md # Teori komputasi stat
├── 07_Bestiary/                 # Database 80 monster & script AI Yanfly
├── 08_Story/                    # Naskah cerita (Prologue, Untold, Light Path)
├── 09_Maps/                     # Peta referensi kartografi Nusvanir
├── Concept Art/                 # Aset seni konseptual karakter & lokasi
├── Database/                    # File database mentah (Spreadsheet master)
├── tools/                       # Skrip automasi sinkronisasi & builder database
├── Kitab_Nusvanir_Kodex_Semesta.md # Master Codex Semesta Nusvanir (BAB I-VII)
└── README.md                    # Dokumentasi utama repositori
```

---

## 🛠️ Panduan Penggunaan & Integrasi

### Untuk Game Developer (RPG Maker MV / MZ)
1. **Penerapan Tipe:** Buka tab *Types* di database RPG Maker MV, lalu selaraskan daftar *Skill Types, Elements, Weapon Types,* dan *Armor Types* sesuai panduan [STANDAR_DATABASE_TYPES_RPG_MAKER.md](06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md).
2. **Implementasi Kelas & Senjata:** Salin parameter stat, slot equipment, dan formula damage dari direktori `06_Sistem Game & Ekonomi/Class/` dan `Equipment/`.
3. **Konfigurasi AI Lawan:** Salin blok tag `<AI Priority> ... </AI Priority>` pada setiap berkas monster di `07_Bestiary/` langsung ke kotak *Note* musuh di RPG Maker MV (membutuhkan plugin `YEP_BattleAICore`).

### Untuk Penulis & Narator Cerita
* Pelajari [Kitab Nusvanir: Kodex Semesta](Kitab_Nusvanir_Kodex_Semesta.md) untuk memahami garis batas hukum dunia, faksi politik, sejarah peradaban, dan konsistensi terminologi nusantara sebelum menyusun dialog maupun ekspansi quest.

### Optimalisasi Obsidian
* Repositori ini dikonfigurasi penuh untuk software catatan **Obsidian**. Semua tautan antar-dokumen menggunakan format standar markdown yang saling bertaut (*bidirectional links*) dan mendukung visualisasi grafik pengetahuan (*Graph View*).

---

## 📜 Kontributor & Lisensi

* **Konsep Semesta & Desain Game:** Tim Pengembang Semesta Nusvanir.
* **Lisensi Konten:** Hak cipta cerita, worldbuilding, dan basis data dilindungi. Digunakan secara eksklusif untuk proyek semesta Nusvanir.
