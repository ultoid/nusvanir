---
title: Pyrowisp
tags:
  - Bestiary
---

# Pyrowisp

## Deskripsi

Bola api melayang menyerupai Banaspati yang mampu melepaskan ledakan mematikan. Pyrowisp lebih tepat dikenali dari panas dan lontaran apinya daripada diikuti sebagai penunjuk jalan. Meski namanya mirip Wisp, catatan keduanya menekankan ancaman yang berbeda: serangan api terbuka dan penyesatan.

## Bentuk

Wujudnya berupa gumpalan api dengan pusat terang dan lidah-lidah nyala yang terus melengkung mengitari inti. Batas tubuh tampak membesar saat api berkumpul, lalu berkerut sesudah lontaran dilepaskan. Asap tipis dan bara mengikuti gerakannya tanpa membentuk tubuh berkaki atau bersayap. Bayangan wajah yang sesekali terbaca pada nyala merupakan kesan visual, bukan penetapan roh seseorang di dalamnya.

## Tingkah Laku

Agresif dan berbahaya untuk didekati. Ia dapat melayang menghadapi gangguan, menahan posisi, lalu melontarkan api ke arah yang menarik perhatiannya. Menjauh dari satu nyala tidak selalu berarti keluar dari jangkauan panas di sekitarnya. Belum ada dasar untuk menyatakan bahwa ia lahir dari Wisp, merupakan tahap pertumbuhan tertentu, atau dapat dipelihara hanya dengan menyediakan bahan bakar.

## Habitat

Rawa Kering adalah lokasi lama yang belum terpetakan. Cekungan rawa yang mengering di pinggiran hutan Mandala menjadi habitatnya. Kesamaan nama dengan Balairung Kaldera Mahasvara tidak membuktikan bahwa makhluk ini berasal dari ibu kota Nagarasven di Agnitra.

## Kisah — Api yang Menunggu

Dua pengelana menyangka cahaya di cekungan kering sebagai api unggun rombongan lain. Yang lebih muda hendak turun meminta tempat bermalam, tetapi rekannya melihat nyala itu melayang tanpa kayu di bawahnya.

Mereka baru berbalik ketika cahaya membesar dan lontaran api menyambar tanah tempat mereka semula berdiri. Dari lereng yang lebih tinggi, keduanya menyaksikan bara berputar di atas cekungan. Malam itu mereka memilih gelap yang mereka kenal daripada cahaya yang tidak mempunyai penjaga.

> Acuan: [Mandala](../../03_Region/01_Mandala%20Kingdom/Mandala.md); [Balairung Kaldera Mahasvara](../../03_Region/04_Agnitra/Cities%20%26%20Town/Balairung%20Kaldera%20Mahasvara.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `26.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Spirit` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Water` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Burning, Caster` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **9** | **16** | **4** | **14** | **15** | **8** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `198` *(Base 33 + VIT×15 + STR×5)* | **DEF** | `17` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `26` *(INT×8)* | **MDF** | `20` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `78` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `31` *(Base + INT×2)* |
| **ATK** | `20` *(Formula Magic)* | **Action Speed** | `22` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.5%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `104.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.24%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.48%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.76%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Ember Bolt** | `02 Fire` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45)` |
| **Flare Pulse** | `02 Fire` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Wisp Detonation** | `02 Fire` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Wisp Detonation, Lowest HP%
Turn 2+: Flare Pulse, Random
Always: Ember Bolt, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 50%, Water: 150%
* **Resistensi Status:** Burn: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `40` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `30` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `15` | Mata uang resmi penjelajahan |
| **Drop 1** | `Wisp Core` (`35%`) | Material alam / crafting |
| **Drop 2** | `Pyrowisp Crystal` (`20%`) | Komponen sekunder |
