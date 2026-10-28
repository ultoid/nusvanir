---
title: Krakentis Sang Pemutar Arus
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Krakentis Sang Pemutar Arus

## Deskripsi

Gurita purba raksasa yang gerakan tentakelnya dapat membentuk pusaran besar dan menyeret armada. Dalam perjalanan menuju Thalantira, Krakentis menghadang kapal Rama sampai sihir suara sang Echomancer melumpuhkan pusat sarafnya cukup lama bagi kapal untuk lolos.

## Bentuk

Tubuh utamanya tersembunyi di kedalaman. Tentakel berduri naik mengelilingi kapal, masing-masing cukup tebal untuk menutup bagian lambung. Pengisap besar memiliki tepian keras untuk mempertahankan cengkeraman dalam badai. Kulit gelap berubah pucat pada bagian yang menegang. Mata dan pusat saraf berada dekat pangkal tubuh, jauh lebih sulit dijangkau daripada ujung tentakel.

## Tingkah Laku

Buas ketika kapal memasuki arus buruannya. Ia memutar tentakel di dasar laut sebelum menyerang, memakai pusaran untuk mengurangi kendali kapal. Cengkeraman terhenti sementara ketika Rama menghantam pusat sarafnya dengan gelombang sonik. Kejadian itu menunjukkan respons biologis tertentu, bukan kelemahan universal dengan durasi gameplay baru.

## Habitat

Palung Kematian dan perairan dalam di sekitarnya pada jalur menuju Raksamala. Ruang luas di dasar laut memungkinkan tentakel membangun putaran arus sebelum tubuh utama terlihat. Krakentis ini tidak otomatis sama dengan pemilik Kraken Tentacle di Thalantira.

## Kisah - Teriakan Sang Echomancer

Tentakel Krakentis menutup jalur kapal Oak hitam. Saat Hector bersiap menyerang, Rama meninggalkan kemudi dan melepaskan gelombang suara padat ke pusat saraf monster. Otot Krakentis membeku sesaat. Rama kembali merebut kemudi dan membawa kapal melewati celah tentakel sebelum makhluk itu pulih. Mereka menang bukan dengan membunuh sang pemutar arus, melainkan dengan menciptakan satu kesempatan untuk lolos.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [05 Rahasia Sang Echomancer](../../08_Story/02_Prologue/05_Rahasia_Sang_Echomancer.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `74.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T9 (Lord)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Large, Ancient, Caster` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **141** | **63** | **56** | **106** | **92** | **149** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `39900` *(Base 36960 + VIT×15 + STR×5)* | **DEF** | `294` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `502` *(INT×8)* | **MDF** | `315` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `1047` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `410` *(Base + INT×2)* |
| **ATK** | `310` *(Formula Magic)* | **Action Speed** | `138` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `96.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `25.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `24.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `30.8%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `203.5%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `174.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `4.47%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `1.89%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `9.66%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Tentacle** | `Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45 (Curse 30%)` |
| **Maelstrom Prison** | `Water` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35 (Root 50%)` |
| **World-Turning Current** | `Water` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Freeze: 25%, Instant Death: 0%, Paralyze: 25%, Root: 75%, Stun: 25%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `18750` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `14062` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `4800` | Mata uang resmi penjelajahan |
| **Drop 1** | `Primordial Crystal` (`30%`) | Material alam / crafting |
| **Drop 2** | `Spirit Thread` (`20%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Ring of the Abyssal Tide` (`5%`) | Rampasan unik / piala bos |
