---
title: Mithralis
tags:
  - Bestiary
  - Boss
---

# Mithralis

## Deskripsi

Naga penjaga Mithril Nest dengan sisik ringan yang tetap kuat menahan tekanan penerbangan. Ia menguasai badai api dan berbelok cepat di antara tebing Mahasvara. Kilau perak-kebiruan sayapnya mencerminkan Mithril, material yang memungkinkan perlindungan kuat tanpa beban berat yang menghambat gerak.

## Bentuk

Tubuhnya ramping, dengan leher lentur serta ekor panjang untuk menjaga keseimbangan. Lempeng Mithril tipis saling menutup pada dada, bahu, dan punggung, mengikuti gerakan tanpa membuat siluetnya berat. Bagian penyangga sayap berkilau perak-kebiruan; selaput di antaranya tampak kemerahan saat magma menyinari dari bawah. Cakar belakang terlipat rapat ketika ia menukik. Ringannya sisik memungkinkan perubahan arah tajam, sementara kekuatannya melindungi tubuh saat menghadapi angin keras. Bara mengikuti pusaran udara ketika badai api dikerahkan.

## Kepribadian dan Sikap

Mithralis ramah, kompetitif, dan bangga pada keterampilan yang terus diasah. Ia menyukai adu kecepatan, tetapi menilai ketepatan manuver serta kemampuan kembali dengan selamat sama tinggi dengan kemenangan. Kadang ia mengira naga muda mampu mengikuti kecepatannya; ketika keliru, ia bersedia mengakui tanggung jawab dan mengulang latihan. Ujiannya menuntut penantang menguasai gerak, bukan sekadar bertahan dihantam. Baginya, pemegang Mithril harus memahami kebebasan bergerak sebagai kesempatan bertindak tepat, bukan alasan mengabaikan orang yang tertinggal.

## Lokasi Nest

Mithril Nest berada di lereng timur Mahasvara yang curam, terbuka, dan berangin. Mithralis bertengger pada tebing berlapis bijih perak-kebiruan serta mengawasi latihan naga muda. Nest ini mewakili kekuatan ringan Mithril dan pertahanan udara Agnitra; pusaka atau zirahnya menjadi penghargaan bagi penantang yang lulus ujian tanding. Langit kawah tetap menjadi wilayah jelajah Mithralis, sedangkan sarang utamanya berada di Puncak Angin Perak.

## Kisah — Putaran yang Dibatalkan

Mithralis memimpin penerbangan melintasi sisi kawah ketika abu naik lebih tinggi dari biasanya. Seekor naga muda mencoba mengikuti putarannya, lalu kehilangan jarak dan mulai turun terlalu dekat dengan arus panas.

Mithralis membatalkan lintasan, berbalik lebar, dan mengarahkan penerbangan menuju tempat mendarat. Naga muda itu meminta maaf karena memperlambat perjalanan. Sang penjaga mengakui bahwa ia telah memilih kecepatan tanpa memeriksa kemampuan pengikutnya. Mereka menunggu abu mereda sebelum mencoba lagi. Kali ini Mithralis terus menoleh, memastikan keberhasilan perjalanan dihitung dari siapa yang tiba bersama, bukan siapa yang paling dahulu mencapai ujungnya.

> Acuan: [Mithril Nest](../../03_Region/04_Agnitra/Cities%20%26%20Town/Mithril%20Nest.md); [Nagarasven](../../04_Ras/02_Wuru%20Loka/Nagarasven_%28Naga%29.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `56.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Sniper` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Ranged` | Formula serangan dasar |
| **Elemen Utama** | `Wind/Light` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Large, Draconic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **46** | **24** | **110** | **60** | **66** | **82** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `10170` *(Base 8710 + VIT×15 + STR×5)* | **DEF** | `146` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `188` *(INT×8)* | **MDF** | `144` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `522` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `168` *(Base + INT×2)* |
| **ATK** | `243` *(Formula Ranged)* | **Action Speed** | `99` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `100.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `18.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `31.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `17.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `185.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `141.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.46%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.72%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.28%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Silver Feather Lance** | `Wind` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Gale Wing** | `Wind` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Skyline Barrage** | `Wind` / Certain Hit | `0 SP` | HP <= 50% (Prioritas 6.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Light: 75%, Wind: 75%
* **Resistensi Status:** Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `3920` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `2940` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1050` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Storm Feather` (`25%`) | Material alam / crafting |
| **Drop 2** | `Astral Crystal` (`15%`) | Komponen sekunder |
| **Drop 3** | `Spirit Thread` (`10%`) | Rampasan langka |
| **Boss / Unique Drop** | `Silverwing Visor / Silverwing Mantle / Silverwing Boots` (`5%`) | Rampasan unik / piala bos |
