---
title: Goblin
tags:
  - Bestiary
---

# Goblin

## Deskripsi

Penghuni gua bertubuh pendek yang dikenal sebagai Ebu Gogo. Goblin menjadi jauh lebih berani ketika bergerombol: suara dari depan dapat menutupi gerakan anggota lain di sisi jalan. Mereka tidak perlu mengalahkan rombongan sekaligus untuk membahayakannya; cukup membuat seorang pengelana tertinggal.

## Bentuk

Tubuhnya pendek dengan bahu membungkuk, lengan relatif panjang, dan jemari yang kuat untuk mencengkeram batu. Wajah lebar, alis menonjol, serta rambut kasar yang tidak rata memperkuat kesan penghuni lorong lembap. Kulit berwarna tanah kusam dan kuku kotor melengkapi rupanya. Ia tidak diberi telinga atau ciri ras Asrivana hanya karena namanya menggunakan istilah Goblin; Ebu Gogo tetap menjadi acuan identitas yang tercatat.

## Tingkah Laku

Beringas dalam kelompok tetapi lebih berhati-hati ketika sendirian. Mereka mengintai jalur sempit, saling memanggil, lalu mendekat setelah lawan kehilangan arah. Individu yang terluka dapat mundur ke celah sementara anggota lain mengalihkan perhatian. Pola ini menggambarkan koordinasi kawanan, bukan bukti bahwa mereka memiliki kerajaan, kasta, atau kebudayaan yang belum ditulis.

## Habitat

Sistem gua merupakan habitat yang tercatat. Gua pada lereng luar Arkananta menjadi bagian dari persebarannya. Prologue juga mencatat Goblin keluar dari portal yang dibuka Wight di pesisir Aqualis; ini merupakan rute invasi, bukan alasan menjadikan Goblin fauna pantai.

## Kisah — Suara dari Lorong Kiri

Pemandu rombongan di lereng Arkananta mendengar teriakan dari lorong kiri, tetapi melihat debu jatuh dari celah kanan. Ia meminta semua orang tetap berjalan rapat. Seorang pengangkut hampir memisahkan diri untuk mengejar sosok kecil yang memperlihatkan kantong bekalnya.

Baru setelah obor kedua diarahkan ke kanan, tampak beberapa tangan menggenggam tepian batu. Rombongan itu mundur bersama. Teriakan berhenti begitu tidak ada lagi orang yang mau masuk sendirian.

> Acuan: [Threat](../../03_Region/05_Arkananta/Threat.md); [03 Teror di Pesisir Timur](../../08_Story/02_Prologue/03_Teror_di_Pesisir_Timur.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `19.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Pack Hunter` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **15** | **2** | **4** | **14** | **15** | **10** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `231` *(Base 6 + VIT×15 + STR×5)* | **DEF** | `22` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `16` *(INT×8)* | **MDF** | `18` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `100` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `19` *(Base + INT×2)* |
| **ATK** | `32` *(Formula Melee)* | **Action Speed** | `22` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `155.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `105.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.30%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.06%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.80%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Rusty Slash** | `Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Dirty Trick** | `Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Goblin Rush** | `Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 150%
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
