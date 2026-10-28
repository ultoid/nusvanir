---
title: Leyak
tags:
  - Bestiary
---

# Leyak

## Deskripsi

Penyihir iblis dengan tubuh yang mengalami mutasi hewani dan serangan berupa kutukan. Leyak berbahaya karena lawan dapat terlalu sibuk mengamati perubahan rupanya hingga mengabaikan gerakan merapal. Bentuk hewan yang tampak pada tubuhnya tidak cukup untuk menentukan dari ras mana ia berasal.

## Bentuk

Siluet dasarnya menyerupai sosok tegak, tetapi proporsi anggota tubuh tidak lagi serasi. Jari memanjang menjadi cakar, punggung membungkuk, dan bagian wajah bercampur dengan rahang atau gigi hewani. Rambut kusut serta kain koyak menutup sebagian perubahan sehingga bentuknya sulit dikenali dalam gelap. Mutasinya tidak ditetapkan selalu sama pada setiap individu dan tidak disamakan dengan kepala terbang Strigoi.

## Tingkah Laku

Agresif dengan cara mengintimidasi dan mengutuk, bukan sekadar menerkam. Ia dapat mempertahankan jarak, mencari penghalang, atau memanfaatkan kepanikan untuk melanjutkan rapalan. Sosok yang mundur belum tentu menyerah. Meski disebut penyihir dalam entri lama, kemampuan merapal tidak digunakan untuk memutuskan konflik tentang kesadaran Dhemit atau membuktikan bahwa semua Leyak berasal dari golongan tersebut.

## Habitat

Lokasi lama Pulau Asrivana belum memiliki padanan wilayah yang terverifikasi. Tepi hutan Astradipa yang mengalami gangguan sihir gelap menjadi salah satu tempat kemunculannya. Penempatan ini tidak menyatakan Astradipa adalah pulau maupun bahwa Asrivana berubah menjadi Leyak.

## Kisah — Bayangan di Akar Pohon

Seorang penjaga Akar-Dipa melihat bayangan manusia membungkuk di antara akar, tetapi tangan yang keluar darinya berakhir dengan cakar. Ia tidak segera mengejar. Dari balik pohon lain, rekannya melihat bibir sosok itu terus bergerak meskipun tubuhnya tampak sedang bersembunyi.

Mereka memanggil bantuan dan menutup jalur warga sebelum mendekat. Ketika bayangan itu berpindah, yang ditinggalkannya bukan korban yang berhasil dipancing keluar, melainkan jalan yang sudah kosong.

> Acuan: [Threat](../../03_Region/02_Astradipa/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `23.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T3 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Caster, Demonic, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **15** | **28** | **8** | **21** | **21** | **14** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `612` *(Base 327 + VIT×15 + STR×5)* | **DEF** | `29` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `52` *(INT×8)* | **MDF** | `35` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `120` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `57` *(Base + INT×2)* |
| **ATK** | `34` *(Formula Magic)* | **Action Speed** | `32` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `7.2%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `6.7%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `4.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `156.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `107.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.42%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.84%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.12%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Cursed Bolt** | `11 Dark` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45 (Curse 30%))` |
| **Blood Hex** | `11 Dark` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Leyak Possession** | `11 Dark` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25 (Curse 30%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Leyak Possession, Lowest HP%
State === Taunt: Blood Hex, Random
Turn % 2 == 0: Blood Hex, Random
Always: Cursed Bolt, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `150` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `112` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `50` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`35%`) | Material alam / crafting |
| **Drop 2** | `Kala Crystal` (`8%`) | Komponen sekunder |
