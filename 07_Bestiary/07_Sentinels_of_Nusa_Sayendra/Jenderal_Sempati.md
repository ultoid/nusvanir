---
title: Jenderal Sempati
tags:
  - Bestiary
  - Boss
---

# Jenderal Sempati

## Deskripsi

Saudara Jatayu dan Sentinel utara dengan bulu merah menyala yang menyebarkan bara api. Sempati menjadi kekuatan penahan ketika ancaman berusaha memecah formasi udara. Panas yang mengiringi kepakannya menandai batas yang tidak boleh dilewati musuh, sementara kedudukannya sebagai saudara sang komandan tidak menggantikan tanggung jawab pribadi terhadap pasukannya.

## Bentuk

Sempati bertubuh besar dengan bulu merah-tembaga pada dada dan sayap. Ujung bulu berubah jingga ketika panas meningkat, seolah bara bergerak mengikuti bentangan sayap. Paruhnya tebal, cakar keemasan gelap, dan pelindung bahu menyisakan ruang agar sendi sayap dapat bergerak penuh. Bekas gosong tersebar pada bulu luar akibat latihan di tengah api yang ia ciptakan sendiri. Ia tidak terus menyala; bara muncul ketika tenaga dikumpulkan dan padam perlahan setelah pendaratan.

## Kepribadian dan Sikap

Sempati hangat kepada pasukan yang dikenalnya, terbuka menyampaikan ketidaksetujuan, dan mudah terpancing bila keselamatan keluarganya dipertaruhkan. Ia sering menjadi suara yang lebih langsung dibanding Jatayu. Meski demikian, ia tidak ingin dinilai hanya sebagai saudara komandan dan bekerja keras membangun kepercayaan melalui tugas. Amarahnya dapat memperbesar kekuatan sekaligus mempersempit pertimbangan, sehingga ia mengandalkan perwira lain untuk mengingatkan batas pengejaran. Ia menghormati keberanian yang dipakai melindungi, bukan keberanian yang hanya mencari nama.

## Kedudukan dan Kuil Penjagaan

Kuil Angin Utara Sayendra menjadi pos penjagaan Sempati. Wilayah ini mengawasi arus dingin dan jalur awan yang dapat menyembunyikan pendekatan musuh. Pendar baranya membantu menjaga penanda penerbangan ketika kabut menutup pandangan. Hubungannya dengan Puncak Emas Swargaloka bersifat militer dan spiritual; rincian bentuk Kuil Angin Utara belum ditulis dalam dokumen wilayah.

## Kisah - Bara untuk Jalan Pulang

Kabut utara menelan penanda yang biasa digunakan patroli untuk kembali. Sempati ingin mengejar kawanan yang baru saja dipukul mundur, tetapi mendengar panggilan dari dua prajurit muda yang kehilangan arah. Ia menghentikan pengejaran dan membentangkan sayap.

Bara bergerak dari satu ujung bulu ke ujung lain, membentuk garis merah di dalam kabut. Kedua prajurit mengikuti cahaya itu menuju kuil. Musuh lolos dari jangkauan malam tersebut, namun seluruh patroli pulang. Ketika seorang perwira meminta maaf karena sasaran terlepas, Sempati menjawab bahwa kemenangan yang meninggalkan penjaganya di langit bukan kemenangan yang layak dibawa pulang.

> Acuan: [Nusa Sayendra](../../03_Region/07_Nusa%20Sayendra/Nusa_Sayendra.md); [Garuda](../../04_Ras/02_Wuru%20Loka/Garuda.md); [Puncak Emas Swargaloka](../../03_Region/07_Nusa%20Sayendra/Cities%20%26%20Town/Puncak%20Emas%20Swargaloka.md); [Pasukan Ksatria Sayap Garuda](../../03_Region/07_Nusa%20Sayendra/Faksi%20%26%20Institusi/Pasukan%20Ksatria%20Sayap%20Garuda.md); [Sumpah Penjaga Langit](../../03_Region/07_Nusa%20Sayendra/Agama%20%26%20Kepercayaan/Sumpah%20Penjaga%20Langit.md); [Threat](../../03_Region/07_Nusa%20Sayendra/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `62.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Garuda` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Holy, Wind` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **109** | **25** | **42** | **66** | **75** | **62** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `13950` *(Base 12475 + VIT×15 + STR×5)* | **DEF** | `148` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `202` *(Base 2 + INT×8)* | **MDF** | `146` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `548` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `170` *(Base + INT×2)* |
| **ATK** | `239` *(Formula Melee)* | **Action Speed** | `113` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.3%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `18.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `191.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `131.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.86%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.75%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.24%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Shadow Lunge** | `11 Dark` / Physical Attack | `14 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 2.1 - b.def * 0.3)` |
| **Phantom Slash** | `01 Neutral` / Physical Attack | `30 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 3.0 - b.def * 0.08)` |
| **Shadow Dance : Omnislash** | `11 Dark` / Physical Attack | `50 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.atk * 0.8 - b.def * 0.03 per hit (6 hits) (Shadow Mark))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Shadow Dance : Omnislash, All Foes
Turn % 3 == 0: Phantom Slash, Highest ATK
HP% <= 50%: Shadow Dance : Omnislash, Lowest HP%
Always: Shadow Lunge, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Earth: 150%, Light: 50%, Wind: 50%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5600` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4200` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1500` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Storm Feather` (`35%`) | Material alam / crafting |
| **Drop 2** | `Spirit Thread` (`20%`) | Komponen sekunder |
| **Drop 3** | `Astral Crystal` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Sempati Skyguard / Golden Sentinel Boots` (`5%`) | Rampasan unik / piala bos |
