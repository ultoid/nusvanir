---
title: Homunculus
tags:
  - Bestiary
---

# Homunculus

## Deskripsi

Boneka kuno parasit yang juga disebut Jenglot. Homunculus dapat disangka benda temuan sampai ia menempel pada makhluk hidup dan perlahan mengisap daya hidupnya. Bahayanya terletak pada kedekatan: tubuh kecil membuatnya mudah dibawa keluar dari reruntuhan oleh orang yang merasa telah menemukan pusaka.

## Bentuk

Wujudnya kecil dan kaku, menyerupai figur yang mengering bersama usia. Rambut panjang tidak sebanding dengan ukuran kepala, jemari tipis melengkung ke dalam, dan kuku tampak menonjol pada tangan serta kaki. Permukaan tubuh menyerupai kulit tua yang berkerut, bukan batu pahatan. Mata yang nyaris tertutup serta mulut sempit menyulitkan orang membedakannya dari benda mati. Tidak ditetapkan siapa pembuatnya atau bahan ritual yang melahirkannya.

## Tingkah Laku

Tidak menunjukkan keganasan melalui serbuan terbuka. Ia menunggu kontak atau kesempatan menempel, sehingga ketenangannya justru menipu. Korban yang menganggapnya jimat dapat terlambat menyadari bahwa rasa lemah datang setelah benda itu dibawa. Jika ditemukan pada tubuh atau barang bawaan, bentuknya yang kecil tidak boleh dianggap bukti ia aman. Jalur pemurnian dan efek parasit spesifik masih memerlukan sumber tersendiri.

## Habitat

Reruntuhan kuil merupakan lokasi lama. Kompleks kuno di sekitar Valkindra menjadi tempat kemunculannya karena lore wilayah tersebut sudah memuat penyelidikan sihir terlarang dan reruntuhan. Ini bukan pernyataan bahwa kuil aktif atau seluruh pemujaan di Mandala menciptakan Homunculus.

## Kisah — Temuan dalam Lipatan Kain

Seorang pembantu ekspedisi dari Valkindra menyelipkan figur kecil ke dalam kain, berharap menjualnya setelah pulang. Sepanjang perjalanan ia terus meminta rombongan berhenti, padahal bawaannya paling ringan.

Ketika kainnya dibuka untuk mencari perbekalan, figur itu tidak lagi berada di tempat semula. Jari-jari keringnya mencengkeram bagian dalam lengan baju. Pemimpin ekspedisi menghentikan perjalanan menuju pasar dan membawa temuan itu beserta pembawanya untuk diperiksa. Tidak seorang pun menyebutnya cendera mata lagi.

> Acuan: [Valkindra](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Valkindra.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `22.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Construct` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Corrupted, Lifesteal` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **10** | **3** | **4** | **18** | **15** | **9** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `209` *(Base 24 + VIT×15 + STR×5)* | **DEF** | `19` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `24` *(INT×8)* | **MDF** | `20` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `85` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `28` *(Base + INT×2)* |
| **ATK** | `22` *(Formula Melee)* | **Action Speed** | `22` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `3.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `104.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.27%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.09%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.78%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Life Siphon** | `11 Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45)` |
| **Malformed Strike** | `11 Dark` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Unstable Burst** | `11 Dark` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Unstable Burst, Lowest HP%
Turn 2+: Malformed Strike, Random
Always: Life Siphon, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%
* **Resistensi Status:** Bleed: 0%, Paralyze: 50%, Poison: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `40` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `30` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `15` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`35%`) | Material alam / crafting |
| **Drop 2** | `Wisp Core` (`15%`) | Komponen sekunder |
