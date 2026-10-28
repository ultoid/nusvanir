---
title: Kepiting Batu Karang
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Kepiting Batu Karang

## Deskripsi

Krustasea raksasa perairan dangkal yang menyamar sebagai formasi karang. Ia menunggu kapal menabrak cangkangnya, lalu bangun untuk mencapit puing dan kru yang jatuh. Dagingnya bernilai bagi pelabuhan Aqualis, tetapi perburuan langsung di habitatnya hanya dilakukan nelayan berpengalaman seperti Rama.

## Bentuk

Cangkangnya lebar, bertingkat, dan ditumbuhi karang tajam serta lumut laut. Dua capit besar terlipat menyerupai bongkah terpisah. Mata kecil berada dalam cekungan yang tertutup saat ia diam. Kaki beruas tersembunyi di pasir, membuat seluruh tubuh tampak sebagai batu sampai dasar laut terangkat. Warna serta organisme pada cangkang berubah mengikuti tempat ia menetap.

## Tingkah Laku

Penyergap yang cenderung diam sampai lambung, jangkar, atau mangsa menyentuh wilayahnya. Setelah bangun ia mencapit benda terdekat dan mempertahankan posisi. Ia tidak memburu kapal jauh ke laut dalam. Nelayan dapat mengenali perbedaan arus dan susunan karang, tetapi pendekatan tetap berbahaya.

## Habitat

Perairan Dangkal Rangkaruna di bagian utara dan barat laut, khususnya gugusan karang pada jalur di luar Aqualis. Pasir dan karang hidup menyamarkan tubuhnya; lokasi itu juga cukup dekat untuk dijangkau perahu pemburu.

## Kisah - Buruan Pak Tua Rama

Penduduk Aqualis mengenal Rama sebagai satu-satunya nelayan yang berani mencari Kepiting Batu Karang langsung di habitatnya. Ia tidak menganggap setiap batu sebagai mangsa. Rama membaca buih, menunggu mata kecil terbuka di sela karang, lalu memilih jalan mendekat yang masih menyisakan arus untuk melarikan diri. Keberaniannya lahir dari pengetahuan laut, bukan keyakinan bahwa capit raksasa itu dapat diremehkan.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [03 Teror di Pesisir Timur](../../08_Story/02_Prologue/03_Teror_di_Pesisir_Timur.md); [Aqualis](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Aqualis.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `73.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T6 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water/Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **57** | **13** | **24** | **44** | **37** | **67** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3250` *(Base 1960 + VIT×15 + STR×5)* | **DEF** | `129` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `106` *(Base 2 + INT×8)* | **MDF** | `106` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `469` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `91` *(Base + INT×2)* |
| **ATK** | `126` *(Formula Melee)* | **Action Speed** | `55` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `11.6%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `12.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `13.3%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `171.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `133.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.01%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.39%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.82%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Coral Claw** | `03 Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Stone Shell** | `04 Earth` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Reef Crusher** | `03 Water` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25 (Stun 25%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Reef Crusher, Lowest HP%
State === Taunt: Stone Shell, Random
Turn % 2 == 0: Stone Shell, Random
Always: Coral Claw, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Lightning: 150%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `720` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `540` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `200` | Mata uang resmi penjelajahan |
| **Drop 1** | `Obsidian` (`25%`) | Material alam / crafting |
| **Drop 2** | `Spirit Stone` (`15%`) | Komponen sekunder |
