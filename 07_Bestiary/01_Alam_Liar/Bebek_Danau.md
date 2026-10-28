---
title: Bebek Danau
tags:
  - Bestiary
---

# Bebek Danau

## Deskripsi

Unggas air yang mencari makan sambil bergerak beriringan di tepian danau. Dari daratan, kawanannya tampak tenang; di bawah air, kaki mereka terus mengayuh melawan arus. Bebek Danau cepat menyadari perubahan gerakan di sekelilingnya, dan kepanikan seekor anggota dapat membuat seluruh kawanan meninggalkan tepian.

## Bentuk

Tubuhnya membulat dengan dada rendah, leher yang mudah menjulur ke air, serta paruh lebar untuk menyisir permukaan berlumpur. Bulunya memadukan cokelat tanah pada punggung dan warna lebih pucat di perut. Lapisan bulu luar tampak licin ketika basah, sementara kaki berselaput tersembunyi di bawah tubuh ketika berenang. Tidak ada ciri yang mengharuskannya dianggap sebagai elemental air.

## Tingkah Laku

Tidak buas dan lebih suka menjauh dari keributan. Kawanan berjalan beriringan ketika mencari makan, lalu merapat jika ada ancaman. Induk yang melindungi anak dapat mendesis, mengepak, atau mematuk tangan yang terlalu dekat. Jika tersedia jalan ke air, ia lebih memilih membawa anaknya berenang menjauh daripada terus melawan.

## Habitat

Danau Mandala serta perairan tenang di kawasan agraris Arthiska, terutama tepian sungai yang terlindung dan berdekatan dengan persawahan. Kawanan mencari makan di tepian dangkal dan kembali ke air ketika terganggu.

## Kisah — Iringan yang Salah

Seorang anak pembawa benih di Arthiska berhenti untuk mengikat sandal. Ketika berdiri lagi, ia mendapati beberapa Bebek Danau mengikuti butiran yang jatuh dari kantongnya. Semakin cepat ia berjalan, semakin panjang iringan kecil itu.

Di pematang berikutnya, seekor induk menghadangnya sambil mendesis. Anak itu baru menyadari bahwa ia telah membawa anak-anak bebek menjauh dari air. Ia menutup kantong, berbalik, dan mengantar rombongan itu pulang—dengan induk yang terus mengawasi tumitnya.

> Acuan: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `3.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Balanced` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic` | Penanda taktis unit |

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
| **Water Peck** | `03 Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Wing Splash** | `03 Water` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Panic Flutter** | `03 Water` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Panic Flutter, Lowest HP%
Turn 2+: Wing Splash, Random
Always: Water Peck, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Clear Crystal` (`15%`) | Material alam / crafting |
