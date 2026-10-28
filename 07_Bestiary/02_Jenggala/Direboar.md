---
title: Direboar
tags:
  - Bestiary
---

# Direboar

## Deskripsi

Babi siluman raksasa yang juga disebut Celeng Ngepet. Lapisan hitam menyerupai baja membuat tubuhnya tampak seperti bongkah logam bergerak di antara pepohonan. Berbeda dari Babi Hutan yang menyerbu untuk membuka jalan keluar, Direboar dalam catatan serangan Jenggala dapat terus menerjang ke arah kerumunan.

## Bentuk

Bahu menjulang di atas kepala rendah, dengan moncong lebar dan taring besar melengkung di kedua sisi rahang. Punggungnya berlapis kulit hitam keras yang memantulkan cahaya dalam bidang-bidang kusam. Bulu kasar menonjol di sela lipatan leher dan sepanjang tengkuk. Kaki pendek serta tebal menahan tubuh yang sangat berat. Istilah kulit baja dipertahankan dari sumber, tanpa menetapkan bahwa tubuhnya merupakan bijih yang dapat ditambang.

## Tingkah Laku

Sangat agresif ketika menerobos atau mengejar. Ia menggesekkan taring, menghentakkan kaki, dan merendahkan kepala sebelum serbuan terbuka, tetapi tutupan hutan dapat menyembunyikan tanda tersebut. Setelah terhalang, ia berusaha mencari celah untuk menerjang lagi. Sebutan Celeng Ngepet tidak otomatis membuktikan bahwa setiap individu merupakan manusia yang berubah demi mencuri kekayaan; mekanisme asal itu belum ada dalam canon Nusvanir.

## Habitat

Hutan Bayangan adalah habitat lama yang belum terpetakan. Kawasan berhutan Raksamala menjadi tempat kemunculannya, sedangkan kemunculannya melalui portal di pesisir Aqualis sudah tercatat dalam Prologue. Lokasi penyerbuan tidak harus menjadi habitat alaminya.

## Kisah — Di Belakang Gerobak

Dalam kisah tambahan tentang dampak serbuan di pesisir Mandala, seorang pengangkut memilih berlindung di balik gerobak kosong. Derap berat mendekat dari antara rumah. Ketika moncong hitam muncul, ia meninggalkan perlindungannya dan berlari ke celah dinding.

Gerobak itu terangkat oleh taring sebelum jatuh dalam serpihan. Ia selamat bukan karena membawa senjata lebih kuat, melainkan karena berhenti menganggap kayu tipis sebagai tembok. Kisah ini tidak menambahkan peran baru pada tokoh utama Prologue.

> Acuan: [Raksamala](../../03_Region/10_Raksamala/Raksamala.md); [03 Teror di Pesisir Timur](../../08_Story/02_Prologue/03_Teror_di_Pesisir_Timur.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `18.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Large, Armored, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **25** | **4** | **12** | **21** | **19** | **18** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `782` *(Base 387 + VIT×15 + STR×5)* | **DEF** | `40` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `32` *(INT×8)* | **MDF** | `32` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `160` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `33` *(Base + INT×2)* |
| **ATK** | `56` *(Formula Melee)* | **Action Speed** | `28` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `6.8%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `7.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `5.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `159.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `109.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.54%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.12%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.12%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Corrupted Charge** | `Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Black Tusk** | `Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Frenzied Gore** | `Dark` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%
* **Resistensi Status:** Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`35%`) | Material alam / crafting |
| **Drop 2** | `Jenggala Claw` (`30%`) | Komponen sekunder |
