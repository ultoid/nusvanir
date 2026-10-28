---
title: Mamon
tags:
  - Bestiary
  - Boss
---

# Mamon

## Deskripsi

Panglima Keserakahan, penguasa korupsi materi, koin terkutuk, dan golem logam karatan. Ia menjadikan keinginan memiliki sebagai beban yang menghancurkan tubuh serta jiwa. Berbeda dari komandan lain, Mamon tercatat menyerang gereja Aqualis untuk merebut bayi kembar yang terikat kutukan Sangrahal.

## Bentuk

Mamon berbentuk iblis kurus dengan koin emas tertanam langsung pada daging. Kedua tangan memanjang sebagai cakar pemungut, dan pecahan logam berkarat bergerak di sekitarnya mengikuti sihir magnetis. Tubuhnya tampak rapuh, tetapi lapisan koin membentuk bidang pelindung tidak rata. Dalam pertempuran ia memanggil golem dari besi yang dapat menyatu kembali setelah dihancurkan. Kilau emas pada tubuhnya selalu bercampur noda gelap dan karat.

## Kepribadian dan Sikap

Mamon licik, posesif, dan menganggap segala sesuatu memiliki harga yang dapat dimanipulasi. Ia menyukai perjanjian yang tampak menguntungkan korban, lalu mengubah kepemilikan menjadi jerat. Ia berkomunikasi melalui koin terkutuk dengan saudagar korup dan memanfaatkan keserakahan tanpa perlu hadir. Saat sesuatu yang diklaimnya direbut, ketenangan itu berubah menjadi kegigihan kejam. Kepatuhannya kepada Sangrahal membawa dirinya ke Aqualis untuk menagih jiwa yang dianggap milik kerajaan.

## Kedudukan dan Benteng

Fortress of Greed adalah tambang emas kutukan bawah tanah dengan permata, relik, dan koin bernoda darah. Mamon menguasai Tambang Emas Berdarah serta golem penjaganya. Setiap harta yang diambil menambah beban korban. Benteng ini menjadi basisnya sebelum ia muncul di Aqualis dan sebelum Raksamala dihancurkan Hector.

## Kisah - Penagih di Gereja Aqualis

Mamon datang ke gereja Aqualis untuk menagih bayi kembar yang terikat kutukan Sangrahal. Ia membangkitkan mayat, memanggil golem besi, dan menekan para pembela sampai Hector menggunakan Avatar Garuda untuk menahannya. Pecahan golem terus menyatu kembali di bawah sihir sang panglima.

Jane, Cassian, dan Hector bertahan bersama sampai kekuatan ungu dari salah satu bayi meledak dan memusnahkan Mamon. Kematian itu mengakhiri penagihan malam tersebut, tetapi juga memperlihatkan bahwa sesuatu yang lebih asing daripada kegelapan Raksamala telah berdiam dalam kehidupan si kembar.

> Acuan: [Mamon](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Mamon.md); [Fortress of Greed](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Greed.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md); [10 Jalan yang Terbelah](../../08_Story/02_Prologue/10_Jalan_yang_Terbelah.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `69.0` | Sheet `NUSV-ENEMIES` |
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

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Soul Extract** | `01 Neutral` / Magical Attack | `12 MP` | Always (Prioritas 5.0) | `-` |
| **Mana Corruption** | `01 Neutral` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Abyssal Life Drain** | `11 Dark` / Magical Attack | `15 MP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.mat * 1.7 - b.mdf * 0.4)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Abyssal Life Drain, All Foes
Turn % 3 == 0: Mana Corruption, Highest ATK
HP% <= 50%: Abyssal Life Drain, Lowest HP%
Always: Soul Extract, Lowest DEF
</AI Priority>
```

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
