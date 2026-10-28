---
title: Kraken Tentacle
tags:
  - Bestiary
---

# Kraken Tentacle

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Bagian tentakel raksasa yang menyerang kapal di perairan Thalantira. Apa yang terlihat di permukaan hanyalah anggota tubuh, bukan ukuran utuh pemiliknya. Satu lengkungan yang disangka gelombang dapat berubah menjadi belitan yang menahan lambung, sementara bagian lain tetap bergerak jauh di bawah air.

## Bentuk

Tentakelnya tebal, lentur, dan berangsur menyempit menuju ujung. Permukaan luar gelap seperti batu basah, dengan lipatan melingkar yang mengencang ketika mencengkeram. Pada sisi dalam, deretan pengisap besar membantu menempel pada permukaan licin. Bekas air mengalir di antara tonjolan kulit ketika anggota tubuh itu terangkat. Ujungnya dapat menyusup lebih dahulu ke celah karang sebelum bagian yang jauh lebih berat mengikuti. Wujud lengkap makhluk di kedalaman tidak diperlihatkan oleh nama entri ini.

## Tingkah Laku

Agresif terhadap sesuatu yang melintasi ruang jangkaunya. Tentakel meraba, menahan, lalu menarik; gerakan yang tampak lambat dapat berubah menjadi hentakan ketika pegangan sudah kuat. Gangguan pada satu bagian membuat belitan menegang atau bergeser ke sisi lain. Melepas satu cengkeraman belum memastikan seluruh ancaman menjauh. Tentakel termasuk manifestasi makhluk air dalam pengungkapan Prologue, tetapi pengamatan itu tidak memastikan berapa banyak individu yang berada di bawah permukaan.

## Habitat

Perairan dalam sekitar Thalantira, terutama jurang di dekat cincin karang sebagai tempat tubuh utamanya tersembunyi. Anggota tubuh dapat menjangkau bagian yang lebih dangkal tanpa membuat keseluruhan makhluk menetap di pantai. Namanya tidak cukup untuk menyamakan pemilik tentakel ini dengan setiap makhluk bernama Kraken di wilayah Nusvanir lain.

## Kisah — Batu yang Ditarik Laut

Sebuah bongkah karang retak oleh gelombang dan jatuh ke saluran sempit. Arus menekannya di antara dinding batu, tempat pusaran biasa menyeret benda-benda dari permukaan. Sesuatu yang gelap melingkari bongkah itu dari bawah.

Belitan mengencang, lalu melepaskan dan mencoba dari sisi lain. Batu akhirnya terguling ke kedalaman. Tentakel mengikuti tanpa memecah permukaan lagi. Saluran kembali terbuka, seolah laut sendiri baru saja memindahkan penghalang yang mengganggu jalannya.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `38.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Aquatic, Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **90** | **18** | **36** | **53** | **51** | **76** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4370` *(Base 2780 + VIT×15 + STR×5)* | **DEF** | `159` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `143` *(INT×8)* | **MDF** | `129` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `580` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `119` *(Base + INT×2)* |
| **ATK** | `198` *(Formula Melee)* | **Action Speed** | `77` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `14.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `15.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `15.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `184.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `138.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.28%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.54%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.56%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Tentacle Slam** | `Void` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Stun 25%)` |
| **Abyssal Grasp** | `Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35 (Root 50%)` |
| **Crushing Coil** | `Void` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25 (Root 50%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Void: 50%, Water: 50%
* **Resistensi Status:** Curse: 50%, Root: 75%, Stun: 70%
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
