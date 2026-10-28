---
title: Thalantira Gargoyle
tags:
  - Bestiary
---

# Thalantira Gargoyle

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Patung batu bersayap yang dapat meninggalkan tempat bertenggernya dan bergerak sebagai ancaman hidup. Permukaan keras membuat tubuhnya tampak tidak terganggu oleh benturan ringan. Di Thalantira, membedakan hiasan batu dari sesuatu yang sedang mengawasi menjadi sulit ketika sayap terlipat mengikuti bentuk tebing.

## Bentuk

Tubuhnya tegap dan berat, dengan lengan bercakar, kepala berahang menonjol, serta kaki yang menekuk untuk mencengkeram tepian. Sepasang sayap batu terlipat bertingkat di belakang bahu seperti bidang pahatan. Retakan tipis dan bercak mineral membedakan permukaannya dari makhluk bersisik. Mata terletak dalam cekungan yang hampir selalu gelap. Saat bergerak, debu jatuh dari lipatan sayap, tetapi tubuh tidak pecah mengikuti garis retak yang terlihat. Bentuk pahatan itu diproyeksikan langsung oleh Uru dan tidak memerlukan pemahat fisik.

## Tingkah Laku

Diam untuk mengawasi, lalu agresif ketika ruang yang dijaganya dimasuki. Ia dapat merendahkan kepala, membuka cakar, dan membentangkan sayap sebelum meninggalkan batu. Setelah gangguan menjauh, Gargoyle kembali mencari ketinggian alih-alih terus mengejar tanpa arah. Catatan lama tentang kulit kebal menyatakan ketangguhan, tanpa menjelaskan bahwa semua jenis kekuatan pasti gagal terhadapnya.

## Habitat

Udara Thalantira adalah lokasi sumber. Tepian batu tinggi di dekat jalur kuil menjadi tempat bertenggernya; keberadaan arsitektur kuil mengikuti Prologue. Penempatan ini tidak menambahkan kota yang pernah dihuni atau menganggap semua tebing adalah reruntuhan. Gargoyle tidak disebut khusus dalam daftar makhluk yang tampil saat pengungkapan pulau.

## Kisah — Patung yang Berpindah

Hujan menuruni dinding batu dan membasahi sosok bersayap di tepian atas. Seekor hewan kecil mencari tempat kering di bawahnya. Ketika cakar bergerak, hewan itu berlari meninggalkan ceruk tanpa menoleh.

Sayap batu terbuka, menyapu air dalam garis lebar. Gargoyle melayang ke tonjolan lain yang menghadap jalur masuk, lalu membeku kembali dengan kepala menunduk. Di tempat semula tinggal bekas kering berbentuk kaki. Hujan perlahan menghapusnya, sampai tak ada tanda bahwa penjaga itu pernah memilih tempat berbeda.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [07 Tiga Kuil Penjaga](../../08_Story/02_Prologue/07_Tiga_Kuil_Penjaga.md); [08 Ujian Para Pelindung](../../08_Story/02_Prologue/08_Ujian_Para_Pelindung.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `44.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Construct` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Bruiser` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **90** | **18** | **36** | **53** | **51** | **76** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4370` *(Base 2780 + VIT×15 + STR×5)* | **DEF** | `159` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `143` *(INT×8)* | **MDF** | `129` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `580` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `119` *(Base + INT×2)* |
| **ATK** | `198` *(Formula Melee)* | **Action Speed** | `77` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `14.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `15.5%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `15.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `184.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `138.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.28%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.54%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.56%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Voidstone Claw** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Curse 30%)` |
| **Wing Guard** | `Void` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Gargoyle Dive** | `Void` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Light: 150%, Void: 50%
* **Resistensi Status:** Bleed: 0%, Curse: 50%, Paralyze: 50%, Poison: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1120` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `840` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `300` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
