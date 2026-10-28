---
title: Ubur-Ubur Pijar Kematian
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Ubur-Ubur Pijar Kematian

## Deskripsi

Kawanan ubur-ubur raksasa yang memancarkan cahaya biru dan sengatan pelumpuh. Pada malam hari pendar mereka dapat tampak seperti jalur aman, padahal seseorang yang jatuh di antara tentakel berisiko tenggelam tanpa mampu bergerak.

## Bentuk

Kubah tubuhnya bening kebiruan dengan inti bercahaya yang berdenyut. Tentakel panjang menggantung dalam beberapa lapis; benang halus di antaranya sulit dilihat sebelum menyentuh kulit. Arus listrik melompat sebagai kilatan pendek ketika kawanan berdekatan. Ukuran individu berbeda-beda, menciptakan hamparan cahaya pada permukaan.

## Tingkah Laku

Mengikuti arus dalam kawanan dan tidak perlu mengejar korban. Kontak tentakel memicu sengatan, sedangkan gangguan keras dapat membuat beberapa individu melepaskan energi sekaligus. Dalam Prologue mereka menghantam lambung kapal hingga tampak meledak. Perilaku ini tidak memastikan bahwa ledakan selalu membunuh tubuh ubur-ubur atau merupakan tindakan sadar.

## Habitat

Permukaan Zona Badai Abadi pada malam hari, terutama ketika arus membawa makanan dari kedalaman. Pendar mudah terlihat dalam air gelap, tetapi tentakel dapat menjangkau jauh di luar inti cahaya.

## Kisah - Laut yang Menyala

Kawanan Ubur-Ubur Pijar menghantam lambung kapal Rama di tengah tiga hari serangan. Cahaya biru menyala pada ombak, memaksa Hector dan Cassian melindungi kapal tanpa jatuh ke air. Di antara badai, keindahan pendar itu hanya memberi peringatan tentang tempat yang tidak boleh disentuh.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [05 Rahasia Sang Echomancer](../../08_Story/02_Prologue/05_Rahasia_Sang_Echomancer.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `80.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Water/Lightning` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Caster, Poisonous` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **55** | **103** | **22** | **53** | **57** | **60** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3420` *(Base 2245 + VIT×15 + STR×5)* | **DEF** | `117` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `232` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `430` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `206` *(Base + INT×2)* |
| **ATK** | `121` *(Formula Magic)* | **Action Speed** | `86` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `12.7%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `14.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `170.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `130.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.80%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `3.09%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.48%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Volt Tentacle** | `Lightning` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45 (Paralyze 30%)` |
| **Paralyzing Glow** | `Water` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35` |
| **Deathlight Discharge** | `Light` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Lightning: 125%, Water: 50%
* **Resistensi Status:** Poison: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Mana Crystal` (`20%`) | Material alam / crafting |
| **Drop 2** | `Wisp Core` (`15%`) | Komponen sekunder |
