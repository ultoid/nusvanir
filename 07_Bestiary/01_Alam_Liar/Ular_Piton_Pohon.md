---
title: Ular Piton Pohon
tags:
  - Bestiary
---

# Ular Piton Pohon

## Deskripsi

Penyergap pepohonan yang menyamarkan tubuhnya sebagai bagian dari cabang. Ular Piton Pohon menunggu mangsa mendekati jangkauan sebelum menggigit dan melilit. Catatan fauna Nusvanir juga menyebut kemampuan meracuni; sifat ini membedakannya dari anggapan umum tentang piton biasa, sementara asal kemampuan tersebut belum dijelaskan.

## Bentuk

Tubuhnya panjang dan berotot, dengan bagian perut cukup lebar untuk menahan berat pada cabang. Sisiknya memadukan hijau lumut, cokelat kulit kayu, dan bercak gelap yang memecah garis tubuh. Kepala sedikit lebih lebar daripada leher, rahang tampak rapat ketika diam, dan lidah bercabang keluar sesekali untuk mengenali sekeliling. Ekor meruncing membantu menambatkan tubuh pada ranting. Tubuhnya tidak memiliki tanduk, sayap, atau tanda korupsi.

## Tingkah Laku

Buas sebagai penyergap mangsa, tetapi tidak perlu digambarkan mengejar setiap orang yang lewat. Ia mengandalkan diam, jarak dekat, dan lilitan. Jika cabang tempatnya bertumpu diguncang atau tubuhnya disentuh, ia dapat menarik kepala, mengencangkan lilitan, lalu menggigit untuk mempertahankan diri. Kemampuan racunnya tetap dipertahankan sebagai ciri Nusvanir; mekanisme dan asalnya tidak ditebak sebagai hasil kutukan.

## Habitat

Cabang dan ranting besar pada lapisan bawah kanopi Astradipa, dekat jalur satwa di antara akar dan dahan. Tidak setiap cabang dekat permukiman Asrivana dihuni ular; ia memilih tempat yang memberi tumpuan tubuh dan perlindungan untuk menyergap.

## Kisah — Pegangan yang Bernapas

Seorang pembawa perbekalan menuju Akar-Dipa hendak menarik tubuhnya melewati akar besar. Tangannya hampir meraih sebuah cabang ketika pengawal Asrivana mengetukkan ujung tombak pada tanah. Cabang itu perlahan mengangkat kepala.

Mereka mundur dan memilih pijakan lain. Ular tersebut tidak mengejar, hanya mengencangkan tubuh pada tempatnya semula. Sesampainya di benteng, si pembawa perbekalan mengaku telah diselamatkan dari monster. Pengawalnya mengoreksi dengan tenang: ia diselamatkan dari kebiasaannya meraih sesuatu sebelum melihat.

> Acuan: [Astradipa](../../03_Region/02_Astradipa/Astradipa.md) dan [Akar-Dipa](<../../03_Region/02_Astradipa/Cities & Town/Akar Dipa.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `15.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Wind` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Poisonous` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **12** | **4** | **4** | **20** | **15** | **11** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `380` *(Base 155 + VIT×15 + STR×5)* | **DEF** | `22` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `28` *(INT×8)* | **MDF** | `23` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `99` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `32` *(Base + INT×2)* |
| **ATK** | `26` *(Formula Melee)* | **Action Speed** | `23` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `6.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `4.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `154.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `105.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.33%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.12%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.82%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Venom Bite** | `Poison` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45 (Poison 50%)` |
| **Coiling Bind** | `Earth` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35 (Root 50%)` |
| **Canopy Ambush** | `Earth` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Wind: 150%
* **Resistensi Status:** Poison: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `80` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `60` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `30` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Fang` (`30%`) | Material alam / crafting |
