---
title: Hydra
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Hydra

## Deskripsi

Hydra Rangkaruna berkepala delapan adalah ancaman palung yang mampu menghancurkan galleon perang. Napas beracun dan gigitannya melumerkan besi. Davy Jones dikenal pernah menaklukkan salah satunya, membuktikan makhluk ini dapat dikalahkan tanpa menyamakannya dengan Hydra Jurang, penjaga berakal di Thalantira.

## Bentuk

Tubuhnya menyerupai ular laut tebal dengan delapan leher yang tumbuh dari bahu bersisik. Setiap kepala memiliki rahang panjang, insang berlapis, dan mata yang mengawasi arah berbeda. Sirip punggung membantu tubuh utama bertahan di arus palung. Warna sisiknya biru gelap kehijauan; cairan racun meninggalkan noda pada gigi serta air di sekitar mulut.

## Tingkah Laku

Buas dan teritorial. Kepala-kepalanya dapat mengawasi kapal, mangsa, dan ancaman lain sekaligus, lalu menyerang dari beberapa sudut. Jika satu kepala teralihkan, kepala lain tetap menjaga tubuh utama. Ia mengejar sesuatu yang memasuki wilayah palung, tetapi tidak dinyatakan mampu berbicara atau berunding seperti Hydra Jurang.

## Habitat

Palung Kematian pada jalur menuju Pulau Raksamala. Kedalaman, arus naik, dan dinding palung memberi ruang bagi tubuh utamanya untuk tersembunyi sebelum kepala mencapai permukaan.

## Kisah - Delapan Bayangan di Bawah Lunas

Delapan bayangan memanjang muncul di bawah kapal pemburu. Awak mengira mereka melihat kawanan ular, sampai seluruh leher berbelok mengikuti satu tubuh. Kapal membuang muatan berbau tajam ke arah arus lain. Beberapa kepala mengejarnya, memberi waktu layar menangkap angin. Hydra kembali ke palung setelah kapal keluar dari batas wilayahnya.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [01 Bisikan Pulau Terkutuk](../../08_Story/02_Prologue/01_Bisikan_Pulau_Terkutuk.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `72.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Large, Regenerator` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **106** | **21** | **42** | **58** | **54** | **89** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `12995` *(Base 11130 + VIT×15 + STR×5)* | **DEF** | `186` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `167` *(INT×8)* | **MDF** | `151` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `677` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `140` *(Base + INT×2)* |
| **ATK** | `233` *(Formula Melee)* | **Action Speed** | `81` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `15.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `17.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `17.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `190.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `144.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.67%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.63%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.94%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Hydra Bite** | `Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Regenerate Heads** | `Water` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.2 + 30 (HP Regen 3 turns)` |
| **Many-Headed Assault** | `Water` / Physical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `3920` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `2940` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1050` | Mata uang resmi penjelajahan |
| **Drop 1** | `Primordial Crystal` (`18%`) | Material alam / crafting |
| **Drop 2** | `Spirit Stone` (`18%`) | Komponen sekunder |
| **Drop 3** | `Beast Fang` (`30%`) | Rampasan langka |
