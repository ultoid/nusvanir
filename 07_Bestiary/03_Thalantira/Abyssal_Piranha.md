---
title: Abyssal Piranha
tags:
  - Bestiary
---

# Abyssal Piranha

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Ikan pemangsa Thalantira yang rahangnya mampu merobek zirah adamantite. Tubuh yang jauh lebih kecil daripada para raksasa laut pulau ini membuatnya mudah terabaikan. Kilatan singkat di antara karang dapat menjadi satu-satunya tanda sebelum air yang semula kosong dipenuhi gerakan menggigit.

## Bentuk

Tubuhnya pipih dari samping dan padat di belakang kepala, dengan pangkal ekor kuat untuk menyentak melawan arus. Sisik kelabu kebiruan memantulkan cahaya ungu dari pulau sebagai kilatan patah. Rahang bawah sedikit menonjol; gigi segitiga tersusun rapat sehingga mulut yang tertutup tetap tampak bergerigi. Sirip pendek menjaga tubuhnya tidak mudah tersangkut di lorong karang. Saat berbalik serentak, kawanan terlihat seperti serpihan logam yang dituang ke dalam air.

## Tingkah Laku

Buas dan cepat bereaksi terhadap mangsa yang terdesak. Kawanan menyebar mengikuti celah, lalu berkumpul ketika salah satu menemukan kesempatan menggigit. Gangguan besar membuatnya berpencar sementara sebelum mendekat dari sisi lain. Pertahanan tubuh mangsa tidak selalu menghalanginya, tetapi sifat perobek zirah tidak berarti ia memakan logam sebagai makanan utama. Dalam pengungkapan Prologue, piranha termasuk makhluk air yang muncul ketika kedamaian pulau runtuh.

## Habitat

Uru biasa memproyeksikan kawanan ini di perairan Thalantira, terutama celah cincin karang, saluran sempit berarus deras, dan kantong air di balik batu. Kemunculannya di daratan pada kekacauan Prologue terjadi karena Uru dapat membentuk proyeksi tanpa mengikuti batas perpindahan populasi biologis.

## Kisah — Kilatan di Celah Karang

Seekor ikan besar berlindung dari pusaran di antara dua dinding karang. Ruang itu tampak kosong sampai kilatan kecil bergerak di dekat ekornya. Ia mengibas kuat, mengusir satu bayangan, tetapi gerakan itu membawanya semakin dalam ke lorong sempit.

Dari bawah batu, kilatan lain datang. Air bergolak sesaat, lalu arus kembali berjalan seperti sebelumnya. Kawanan piranha menyebar ke celah masing-masing. Di atasnya, gelombang terus memukul benteng karang; tak ada perubahan pada permukaan yang menunjukkan apa yang baru saja terjadi.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `31.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Voidborn, Pack Hunter` | Penanda taktis unit |

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
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Void Bite** | `Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Curse 30%)` |
| **Abyssal Swarm** | `Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35 (Curse 30%)` |
| **Feeding Frenzy** | `Void` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Light: 150%, Lightning: 125%, Void: 50%, Water: 50%
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
