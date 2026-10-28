---
title: Babi Hutan
tags:
  - Bestiary
---

# Babi Hutan

## Deskripsi

Penggali tanah yang mengikuti bau umbi sampai ke tepian ladang. Babi Hutan bukan pemburu manusia, tetapi serbuannya dapat membubarkan rombongan yang menghalangi jalan pulang kawanannya. Bekas tanah teraduk dan akar tercabut sering menjadi petunjuk keberadaannya sebelum tubuhnya terlihat.

## Bentuk

Tubuhnya rendah dan berat, dengan bahu menonjol serta leher pendek yang tampak menyatu dengan kepala. Moncongnya lebar dan berlumpur, diapit taring yang melengkung keluar dari rahang bawah. Bulu kasar berwarna cokelat gelap hingga kelabu membentuk garis lebih tebal sepanjang tengkuk. Kakinya pendek tetapi kokoh, sehingga siluetnya menyerupai bongkah akar yang tiba-tiba bergerak di bawah semak.

## Tingkah Laku

Mencari akar, umbi, dan sisa tanaman budidaya dengan menggali tanah. Ia cenderung menjauh ketika mengetahui ada orang, tetapi dapat mengamuk jika terluka, dikepung, atau dipisahkan dari anaknya. Dengusan keras, tengkuk menegang, dan kaki depan menggaruk tanah menjadi tanda agar orang mundur. Serbuannya bertujuan membuka jalan keluar, bukan memburu lawan tanpa henti.

## Habitat

Semak dan tanah lembap pada hutan perbatasan Hermindar, di luar jalur permukiman. Akar, umbi, dan tutupan tumbuhan yang rapat menyediakan makanan sekaligus perlindungan. Kawasan ini memperjelas habitat yang dahulu hanya disebut Pinggiran Jenggala.

## Kisah — Jejak di Samping Jalan Baja

Rombongan pembawa perkakas dari Hermindar menemukan jalan mereka dibongkar sesuatu pada malam hari. Seorang penjaga menuduh gerombolan Jenggala sedang menyiapkan penyergapan. Pandai besi yang menyertainya justru berjongkok, memungut umbi yang tergigit, lalu menunjuk jejak kecil di belakang jejak yang besar.

Mereka menunggu. Seekor induk Babi Hutan keluar dari semak bersama anak-anaknya dan menyeberang tanpa mendekati rombongan. Hari itu, perjalanan terlambat bukan karena perang, melainkan karena sebuah keluarga lain juga hendak pulang.

> Acuan: [Hermindar](<../../03_Region/01_Mandala Kingdom/Cities & Town/Hermindar.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `2.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | **1** | **2** | **10** | **10** | **5** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `126` *(Base 1 + VIT×15 + STR×5)* | **DEF** | `13` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `8` *(INT×8)* | **MDF** | `10` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `65` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `11` *(Base + INT×2)* |
| **ATK** | `21` *(Formula Melee)* | **Action Speed** | `15` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `102.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.15%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.50%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Boar Charge** | `01 Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Tusk Gore** | `01 Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Wild Rush** | `01 Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Wild Rush, Lowest HP%
Turn 2+: Tusk Gore, Random
Always: Boar Charge, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 150%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`30%`) | Material alam / crafting |
| **Drop 2** | `Beast Fang` (`20%`) | Komponen sekunder |
