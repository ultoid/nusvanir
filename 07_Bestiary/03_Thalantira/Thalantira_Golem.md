---
title: Thalantira Golem
tags:
  - Bestiary
---

# Thalantira Golem

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Makhluk batu yang diproyeksikan Uru untuk menjaga kawasan kuil Thalantira. Wujudnya menyatukan kesan benda tak bergerak dan tubuh yang dapat menghalangi jalan; bahkan susunan batu yang tampak sederhana dapat menjadi bagian dari ilusi pulau yang menunggu perintah penciptanya.

## Bentuk

Tubuh penjaganya tersusun dari bongkah besar: dada lebar, lengan berat, dan kaki pendek yang menapak rata. Kepala masuk di antara bahu, menyisakan celah gelap seperti tempat mata. Permukaan kasar memuat lekuk aus dan mineral pucat yang mengikuti sambungan. Jari-jari tampak seperti potongan batu yang dapat mengatup. Prologue juga memperlihatkan golem kecil setinggi lutut di lorong Kuil Tanah; ukuran itu tidak dipaksakan menjadi ukuran tetap seluruh penjaga batu.

## Tingkah Laku

Perilakunya harus dibaca sesuai keadaan pulau. Pada kunjungan awal Hector dan Cassian, golem kecil menjerit dengan decitan batu lalu bersembunyi ketakutan. Pada pengungkapan berikutnya, Golem muncul bersama monster darat yang mengancam. Saat berjaga, tubuh besar menutup lintasan dan bergerak ketika batas ruangnya dilanggar. Belum dipastikan apakah sosok kecil dan besar merupakan individu yang berubah, perbedaan ukuran alami, atau bagian dari penampakan ilusi.

## Habitat

Uru biasa memproyeksikannya di kawasan kuil, terutama lorong bercabang Kuil Tanah. Ambang ruangan dan jalan berbatu memberi tempat bagi tubuh penjaga untuk melebur dengan lingkungan. Kuil serta Golem merupakan bagian dari susunan ilusi dan tidak membuktikan pernah adanya kerajaan atau pemukiman di Thalantira.

## Kisah — Suara Kecil di Lorong Batu

Cahaya dari tongkat Cassian memasuki lorong Kuil Tanah. Hector berjalan dengan pedang siap, menunggu sesuatu yang cukup besar untuk menjelaskan keganjilan pulau. Yang muncul justru tubuh-tubuh batu kecil di dekat kaki mereka.

Golem itu menjerit dan berlari menyembunyikan diri. Tidak ada serbuan, hanya decitan yang menghilang di percabangan. Hector menggerutu melihat monster ketakutan pada manusia. Perjalanan mereka berlanjut, tetapi kelucuan singkat itu menjadi bagian lain dari kedamaian yang terlalu mudah diterima sebelum kebenaran pulau terbuka.

> Acuan: [07 Tiga Kuil Penjaga](../../08_Story/02_Prologue/07_Tiga_Kuil_Penjaga.md); [08 Ujian Para Pelindung](../../08_Story/02_Prologue/08_Ujian_Para_Pelindung.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md); [Thalantira](../../03_Region/11_Thalantira/Thalantira.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `45.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Construct` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Mini Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Magic` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Large, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **105** | **26** | **44** | **70** | **56** | **126** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `13125` *(Base 10710 + VIT×15 + STR×5)* | **DEF** | `242` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `205` *(INT×8)* | **MDF** | `199` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `860` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `169` *(Base + INT×2)* |
| **ATK** | `232` *(Formula Melee)* | **Action Speed** | `84` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `18.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `23.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `190.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `163.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.78%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.78%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.76%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Voidstone Fist** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Curse 30%)` |
| **Ancient Barrier** | `Void` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Thalantira Quake** | `Void` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Magic: 150%, Void: 50%
* **Resistensi Status:** Bleed: 0%, Curse: 50%, Freeze: 70%, Paralyze: 70%, Poison: 0%, Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `3400` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `2550` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `880` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
