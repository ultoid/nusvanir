---
title: Rusa Tanduk-Cabang
tags:
  - Bestiary
---

# Rusa Tanduk-Cabang

## Deskripsi

Herbivora besar yang tanduknya menyerupai ranting di antara pepohonan Astradipa. Rusa Tanduk-Cabang dapat berdiri diam di batas cahaya sampai tubuhnya sukar dipisahkan dari hutan. Ketika berjalan di antara tumbuhan pendar, cahaya yang memantul pada tanduknya mudah disangka berasal dari tubuh rusa itu sendiri.

## Bentuk

Tubuhnya tinggi dan berisi, ditopang kaki ramping dengan kuku terbelah. Tanduk bercabang tumbuh melebar dan meninggi seperti susunan ranting muda, menjadikan kepala tampak jauh lebih besar ketika dilihat dari depan. Bulu cokelat kemerahan dengan bagian leher lebih gelap sesuai dengan batang dan tanah hutan. Moncong panjang, telinga lebar, dan mata di sisi kepala memberi kesan selalu siaga. Tanduknya tidak ditetapkan memiliki cahaya atau kekuatan magis sendiri.

## Tingkah Laku

Memakan tumbuhan dan umumnya memilih menjauh dari pendatang. Ia berhenti mengunyah ketika mencium bau asing, lalu mengarahkan telinga sebelum berlari. Individu yang menjaga ruang atau terdesak dapat menundukkan tanduk dan menyeruduk. Anak yang terlihat sendirian tidak otomatis ditinggalkan; induknya mungkin sedang menunggu di balik pepohonan.

## Habitat

Lantai Hutan Astradipa dan ruang terbuka di antara akar raksasa. Cabang rendah yang terlalu rapat membatasi gerak tanduknya, sehingga rusa memilih jalur yang cukup lapang. Ia merupakan penghuni ekosistem bawah, bukan hewan yang berlari di jembatan kota kanopi.

## Kisah — Ranting yang Menoleh

Seorang penjaga muda Asrivana mengira ranting di dekat jalur patroli telah berubah posisi sejak sore. Ia mendekat sambil memperhatikan cahaya tumbuhan yang tersangkut pada bentuk bercabang itu. Lalu ranting tersebut menoleh.

Seekor Rusa Tanduk-Cabang berdiri di balik akar besar, dengan anaknya berlindung pada sisi yang teduh. Penjaga itu menurunkan busur dan mengambil jalan memutar. Dalam laporan malamnya ia hanya mencatat jalur terhalang, tanpa merasa perlu mengusir penghuni hutan yang sudah lebih dahulu berada di sana.

> Acuan: [Astradipa](../../03_Region/02_Astradipa/Astradipa.md) dan [Akar-Dipa](<../../03_Region/02_Astradipa/Cities & Town/Akar Dipa.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `12.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Balanced` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | **1** | **4** | **10** | **10** | **5** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `120` *(Base 5 + VIT×15 + STR×5)* | **DEF** | `12` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `10` *(Base 2 + INT×8)* | **MDF** | `10` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `61` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `14` *(Base + INT×2)* |
| **ATK** | `18` *(Formula Melee)* | **Action Speed** | `15` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `102.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.15%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.50%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Antler Strike** | `01 Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Forest Rush** | `01 Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Branching Charge** | `01 Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Branching Charge, Lowest HP%
Turn 2+: Forest Rush, Random
Always: Antler Strike, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 150%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Deer Hide` (`45%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`20%`) | Komponen sekunder |
