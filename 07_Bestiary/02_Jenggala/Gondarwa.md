---
title: Gondarwa
tags:
  - Bestiary
---

# Gondarwa

## Deskripsi

Raksasa hutan berbulu tebal yang kehadirannya dapat dikenali dari jalur tumbuhan yang patah pada ketinggian tidak biasa. Gondarwa mengandalkan kekuatan tubuh, bukan rupa senjata yang dibawanya. Kesunyian sesaat sebelum ia bergerak lebih berbahaya daripada suara langkahnya yang sudah menjauh.

## Bentuk

Tubuhnya tinggi dan lebar, dengan lengan berat yang menggantung di sisi paha. Bulu kusut menutupi bahu, dada, serta punggung; serpihan kulit kayu dan daun dapat tersangkut di dalamnya. Wajah sebagian tenggelam di balik rambut, menyisakan mata dalam dan rahang besar. Warna cokelat gelap serta hitam tanah dipilih untuk menyatu dengan batang tua. Wujud berbulu tidak menjadikannya Hanorok atau kerabat yang sudah dipastikan.

## Tingkah Laku

Teritorial dan mudah menjadi ganas ketika jalur atau tempat berdiamnya diganggu. Ia dapat merobohkan semak, menghantam batang, atau mengentakkan kaki sebagai tanda kehadiran sebelum mendekat. Pendatang yang terus menekan dapat memancing serangan langsung. Diet dan susunan kelompoknya belum cukup jelas untuk menyatakan bahwa ia selalu memangsa manusia atau hidup sebagai penjaga hutan yang baik hati.

## Habitat

Catatan Jenggala Dalam menjelaskan habitat yang rapat tetapi bukan region administratif. Lantai hutan Astradipa yang jauh dari jalur aman menjadi salah satu lokasi kemunculannya. Ancaman Jenggala terhadap Akar-Dipa mendukung konteks perjumpaan tersebut, tanpa menjadikan seluruh hutan sebagai wilayah Gondarwa.

## Kisah — Batang yang Tidak Ditebang

Sebuah patroli Asrivana menemukan pohon muda patah di tengah jalur bawah Astradipa. Tidak ada bekas kapak. Serat batang terpelintir seolah diremas dari kedua arah. Penjaga terdepan hendak melewatinya ketika tanah bergetar dari sisi rimbun.

Mereka mengubah jalur dan menandai lokasi itu untuk patroli berikutnya. Di belakang, terdengar satu hantaman berat pada kayu. Tidak ada pengejaran, tetapi mereka tidak kembali untuk memastikan apakah peringatan kedua akan tetap berupa suara.

> Acuan: [Threat](../../03_Region/02_Astradipa/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `20.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **25** | **4** | **12** | **21** | **19** | **18** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `782` *(Base 387 + VIT×15 + STR×5)* | **DEF** | `40` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `32` *(INT×8)* | **MDF** | `32` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `160` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `33` *(Base + INT×2)* |
| **ATK** | `56` *(Formula Melee)* | **Action Speed** | `28` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `6.8%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `7.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `5.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `159.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `109.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.54%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.12%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.12%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Stone Fist** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Earthen Roar** | `Earth` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Gondarwa Crush** | `Earth` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25 (Stun 25%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 150%
* **Resistensi Status:** Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Stone` (`18%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`25%`) | Komponen sekunder |
