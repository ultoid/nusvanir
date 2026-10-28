---
title: Ogre
tags:
  - Bestiary
---

# Ogre

## Deskripsi

Raksasa hijau pemakan daging mentah yang juga dikenal sebagai Buto Ijo. Ogre menggunakan tubuh besarnya untuk memaksa jalan melalui penghalang dan dapat membuat perlindungan kayu terasa rapuh. Kemunculannya bersama Goblin dalam serbuan tidak berarti keduanya merupakan satu spesies atau memiliki hubungan keluarga.

## Bentuk

Badannya sangat besar dengan dada lebar, perut berat, dan lengan tebal yang menggantung rendah. Kulit hijau kusam berlipat pada leher serta siku, sementara kepala tampak kecil dibandingkan bahunya. Rahang lebar, gigi kasar, dan hidung pipih memperkuat rupa yang sudah disebut Buto Ijo. Tangan besarnya mampu menggenggam benda yang bagi manusia harus diangkat bersama. Ciri ini tidak digunakan untuk menyamakannya dengan Butoraksa atau Troliogoro.

## Tingkah Laku

Buas dan berbahaya di dekat sumber makanan. Ia dapat mendekati bau daging, menyingkirkan penghalang, dan menyerang makhluk yang mencoba merebut atau mempertahankan makanan itu. Ketika terluka, gerakannya semakin kasar dan sulit diperkirakan. Tidak semua Ogre dapat dianggap bodoh atau tidak mampu belajar; tingkat kecerdasan serta susunan kelompoknya belum ditetapkan.

## Habitat

Gunung Bebatuan adalah habitat lama tanpa region jelas. Lereng berbatu Arkananta yang berdekatan dengan jalur portal liar menjadi bagian dari persebarannya. Prologue mencatat Ogre muncul di pesisir Aqualis melalui portal, sehingga pantai merupakan lokasi serangan yang terbukti, bukan habitat asal yang dipaksakan.

## Kisah — Pintu yang Terlalu Kecil

Seorang pengangkut berlindung di pondok jalan lereng Arkananta ketika mendengar langkah berat. Ia sempat lega karena pintunya terlalu kecil untuk sosok hijau yang muncul di luar. Lalu tangan besar meraih kusen dan membuat seluruh dinding berderak.

Pengangkut itu keluar lewat celah belakang sebelum atap merosot. Dari kejauhan ia melihat makhluk itu membongkar kantong daging yang tertinggal. Pintu yang kuat baginya ternyata hanya benda lain yang dapat ditarik dari tempatnya.

> Acuan: [Threat](../../03_Region/05_Arkananta/Threat.md); [03 Teror di Pesisir Timur](../../08_Story/02_Prologue/03_Teror_di_Pesisir_Timur.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `25.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Berserker` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T4 (Mini Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **45** | **6** | **16** | **30** | **29** | **19** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `2420` *(Base 1910 + VIT×15 + STR×5)* | **DEF** | `51` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `48` *(INT×8)* | **MDF** | `47` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `205` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `48` *(Base + INT×2)* |
| **ATK** | `98` *(Formula Melee)* | **Action Speed** | `44` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `88.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `9.3%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `9.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `6.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `166.7%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `109.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.57%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.18%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.54%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Ogre Smash** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Stun 25%)` |
| **Ground Slam** | `Earth` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35 (Stun 25%)` |
| **Rampaging Crush** | `Earth` / Physical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.atk * 1.85 - b.def * 0.25 (Stun 25%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 150%
* **Resistensi Status:** Freeze: 70%, Paralyze: 70%, Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `520` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `390` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `160` | Mata uang resmi penjelajahan |
| **Drop 1** | `Butoraksa Bone` (`18%`) | Material alam / crafting |
| **Drop 2** | `Beast Bone` (`40%`) | Komponen sekunder |
