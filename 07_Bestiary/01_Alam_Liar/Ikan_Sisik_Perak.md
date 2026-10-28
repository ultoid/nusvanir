---
title: Ikan Sisik Perak
tags:
  - Bestiary
---

# Ikan Sisik Perak

## Deskripsi

Ikan air tawar yang sisiknya memantulkan cahaya ketika kawanannya berbelok serentak. Sering dianggap mudah ditangkap karena bergerak dekat permukaan, padahal kilatan yang terlihat dapat berasal dari arah yang berbeda dengan gerakan tubuhnya. Kawanan yang mendadak merapat menandakan ada gangguan di air, bukan selalu gejala sihir.

## Bentuk

Tubuhnya ramping dan sedikit pipih ke samping, dengan ekor bercabang serta sirip tipis yang tampak tembus cahaya. Sisik keperakan lebih terang pada sisi tubuh dan perut, sementara punggung berwarna kelabu kehijauan. Mulutnya kecil, matanya membulat, dan tepian sisik membentuk pola rapat seperti kepingan logam halus. Kilau tersebut merupakan ciri rupa, bukan pernyataan bahwa tubuhnya mengandung perak yang dapat ditambang.

## Tingkah Laku

Tidak agresif terhadap manusia. Ia bergerak berkelompok di perairan tenang, menyambar makanan kecil lalu segera kembali ke kawanan. Getaran mendadak atau bayangan besar membuatnya berpencar, sebelum berkumpul lagi di bawah naungan tepian. Ia menghindari air yang terlalu gaduh dan tidak menyerang nelayan yang masuk ke sungai.

## Habitat

Sungai dan danau air tawar, dengan jaringan sungai tenang Arthiska sebagai salah satu habitat utamanya. Ikan ini juga dapat dijumpai pada bagian sungai yang sesuai di sekitar Lingkar Samodra, meskipun kanal bongkar muat yang sibuk bukan tempat pemijahan utamanya.

## Kisah — Cahaya yang Tidak Dijual

Seorang pedagang di Lingkar Samodra melihat kilatan di bawah dermaga dan menyangka muatan perak telah jatuh dari kapal. Ia menawarkan upah kepada anak pengangkut untuk mengambilnya. Anak itu menurunkan sebuah wadah, lalu mengangkat air bersama seekor ikan kecil.

Pedagang tersebut akhirnya membayar juga. Bukan untuk membeli perak, katanya, melainkan untuk membeli pelajaran sebelum ia menyuruh seluruh pekerja menguras kanal.

> Acuan habitat: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>) dan [Lingkar Samodra](<../../03_Region/01_Mandala Kingdom/Cities & Town/Mandala Capital.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `7.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Balanced` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic` | Penanda taktis unit |

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
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Fin Slash** | `Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Silver Splash** | `Water` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **School Rush** | `Water` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

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
| **Drop 1** | `Clear Crystal` (`20%`) | Material alam / crafting |
