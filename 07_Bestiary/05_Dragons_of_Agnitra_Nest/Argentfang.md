---
title: Argentfang
tags:
  - Bestiary
  - Boss
---

# Argentfang

## Deskripsi

Naga penjaga Silver Nest yang membawa dingin perak murni dan api pucat membeku. Kehadirannya menjaga tempat pemulihan naga yang hampir menyerah pada naluri Feral. Geraknya tetap senyap, tetapi kekuatannya kini dipahami melalui tugas pemurnian: menghentikan ancaman tanpa menghilangkan kesempatan bagi yang masih dapat diselamatkan.

## Bentuk

Sisik perak murni menutupi tubuh rampingnya, dengan kilau putih yang menyatu dengan salju dan kristal es. Taring panjang memantulkan cahaya seperti bulan pada permukaan beku, sementara tanduk pendek mengikuti garis kepala. Sayap dilipat rapat ketika ia berjalan di antara ceruk pemulihan. Udara dingin berkumpul di sekitar sisik, menekan panas yang terbawa dari lereng vulkanik. Ketika rahangnya terbuka, uap tipis mendahului nyala pucat. Embun beku tertinggal pada batu yang dilewatinya, menandai pertemuan kekuatan naga dengan sifat dingin Silver.

## Kepribadian dan Sikap

Argentfang tenang, selektif, dan peka terhadap penderitaan yang disembunyikan di balik amarah. Ia tidak mudah percaya pada ucapan tentang niat baik; ia memperhatikan bagaimana seseorang memperlakukan makhluk yang lemah atau kehilangan kendali. Terhadap naga yang sedang dipulihkan ia sabar, tetapi ia keras kepada orang yang hendak memanfaatkan keadaan mereka. Ia menguji kemurnian niat tanpa mencari kematian penantang. Ketertutupannya dapat terasa dingin, namun ia mengingat janji kecil dan pertolongan yang diberikan tanpa mengharapkan hadiah.

## Lokasi Nest

Silver Nest terletak di lembah utara Agnitra, wilayah bersalju yang didinginkan oleh energi perak murni. Argentfang menjaga ceruk dan jalur di antara kristal es Lembah Cermin Suci, tempat pemulihan spiritual naga berlangsung. Nest ini mewakili pemurnian Silver dan kekuatannya melawan makhluk gaib. Pusaka perak diberikan kepada mereka yang membuktikan kelayakan hati. Lokasi ini menggantikan sebutan Gua Gelap Agnitra yang sebelumnya belum terpetakan.

## Kisah — Perak untuk Mereka yang Menunggu

Seorang penantang datang ke Silver Nest untuk memperoleh pusaka perak. Di jalan menuju ceruk Argentfang, ia melihat naga muda yang menggigil dan mencakar es dalam kegelisahan. Ia berhenti pada jarak aman, memanggil penjaga pemulihan, lalu menunggu sampai bantuan tiba.

Ketika akhirnya menghadap Argentfang, ia meminta maaf karena terlambat. Sang naga menanyakan mengapa ia berhenti meskipun tidak mengenal yang sedang kesakitan. Penantang itu menjawab bahwa hadiah dapat menunggu. Argentfang menundukkan kepala dan mempersilakannya masuk. Ujian belum berakhir, tetapi untuk pertama kalinya mereka berbicara tentang perak sebagai sesuatu yang akan dipakai untuk melindungi, bukan sekadar dimiliki.

> Acuan: [Silver Nest](../../03_Region/04_Agnitra/Cities%20%26%20Town/Silver%20Nest.md); [Nagarasven](../../04_Ras/02_Wuru%20Loka/Nagarasven_%28Naga%29.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `55.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T6 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark/Lightning` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Large, Draconic, Frenzy` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **78** | **18** | **30** | **55** | **61** | **43** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `7020` *(Base 5985 + VIT×15 + STR×5)* | **DEF** | `103` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `140` *(INT×8)* | **MDF** | `102` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `391` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `120` *(Base + INT×2)* |
| **ATK** | `171` *(Formula Melee)* | **Action Speed** | `91` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `91.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `14.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `12.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `179.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `121.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.29%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.54%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.30%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Lunar Claw** | `Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Moonshadow Dive** | `Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Frenzied Moonfang** | `Dark` / Physical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%, Lightning: 75%
* **Resistensi Status:** Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `2520` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1890` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `700` | Mata uang resmi penjelajahan |
| **Drop 1** | `Mithril Dragon Fang` (`30%`) | Material alam / crafting |
| **Drop 2** | `Mithril Dragon Claw` (`20%`) | Komponen sekunder |
| **Drop 3** | `Eclipse Feather` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Moonfang Nighthelm / Moonfang Shadowcoat / Moonfang Stalkers` (`5%`) | Rampasan unik / piala bos |
