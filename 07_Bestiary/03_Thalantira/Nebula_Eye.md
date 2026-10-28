---
title: Nebula Eye
tags:
  - Bestiary
---

# Nebula Eye

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Mata kosmis melayang yang melepaskan sinar mematikan ke arah pandangannya. Kehadirannya membuat ruang terbuka di Thalantira terasa seperti tempat yang terus diawasi. Ia tidak perlu mengepakkan sayap untuk mengubah ketinggian, dan diamnya di udara dapat disangka cahaya ganjil sampai pupil berputar mengikuti gerakan di bawah.

## Bentuk

Sebuah bola besar menjadi pusat tubuh, dibingkai lapisan berkabut yang berputar perlahan. Irisnya memuat lingkaran warna ungu dan biru kusam, dengan pupil gelap yang tampak semakin dalam ketika cahaya berkumpul. Serabut halus menjuntai dari bagian belakang seperti asap yang menolak terurai. Tidak ada wajah, paruh, atau anggota gerak untuk membantu membaca arah niatnya. Perubahan arah tampak dari pergeseran pupil lebih dahulu, lalu seluruh bola mengikuti dengan putaran lambat.

## Tingkah Laku

Mengancam melalui pengamatan dan tembakan dari jarak terbuka. Ia berhenti di atas jalur yang menarik perhatiannya, mengikuti satu gerakan, lalu memusatkan cahaya sebelum menyerang. Gangguan dari arah lain dapat membuatnya berputar tanpa berpindah tempat. Menunduk di balik batu tidak menjamin ia telah kehilangan sasaran. Nebula Eye muncul di langit pada pengungkapan Prologue, tetapi nama dan bentuknya tidak membuktikan bahwa ia merupakan mata milik Uru.

## Habitat

Udara di atas Thalantira, terutama celah langit antara tajuk hutan dan tebing pedalaman sebagai wilayah melayangnya. Ruang terbuka memberi garis pandang panjang, sementara kabut gunung menyamarkan batas tubuhnya. Tidak ada sarang berbentuk bangunan atau tempat pemujaan baru yang diperlukan untuk menjelaskan keberadaannya.

## Kisah — Tatapan di Antara Tajuk

Angin membuka celah pada tajuk, memperlihatkan mata besar yang menggantung di atas hutan. Di bawahnya, seekor makhluk darat berhenti bergerak. Pupil itu terus menghadap ke tempat persembunyiannya meskipun daun kembali menutup pandangan.

Cahaya mengumpul, lalu sebuah sinar memotong sela cabang. Batang yang terkena berasap. Makhluk di bawah sudah menyelinap ke lekukan akar, tetapi mata itu belum pergi. Ia berputar sedikit demi sedikit, menunggu gerakan berikutnya di hutan yang mendadak sunyi.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md); [Uru](../../05_Karakter%20%26%20Tokoh%20Penting/11_Entitas_Purba/Uru.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `41.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Void` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying, Caster` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **81** | **35** | **34** | **80** | **70** | **86** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `5130` *(Base 3435 + VIT×15 + STR×5)* | **DEF** | `169` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `283` *(Base 3 + INT×8)* | **MDF** | `183` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `612` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `238` *(Base + INT×2)* |
| **ATK** | `179` *(Formula Magic)* | **Action Speed** | `105` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `91.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `17.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `20.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `181.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `143.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.58%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `1.05%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.52%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Void Gaze** | `Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45 (Curse 30%)` |
| **Gravity Pulse** | `Void` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35` |
| **Nebula Collapse** | `Void` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Light: 150%, Void: 50%
* **Resistensi Status:** Curse: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1700` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1275` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `440` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
