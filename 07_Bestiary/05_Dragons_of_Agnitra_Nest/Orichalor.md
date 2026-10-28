---
title: Orichalor
tags:
  - Bestiary
  - Boss
---

# Orichalor

## Deskripsi

Naga penjaga Orichalcum Nest dengan sisik merah-emas yang menghantarkan sihir. Energi mengalir di sepanjang tubuhnya sebelum terkumpul menjadi berkas cahaya suci yang amat panas. Kekuatan Orichalor mencerminkan keunggulan Orichalcum sebagai konduktor: kemampuan menyalurkan tenaga dengan tepat sama pentingnya dengan besarnya tenaga itu sendiri.

## Bentuk

Sisik Orichalcum menutupi leher panjang, dada, dan pangkal sayap. Permukaannya tampak emas saat beristirahat, lalu memancarkan warna merah dari sela lempeng ketika sihir mengalir. Tanduk melengkung membingkai kepala seperti cabang penghantar yang mengarahkan pendar ke rahang. Sayap lebar berselaput pucat memperlihatkan jalur cahaya yang berdenyut mengikuti pemusatan tenaga. Sebelum semburan dilepaskan, seluruh aliran itu mengerucut hingga bayangan bebatuan menjadi tajam. Tubuhnya lebih menonjolkan aliran energi daripada ketebalan zirah.

## Kepribadian dan Sikap

Orichalor teliti, terpelajar, dan menghormati orang yang memahami apa yang mereka gunakan. Ia senang berdiskusi tentang sihir, terutama dengan tamu yang bersedia mengakui kesalahan perhitungannya. Harga dirinya kadang membuat koreksi sulit diterima, tetapi alasan yang kuat dapat mengubah pendiriannya. Ia menilai penantang melalui penguasaan serta kendali sihir, bukan keberanian menerima luka. Kecerobohan yang membahayakan orang lain membuatnya menghentikan ujian: baginya, pemegang Orichalcum harus mampu mengarahkan kekuatan tanpa diperbudak keinginan memamerkannya.

## Lokasi Nest

Orichalcum Nest berada di selatan kawah utama Mahasvara, di antara celah gas magis, uap kemerahan, dan percikan emas. Orichalor berdiam dekat teras tempat para tetua bermeditasi serta merapal penyegelan. Nest ini mewakili daya hantar sihir Orichalcum, bahan berharga bagi tongkat dan artefak pusaka. Penantang diuji melalui duel sihir sebelum layak menerima intisarinya. Penempatan ini menggantikan lokasi puncak timur pada catatan lama.

## Kisah — Cahaya yang Ditahan

Seorang pengunjung yang memperoleh pengawalan tiba di teras Orichalcum Nest dan meminta melihat semburan sang naga. Ia menyebutnya bukti keagungan, seolah permintaan itu merupakan penghormatan. Orichalor mengarahkan pandangan ke jalur di bawah teras.

Di sana, rombongan lain masih berjalan melintasi batu. Sang pengunjung akhirnya memahami apa yang tidak ia perhitungkan. Ia menarik permintaannya dan menunggu sampai seluruh rombongan mencapai perlindungan. Orichalor tetap tidak menyemburkan cahaya. Percakapan mereka baru dimulai setelah tamunya berhenti menganggap kekuatan penjaga sebagai pertunjukan yang dapat diminta sesuka hati.

> Acuan: [Orichalcum Nest](../../03_Region/04_Agnitra/Cities%20%26%20Town/Orichalcum%20Nest.md); [Nagarasven](../../04_Ras/02_Wuru%20Loka/Nagarasven_%28Naga%29.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `54.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Light/Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Dark` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Large, Draconic, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **87** | **21** | **36** | **58** | **48** | **106** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `14125` *(Base 12100 + VIT×15 + STR×5)* | **DEF** | `202` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `167` *(INT×8)* | **MDF** | `166` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `724` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `140` *(Base + INT×2)* |
| **ATK** | `192` *(Formula Melee)* | **Action Speed** | `72` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `14.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `16.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `19.3%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `183.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `153.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.18%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.63%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.04%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Golden Wing** | `10 Holy` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Solar Scale Guard** | `02 Fire` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Radiant Dragon Breath** | `02 Fire` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Radiant Dragon Breath, All Foes
Turn % 3 == 0: Solar Scale Guard, Highest ATK
HP% <= 50%: Radiant Dragon Breath, Lowest HP%
Always: Golden Wing, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Fire: 75%, Light: 75%
* **Resistensi Status:** Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `3920` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `2940` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1050` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Golden Scale` (`25%`) | Material alam / crafting |
| **Drop 2** | `Astral Crystal` (`15%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`10%`) | Rampasan langka |
| **Boss / Unique Drop** | `Goldenscale Crown / Goldenscale Aegisplate / Goldenscale Greaves` (`5%`) | Rampasan unik / piala bos |
