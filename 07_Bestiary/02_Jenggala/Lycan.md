---
title: Lycan
tags:
  - Bestiary
---

# Lycan

## Deskripsi

Manusia harimau beraura petir yang dikenal sebagai Cindaku. Lycan Nusvanir dikenali dari perpaduan tubuh humanoid, ciri harimau, dan kilatan listrik di sekitar gerakannya. Namanya tidak menjadikannya manusia serigala atau makhluk yang harus berubah ketika bulan purnama.

## Bentuk

Tubuhnya tegak dan berotot dengan bahu lebar, tangan bercakar, serta tungkai yang dapat merendah ketika bersiap melompat. Bulu belang memadukan kuning tua dan hitam, sementara wajah mempertahankan perpaduan tatapan manusia dengan moncong serta kumis harimau. Bulu tengkuk terangkat ketika aura petir menguat; kilatan pendek tampak menyusuri garis tubuh, bukan perhiasan logam yang dikenakannya.

## Tingkah Laku

Waspada, teritorial, dan sangat berbahaya ketika memilih menyerang. Ia dapat mengamati pendatang sebelum menunjukkan gigi atau merendahkan tubuh. Serangannya mengandalkan lompatan dan cakar, sementara aura petir mempertegas ancaman yang sudah tercatat. Perilaku ini tidak menetapkan bahwa ia selalu jahat, dapat dijinakkan, atau mempunyai aturan perubahan bentuk yang sama pada setiap individu.

## Habitat

Lereng Gunung Emas adalah habitat sumber yang belum ditemukan pemetaan pastinya. Lereng berhutan Arkananta menjadi persebaran regionalnya; pemetaan nama Gunung Emas tetap belum dipastikan. Gunung Emas tidak disamakan dengan Puncak Emas Swargaloka, yang merupakan habitat melayang bangsa Garuda.

## Kisah — Belang dalam Hujan

Rombongan pembawa obat di lereng Arkananta melihat kilatan di bawah pepohonan meskipun suara guntur sudah menjauh. Pada cahaya berikutnya, tampak sosok tegak dengan belang harimau berdiri di jalur sempit.

Pemandu meminta semua orang menurunkan bungkusan yang menutupi pandangan dan mundur bersama. Sosok itu tidak mengikuti mereka ke jalan berbatu. Mereka memilih menginap sebelum melanjutkan perjalanan, tanpa menganggap pertemuan singkat tersebut sebagai izin untuk kembali melewati wilayah yang sama.

> Acuan: [Threat](../../03_Region/05_Arkananta/Threat.md); [Puncak Emas Swargaloka](../../03_Region/07_Nusa%20Sayendra/Cities%20%26%20Town/Puncak%20Emas%20Swargaloka.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `24.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Lightning` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Ice` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Frenzy, Lightning` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **25** | **4** | **12** | **21** | **21** | **17** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `714` *(Base 334 + VIT×15 + STR×5)* | **DEF** | `38` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `32` *(INT×8)* | **MDF** | `32` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `155` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `35` *(Base + INT×2)* |
| **ATK** | `56` *(Formula Melee)* | **Action Speed** | `32` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `7.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `7.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `4.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `159.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `108.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.51%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.12%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.18%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Lightning Claw** | `Lightning` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Paralyze 30%)` |
| **Savage Bite** | `Lightning` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Thunder Frenzy** | `Lightning` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `- (Paralyze 30%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Ice: 150%, Lightning: 75%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Lycan Hide` (`45%`) | Material alam / crafting |
| **Drop 2** | `Beast Fang` (`25%`) | Komponen sekunder |
