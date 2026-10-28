---
title: Strigoi
tags:
  - Bestiary
---

# Strigoi

## Deskripsi

Undead terbang yang dikenal sebagai Kuyang dan mengisap daya hidup korbannya. Strigoi lebih mudah mencapai tepian rumah atau tempat singgah daripada pemangsa yang harus berjalan melalui pintu. Suara di atas atap dapat membuat orang menengadah tepat ketika ancaman bergerak mendekati sisi lain bangunan.

## Bentuk

Sebagaimana sebutannya, Kuyang, Strigoi berwujud kepala terbang dengan rambut panjang dan sisa tubuh yang menggantung di bawahnya. Wajahnya pucat, matanya cekung, dan gerak rambut dapat menyamarkan arah terbang dalam cahaya redup. Tidak ada sayap kelelawar yang diperlukan untuk menjelaskan wujudnya. Cara tubuhnya terpisah, asal manusia, dan ritual pembentukannya belum diketahui.

## Tingkah Laku

Memangsa dan mengintai korban yang terpisah dari rombongan. Ia dapat berputar di luar jangkauan, menunggu celah, lalu mendekat untuk mengisap daya hidup. Jika dihalau, ia mencari sudut lain alih-alih selalu bertahan dalam serangan frontal. Tidak ditambahkan aturan bahwa hanya kelompok korban tertentu yang dapat diserang atau bahwa ia harus pulang ke tubuh asal sebelum fajar.

## Habitat

Pinggiran desa adalah tempat kemunculan yang tercatat tanpa desa bernama. Permukiman luar di kawasan utara Mandala menjadi tempat kemunculannya yang selaras dengan ancaman gaib sekitar Valkindra. Ini bukan klaim bahwa seluruh desa Mandala mengalami serangan rutin atau bahwa Strigoi otomatis anggota Dhemit.

## Kisah — Bayangan di Cucuran Atap

Seorang penjaga penginapan luar kota mendengar sesuatu menyeret di atas atap dan menyuruh tamunya tetap di dalam. Ketika lentera diarahkan ke cucuran, rambut panjang jatuh melewati balok, disusul wajah yang tidak mempunyai pijakan.

Ia menutup celah jendela dan membangunkan seluruh penghuni agar tidak ada yang pergi memeriksa sendirian. Bayangan itu mengitari rumah sampai langkah patroli terdengar dari jalan. Tidak seorang pun keluar untuk memastikan ke mana ia terbang.

> Acuan: [Valkindra](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Valkindra.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `27.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Undead` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Undead, Lifesteal` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **15** | **28** | **8** | **21** | **21** | **14** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `612` *(Base 327 + VIT×15 + STR×5)* | **DEF** | `29` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `52` *(INT×8)* | **MDF** | `35` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `120` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `57` *(Base + INT×2)* |
| **ATK** | `34` *(Formula Magic)* | **Action Speed** | `32` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `7.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `6.7%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `4.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `107.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.42%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.84%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.12%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Blood Claw** | `Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45` |
| **Life Siphon** | `Dark` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.15 - b.mdf * 0.45` |
| **Crimson Flight** | `Light` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%
* **Resistensi Status:** Bleed: 0%, Poison: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Wight Shroud` (`30%`) | Material alam / crafting |
| **Drop 2** | `Spirit Dust` (`25%`) | Komponen sekunder |
