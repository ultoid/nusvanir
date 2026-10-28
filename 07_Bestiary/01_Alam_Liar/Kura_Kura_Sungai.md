---
title: Kura-Kura Sungai
tags:
  - Bestiary
---

# Kura-Kura Sungai

## Deskripsi

Penghuni tepian sungai yang membawa perlindungannya sendiri ke mana pun pergi. Kura-Kura Sungai dapat bertahan diam begitu lama hingga disangka batu, tetapi segera mencari air ketika merasa jalur mundurnya terbuka. Tempurung tebal membuatnya tahan gangguan, bukan kebal terhadap bahaya.

## Bentuk

Tempurungnya tebal dan agak merendah, dengan bidang-bidang keras yang membentuk pola tidak beraturan. Warna cokelat batu dan hijau kusam cocok dengan tepian berlumpur; lapisan lumut tipis dapat menempel pada individu yang sering berada di air. Kepalanya kecil dibandingkan tempurung, lehernya berkerut, dan kaki berjari bercakar membantunya berpijak pada lumpur serta akar yang licin.

## Tingkah Laku

Tenang dan tidak memburu manusia. Ia berjemur di tempat yang mudah digunakan untuk kembali ke air. Saat didekati, ia dapat menarik kepala dan kaki ke dalam tempurung atau meluncur ke sungai. Jika diangkat atau dijepit, ia mencakar dan menggigit; membalik tubuhnya bukan cara aman untuk memperlakukannya sebagai benda mati.

## Habitat

Tepian sungai tenang di kawasan Arthiska yang menyediakan lumpur, akar, dan tempat berjemur. Ia menyukai bagian aliran yang jauh dari lalu lintas perahu dan dapat segera kembali ke air dari tempat istirahatnya.

## Kisah — Batu Penahan Kain

Seorang penenun Arthiska menjemur kain di tepi sungai dan mengambil benda bundar untuk menahan ujungnya. Beberapa saat kemudian, kain itu bergerak perlahan menuju air. Ia menariknya kembali dan mendapati kepala kecil keluar dari benda yang dikiranya batu.

Penenun itu meletakkan kura-kura di tepian. Hewan tersebut menunggu sampai bayangan manusia menjauh sebelum masuk ke air. Untuk sisa hari itu, sang penenun memeriksa setiap batu yang hendak dipakainya, sementara murid-muridnya berusaha menahan tawa.

> Acuan sungai dan kerajinan tekstil: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `10.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | **1** | **2** | **10** | **8** | **7** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `150` *(Base 5 + VIT×15 + STR×5)* | **DEF** | `15` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `8` *(INT×8)* | **MDF** | `11` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `71` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `10` *(Base + INT×2)* |
| **ATK** | `17` *(Formula Melee)* | **Action Speed** | `12` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `152.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `103.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.21%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.46%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Shell Bash** | `03 Water` / Certain Hit | `0 SP` | Always (Prioritas 5.0) | `-` |
| **Withdraw** | `03 Water` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **River Ram** | `03 Water` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25 (Stun 25%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: River Ram, Lowest HP%
Turn 2+: Withdraw, Random
Always: Shell Bash, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`20%`) | Material alam / crafting |
