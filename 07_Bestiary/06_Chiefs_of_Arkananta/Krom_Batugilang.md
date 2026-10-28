---
title: Krom Batugilang
tags:
  - Bestiary
  - Boss
---

# Krom Batugilang

## Deskripsi

Kepala Suku Butoraksa dan petarung yang menguasai pertambangan luar Arkananta. Krom Batugilang dikenal ganas di medan laga, tetapi kecerdikannya dalam barter membuatnya lebih berbahaya daripada pemimpin yang hanya mengandalkan kekuatan. Ia menilai mineral, senjata, dan pasokan berdasarkan kegunaan nyata bagi sukunya, bukan berdasarkan kemilau koin.

## Bentuk

Krom adalah Butoraksa purba berukuran sangat besar dengan kulit hijau gelap yang tertutup bekas luka. Darah monster dilukiskan pada dada, bahu, dan lengan membentuk pola spiral Akar Darah. Senjatanya berupa palu raksasa dari tulang paha Behemoth; gagangnya dibungkus kulit agar tidak terlepas saat ia melompat di antara batu. Bahu lebar dan kaki kuat membantunya menahan benturan ketika mendarat. Catatan lama menyebut gada angin puting beliung, tetapi profil tokoh menetapkan palu tulang sebagai senjata visual utamanya.

## Kepribadian dan Sikap

Krom berani, dominan, dan menikmati negosiasi yang membuat lawan mengungkap kebutuhan mereka lebih dahulu. Ia tidak menyamakan keramahan dengan kemurahan hati: setiap pertukaran harus memberi manfaat jelas bagi Butoraksa. Dalam pertempuran ia agresif serta menganggap luka sebagai bagian dari kehormatan, tetapi ia tidak membuang prajurit demi kemenangan yang tidak berguna. Orang yang meremehkannya sebagai sosok biadab mudah kehilangan posisi tawar. Ia juga menyimpan dendam terhadap Troliogoro karena sengketa batas gua, meski kebutuhan sukunya dapat memaksanya menahan permusuhan sementara.

## Kedudukan dan Wilayah

Krom memimpin Gua Garbhagiri, pusat peradaban Butoraksa yang meluas jauh ke bawah kawasan berbatu Arkananta barat. Suku di bawahnya menguasai area pertambangan luar dan memperdagangkan bijih kasar dengan pihak yang membawa senjata atau pasokan berguna. Jembatan Tebing Arkananta pada lokasi Bestiary lama menjadi jalur patroli serta titik pengawasan menuju tambang, bukan pusat pemukiman. Ornamen tulang, daging bakar, dan kulit samak memenuhi wilayah kekuasaannya.

## Kisah — Harga Sebuah Mata Palu

Seorang penempa dari luar membawa mata palu baja dan meminta bijih Arkananta sebagai gantinya. Krom memeriksa logam itu, lalu menjatuhkannya ke batu sampai salah satu sisi retak. Sang penempa memprotes bahwa ujian tersebut merusak barang dagangannya.

Krom menjawab bahwa alat yang patah di gua dapat membunuh penambang yang menggunakannya. Ia menawarkan bijih lebih sedikit untuk baja yang tersisa. Sang penempa meminta kesempatan memperbaiki mata palu di tempat dan menunjukkan cara tempa yang lebih kuat. Krom menerima usulan itu. Saat pertukaran selesai, keduanya mendapat lebih dari benda: Butoraksa memperoleh pengetahuan, dan sang penempa pulang memahami bahwa kepala suku itu menguji nilai melalui keselamatan kaumnya.

> Acuan: [Krom Batugilang](../../05_Karakter%20%26%20Tokoh%20Penting/05_Arkananta/Krom%20Batugilang.md); [Butoraksa (Orc)](../../04_Ras/02_Wuru%20Loka/Butoraksa_%28Orc%29.md); [Gua Garbhagiri](../../03_Region/05_Arkananta/Cities%20%26%20Town/Gua%20Garbhagiri.md); [Religion](../../03_Region/05_Arkananta/Religion.md); [Economy](../../03_Region/05_Arkananta/Economy.md); [Pegunungan Arkananta](../../03_Region/05_Arkananta/Arkananta.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `58.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T5 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth/Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Water` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Earth, Wind, Large` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **60** | **11** | **24** | **38** | **38** | **45** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `5460` *(Base 4485 + VIT×15 + STR×5)* | **DEF** | `97` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `86` *(INT×8)* | **MDF** | `81` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `365` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `84` *(Base + INT×2)* |
| **ATK** | `132` *(Formula Melee)* | **Action Speed** | `57` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `11.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `11.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `10.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `172.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `122.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.35%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.33%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.42%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Heavy Impact** | `Neutral` / Physical Attack | `18 SP` | Always (Prioritas 5.0) | `a.atk * 1.7 - b.def * 0.3 (Crit: Yes)` |
| **Tectonic Tremor** | `Earth` / Magical Attack | `20 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.3 - b.mdef * 0.3` |
| **Gale Force** | `Wind` / Magical Attack | `20 SP` | HP <= 50% (Prioritas 6.0) | `a.mat * 1.3 - b.mdef * 0.3` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Water: 150%, Wind: 75%
* **Resistensi Status:** Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1540` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1155` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `455` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Stone` (`25%`) | Material alam / crafting |
| **Drop 2** | `Adamantine` (`12%`) | Komponen sekunder |
| **Drop 3** | `Arkananta Horn` (`25%`) | Rampasan langka |
| **Boss / Unique Drop** | `Krom Stonewind Crown / Stonewind Battle Garb / Stonewind Boots` (`5%`) | Rampasan unik / piala bos |
