---
title: Burung Puyuh Hutan
tags:
  - Bestiary
---

# Burung Puyuh Hutan

## Deskripsi

Unggas kecil yang mengandalkan diam dan penyamaran sebelum menggunakan sayapnya. Burung Puyuh Hutan sering baru terlihat ketika seseorang hampir menginjak tempat persembunyiannya. Kepakannya singkat tetapi mengejutkan, cukup untuk mengalihkan perhatian sementara ia kembali menghilang ke rumpun lain.

## Bentuk

Tubuhnya membulat, berleher pendek, dengan kepala kecil dan kaki yang lebih cocok berlari di bawah semak daripada bertengger tinggi. Sayap pendeknya menempel rapat pada badan. Pola bulu cokelat, krem, dan hitam menyerupai pecahan serasah; bagian punggung lebih gelap daripada perut. Saat merunduk, bentuk kepalanya hampir hilang di antara bahu sehingga tampak seperti gumpalan daun.

## Tingkah Laku

Pemalu dan tidak buas. Ia mencari biji serta serangga kecil di bawah tutupan tumbuhan, lalu membeku ketika mendengar ancaman. Jika persembunyiannya terbuka, ia berlari atau terbang rendah dalam ledakan singkat. Induk dapat menarik perhatian menjauh dari anaknya, tetapi tidak melawan manusia dalam pengejaran panjang.

## Habitat

Semak hutan serta batas kebun dan hutan ringan di kawasan Arthiska. Biji, serasah, dan penutup tanah mendukung kehidupannya dekat permukaan tanah; ia tidak bergantung pada kanopi tinggi.

## Kisah — Kepakan di Pematang

Seorang calon penjaga yang pulang dari latihan merasa sedang dibuntuti di pinggiran kebun Arthiska. Setiap ia berhenti, semak di sampingnya ikut diam. Ia menggenggam tongkat dan berbalik mendadak.

Seekor puyuh meledak keluar dari dekat sandalnya. Sang calon penjaga jatuh terduduk, sementara seekor induk lain membawa anak-anaknya menyusup menjauhi jalan. Petani yang melihat kejadian itu tidak menertawakannya. Ia hanya meminta agar lain kali orang berjalan sedikit lebih jauh dari semak tempat unggas bersarang.

> Acuan: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `6.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Sniper` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Ranged` | Formula serangan dasar |
| **Elemen Utama** | `Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **4** | **1** | **10** | **10** | **11** | **6** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `108` *(VIT×15 + STR×5)* | **DEF** | `11` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `9` *(Base 1 + INT×8)* | **MDF** | `10` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `58` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `13` *(Base + INT×2)* |
| **ATK** | `22` *(Formula Ranged)* | **Action Speed** | `16` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `6.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `103.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.18%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.56%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Feather Dart** | `05 Air` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Gust Peck** | `05 Air` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Scatter Flight** | `10 Holy` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `-` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Scatter Flight, Lowest HP%
Turn 2+: Gust Peck, Random
Always: Feather Dart, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Wind: 75%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`20%`) | Material alam / crafting |
