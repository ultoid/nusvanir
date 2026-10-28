---
title: Abyssal Treant
tags:
  - Bestiary
---

# Abyssal Treant

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Pohon berjalan yang membawa aura korupsi di hutan Thalantira. Diamnya menyerupai ketenangan batang tua, tetapi akar dapat terangkat dan bergerak mengejar. Pertemuannya dengan Rama memperlihatkan bahaya yang lebih ganjil daripada pemangsaan: ia menyerang orang yang hendak menyelamatkan Shinta sambil membiarkan perempuan itu tetap berada dalam kedamaian palsu pulau.

## Bentuk

Batangnya besar dan berpilin, dengan pangkal akar yang membuka seperti jemari mencengkeram tanah. Kulit kayu gelap terbelah oleh rongga panjang; di antaranya tampak lembap seolah bagian dalam pohon tak pernah mengering. Cabang rendah menjulur sebagai sulur penahan, sedangkan tajuk berat menyamarkan gerakan tubuh di antara pepohonan. Rupanya tetap menyerupai pohon, tanpa wajah manusia pada batangnya. Ketika berjalan, tanah terangkat bersama akar sebelum jatuh kembali dalam gumpalan.

## Tingkah Laku

Berbahaya, tetapi tidak selalu menyerang semua orang dengan cara sama. Treant yang dihadapi Rama menghalanginya mendekati Shinta dan menghantamnya hingga terlempar ke perahu. Sikap melindungi Shinta tidak membuatnya penjaga yang baik hati: tindakan itu mempertahankan pemisahan pasangan tersebut. Saat ilusi pulau tersingkap dalam Prologue, Treant juga hadir di antara monster darat. Pola serangan selektif pada Shinta merupakan kejadian tertentu, bukan jaminan bahwa orang yang bersikap tenang akan diabaikan.

## Habitat

Hutan pedalaman Thalantira, terutama jalur rapat di antara pantai dan pusat pulau. Akar besar dan cahaya yang terhalang tajuk cocok untuk menyembunyikan tubuhnya. Hutan yang tampak tenteram saat kedatangan Hector dan Cassian harus dibaca bersama pengungkapan ilusi; keindahan tersebut tidak cukup untuk memastikan suatu jalur bebas Treant.

## Kisah — Akar di Antara Dua Tangan

Rama telah menemukan Shinta, tetapi belum berhasil membawanya pulang. Istrinya masih menari di dalam ketenteraman yang tidak dapat ia bagikan. Ketika Rama mencoba menariknya pergi, sulur kayu bergerak di antara mereka.

Treant tidak menerkam Shinta. Ia justru menghadapkan tubuhnya kepada Rama, seolah tangan sang suami merupakan gangguan yang harus disingkirkan. Rama melawan sampai akar besar menghantam dan melemparkannya ke perahu yang rusak. Hutan kembali menutup jarak di antara mereka; istrinya masih berada di pulau ketika ia kehilangan kesempatan mendekat.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [06 Kutukan dan Pengorbanan](../../08_Story/02_Prologue/06_Kutukan_dan_Pengorbanan.md); [07 Tiga Kuil Penjaga](../../08_Story/02_Prologue/07_Tiga_Kuil_Penjaga.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `32.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Plant` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Ancient, Voidborn, Large, Regenerator` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **75** | **18** | **28** | **53** | **46** | **90** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4750` *(Base 3025 + VIT×15 + STR×5)* | **DEF** | `172` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `143` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `620` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `119` *(Base + INT×2)* |
| **ATK** | `164` *(Formula Melee)* | **Action Speed** | `69` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `90.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `13.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `13.9%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `178.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `145.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.70%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.54%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.64%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Voidroot Lash** | `Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Curse 30%)` |
| **Ancient Bark** | `Void` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Abyssal Overgrowth** | `Dark` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25 (Curse 30%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 150%, Void: 50%
* **Resistensi Status:** Curse: 50%, Instant Death: 0%, Root: 0%, Stun: 70%
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
