---
title: Blackhorn
tags:
  - Bestiary
  - Boss
---

# Blackhorn

## Deskripsi

Naga penjaga Adamantite Nest yang tubuhnya dilindungi zirah alami Adamantite. Logam hitam ini terkenal mampu meredam atau memantulkan sihir, menjadikan Blackhorn benteng hidup di kedalaman Mahasvara. Ia bergerak lambat dan menyemburkan magma murni; menghadapi kekuatannya menuntut keteguhan, bukan sekadar semburan sihir yang lebih terang.

## Bentuk

Tubuhnya berat pada dada dan bahu, ditopang empat kaki bercakar lebar. Lempeng Adamantite hitam bertumpuk rapat dari tengkuk hingga pangkal ekor, membentuk perlindungan tebal dengan sambungan sempit. Sepasang tanduk kusam melengkung ke belakang seperti bongkah logam yang ditempa bersama kepala. Sayapnya terlipat dekat tubuh dan jarang dibuka dalam lorong. Cahaya sihir yang menyentuh zirah dapat meredup atau terpental pada permukaannya, sementara pijar magma tetap terlihat di sela rahang. Ketika ia berdiam, tubuhnya hampir menyatu dengan dinding gua hitam.

## Kepribadian dan Sikap

Blackhorn sabar, tertutup, dan teguh menjaga batas yang dipercayakan kepadanya. Ia menghargai ketahanan serta kesungguhan yang dibuktikan dalam waktu panjang. Pujian tidak mudah melunakkan sikapnya, tetapi orang yang bertahan menghadapi kesulitan tanpa mengorbankan rekannya dapat memperoleh rasa hormatnya. Seperti zirahnya, keputusan Blackhorn sulit ditembus; ia kadang terlambat menerima perubahan yang diperlukan. Dalam ujian ia menuntut penantang memahami berat tanggung jawab sebelum berhak menerima material pelindung yang begitu kuat.

## Lokasi Nest

Adamantite Nest berada di dasar lereng barat Gunung Mahasvara, di balik labirin gua dengan dinding hitam yang menyerap suara. Blackhorn menjaga bagian dalam sarang, tempat naga dapat beristirahat menyerupai patung selama berabad-abad. Nest ini mewakili ketahanan Adamantite dan pertahanan bawah tanah Agnitra. Bahan tempaan yang diberikan kepada penantang yang layak membawa fungsi tersebut: perlindungan terhadap sihir dan senjata yang sanggup menghadapi naga.

## Kisah — Jawaban di Bawah Tanduk

Seorang pembawa pesan berhenti di depan sosok hitam yang menutupi jalan. Ia telah menyiapkan banyak pujian, tetapi lupa kalimat pertama ketika mata Blackhorn terbuka. Naga itu hanya menanyakan keperluannya.

Pembawa pesan mengakui bahwa ia tidak mengetahui jalan berikutnya dan takut salah memasuki sarang. Blackhorn lama tidak menjawab. Lalu kepalanya bergeser, memperlihatkan jalan yang semula tertutup bayangan tanduk. Ia memberi petunjuk menuju tempat pemeriksaan dan meminta orang itu menunggu pengawalan. Pesan tersebut akhirnya dapat diteruskan karena pembawanya berani mengaku tidak tahu, bukan karena berhasil membuat sang penjaga terkesan.

> Acuan: [Adamantite Nest](../../03_Region/04_Agnitra/Cities%20%26%20Town/Adamantite%20Nest.md); [Nagarasven](../../04_Ras/02_Wuru%20Loka/Nagarasven_%28Naga%29.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `53.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T6 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth/Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Water` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Large, Draconic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **81** | **16** | **34** | **48** | **43** | **66** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `8970` *(Base 7575 + VIT×15 + STR×5)* | **DEF** | `140` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `124` *(INT×8)* | **MDF** | `113` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `512` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `106` *(Base + INT×2)* |
| **ATK** | `179` *(Formula Melee)* | **Action Speed** | `65` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `91.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `13.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `14.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `13.8%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `181.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `133.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.98%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.48%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.04%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Blackhorn Ram** | `04 Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45 (Stun 25%))` |
| **Draconic Crush** | `04 Earth` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Stun 25%))` |
| **Obsidian Breath** | `04 Earth` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Obsidian Breath, All Foes
Turn % 3 == 0: Draconic Crush, Highest ATK
HP% <= 50%: Obsidian Breath, Lowest HP%
Always: Blackhorn Ram, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 75%, Water: 150%
* **Resistensi Status:** Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `2520` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1890` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `700` | Mata uang resmi penjelajahan |
| **Drop 1** | `Mithril Dragon Fang` (`35%`) | Material alam / crafting |
| **Drop 2** | `Mithril Dragon Claw` (`20%`) | Komponen sekunder |
| **Drop 3** | `Mahasvara Crystal` (`15%`) | Rampasan langka |
| **Boss / Unique Drop** | `Blackhorn Cresthelm / Blackhorn Scaleplate / Blackhorn Sabatons` (`5%`) | Rampasan unik / piala bos |
