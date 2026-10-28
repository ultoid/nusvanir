---
title: Deepwater Siren
tags:
  - Bestiary
---

# Deepwater Siren

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Penyanyi ilusi dari perairan Thalantira yang dapat menarik pelaut menuju kematian. Suaranya memberi kesan bahwa sesuatu yang dicari berada sedikit lebih dekat daripada kenyataan. Di laut dengan karang tajam dan arus mustahil, kesalahan kecil dalam menilai arah sudah cukup untuk membawa pendengar keluar dari jalur selamat.

## Bentuk

Tubuhnya menampilkan sosok menyerupai manusia pada bagian kepala dan dada, lalu memanjang menjadi ekor bersirip yang menyatu dengan gelap air. Rambut halus terurai mengikuti arus, sementara selaput tipis pada lengan bergetar ketika tubuh berbelok. Wajahnya sukar dipastikan karena riak dan pembiasan terus mengubah garis mata serta mulut. Sisik kebiruan tampak paling terang di tenggorokan. Rupa yang terlihat melalui ilusinya tidak selalu mencerminkan tubuh yang sedang bergerak di bawah permukaan.

## Tingkah Laku

Memikat dan berbahaya, dengan kecenderungan mengarahkan mangsa sebelum mendekat. Siren mempertahankan jarak di balik riak, memindahkan sumber nyanyian, lalu menunggu korban kehilangan arah. Ketika terancam, ia dapat menyelam dan memanfaatkan lorong karang untuk memutus pengejaran. Nyanyian lembut bukan tanda keramahan. Kehadirannya tercatat bersama makhluk air pada pengungkapan Prologue, tetapi kemampuan ilusi pribadinya tidak membuktikan bahwa dialah pencipta selubung ilusi seluruh pulau.

## Habitat

Perairan sekitar Thalantira, dengan cekungan dalam di belakang benteng karang sebagai tempat bersembunyinya. Gaung pada dinding batu dan gerak air mendukung kesulitan menemukan sumber suaranya. Habitat ini tidak membutuhkan permukiman pelaut di pulau; ancamannya berlaku bagi siapa pun yang mencoba menembus perairan terlarang tersebut.

## Kisah — Nyanyian Tanpa Pantai

Badai membuka sebuah lorong tenang di antara karang. Dari ujungnya terdengar nyanyian, lembut seperti datang dari pantai yang terlindung. Sosok pucat mengambang sebentar di permukaan sebelum lenyap di balik busa.

Siren berenang mengikuti lorong itu sampai dasar laut jatuh menjadi jurang. Nyanyiannya masih terdengar seolah berasal dari daratan. Ketika gelombang menutup jalan masuk, ia berhenti dan mendengarkan air. Pantai yang dijanjikan suaranya tidak pernah ada; hanya karang, kedalaman, dan tubuhnya yang menunggu.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `35.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Void/Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Aquatic, Caster, Sonic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **63** | **27** | **24** | **66** | **57** | **66** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3610` *(Base 2305 + VIT×15 + STR×5)* | **DEF** | `131` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `214` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `476` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `183` *(Base + INT×2)* |
| **ATK** | `138` *(Formula Magic)* | **Action Speed** | `86` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `14.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `173.7%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `133.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.98%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.81%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.60%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Song** | `11 Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45 (Silence 35%))` |
| **Drowning Lure** | `03 Water` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Siren Resonance** | `09 Sound` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Siren Resonance, Lowest HP%
State === Taunt: Drowning Lure, Random
Turn % 2 == 0: Drowning Lure, Random
Always: Abyssal Song, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Void: 50%, Water: 50%
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
