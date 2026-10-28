---
title: Serigala Kelabu
tags:
  - Bestiary
---

# Serigala Kelabu

## Deskripsi

Pemangsa kawanan yang menguji kelemahan mangsa sebelum mendekat. Serigala Kelabu tidak selalu menyerang dari arah suara lolongannya; anggota lain dapat bergerak diam di antara pepohonan. Ketika kesempatan buruk, kawanan dapat mundur dan menunggu alih-alih mempertaruhkan seluruh anggotanya.

## Bentuk

Tubuhnya ramping tetapi berotot, dengan dada dalam, tungkai panjang, dan telapak lebar. Bulu kelabu berlapis cokelat arang lebih tebal pada tengkuk serta bahu, menyamarkan garis tubuh di antara kabut dan batang pohon. Moncongnya memanjang, telinganya tegak, dan ekornya berbulu lebat. Individu yang basah tampak lebih kurus daripada ketika bulunya kering, sehingga ukurannya mudah disalahkirakan dari kejauhan.

## Tingkah Laku

Buas sebagai pemburu, namun waspada terhadap kelompok manusia yang teratur. Kawanan berkomunikasi melalui suara, posisi tubuh, dan gerakan telinga. Ternak terpisah atau hewan yang terluka lebih mudah menarik perhatian mereka. Mereka dapat menjadi agresif ketika sarang didekati atau ketika terdesak; gigi diperlihatkan dan geraman rendah mendahului sebagian serangan, tetapi penyergapan berburu dapat berlangsung tanpa peringatan itu.

## Habitat

Hutan rimbun di luar Valkindra, pada kawasan utara Mandala yang lebih dingin dan berkabut. Kawanan memanfaatkan tutupan pepohonan di sekitar jalur liar. Kehadirannya dekat reruntuhan tidak menjadikannya makhluk kutukan.

## Kisah — Lolong di Luar Cahaya

Menjelang malam di luar Valkindra, seorang pengawal mendengar lolongan dan ingin menyalakan tanda bahaya. Rekannya memintanya memeriksa gerobak belakang terlebih dahulu. Seekor hewan penarik pincang telah tertinggal, sementara bayangan kelabu bergerak di sela kabut.

Mereka merapatkan rombongan dan membawa hewan itu kembali ke tengah. Bayangan tersebut mengikuti sebentar, lalu menghilang. Ketika Menara Matahari terlihat di kejauhan, pengawal itu mengerti bahwa tidak semua ancaman malam berasal dari retakan dimensi; sebagian hanya menunggu kelengahan di jalan.

> Acuan iklim dan kota: [Valkindra](<../../03_Region/01_Mandala Kingdom/Cities & Town/Valkindra.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `14.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Pack Hunter` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **17** | **2** | **6** | **16** | **15** | **11** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `420` *(Base 170 + VIT×15 + STR×5)* | **DEF** | `25` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `18` *(Base 2 + INT×8)* | **MDF** | `21` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `109` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `22` *(Base + INT×2)* |
| **ATK** | `37` *(Formula Melee)* | **Action Speed** | `23` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.8%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `105.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.33%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.06%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.82%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Wolf Fang** | `Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Pack Howl** | `Neutral` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Lupine Rush** | `Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 150%
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
