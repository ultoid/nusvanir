---
title: Hiu Purba Tulang
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Hiu Purba Tulang

## Deskripsi

Kerangka hiu raksasa yang digerakkan mana kegelapan serta dendam para pelaut tenggelam. Ia melintas di antara bangkai kapal tanpa tubuh hidup, tetapi rahang tulangnya masih mampu merobek lambung baja. Keberadaannya membuat kuburan kapal Rangkaruna menjadi tempat maut bahkan bagi penyelam yang mengira pemangsa di sana telah lama mati.

## Bentuk

Tengkoraknya lebar dengan deretan taring tulang tidak rata. Ruas tulang belakang memanjang menuju ekor yang bergerak seolah masih memiliki otot. Sirip hanya tersisa sebagai rangka keras, diselimuti kabut hitam tipis yang menjaga susunannya tetap utuh. Cahaya redup terlihat dalam rongga mata dan sela rusuk. Pecahan rantai, jaring, atau kayu kapal kerap tersangkut pada kerangkanya.

## Tingkah Laku

Agresif terhadap gerakan dan getaran di wilayah bangkai kapal. Ia mengitari sasaran, menembus celah reruntuhan, lalu menyerang dari sisi yang tertutup papan. Kerangka yang terpisah dapat kembali ditarik oleh kabut pengikatnya, tetapi batas pemulihan itu belum diketahui. Ia bukan Dhemit yang telah dipastikan; sumber hanya menyebut mana gelap dan dendam pelaut sebagai penggerak.

## Habitat

Kuburan Kapal di dalam Zona Badai Abadi, terutama cekungan tempat arus mengumpulkan puing, jangkar, dan tulang pelaut. Struktur kapal tenggelam memberi jalur berlindung sekaligus perangkap bagi mangsa.

## Kisah - Rahang di Antara Tiang Patah

Seekor ikan besar masuk ke lambung kapal tenggelam untuk menghindari badai. Tulang rusuk putih bergerak di balik tiang yang patah. Hiu Purba menembus bukaan tanpa menggeser satu papan pun, kabut gelap menarik rangkanya melewati reruntuhan. Ikan itu lolos melalui lubang kecil; sang hiu kembali mengitari bangkai, menunggu getaran berikutnya.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `71.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T6 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **66** | **15** | **26** | **50** | **58** | **37** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `2340` *(Base 1455 + VIT×15 + STR×5)* | **DEF** | `88` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `119` *(INT×8)* | **MDF** | `87` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `337` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `103` *(Base + INT×2)* |
| **ATK** | `145` *(Formula Melee)* | **Action Speed** | `87` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `90.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `13.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `11.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `175.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `118.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.11%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.45%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.06%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Bone Fang** | `03 Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Ancient Rush** | `03 Water` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Bloodwater Frenzy** | `03 Water` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `-` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Bloodwater Frenzy, Lowest HP%
State === Taunt: Ancient Rush, Random
Turn % 2 == 0: Ancient Rush, Random
Always: Bone Fang, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `720` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `540` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `200` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`35%`) | Material alam / crafting |
| **Drop 2** | `Beast Fang` (`25%`) | Komponen sekunder |
