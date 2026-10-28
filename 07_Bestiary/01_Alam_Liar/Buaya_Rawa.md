---
title: Buaya Rawa
tags:
  - Bestiary
---

# Buaya Rawa

## Deskripsi

Pemangsa penyergap yang dapat menyerupai batang kayu hanyut ketika tidak bergerak. Buaya Rawa menunggu mangsa mendekati tepian sebelum menerjang dari jarak dekat. Permukaan air yang tenang tidak menandakan tempat itu aman, terutama jika jejak hewan berkumpul pada jalur turun menuju air.

## Bentuk

Tubuhnya memanjang dan rendah, dengan rahang lebar serta ekor berotot yang pipih ke samping. Lempeng keras di punggung membentuk deretan tonjolan seperti batu yang terendam. Warna kelabu zaitun dan noda lumpur membuat batas antara kulit dan air keruh sulit dibedakan. Mata serta lubang hidung terletak tinggi pada kepala, memungkinkan sebagian besar tubuhnya tersembunyi. Ungkapan pertahanan baja menggambarkan ketangguhan tubuh, bukan kulit yang benar-benar terbuat dari logam.

## Tingkah Laku

Buas sebagai pemangsa, tetapi tidak terus-menerus mengejar segala sesuatu. Ia menghemat gerakan dan memanfaatkan jarak dekat. Individu yang menjaga sarang atau kehilangan jalan kembali ke air dapat menjadi sangat agresif. Mendesis dan membuka rahang merupakan peringatan; mendekatinya karena mengira ia lamban di darat adalah kesalahan berbahaya.

## Habitat

Rawa dan genangan liar di luar kawasan sungai pertanian Arthiska, terutama tepian berlumpur tempat hewan mendekati air. Catatan lama juga menyebut Rawa Beracun, tetapi letak wilayah bernama itu masih belum terpetakan. Tidak semua rawa yang dihuni buaya merupakan perairan beracun.

## Kisah — Tambatan yang Bergerak

Di pinggiran Arthiska, seorang pengangkut hasil panen hendak menambatkan perahu pada batang gelap di tepi air. Rekannya menarik tali sebelum simpul itu dilemparkan. Batang tersebut memiliki mata.

Ketika perahu bergeser menjauh, benda itu tenggelam tanpa suara. Mereka memilih tepian lain, meskipun harus memanggul karung lebih jauh. Setibanya di pasar, yang mereka ceritakan bukan monster raksasa, melainkan betapa dekatnya tangan seseorang dengan sesuatu yang dikiranya kayu.

> Acuan bentang air: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `5.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **14** | **2** | **6** | **16** | **12** | **15** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `500` *(Base 205 + VIT×15 + STR×5)* | **DEF** | `29` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `18` *(Base 2 + INT×8)* | **MDF** | `23` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `123` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `21` *(Base + INT×2)* |
| **ATK** | `31` *(Formula Melee)* | **Action Speed** | `18` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `155.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `107.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.45%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.06%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.78%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Jaw Snap** | `03 Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Death Roll** | `11 Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Mud Ambush** | `04 Earth` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Mud Ambush, Lowest HP%
State === Taunt: Death Roll, Random
Turn % 2 == 0: Death Roll, Random
Always: Jaw Snap, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `80` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `60` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `30` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Fang` (`35%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`25%`) | Komponen sekunder |
