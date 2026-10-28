---
title: Naga Laut Penghancur
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Naga Laut Penghancur

## Deskripsi

Naga air purba tanpa mata yang berburu melalui sonar listrik. Sisiknya menyimpan energi petir dari badai, lalu tubuhnya melesat keluar air untuk merobek tiang kapal. Ia merupakan pemangsa badai Rangkaruna dan tidak otomatis bagian dari Nagarasven Agnitra hanya karena disebut naga.

## Bentuk

Tubuh panjang dan berotot dilapisi sisik biru kehitaman dengan garis listrik pada sisinya. Rongga mata tertutup sisik utuh; deretan organ sonar berada di sekitar rahang dan leher. Sirip besar menggantikan sayap, sedangkan cakar depan pendek membantu mencengkeram kayu. Tanduk pipih mengarahkan air ketika ia menembus permukaan.

## Tingkah Laku

Pemangsa aktif yang mengikuti pantulan suara dan medan listrik. Ia mengitari kapal dalam kedalaman, mengirim pulsa, lalu menyerang bagian tinggi setelah menyimpan petir. Suara keras dapat mengubah pembacaan arah, tetapi belum ditetapkan sebagai kelemahan. Ia menjadi agresif di zona badai tempat energinya mudah terisi.

## Habitat

Zona Badai Abadi di selatan dan tenggara Rangkaruna, antara permukaan yang disambar petir dan lapisan air tempat gema merambat jauh. Ia naik untuk menyerap energi lalu kembali berburu di bawah gelombang.

## Kisah - Tiang yang Menjawab Petir

Petir menyambar laut dan garis biru bergerak di bawah kapal kosong yang hanyut. Naga Laut mengirim pulsa ke arah tiang, menerima gema, lalu melesat menabraknya. Kayu patah jatuh ke air. Makhluk itu berputar sekali, menyadari tidak ada mangsa hidup, dan kembali ke badai mengikuti sambaran berikutnya.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `76.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Large, Draconic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **138** | **28** | **54** | **70** | **66** | **115** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `18400` *(Base 15985 + VIT×15 + STR×5)* | **DEF** | `241` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `221` *(INT×8)* | **MDF** | `196` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `871` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `182` *(Base + INT×2)* |
| **ATK** | `303` *(Formula Melee)* | **Action Speed** | `99` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `95.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `18.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `20.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `22.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `202.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `157.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.45%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.84%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.94%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Sea Dragon Fang** | `Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Tidal Crash** | `Water` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Cataclysmic Breath** | `Water` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5950` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4462` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1540` | Mata uang resmi penjelajahan |
| **Drop 1** | `Primordial Crystal` (`22%`) | Material alam / crafting |
| **Drop 2** | `Storm Wyvern Fang` (`15%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`10%`) | Rampasan langka |
