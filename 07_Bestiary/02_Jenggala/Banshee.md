---
title: Banshee
tags:
  - Bestiary
---

# Banshee

## Deskripsi

Hantu wanita yang dikenal pula dengan sebutan Kuntilanak. Jerit Banshee bukan sekadar suara untuk menakut-nakuti: getarannya dapat mengguncang pertahanan dan memecah ketenangan orang yang menghadapinya. Sosoknya sering lebih dahulu dikenali dari arah tangisan yang tidak sesuai dengan tempat tubuhnya terlihat.

## Bentuk

Wujudnya menyerupai perempuan berambut panjang, dengan wajah pucat yang sebagian tertutup helaian gelap. Kain lusuh menggantung dari bahu dan bergerak seolah tertarik angin yang tidak menyentuh daun di sekitarnya. Saat menjerit, rahang terbuka lebar dan garis wajah yang semula samar menjadi tajam. Rupa ini tidak menambahkan sayap atau tubuh burung; ancamannya tetap terletak pada manifestasi hantu dan kekuatan suara.

## Tingkah Laku

Berbahaya dan tidak dapat dinilai seperti satwa yang sedang mencari makan. Ia mengawasi pendatang dari dekat pohon tempat kemunculannya sebelum mengeluarkan tangisan. Orang yang terus mendekat dapat memancing jeritan yang lebih keras. Tindakan tampak mengundang atau menyerupai kesedihan tidak membuktikan bahwa ia meminta pertolongan, maupun bahwa setiap Banshee berasal dari kisah kematian yang sama.

## Habitat

Pohon beringin raksasa adalah lokasi sumber tanpa region pasti. Tepian hutan tua di sekitar Hermindar menjadi salah satu tempat kemunculannya. Tidak semua pohon beringin ditetapkan berhantu, dan bentuk roh tidak otomatis memastikan bahwa Banshee termasuk Dhemit.

## Kisah — Tangis di Balik Batang

Seorang pembawa kayu dari luar Hermindar mendengar perempuan menangis di balik pohon besar. Ia meletakkan bebannya, tetapi orang yang berjalan bersamanya justru memperhatikan daun: tidak satu pun bergerak meskipun kain putih di dekat batang berkibar.

Mereka mundur. Tangisan itu berubah menjadi jeritan, membuat ikatan pada tumpukan kayu bergetar. Setelah mencapai jalan terbuka, pembawa kayu menyadari bahwa sejak awal tidak pernah terdengar suara napas di sela tangisan tersebut.

> Acuan: [Hermindar](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Hermindar.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `17.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Undead` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Sound` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Iron` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Caster, Flying, Undead, Sonic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **18** | **6** | **6** | **26** | **21** | **16** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `646` *(Base 316 + VIT×15 + STR×5)* | **DEF** | `33` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `48` *(INT×8)* | **MDF** | `35` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `136` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `50` *(Base + INT×2)* |
| **ATK** | `39` *(Formula Magic)* | **Action Speed** | `32` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `7.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `6.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `5.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.6%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `108.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.48%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.18%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.16%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Wailing Cry** | `Sound` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `a.mat * 1.15 - b.mdf * 0.45` |
| **Soul Shriek** | `Sound` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.45 - b.mdf * 0.35 (Silence 35%)` |
| **Deathly Requiem** | `Dark` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.mat * 1.85 - b.mdf * 0.25 (Silence 35%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Iron: 150%, Light: 150%, Sound: 75%
* **Resistensi Status:** Bleed: 0%, Poison: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Wight Shroud` (`30%`) | Material alam / crafting |
| **Drop 2** | `Spirit Dust` (`35%`) | Komponen sekunder |
