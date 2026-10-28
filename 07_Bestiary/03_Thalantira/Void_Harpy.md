---
title: Void Harpy
tags:
  - Bestiary
---

# Void Harpy

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Makhluk burung-manusia yang memanah energi dari balik awan Thalantira. Siluetnya dapat menyerupai sosok yang menggantung di udara sebelum sayap terbuka. Ia memburu ruang terbuka di bawahnya, tempat sasaran harus memperlihatkan gerakan untuk berpindah dari satu perlindungan ke perlindungan lain.

## Bentuk

Kepala dan dada menyerupai manusia, berpadu dengan sayap berbulu gelap yang tumbuh di punggung serta tungkai burung bercakar. Sepasang lengan bebas merentang untuk membentuk lengkung energi seperti busur. Bulu panjang pada pinggang dan ekor mengikuti perubahan arah, sementara wajah sebagian tertutup rambut tipis yang tertiup ke belakang. Cahaya ungu berkumpul di antara kedua tangan sebelum memanjang sebagai anak panah. Susunan anggota tubuhnya memungkinkan ia terbang sambil memanah.

## Tingkah Laku

Agresif dari ketinggian dan enggan turun ke jangkauan lawan. Ia melintas di balik kabut, mengubah sudut bidik, lalu menunggu gerakan berikutnya. Jika terancam di udara, Harpy menggunakan cakar untuk mempertahankan ruang sebelum naik lagi. Rupa manusia tidak menjamin kesediaan berunding. Kehadirannya dalam langit pengungkapan Prologue sudah tercatat, tetapi tidak ada dasar untuk menyebutnya anggota Garuda atau keturunan ras bersayap tertentu.

## Habitat

Udara Thalantira, terutama tepian awan di atas tebing dan bukaan hutan sebagai jalur mengintainya. Tempat bertengger sempit di dinding batu memberi pandangan ke bawah tanpa menambahkan sarang berupa desa. Kabut serta angin pulau membantunya menyembunyikan perpindahan, walaupun itu bukan bukti bahwa ia mengendalikan seluruh badai.

## Kisah — Panah di Antara Dua Awan

Kabut bergeser di atas sebuah jalur batu. Di bawahnya, seekor makhluk darat meninggalkan bayangan tebing menuju hutan. Garis cahaya muncul dari awan dan menghantam batu tepat di belakangnya.

Harpy melintas ke sisi lain, menarik lengkung bercahaya di antara tangannya. Sasaran telah masuk ke bawah tajuk sebelum anak panah berikutnya dilepas. Ia bertahan di atas bukaan, sayap bergerak melawan angin. Ketika tak ada lagi gerakan di tanah, sosok itu naik dan kembali hilang bersama kabut.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `46.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **86** | **20** | **36** | **61** | **72** | **49** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3420` *(Base 2255 + VIT×15 + STR×5)* | **DEF** | `117` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `160` *(INT×8)* | **MDF** | `116` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `437` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `135` *(Base + INT×2)* |
| **ATK** | `190` *(Formula Melee)* | **Action Speed** | `108` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `19.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `16.3%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `14.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `183.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `124.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.47%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.60%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.86%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Void Talon** | `11 Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45 (Curse 30%))` |
| **Shrieking Gale** | `05 Air` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35 (Silence 35%))` |
| **Abyssal Dive** | `11 Dark` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25 (Curse 30%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Abyssal Dive, Lowest HP%
State === Taunt: Shrieking Gale, Random
Turn % 2 == 0: Shrieking Gale, Random
Always: Void Talon, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Light: 150%, Void: 50%, Wind: 75%
* **Resistensi Status:** Curse: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
