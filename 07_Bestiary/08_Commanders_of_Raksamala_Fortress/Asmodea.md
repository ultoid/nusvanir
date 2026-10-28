---
title: Asmodea
tags:
  - Bestiary
  - Boss
---

# Asmodea

## Deskripsi

Panglima Bhuta dan penjaga Fortress of Lust yang menaklukkan lawan melalui keinginan terdalam mereka. Suaranya membentuk mimpi indah yang membuat korban menolak bangun, sementara tubuh asli mereka perlahan layu dan jiwanya dipintal menjadi Dhemit.

## Bentuk

Wujud asli Asmodea adalah Bhuta bersiluet ramping dengan sayap gelap dan suara yang terasa datang dari jarak berbeda. Penampilannya tidak tetap: ia dapat menyerupai orang yang paling dicintai, dirindukan, atau dihasrati sasaran. Dalam wujud tiruan, ketidakwajaran tampak pada bayangan yang terlambat bergerak dan mata yang tidak berubah ketika wajah tersenyum. Ia tidak membawa senjata fisik; suara, gestur, dan ilusi menjadi alat utamanya.

## Kepribadian dan Sikap

Asmodea sabar, manipulatif, dan sangat peka terhadap kebutuhan yang tidak berani diucapkan orang lain. Ia jarang memaksa pada awal pertemuan, lebih suka membuat korban merasa memilih sendiri. Penolakan dianggap tantangan untuk menemukan hasrat yang lebih tersembunyi. Kesetiaannya kepada Sangrahal terikat struktur Raksamala, tetapi ia tetap memiliki kecerdikan pribadi. Ia memperlakukan bawahan sebagai perpanjangan rencana, bukan sahabat, dan membuang penyamaran yang tidak lagi berguna.

## Kedudukan dan Benteng

Fortress of Lust berupa istana bawah tanah yang berubah mengikuti hasrat pengunjung. Asmodea menguasai pusat labirin mimpi dan menyimpan Segel Hawa Nafsu di balik wajah aslinya. Segel itu hanya tampak kepada orang yang menolak seluruh rupa yang ia tawarkan.

## Kisah - Mimpi yang Memilih Wajah

Seorang penyusup melihat rumah yang telah lama hilang dan mendengar suara keluarganya dari balik pintu. Asmodea tidak muncul sebagai monster; ia memakai wajah seseorang yang paling dirindukan penyusup itu dan memintanya beristirahat.

Ketika tangan penyusup menyentuh gagang pintu, ia melihat bayangannya sendiri bergerak terlambat. Ia memejamkan mata dan menyebutkan alasan kedatangannya berulang kali. Taman indah berubah menjadi lorong berduri. Asmodea tertawa dari banyak arah, tetapi korban telah menemukan satu hal yang tidak dapat diberikan ilusi: pilihan untuk tetap berjalan meski kerinduan belum sembuh.

> Acuan: [Asmodea](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Asmodea.md); [Fortress of Lust](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Lust.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Dhemit](../../04_Ras/04_Drahkthar/Dhemit.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `64.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Caster, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **103** | **45** | **40** | **88** | **73** | **108** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `20900` *(Base 18765 + VIT×15 + STR×5)* | **DEF** | `214` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `357` *(INT×8)* | **MDF** | `231` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `766` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `300` *(Base + INT×2)* |
| **ATK** | `226` *(Formula Magic)* | **Action Speed** | `110` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `21.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `19.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `24.0%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `188.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `154.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.24%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `1.35%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.08%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Chains** | `Dark` / Magical Attack | `16 MP` | Always (Prioritas 5.0) | `a.mat * 1.2 - b.mdf * 0.4` |
| **Umbral Veil** | `Dark` / Magical Attack | `10 MP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Soul Rupture** | `Neutral` / Magical Attack | `35 MP` | HP <= 50% (Prioritas 6.0) | `a.mat * 2.0 - b.mdf * 0.6` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `8500` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `6375` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `2200` | Mata uang resmi penjelajahan |
| **Drop 1** | `Kala Crystal` (`25%`) | Material alam / crafting |
| **Drop 2** | `Spirit Thread` (`15%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`10%`) | Rampasan langka |
