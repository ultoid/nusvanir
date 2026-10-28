---
title: Manta Ray Void
tags:
  - Bestiary
---

# Manta Ray Void

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Pari dari kedalaman Thalantira yang meluncur dengan tenang sebelum melepaskan energi mematikan. Tubuhnya menyerupai bayangan lebar yang terlepas dari dasar laut. Pada air gelap, cahaya yang berkumpul di depannya lebih mudah terlihat daripada gerakan sirip yang membawanya mendekat.

## Bentuk

Cakram tubuhnya melebar ke samping sebagai sepasang sirip lentur, dengan tepian melengkung yang naik turun mengikuti arus. Punggung gelap memuat bintik pucat menyerupai serpih cahaya, sedangkan bagian bawah kelabu berbaur dengan air keruh. Dua lipatan di dekat mulut membentuk corong pendek saat energi berkumpul. Ekor ramping tertinggal di belakang seperti garis yang sulit diikuti. Kesan kosmis pada rupanya memperkuat nama Void tanpa menjelaskan asalnya sebagai penghuni langit atau ruang antarbintang.

## Tingkah Laku

Menghindari benturan langsung, tetapi berbahaya ketika wilayah lintasannya terganggu. Ia membelok lebar untuk menghadap ancaman dan menahan posisi sebelum melepaskan energi. Jika ruang menyempit, pari mundur ke kedalaman alih-alih memaksa cakram tubuh melewati celah kecil. Ketenangan berenangnya tidak membuktikan bahwa ia jinak. Ia dapat melepaskan serangan energi; belum ada perjumpaan bernama yang memastikan niat atau kecerdasannya.

## Habitat

Laut dalam Thalantira adalah habitat sumber. Lereng bawah laut di luar karang raksasa menjadi jalur meluncurnya, menyediakan ruang lebar bagi siripnya. Ia tidak ditempatkan di kubah udara atau kawah hanya karena namanya bernuansa kosmis. Daftar makhluk yang tampak dalam pengungkapan Prologue tidak menyebut Manta Ray Void secara khusus.

## Kisah — Cahaya di Bawah Pusaran

Di bawah arus yang mengamuk, seekor pari melewati lereng batu dengan gerakan hampir tanpa suara. Pemangsa lain muncul dari celah dan mengikutinya. Pari itu membelok, memperlihatkan sisi bawah yang semula tersembunyi.

Cahaya berkumpul di depan mulutnya. Pemangsa berhenti, tetapi semburan telah membelah air di antara mereka. Endapan naik menutupi lereng. Ketika butir pasir kembali turun, pari sudah meluncur lebih dalam, meninggalkan lorong gelap yang sesaat tadi tampak menyala seperti langit.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [Thalantira](../../03_Region/11_Thalantira/Thalantira.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `39.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Void` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying, Aquatic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **55** | **103** | **22** | **53** | **57** | **60** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3420` *(Base 2245 + VIT×15 + STR×5)* | **DEF** | `117` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `232` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `430` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `206` *(Base + INT×2)* |
| **ATK** | `121` *(Formula Magic)* | **Action Speed** | `86` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `12.7%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `14.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `170.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `130.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.80%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `3.09%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.48%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Void Ray** | `11 Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45 (Curse 30%))` |
| **Phase Glide** | `Void` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Abyssal Pulse** | `11 Dark` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25 (Curse 30%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Abyssal Pulse, Lowest HP%
State === Taunt: Phase Glide, Random
Turn % 2 == 0: Phase Glide, Random
Always: Void Ray, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Light: 150%, Lightning: 125%, Void: 50%, Water: 50%
* **Resistensi Status:** Curse: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
