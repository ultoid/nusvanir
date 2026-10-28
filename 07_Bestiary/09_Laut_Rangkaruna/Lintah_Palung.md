---
title: Lintah Palung
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Lintah Palung

## Deskripsi

Lintah laut seukuran perahu kecil yang menyerang berkelompok dan menempel pada lambung kapal. Mereka mengisap mineral dari kayu maupun besi sampai struktur cepat lapuk. Serangan pertama di dalam badai Rangkaruna memaksa rombongan Rama mempertahankan kapal sebelum ancaman lain muncul.

## Bentuk

Tubuhnya panjang, lunak, dan bersegmen samar, dengan mulut pengisap bundar penuh gigi kecil. Kulit kelabu gelap mengembang setelah menyerap mineral. Beberapa sirip tipis membantu mengarahkan tubuh menuju lambung, sementara lendir membuatnya sulit dilepaskan. Saat menempel, hanya ekor yang tampak bergerak di antara ombak.

## Tingkah Laku

Parasit berkelompok yang mengikuti getaran serta mineral pada kapal. Ia tidak perlu menyerang awak secara langsung untuk menenggelamkan mereka. Setelah melekat, kawanan menyebar pada bagian bawah lambung dan mempertahankan gigitan. Benturan, cahaya, atau panas dapat mengganggu, tetapi efektivitas mekanis belum ditentukan.

## Habitat

Terutama batas Perairan Dangkal dan Zona Badai Abadi, tempat mereka mulai mengikuti jalur kapal. Persebarannya luas hingga perairan sekitar Palung Kematian, tetapi kepadatannya tidak sama di setiap kawasan.

## Kisah - Hisapan Pertama dalam Badai

Begitu kapal Rama menembus badai, lambung bergetar oleh hisapan basah. Lintah Palung telah menempel dari bawah. Hector dan Cassian harus mengusir kawanan sambil mempertahankan kapal dari ombak. Ancaman itu tampak kecil dibanding monster yang datang kemudian, tetapi satu lambung yang lapuk akan mengakhiri perjalanan sebelum mereka melihat palung.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [05 Rahasia Sang Echomancer](../../08_Story/02_Prologue/05_Rahasia_Sang_Echomancer.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `75.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T6 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water/Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Lifesteal` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **48** | **20** | **20** | **55** | **46** | **49** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `2470` *(Base 1495 + VIT×15 + STR×5)* | **DEF** | `98` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `159` *(INT×8)* | **MDF** | `106` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `361` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `139` *(Base + INT×2)* |
| **ATK** | `106` *(Formula Melee)* | **Action Speed** | `69` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `14.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `12.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `13.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `168.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `124.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.47%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.60%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.82%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Leech** | `11 Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45 (Curse 30%))` |
| **Blood Drain** | `03 Water` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Trench Clamp** | `03 Water` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25 (Root 50%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Trench Clamp, Lowest HP%
State === Taunt: Blood Drain, Random
Turn % 2 == 0: Blood Drain, Random
Always: Abyssal Leech, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%, Lightning: 125%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `720` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `540` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `200` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`30%`) | Material alam / crafting |
| **Drop 2** | `Kala Crystal` (`10%`) | Komponen sekunder |
