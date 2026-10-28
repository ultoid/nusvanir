---
title: Pari Kematian Besi
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Pari Kematian Besi

## Deskripsi

Pari purba selebar alun-alun dengan pelat alami sekeras baja dan ekor seperti tombak beracun. Dalam pelayaran Rama, seekor Pari melompat dari air dan mencoba menembus kubah pelindung Cassian.

## Bentuk

Tubuhnya berupa cakram lebar berlapis pelat gelap yang saling menutup. Sirip dada bergerak seperti sayap berat. Mata berada pada sisi atas, sedangkan mulut tersembunyi di bawah. Ekor panjang berakhir pada duri logam alami dengan alur racun. Bekas goresan pada pelat menunjukkan benturan dengan karang dan kapal.

## Tingkah Laku

Buas ketika sesuatu melintas di atas wilayah dangkalnya. Ia mengumpulkan kecepatan di bawah air, melompat, lalu menggunakan ekor untuk menusuk dek atau pertahanan. Setelah serangan gagal ia kembali menyelam dan mencari sudut lain. Kekerasan pelat bukan bukti kebal terhadap seluruh serangan.

## Habitat

Perairan Dangkal Rangkaruna di bagian utara dan barat laut, dengan dasar cukup luas untuk memperoleh kecepatan dan karang sebagai perlindungan. Individu dapat memasuki Zona Badai Abadi ketika mengikuti kapal.

## Kisah - Tombak dari Bawah Ombak

Selama tiga hari serangan Rangkaruna, Pari Kematian Besi melompat dari air dan mengayunkan ekor ke kubah Cassian. Tombak alaminya menghantam perlindungan tanpa mencapai geladak. Para pelaut tidak mengejarnya; mereka menjaga kubah dan terus bergerak, sebab satu serangan yang ditahan bukan jaminan makhluk itu telah pergi.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [05 Rahasia Sang Echomancer](../../08_Story/02_Prologue/05_Rahasia_Sang_Echomancer.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `77.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Sniper` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Ranged` | Formula serangan dasar |
| **Elemen Utama** | `Water/Iron` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **38** | **20** | **94** | **56** | **63** | **70** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3420` *(Base 2180 + VIT×15 + STR×5)* | **DEF** | `124` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `160` *(INT×8)* | **MDF** | `122` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `446` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `143` *(Base + INT×2)* |
| **ATK** | `207` *(Formula Ranged)* | **Action Speed** | `95` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `100.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `17.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `27.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `15.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `180.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `135.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.10%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.60%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.92%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Iron Barb** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Razor Current** | `Water` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35` |
| **Deathray Charge** | `Dark` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Iron: 75%, Lightning: 150%, Water: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Obsidian` (`25%`) | Material alam / crafting |
| **Drop 2** | `Silver` (`15%`) | Komponen sekunder |
