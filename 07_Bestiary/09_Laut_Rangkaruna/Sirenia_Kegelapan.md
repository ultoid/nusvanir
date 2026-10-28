---
title: Sirenia Kegelapan
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Sirenia Kegelapan

## Deskripsi

Makhluk abyssal setengah perempuan dan setengah ikan yang bernyanyi dari balik kabut. Suaranya mengacaukan pikiran nakhoda serta kru sampai mereka saling menyerang atau mengarahkan kapal ke karang. Dalam Prologue, lolongannya mencoba mencuci otak Hector selama pelayaran Rangkaruna.

## Bentuk

Bagian atas tubuh menyerupai perempuan pucat bermata menyala, berlanjut menjadi ekor ikan laut dalam dengan sirip robek. Rambut panjang menyatu dengan kabut dan air. Insang gelap membuka pada leher ketika ia bernyanyi. Gigi kecil tampak ketika melodi berubah menjadi lolongan. Wujud yang terlihat di kabut dapat dipengaruhi ilusi, sehingga tidak selalu sama dengan tubuh di air.

## Tingkah Laku

Memikat dari jarak jauh dan menghindari perlawanan langsung. Sirenia memindahkan sumber suara melalui gema, menguji ketakutan atau kecurigaan kru, lalu memperbesar konflik. Jika ditemukan, ia menyelam di antara karang. Kemampuan mental tidak membuktikan hubungan dengan Deepwater Siren Thalantira atau Asmodea.

## Habitat

Kuburan Kapal di dalam Zona Badai Abadi, tempat kabut, gema, bangkai, dan karang tinggi membuat arah suara sulit dinilai. Jalur sempit di sekitar batu tajam menyediakan akibat mematikan bahkan tanpa serangan fisik.

## Kisah - Lolong di Hari Ketiga

Sirenia melolong dari kejauhan ketika kapal Rama telah tiga hari dihantam monster. Suara itu mencoba memasuki pikiran Hector, sementara kru yang kelelahan harus tetap menjaga arah. Mereka mempertahankan tugas dan menjauh dari karang tanpa mengejar penyanyi di kabut. Bertahan berarti menolak menjadikan setiap pikiran yang muncul sebagai perintah.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [05 Rahasia Sang Echomancer](../../08_Story/02_Prologue/05_Rahasia_Sang_Echomancer.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `79.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Water/Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Caster, Sonic, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **63** | **27** | **24** | **66** | **57** | **66** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3610` *(Base 2305 + VIT×15 + STR×5)* | **DEF** | `131` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `214` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `476` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `183` *(Base + INT×2)* |
| **ATK** | `138` *(Formula Magic)* | **Action Speed** | `86` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `14.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `173.7%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `133.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.98%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.81%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.60%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Dark Siren Song** | `Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45 (Silence 35%)` |
| **Abyssal Lure** | `Dark` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35 (Curse 30%)` |
| **Drowning Dirge** | `Water` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25 (Silence 35%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%, Lightning: 125%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Kala Crystal` (`18%`) | Material alam / crafting |
| **Drop 2** | `Spirit Thread` (`15%`) | Komponen sekunder |
