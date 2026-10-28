---
title: Crystal Basilisk
tags:
  - Bestiary
---

# Crystal Basilisk

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Kadal raksasa dengan tatapan yang dikenal membekukan korbannya. Di bawah cahaya ungu Thalantira, tubuhnya dapat disangka gugusan kristal sebelum kepala bergerak mengikuti sesuatu yang lewat. Bahayanya tidak hanya datang dari rahang: menatap balik untuk memastikan bentuknya dapat menjadi bagian paling buruk dari sebuah perjumpaan.

## Bentuk

Tubuhnya rendah dan panjang, ditopang kaki tebal dengan jemari bercakar yang menyebar pada batu. Sisik besar di punggung membentuk bidang bening keruh, sedangkan bagian perut tampak lebih rapat dan kusam. Tonjolan kristal tumbuh mengikuti tengkuk hingga pangkal ekor, menyerupai pecahan mineral yang tertanam pada kulit. Kelopak keras membingkai mata terang. Ketika kepala terangkat, pantulan pada sisik bergerak lebih dahulu daripada tubuhnya, membuat posisi mata sulit dibedakan dari kilau batu.

## Tingkah Laku

Teritorial dan berbahaya bila didekati. Ia menahan tubuh di tempat, mengangkat kepala, lalu mengikuti gangguan dengan pandangan sebelum bergerak. Ancaman yang terus mendekat dapat memancing serangan terbuka. Keheningan tidak menunjukkan sifat jinak; Basilisk dapat menunggu dari posisi yang hampir tidak berubah. Catatan lama menyebut pembekuannya permanen, tetapi kisah belum menjelaskan batas maupun pemulihannya. Dalam Prologue ia termasuk monster darat yang terlihat setelah selubung damai pulau tersingkap.

## Habitat

Uru biasa memproyeksikan Basilisk pada teras batu di peralihan hutan dan lereng Gunung Ungu, dengan celah yang menyembunyikan tubuh panjangnya. Penempatan ini membentuk perilaku berburu yang meyakinkan, meskipun makhluk tersebut tidak memiliki habitat biologis dan dapat dibentuk kembali di tempat lain oleh penciptanya.

## Kisah — Kristal yang Menoleh

Seekor pemangsa kecil menyusuri tepian batu, mengikuti gerakan di balik semak. Di depannya, deretan kristal memantulkan langit. Ia berhenti ketika salah satu pantulan bergerak melawan arah cahaya.

Kepala Basilisk terangkat perlahan. Pemangsa itu mundur ke balik akar, memutus pandangan sebelum seluruh tubuh panjang muncul dari ceruk. Basilisk tidak mengejar ke hutan rapat. Ia kembali merendahkan kepala, dan lereng kembali tampak seperti batu yang tidak dihuni apa pun.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [Kuil Udara Gunung Ungu](../../03_Region/11_Thalantira/Cities%20%26%20Town/Kuil%20Udara%20Gunung%20Ungu.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `34.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Void/Crystal` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Armored, Petrifying` | Penanda taktis unit |

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
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Crystal Fang** | `Void` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45` |
| **Petrifying Gaze** | `Void` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35 (Petrify 35%)` |
| **Prismatic Rupture** | `Void` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Crystal: 75%, Earth: 150%, Void: 50%
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
