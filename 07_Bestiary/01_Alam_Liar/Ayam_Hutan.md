---
title: Ayam Hutan
tags:
  - Bestiary
---

# Ayam Hutan

## Deskripsi

Unggas penjaga sarang yang lebih sering terdengar daripada terlihat. Ayam Hutan mengais serasah untuk mencari biji dan serangga, lalu menyelinap di bawah semak ketika mendengar langkah asing. Seekor induk yang tampak mudah ditangkap dapat mendadak berbalik menyerang jika pemburu berdiri di antara dirinya dan anak-anaknya.

## Bentuk

Tubuhnya padat dengan dada membulat, leher lentur, dan kaki bersisik yang kokoh untuk mencakar tanah. Bulu punggung berwarna cokelat tembaga dengan guratan gelap menyerupai daun kering; bagian leher jantan memantulkan kilau hijau kusam ketika terkena matahari. Ekornya melengkung, sementara sayapnya pendek dan rapat di sisi tubuh. Penampilannya menyatu dengan lantai hutan, bukan menyerupai unggas bercahaya atau makhluk roh.

## Tingkah Laku

Umumnya waspada tetapi tidak buas. Ia memilih berlari menuju semak daripada menghadapi manusia. Ketika sarangnya didekati, induk merendahkan tubuh, merentangkan sayap, dan mengeluarkan panggilan pendek sebelum mematuk. Gangguan yang berhenti akan membuatnya mundur kembali; ia tidak mengejar penyusup jauh dari sarang.

## Habitat

Hutan ringan di Mandala, terutama tepian hutan di sekitar lahan pertanian Arthiska. Ruang terbuka menyediakan tempat mencari makan, sementara semak di batas kebun menjadi perlindungan dan tempat bersarang.

## Kisah — Penjaga di Bawah Keranjang

Seorang pengantar beras dari Arthiska mendengar kepakan gaduh dari keranjang kosong yang ia tinggalkan dekat pepohonan. Ia mengira seekor Jenggala kecil telah masuk dan segera meraih galah. Namun, yang muncul hanyalah induk Ayam Hutan, berdiri menghadang dengan sayap terbuka.

Di bawah keranjang itu bersembunyi anak-anaknya. Sang pengantar menurunkan galah dan memindahkan keranjangnya perlahan. Ketika ia melanjutkan perjalanan, induk itu sudah kembali mengais tanah, seolah baru saja memenangkan perang yang tidak perlu diketahui siapa pun.

> Acuan wilayah: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `1.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Balanced` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Neutral` | Menerima pengganda kerusakan 2.0x |

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

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Peck** | `01 Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Wing Flap** | `01 Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Fleeing Scratch** | `01 Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Fleeing Scratch, Lowest HP%
Turn 2+: Wing Flap, Random
Always: Peck, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Neutral 100%, Neutral 200% (Weak)
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`35%`) | Material alam / crafting |
