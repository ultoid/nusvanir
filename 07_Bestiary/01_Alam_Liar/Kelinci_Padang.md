---
title: Kelinci Padang
tags:
  - Bestiary
---

# Kelinci Padang

## Deskripsi

Hewan pemakan tumbuhan yang mengandalkan telinga dan kaki belakangnya untuk bertahan hidup. Kelinci Padang dapat berhenti begitu mendadak hingga hampir menyatu dengan tanah, lalu melesat ketika ancaman terlalu dekat. Keberaniannya mendekati kebun tidak berarti ia jinak atau bersedia disentuh.

## Bentuk

Tubuhnya membulat dengan kaki belakang lebih panjang dan kuat daripada kaki depan. Telinga tegak dapat berputar mengikuti suara, sementara hidung kecilnya bergerak ketika mengendus. Bulu cokelat tanah dengan bagian bawah lebih pucat sesuai dengan padang dan kebun kering. Ekornya pendek, tampak seperti gumpalan bulu ketika ia berbalik. Ia tidak memiliki taring besar atau rupa pemburu meskipun ia dapat menggigit untuk membela diri.

## Tingkah Laku

Pasif terhadap manusia dan cenderung melarikan diri. Ia keluar mencari pucuk serta rumput ketika suasana tenang, lalu bersembunyi jika mendengar langkah atau gonggongan. Individu yang ditangkap dapat mencakar, menggigit, dan menendang karena panik. Respons tersebut bersifat membela diri, bukan perubahan menjadi hewan buas.

## Habitat

Kebun dan lahan terbuka dekat pinggiran ibu kota Mandala. Catatan penampakannya di Lingkar Bumi juga mencakup kelinci yang dibawa ke Pasar Agung Bumi. Distrik pasar yang padat itu merupakan tempat perdagangan hewan, bukan padang luas tempat seluruh populasinya hidup liar.

## Kisah — Pelarian dari Pasar Agung

Seekor Kelinci Padang lepas dari keranjang ketika seorang pedagang di Lingkar Bumi berdebat tentang harga. Orang-orang mengejarnya melewati tumpukan kain, karung beras, dan kaki pembeli. Semakin banyak tangan meraih, semakin liar larinya.

Seorang penjaga kios justru membuka jalan menuju sudut yang teduh, lalu meletakkan keranjang miring di sana. Kelinci itu masuk mencari perlindungan. Pedagangnya pulang dengan pelajaran sederhana: sesuatu yang ketakutan tidak menjadi lebih mudah ditangkap hanya karena diteriaki.

> Acuan: [Lingkar Bumi](<../../03_Region/01_Mandala Kingdom/Cities & Town/Mandala Capital.md>).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `9.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Beast` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T1 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Neutral` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `All` | Menerima pengganda kerusakan 2.0x |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **9** | **1** | **4** | **12** | **13** | **4** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `108` *(Base 3 + VIT×15 + STR×5)* | **DEF** | `10` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `9` *(Base 1 + INT×8)* | **MDF** | `9` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `58` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `12` *(Base + INT×2)* |
| **ATK** | `20` *(Formula Melee)* | **Action Speed** | `19` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.0%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.5%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `102.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.12%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.60%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Bite** | `01 Neutral` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Dust Hop** | `01 Neutral` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35)` |
| **Escape Dash** | `01 Neutral` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Escape Dash, Lowest HP%
Turn 2+: Dust Hop, Random
Always: Quick Bite, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** All Elements: 125%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `20` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `15` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `8` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Fang` (`15%`) | Material alam / crafting |
