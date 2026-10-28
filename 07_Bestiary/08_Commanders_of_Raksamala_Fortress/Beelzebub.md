---
title: Beelzebub
tags:
  - Bestiary
  - Boss
---

# Beelzebub

## Deskripsi

Panglima Kerakusan yang menjaga rumah jagal bawah tanah Fortress of Gluttony. Ia memakan materi, sihir, jiwa, bahkan pasukannya sendiri ketika lapar atau marah. Jamuan bentengnya mengubah orang yang menyerah pada makanan menjadi pelayan tanpa akal, menjadikan rasa lapar sebagai pintu menuju kehilangan diri.

## Bentuk

Tubuhnya merupakan campuran lalat raksasa dan babi hutan bermata banyak. Perut transparan memperlihatkan jiwa yang dicerna perlahan, sedangkan mulutnya dipenuhi tentakel lintah untuk menyerap sihir. Sayap serangga yang kotor tidak cukup mengangkat seluruh bobotnya, tetapi terus bergetar dan menyebarkan dengung. Kaki besar berakhir pada kuku tebal; lipatan tubuh dipenuhi mulut kecil yang membuka ketika makanan mendekat.

## Kepribadian dan Sikap

Beelzebub rakus, mudah bosan, dan menilai segala sesuatu berdasarkan apakah dapat dimakan atau diserap. Ia tidak menghargai kesetiaan bawahan karena menganggap mereka cadangan santapan. Kelicikannya muncul melalui jamuan palsu: ia memahami bahwa korban yang lapar akan membenarkan keputusan yang sebelumnya mereka tolak. Ia menjadi agresif ketika sesuatu direbut dari hadapannya, tetapi dapat menunda serangan bila ditawari sumber energi yang lebih besar.

## Kedudukan dan Benteng

Fortress of Gluttony adalah rumah jagal raksasa dengan dinding daging berdenyut, sungai empedu hitam, dan Dapur Perut Bumi. Beelzebub bersemayam di balik meja jamuan ilusi yang menguji rasa lapar pengunjung. Lokasi ini sesuai sebutan Dapur Darah dalam data lama. Benteng dipahami dalam era sebelum peradaban Raksamala dihancurkan Hector.

## Kisah - Jamuan yang Tidak Disentuh

Seorang tawanan dilemparkan ke ruang jamuan setelah berhari-hari tanpa makanan. Beelzebub menunggu di balik meja, membiarkan aroma hidangan memenuhi ruangan. Ia tidak mengancam; ia hanya menyuruh korban memilih satu suapan.

Tawanan itu melihat Jenggala yang telah berubah merangkak di bawah meja dan menyadari harga jamuan tersebut. Ia membalik piring agar aroma tertutup kuah hitam. Beelzebub mengaum, marah bukan karena kehilangan makanan, melainkan karena rasa lapar gagal menguasai keputusan korbannya.

> Acuan: [Beelzebub](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Beelzebub.md); [Fortress of Gluttony](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Gluttony.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `65.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark/Poison` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Large, Poisonous, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **148** | **30** | **58** | **70** | **66** | **123** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `25300` *(Base 22715 + VIT×15 + STR×5)* | **DEF** | `258` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `238` *(INT×8)* | **MDF** | `210` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `931` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `196` *(Base + INT×2)* |
| **ATK** | `325` *(Formula Melee)* | **Action Speed** | `99` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `96.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `18.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `21.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `22.8%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `206.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `161.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.69%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.90%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.10%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Life Drain** | `Neutral` / Magical Attack | `14 MP` | Always (Prioritas 5.0) | `a.mat * 1.7 - b.mdf * 0.4` |
| **Abyssal Life Drain** | `Dark` / Magical Attack | `15 MP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.7 - b.mdf * 0.4` |
| **Dark Purgatory** | `Dark` / Magical Attack | `25 MP` | HP <= 50% (Prioritas 6.0) | `a.mat * 1.8 - b.mdf * 0.3` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%, Poison: 75%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Poison: 50%, Root: 75%, Stun: 40%
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
