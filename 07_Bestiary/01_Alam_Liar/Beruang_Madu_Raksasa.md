---
title: Beruang Madu Raksasa
tags:
  - Bestiary
---

# Beruang Madu Raksasa

## Deskripsi

Penghuni gua hutan yang kekuatannya mudah disalahartikan sebagai kegemaran memburu. Beruang Madu Raksasa dapat membongkar kayu lapuk dengan cakarnya, tetapi tidak setiap batang yang dicabiknya menandai serangan terhadap makhluk lain. Bau makanan yang terbawa rombongan sering lebih menarik perhatiannya daripada rombongan itu sendiri.

## Bentuk

Tubuhnya besar dan berbahu lebar, ditopang tungkai tebal dengan cakar melengkung. Bulunya hitam kecokelatan, dengan bidang pucat seperti bulan sabit yang tidak beraturan pada dada. Moncongnya lebih terang, telinganya membulat, dan bekas getah atau tanah dapat menggumpal pada bulu lengan. Ketika berdiri untuk mengendus, tubuhnya menjulang menutupi pandangan ke mulut gua. Sebutan raksasa menunjukkan wujudnya, bukan bukti bahwa ia berasal dari ras atau kutukan tertentu.

## Tingkah Laku

Bersifat teritorial dan berbahaya jika dikejutkan dari dekat. Ia dapat mengendus atau mengamati sebelum memutuskan mendekat. Gangguan pada tempat berlindung, anak, atau makanan dapat memancing serangan mendadak. Ia memakan madu, serangga, dan buah, sehingga tidak bergantung pada daging semata.

## Habitat

Gua-gua hutan dan pepohonan besar di lereng luar Arkananta. Pertemuan kawasan berbatu dan hutan menyediakan tempat berlindung serta makanan. Persebaran ini tidak menetapkan keberadaannya di inti pegunungan yang masih belum dijelajahi.

## Kisah — Bekal di Mulut Gua

Seorang pencari mineral berlindung dari hujan di bawah batu besar pada lereng Arkananta. Ia baru membuka bekal ketika napas berat terdengar dari belakangnya. Di kedalaman celah itu, dada pucat seekor beruang bergerak perlahan.

Ia meninggalkan bungkusan makanannya dan mundur tanpa mengambil kapak yang tersandar di dinding. Ketika kembali bersama rekannya, bungkus itu sudah terbuka dan kapaknya masih utuh. Sejak itu ia selalu memeriksa jejak sebelum menyebut sebuah gua kosong.

> Acuan: [Arkananta](../../03_Region/05_Arkananta/Arkananta.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `4.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **17** | **2** | **6** | **16** | **14** | **12** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `460` *(Base 195 + VIT×15 + STR×5)* | **DEF** | `26` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `18` *(Base 2 + INT×8)* | **MDF** | `21` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `114` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `21` *(Base + INT×2)* |
| **ATK** | `37` *(Formula Melee)* | **Action Speed** | `21` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.6%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `106.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.36%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.06%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.80%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Heavy Paw** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Honey Rage** | `Earth` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Crushing Maul** | `Earth` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25 (Stun 25%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 150%
* **Resistensi Status:** Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `80` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `60` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `30` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`40%`) | Material alam / crafting |
| **Drop 2** | `Beast Fang` (`30%`) | Komponen sekunder |
