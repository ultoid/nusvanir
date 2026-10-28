---
title: Ahool
tags:
  - Bestiary
---

# Ahool

## Deskripsi

Kelelawar purba raksasa yang membuat mulut gua terasa sempit ketika sayapnya terbentang. Ahool dikenal sebagai pembawa wabah; tempat bertengger yang ditinggalkannya tetap diperlakukan dengan waspada oleh penjelajah. Suara kepakannya dapat terdengar sebelum tubuhnya keluar dari kegelapan, tetapi gema gua menyulitkan orang memperkirakan arah kedatangannya.

## Bentuk

Tubuhnya berat pada dada dan bahu, dengan selaput sayap membentang di antara jemari yang panjang. Bulu gelap menutupi punggung serta tengkuk, sedangkan selaputnya tampak tipis dan berurat jika diterangi dari belakang. Kepala bermoncong pendek, telinga lebar, dan cakar melengkung memberinya siluet yang berbeda dari burung pemangsa. Ketika menggantung, sayap terlipat mengurung tubuh seperti mantel kusut.

## Tingkah Laku

Buas ketika memburu dan sangat defensif di tempat bertengger. Cahaya yang mendadak diarahkan ke sarangnya atau suara benturan berulang dapat memancing terjangan keluar. Ia menggunakan ruang gelap dan ketinggian untuk mendekat, lalu mundur ke langit-langit bila jalur depannya tertutup. Sifat pembawa wabah tidak berarti setiap sentuhan pasti menularkan penyakit; cara penularannya belum dijelaskan dalam lore.

## Habitat

Gua Arkananta merupakan habitat yang tercatat. Mulut gua besar, lorong tinggi, dan celah tebing di lereng luar menjadi tempat bertenggernya. Kehadirannya perlu dibedakan dari penduduk gua Butoraksa, Troliogoro, dan Rakshorien; tidak ada bukti bahwa mereka semua memelihara atau menguasai Ahool.

## Kisah — Atap yang Bergerak

Seorang pencari mineral mengira langit-langit gua Arkananta tertutup kain hitam yang ditinggalkan rombongan terdahulu. Rekannya melihat goresan cakar pada batu dan menghentikan langkahnya sebelum obor diangkat lebih tinggi.

Ketika angin bergerak dari dalam, kain itu membuka diri menjadi sepasang sayap. Mereka mundur meninggalkan karung batu di dekat pintu. Dari lereng, pencari mineral menyaksikan sesuatu yang terlalu besar untuk lorong tadi melintas di atasnya. Ia baru memahami bahwa gua tersebut tidak kosong; pemiliknya hanya sedang tidur.

> Acuan: [Threat](../../03_Region/05_Arkananta/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `16.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Ranged` | Formula serangan dasar |
| **Elemen Utama** | `Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Large, Poisonous` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | **4** | **24** | **24** | **26** | **16** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `612` *(Base 322 + VIT×15 + STR×5)* | **DEF** | `29` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `36` *(Base 4 + INT×8)* | **MDF** | `29` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `120` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `37` *(Base + INT×2)* |
| **ATK** | `53` *(Formula Ranged)* | **Action Speed** | `39` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `8.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `10.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `5.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `157.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `108.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.48%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.12%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.36%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Sonic Screech** | `Sound` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Silence 35%)` |
| **Venom Talon** | `Poison` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35 (Poison 50%)` |
| **Night Dive** | `Wind` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `a.atk * 1.85 - b.def * 0.25` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Wind: 75%
* **Resistensi Status:** Poison: 50%, Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Ahool Hide` (`40%`) | Material alam / crafting |
| **Drop 2** | `Jenggala Claw` (`25%`) | Komponen sekunder |
