---
title: Sapi Perah Mandala
tags:
  - Bestiary
---

# Sapi Perah Mandala

## Deskripsi

Ternak penghasil susu yang mengenali rutinitas penggembala dan cenderung tenang di lingkungan yang dikenalnya. Sapi Perah Mandala bukan hewan perang, tetapi tubuh besarnya dapat mencederai orang ketika panik. Kawanan yang berhenti melangkah serentak biasanya sedang memperhatikan sesuatu yang belum disadari penggembalanya.

## Bentuk

Tubuhnya besar dengan perut membulat, punggung lebar, dan kaki berkuku belah. Bulu krem hingga cokelat muda dengan bercak lebih gelap menjaga kesan ternak dataran subur Mandala. Telinganya lebar dan bergerak mengikuti suara, sementara ekor panjang berumbai mengusir serangga. Tanduk pendek yang melengkung keluar dapat membedakan sebagian individu. Pada betina dewasa, ambing terlihat jelas di bawah bagian belakang perut.

## Tingkah Laku

Jinak dalam pemeliharaan, suka bergerombol, dan tidak menyerang tanpa pemicu. Teriakan, gerakan mendadak, atau bau pemangsa dapat membuat kawanan berhimpitan lalu berlari. Induk lebih mudah marah ketika orang asing mendekati anaknya. Ia dapat menggelengkan kepala, menghentakkan kaki, atau mendorong dengan dahi sebelum benar-benar menyeruduk; penanganan yang tenang lebih efektif daripada pukulan.

## Habitat

Padang rumput dan peternakan Mandala, terutama kawasan agraris sekitar Arthiska yang memiliki air serta jaringan pasokan pangan. Padang penggembalaan terpisah dari terasering padi agar kawanan tidak merusak tanaman.

## Kisah — Ember yang Tidak Terisi

Seorang pembantu peternak di dekat Arthiska mengira sapi yang terus menghindarinya sedang membangkang. Ia mengejar dengan ember sampai seluruh kawanan gelisah. Pemilik kandang datang, meletakkan ember, dan membuka pembatas kecil di ujung halaman.

Seekor anak sapi berlari mendekati induknya. Setelah keduanya tenang, pemerahan baru dapat dilakukan. Hari itu sang pembantu belajar bahwa persediaan pangan kota bergantung pada hal yang tidak tercatat dalam hitungan karung: mengenali apa yang membuat hewan merasa aman.

> Acuan pertanian: [Arthiska](<../../03_Region/01_Mandala Kingdom/Cities & Town/Arthiska.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `13.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Neutral` | Menerima pengganda kerusakan 2.0x |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **8** | **1** | **2** | **10** | **8** | **7** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `150` *(Base 5 + VIT×15 + STR×5)* | **DEF** | `15` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `8` *(INT×8)* | **MDF** | `11` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `71` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `10` *(Base + INT×2)* |
| **ATK** | `17` *(Formula Melee)* | **Action Speed** | `12` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `4.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `152.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `103.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.21%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.46%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Headbutt** | `Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Heavy Stomp** | `Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Stampede** | `Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Neutral 100%, Neutral 200% (Weak)
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`20%`) | Material alam / crafting |
