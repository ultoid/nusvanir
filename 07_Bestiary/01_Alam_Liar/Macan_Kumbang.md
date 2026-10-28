---
title: Macan Kumbang
tags:
  - Bestiary
---

# Macan Kumbang

## Deskripsi

Pemburu malam yang menggunakan cabang besar sebagai tempat mengamati lantai hutan. Macan Kumbang jarang mengumumkan kehadirannya dengan geraman; keheningan di sekitar jalur mangsa dapat menjadi petunjuk yang lebih dahulu terasa. Ia mengandalkan kedekatan dan kejutan, bukan pengejaran panjang di tempat terbuka.

## Bentuk

Tubuhnya memanjang, lentur, dan berotot, dengan bahu yang bergerak jelas di bawah kulit ketika berjalan. Bulu hitam pekat menyembunyikan pola belang bundar yang hanya tampak ketika disinari dari sudut tertentu. Kepalanya lebar, telinganya membulat, dan kumis pucat membingkai moncong. Telapak besar serta ekor panjang membantu keseimbangan di cabang; mata yang memantulkan cahaya tidak berarti ia memiliki penglihatan gaib.

## Tingkah Laku

Buas sebagai pemangsa, tetapi biasanya menghindari rombongan yang gaduh. Ia lebih suka mengamati dari perlindungan dan mendekati mangsa yang terpisah. Ketika terluka, terpojok, atau menjaga anak, sikap menghindar dapat berubah menjadi serangan. Ekor bergerak tajam, telinga merapat, dan tubuh merendah merupakan peringatan yang berbeda dari sikap beristirahat di dahan.

## Habitat

Pepohonan besar Astradipa dengan cabang kuat dan lantai hutan yang teduh. Habitat ini memperjelas catatan lama tentang pohon-pohon tinggi Jenggala, tanpa menjadikannya anggota Jenggala atau penghuni tetap permukiman kanopi Asrivana.

## Kisah — Mata di Atas Jalan

Seorang pembawa pesan yang dipandu melintasi Astradipa melihat sepasang mata di atas jalan. Ia mengangkat lentera, tetapi pemandunya menahan pergelangan tangannya dan mengajaknya terus berjalan dengan tenang.

Setelah melewati pohon itu, mereka menemukan jejak kecil di tanah lunak. Pembawa pesan baru mengerti mengapa mata tersebut tidak beralih darinya. Yang mengawasi mereka bukan penjaga rahasia Asrivana, melainkan seekor induk yang menunggu orang-orang asing menjauh dari anaknya.

> Acuan kanopi: [Astradipa](../../03_Region/02_Astradipa/Astradipa.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `11.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Stealth` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **16** | **3** | **6** | **19** | **19** | **8** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `360` *(Base 160 + VIT×15 + STR×5)* | **DEF** | `20` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `21` *(INT×8)* | **MDF** | `19` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `92` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `23` *(Base + INT×2)* |
| **ATK** | `35` *(Formula Melee)* | **Action Speed** | `29` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `6.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `6.1%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.7%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `104.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.24%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.09%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.92%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Shadow Pounce** | `Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Rending Claw** | `Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Predator Ambush** | `Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 150%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `80` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `60` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `30` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Fang` (`40%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`25%`) | Komponen sekunder |
