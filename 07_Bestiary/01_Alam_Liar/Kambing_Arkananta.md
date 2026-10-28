---
title: Kambing Arkananta
tags:
  - Bestiary
---

# Kambing Arkananta

## Deskripsi

Pemakan tumbuhan pegunungan yang mampu berdiri pada pijakan yang tampak terlalu sempit bagi tubuhnya. Kambing Arkananta lebih percaya pada jalur tebing daripada jalan lebar yang dilalui orang. Gerakannya dapat menunjukkan tempat berpijak, tetapi bukan jaminan bahwa manusia yang mengikutinya akan mampu kembali.

## Bentuk

Tubuhnya padat dengan dada kuat dan tungkai yang berakhir pada kuku terbelah. Tanduk kerasnya melengkung ke belakang, dengan pangkal tebal serta permukaan beralur. Bulu kelabu batu dan cokelat kusam membuat tubuhnya menyatu dengan lereng; bagian leher serta dada lebih lebat untuk menahan udara pegunungan. Mata yang berjauhan pada sisi kepala memberi kesan selalu mengawasi ruang di sekelilingnya.

## Tingkah Laku

Tidak memburu makhluk lain dan biasanya menghindari pendatang dengan naik ke tempat yang lebih tinggi. Ia dapat menghentakkan kaki dan merendahkan tanduk ketika terpojok pada tepian sempit. Induk melindungi anak, sementara individu yang berebut ruang dapat saling menanduk. Menghalangi jalur mundurnya lebih berbahaya daripada sekadar terlihat olehnya dari kejauhan.

## Habitat

Lereng berbatu Pegunungan Arkananta, terutama tepian yang masih ditumbuhi rumput dan semak. Pendatang lebih sering menjumpainya di lereng luar. Keberadaannya tidak menjadi bukti bahwa jalur menuju inti pegunungan aman dilalui.

## Kisah — Jalan yang Bukan untuk Manusia

Seorang pencari mineral mengikuti Kambing Arkananta yang bergerak menuju singkapan batu berkilau. Ia mengira hewan itu telah menemukan jalan pintas. Setelah beberapa langkah, jalur di belakangnya runtuh menjadi kerikil dan kambing tersebut sudah berada di sisi lain celah.

Ia terpaksa meninggalkan kantong mineral agar dapat memanjat kembali. Dari tempat aman, ia melihat kambing itu menunduk memakan rumput yang tumbuh di antara batu. Harta yang dikejar keduanya ternyata berbeda sejak awal.

> Acuan: [Pegunungan Arkananta](<../../03_Region/05_Arkananta/Arkananta.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `8.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Neutral` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Mountain` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | **1** | **2** | **10** | **10** | **5** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `126` *(Base 1 + VIT×15 + STR×5)* | **DEF** | `13` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `8` *(INT×8)* | **MDF** | `10` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `65` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `11` *(Base + INT×2)* |
| **ATK** | `21` *(Formula Melee)* | **Action Speed** | `15` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `102.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.15%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.50%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Horn Ram** | `Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Stun 25%)` |
| **Cliff Kick** | `Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Mountain Charge** | `Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Neutral 100%, Neutral 200% (Weak)
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Arkananta Horn` (`35%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`20%`) | Komponen sekunder |
