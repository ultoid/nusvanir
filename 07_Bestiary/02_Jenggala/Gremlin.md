---
title: Gremlin
tags:
  - Bestiary
---

# Gremlin

## Deskripsi

Makhluk kecil gesit yang dikenal sebagai Tuyul, pengincar koin dan barang bawaan. Gremlin menyukai saat orang sibuk memperhatikan sesuatu yang lain. Bunyi uang jatuh dapat menjadi jejak kehadirannya, tetapi barang yang hilang tidak selalu berada pada arah suara terakhir.

## Bentuk

Tubuhnya kecil dengan kepala tampak besar, bahu sempit, dan lengan yang berakhir pada jemari panjang. Kulit pucat kelabu, rambut tipis, serta mata gelap memberi rupa yang samar-samar menyerupai boneka hidup ketika dilihat dari jauh. Kaki ramping memudahkannya menyelinap di bawah gerobak. Ia tidak bersayap, dan asalnya tidak ditetapkan sebagai anak dari ras fana tertentu; sebutan Tuyul digunakan sesuai entri lama.

## Tingkah Laku

Licik dan oportunistis, lebih sering mencuri daripada menghadapi lawan secara terbuka. Ia menunggu kantong terbuka, mengambil benda kecil, lalu berlari menuju tempat sempit. Ketika tertangkap atau terpojok, ia dapat menggigit dan mencakar. Tindakan yang tampak bermain-main tetap merugikan korbannya; tidak ada aturan canon bahwa ia harus dipelihara atau dikendalikan seorang majikan.

## Habitat

Jalan setapak pada malam hari adalah tempat kemunculan yang tercatat. Jalur pengangkutan di luar Hermindar menjadi tempat kemunculannya karena banyak barang melewati batas hutan dan permukiman. Tidak perlu menjadikannya penyebab semua pencurian di Cakrawala, yang ancaman utamanya sudah dijelaskan sebagai kriminalitas fana.

## Kisah — Koin untuk Jalan Pulang

Seorang pembawa perkakas dari Hermindar mendengar koin berdenting di belakang gerobak. Ia hampir meninggalkan kendali untuk mengejarnya, tetapi melihat jemari pucat masih menyelip di bawah penutup muatan. Ia segera menghentikan gerobak dan memanggil rekannya.

Sosok kecil melompat turun sambil membawa kantong kosong. Koin yang tercecer dikumpulkan bersama sebelum perjalanan dilanjutkan. Malam itu, kehilangan terbesar ternyata bukan uang, melainkan waktu yang mereka habiskan memeriksa setiap simpul.

> Acuan: [Hermindar](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Hermindar.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `21.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Stealth, Thief` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **14** | **2** | **6** | **16** | **19** | **7** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `198` *(Base 23 + VIT×15 + STR×5)* | **DEF** | `17` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `18` *(Base 2 + INT×8)* | **MDF** | `16` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `83` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `20` *(Base + INT×2)* |
| **ATK** | `31` *(Formula Melee)* | **Action Speed** | `28` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `6.6%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `155.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `103.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.21%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.06%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.90%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Claw** | `Wind` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Pocket Sand** | `Wind` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Gremlin Ambush** | `Wind` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Wind: 75%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `40` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `30` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `15` | Mata uang resmi penjelajahan |
| **Drop 1** | `Jenggala Claw` (`30%`) | Material alam / crafting |
| **Drop 2** | `Beast Fang` (`20%`) | Komponen sekunder |
