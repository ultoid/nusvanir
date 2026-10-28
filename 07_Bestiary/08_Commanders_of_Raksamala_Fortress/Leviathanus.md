---
title: Leviathanus
tags:
  - Bestiary
  - Boss
---

# Leviathanus

## Deskripsi

Panglima Kedengkian, monster amfibi yang menjaga Fortress of Envy dan menyerang persatuan kelompok. Racunnya memperbesar perbandingan, iri hati, dan dorongan mengkhianati rekan. Ia membenci keindahan daratan serta matahari, lalu memakai gambaran kehidupan sempurna untuk membuat orang lain membenci pilihan mereka sendiri.

## Bentuk

Tubuh Leviathanus menyerupai ular laut raksasa dengan sisik gelap dan banyak tentakel bayangan. Mata hijau pucat menonjol dari kepala amfibi, sementara selaput pada leher bergerak ketika ia bernapas. Es tumbuh pada ujung tentakel sebelum dilepaskan bersama bisa. Tubuhnya dapat melingkari akar serta dinding Labirin Ratapan, membuat asal serangan sulit ditemukan. Pantulan cermin memecah wujudnya menjadi banyak sosok yang tampak saling mengawasi.

## Kepribadian dan Sikap

Leviathanus pendendam, posesif, dan terus membandingkan miliknya dengan kehidupan pihak lain. Ia pandai menemukan rasa tidak aman dalam kelompok dan mengulangnya sampai terdengar seperti kebenaran. Kepada bawahan ia memberi penghargaan yang sengaja tidak setara agar persaingan tumbuh. Ia membenci Ksatria Aqua yang berulang kali mencegatnya di laut. Ketika lawan saling mempercayai tanpa mencari siapa yang lebih unggul, ketenangannya pecah menjadi kemarahan terbuka.

## Kedudukan dan Benteng

Fortress of Envy tersembunyi di dasar lembah beracun, tersusun dari akar layu, duri, cermin ajaib, dan lantai beracun. Leviathanus menguasai Labirin Ratapan serta Danau Hitam yang disebut data lama. Jalur air memberi akses ke laut tempat ia berhadapan dengan Aqua. Benteng ini merujuk keadaan sebelum kehancuran Raksamala.

## Kisah - Cermin untuk Dua Sahabat

Dua penyusup melihat masa depan berbeda di dalam cermin: satu dipuji sebagai pahlawan, yang lain dilupakan. Leviathanus membisikkan bahwa hanya satu dari mereka yang layak keluar hidup-hidup. Tangan keduanya bergerak menuju senjata.

Salah seorang memecahkan cerminnya sendiri dan meminta rekannya melakukan hal sama. Bayangan sempurna runtuh menjadi pecahan yang hanya memperlihatkan wajah lelah mereka. Leviathanus menyerang dari danau, marah karena perbandingan itu kehilangan permukaan tempat tumbuh.

> Acuan: [Leviathanus](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Leviathanus.md); [Fortress of Envy](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Envy.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `67.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark/Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Aquatic, Large, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **122** | **30** | **50** | **70** | **59** | **147** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `27500` *(Base 24685 + VIT×15 + STR×5)* | **DEF** | `281` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `238` *(INT×8)* | **MDF** | `231` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `999` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `196` *(Base + INT×2)* |
| **ATK** | `269` *(Formula Melee)* | **Action Speed** | `88` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `95.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `17.3%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `20.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `25.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `196.6%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `173.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `4.41%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.90%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.30%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Current** | `Dark` / Magical Attack | `20 SP` | Always (Prioritas 5.0) | `a.mat * 1.2 - b.mdef * 0.3 (Soaked 40%)` |
| **Abyssal Chains** | `Dark` / Magical Attack | `16 MP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.2 - b.mdf * 0.4` |
| **Tsunami** | `Fire` / Magical Attack | `55 SP` | HP <= 50% (Prioritas 6.0) | `Base: a.matk * 8.0. During Rain: Damage x1.5.` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%, Lightning: 125%, Water: 50%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Root: 75%, Stun: 40%
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
