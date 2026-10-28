---
title: Jenderal Suparna
tags:
  - Bestiary
  - Boss
---

# Jenderal Suparna

## Deskripsi

Sentinel barat yang mengendalikan badai salju serta pecahan es di langit Nusa Sayendra. Suparna menggunakan dingin untuk memperlambat ancaman dan membuka ruang bagi formasi lain. Keanggunannya lahir dari kendali gerak yang hemat; ia tidak perlu memenuhi langit dengan serangan ketika perubahan suhu yang tepat dapat mengalihkan seluruh jalur terbang lawan.

## Bentuk

Suparna memiliki tubuh tinggi dengan bulu emas pucat yang tampak keperakan di bawah awan. Lapisan biru muda mengikuti bagian bawah sayap dan ekor, tempat kristal es sering terbentuk sebelum pecah menjadi serbuk. Lehernya panjang, mata tenang, dan paruh ramping memberi siluet yang berbeda dari Jatayu serta Sempati. Perlengkapan ringan berwarna putih menghindari bagian sendi. Ketika memanggil badai, uap membentuk lingkaran di sekeliling sayap sebelum es bergerigi tumbuh mengikuti arus.

## Kepribadian dan Sikap

Suparna tenang, santun, dan sulit dipancing untuk bertindak tergesa-gesa. Ia lebih suka meredakan pertengkaran dengan menunjukkan akibat setiap pilihan daripada meninggikan suara. Sikap terkendali itu dapat disalahartikan sebagai jarak emosional, padahal ia memperhatikan keadaan pasukan secara rinci. Ia keras terhadap tindakan yang mengorbankan ketelitian demi penampilan. Saat menghadapi ancaman, ia menunggu saat yang memberi hasil terbesar dengan kerusakan paling kecil, lalu bergerak cepat sebelum lawan sempat menyesuaikan diri.

## Kedudukan dan Kuil Penjagaan

Kuil Angin Barat Sayendra adalah pos penjagaan Suparna. Dari sisi barat ia memantau perubahan cuaca dan jalur kembali menuju Puncak Emas Swargaloka. Udara dingin pada lapisan tinggi mendukung pembentukan es tanpa menetapkan bahwa wilayah pulau di bawahnya selalu bersalju. Kuil tersebut belum mempunyai deskripsi regional tersendiri, sehingga rincian arsitektur dan jaraknya tetap terbuka.

## Kisah - Es yang Tidak Dijatuhkan

Sebuah kawanan Jenggala terbang di atas jalur yang juga dipakai pengangkut telur suci. Suparna telah membentuk pecahan es, tetapi serangan luas akan mengenai rombongan di bawah. Ia menahan badai dan meminta pengawal mengubah ketinggian.

Setelah jalur kosong, Suparna mendinginkan udara di depan kawanan musuh. Sayap mereka menjadi berat oleh kristal, memaksa semuanya turun menjauh dari Swargaloka. Tidak ada hujan es yang jatuh ke pengangkut. Para prajurit muda kemudian memahami bahwa kendali Suparna terlihat bukan hanya dari apa yang dilepaskan, melainkan dari serangan yang sanggup ia tahan sampai waktunya benar.

> Acuan: [Nusa Sayendra](../../03_Region/07_Nusa%20Sayendra/Nusa_Sayendra.md); [Garuda](../../04_Ras/02_Wuru%20Loka/Garuda.md); [Puncak Emas Swargaloka](../../03_Region/07_Nusa%20Sayendra/Cities%20%26%20Town/Puncak%20Emas%20Swargaloka.md); [Pasukan Ksatria Sayap Garuda](../../03_Region/07_Nusa%20Sayendra/Faksi%20%26%20Institusi/Pasukan%20Ksatria%20Sayap%20Garuda.md); [Sumpah Penjaga Langit](../../03_Region/07_Nusa%20Sayendra/Agama%20%26%20Kepercayaan/Sumpah%20Penjaga%20Langit.md); [Threat](../../03_Region/07_Nusa%20Sayendra/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `63.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Garuda` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Light/Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Dark` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Holy, Caster` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **69** | **130** | **28** | **58** | **60** | **76** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `13950` *(Base 12465 + VIT×15 + STR×5)* | **DEF** | `148` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `292` *(INT×8)* | **MDF** | `179` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `538` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `260` *(Base + INT×2)* |
| **ATK** | `152` *(Formula Magic)* | **Action Speed** | `90` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `90.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `14.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.3%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `176.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `138.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.28%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `3.90%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.92%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Aero Slash** | `Wind` / Magical Attack | `12 SP` | Always (Prioritas 5.0) | `a.mat * 2.1 - b.mdef * 0.2 (Float 50%)` |
| **Holy Nova** | `Light` / Magical Attack | `24 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Celestial Maelstrom** | `Light` / Magical Attack | `55 SP` | HP <= 50% (Prioritas 6.0) | `a.mat * 7.5 - b.mdf * 0.0 (Silence 70% / Blind 70%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Light: 50%, Wind: 50%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5600` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4200` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1500` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Golden Scale` (`25%`) | Material alam / crafting |
| **Drop 2** | `Garuda Storm Feather` (`25%`) | Komponen sekunder |
| **Drop 3** | `Prabha Thread` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Suparna Golden Mantle` (`5%`) | Rampasan unik / piala bos |
