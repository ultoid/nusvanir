---
title: Ksatria Aqua
tags:
  - Bestiary
  - Boss
---

# Ksatria Aqua

## Deskripsi

Penjaga Avalerion yang menggunakan air suci untuk merawat luka di tengah pertempuran. Kehadirannya dikenali dari aliran bening yang tetap terarah meskipun geladak berguncang. Ia menjaga agar prajurit yang terluka dapat meninggalkan garis serang; pertahanan yang dibangunnya tidak selalu berupa tembok, melainkan kesempatan bagi orang lain untuk bertahan.

## Bentuk

Sosoknya tegak dalam zirah berlapis yang memberi ruang pada bahu dan siku untuk bergerak. Kain biru pucat terikat rapat pada pinggang agar tidak terseret air, sementara pelindung lengan memiliki alur menyerupai riak. Tangan yang dibuka saat merawat luka dikelilingi air bercahaya lembut. Permukaan zirah tampak basah ketika sihir mengalir, tetapi tidak terus menetes setelah aliran berhenti. Wajahnya tetap terlihat melalui ketopong terbuka sehingga orang yang ditolong dapat mengikuti isyarat serta arah pandangannya.

## Kepribadian dan Sikap

Aqua sabar dan penuh perhatian, terutama kepada orang yang berusaha menyembunyikan rasa sakit. Ia berbicara dengan tenang, menjelaskan apa yang hendak dilakukan sebelum menyentuh luka, dan memberi kesempatan bagi orang yang ditolong untuk menenangkan diri. Kepada rekannya ia bersikap hangat, tetapi dapat menegur keras prajurit yang memaksakan diri kembali bertempur. Ia mudah merasa bertanggung jawab atas keselamatan orang lain, sehingga kadang sulit menyerahkan perawatan kepada rekannya. Dalam keadaan genting, ia berusaha tetap jujur tentang batas pertolongannya tanpa mematahkan harapan orang yang sedang bergantung kepadanya.

## Lokasi Benteng

Outpost Tirta di pesisir Avalerion menjadi tempat tugas Aqua sebagai penjaga dengan kekuatan air suci. Pos ini menghadap perairan yang bermuara ke Laut Rangkaruna dan menampung pasukan maritim dengan kapal bersayap cahaya. Dermaga, geladak kapal patroli, serta tempat penerimaan prajurit terluka menjadi lingkungan tugasnya. Catatan lama menyebut pos barat; hubungan arah tersebut dengan Tirta belum dipastikan oleh peta regional.

## Kisah — Air yang Tetap Tenang

Sebuah kapal patroli kembali ke Tirta dengan geladak licin dan seorang prajurit yang sulit berdiri. Rekannya mencoba mengangkatnya ketika gelombang menghantam lambung. Aqua meminta mereka berhenti, mengatur pegangan, lalu berlutut di antara peti yang telah diikat.

Air suci bergerak mengikuti tangannya, tidak mengikuti oleng kapal. Setelah luka cukup tertangani untuk pemindahan, ia memberi isyarat kepada pembawa tandu. Prajurit itu dibawa melewati dermaga tanpa harus memaksakan langkah. Aqua baru bangkit ketika tandu mencapai pijakan yang kokoh; baginya, pertolongan belum selesai hanya karena darah berhenti mengalir.

> Acuan: [Outpost Tirta](../../03_Region/03_Avalerion/Cities%20%26%20Town/Outpost_Tirta.md); [Senopati Prabha](../../03_Region/03_Avalerion/Faksi%20%26%20Institusi/Senopati_Prabha.md); [Avalerion](../../03_Region/03_Avalerion/Avalerion.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `49.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T4 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Holy, Water, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **36** | **6** | **14** | **28** | **28** | **26** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `1155` *(Base 585 + VIT×15 + STR×5)* | **DEF** | `57` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `51` *(Base 3 + INT×8)* | **MDF** | `48` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `222` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `51` *(Base + INT×2)* |
| **ATK** | `79` *(Formula Melee)* | **Action Speed** | `42` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `9.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `8.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `6.8%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `163.6%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `113.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.78%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.18%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.64%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Heavy Slash** | `Neutral` / Physical Attack | `10 SP` | Always (Prioritas 5.0) | `a.atk * 1.5 - b.def * 0.5 (Crit: Yes)` |
| **Tidal Surge** | `Water` / Magical Attack | `12 MP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.9 - b.mdf * 0.4 (Soaked 40%)` |
| **Shield Breaker** | `Neutral` / Physical Attack | `15 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.15 - b.def * 0.1 (Vulnerable 30%)` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Light: 50%, Lightning: 150%, Water: 75%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `260` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `195` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `80` | Mata uang resmi penjelajahan |
| **Drop 1** | `Silver` (`25%`) | Material alam / crafting |
| **Drop 2** | `Mana Crystal` (`20%`) | Komponen sekunder |
