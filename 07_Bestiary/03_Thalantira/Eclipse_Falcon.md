---
title: Eclipse Falcon
tags:
  - Bestiary
---

# Eclipse Falcon

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Elang Thalantira yang menyelubungi jalur buruannya dengan kegelapan sebelum menukik. Bayangannya dapat terasa seperti awan yang mendadak menutup matahari, padahal langit di sekeliling masih terbuka. Kecepatan serangannya membuat selang antara hilangnya cahaya dan datangnya cakar terasa sangat singkat.

## Bentuk

Tubuhnya ramping dengan dada berotot, sayap meruncing, dan ekor yang dapat membuka sebagai kemudi. Bulu hitam berkilau ungu pada tepian, sedangkan kepala kecil serta paruh melengkung memberi siluet tajam. Cakar panjang terlipat rapat saat meluncur. Ketika sayap dibentangkan, batas bulunya larut dalam selubung gelap sehingga ukuran tubuh sulit dinilai dari bawah. Di dekat tebing, hanya kilat mata dan garis paruh yang sesekali memisahkannya dari bayangan batu.

## Tingkah Laku

Pemangsa buas yang mengandalkan ketinggian dan kejutan. Ia berputar jauh dari sasaran, memadamkan pandangan di jalur turun, lalu menyerang ketika mangsa berhenti atau berbalik mencari arah. Gangguan dekat tempat bertengger memancing sapuan rendah sebagai peringatan sebelum terjangan berikutnya. Setelah selubung damai Thalantira runtuh, Eclipse Falcon termasuk makhluk yang memenuhi langit Prologue. Kegelapan yang dibawanya tidak dengan sendirinya menyatakan kesetiaan kepada Sangrahal.

## Habitat

Langit Thalantira merupakan wilayah jelajah. Tebing terjal di jalur utara menuju gunung api menjadi tempat bertenggernya, dengan angin naik untuk membantu memperoleh ketinggian. Ia juga dapat melintasi batas hutan, tetapi tidak harus bersarang di Kuil Udara atau menjadi peliharaan Void Wyrm agar berbagi ruang langit tersebut.

## Kisah — Awan yang Mendahului Cakar

Seekor burung kecil meninggalkan celah tebing ketika cahaya kembali menyentuh batu. Ia terbang menuju pepohonan, mengikuti jalur yang biasanya terlindung dari angin. Di tengah lintasan, cahaya hilang lagi.

Burung itu membelok sebelum bayangan pertama menyentuhnya. Cakar Falcon menyambar udara kosong dan menyapu daun di tepi hutan. Sang pemburu naik kembali tanpa bersuara. Di celah tempat burung kecil bersembunyi, terang pulih perlahan, tetapi langit yang terbuka tidak lagi terlihat seperti jalan bebas.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [08 Ujian Para Pelindung](../../08_Story/02_Prologue/08_Ujian_Para_Pelindung.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `36.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Sniper` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Ranged` | Formula serangan dasar |
| **Elemen Utama** | `Void/Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **38** | **20** | **94** | **56** | **63** | **70** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `3420` *(Base 2180 + VIT×15 + STR×5)* | **DEF** | `124` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `160` *(INT×8)* | **MDF** | `122` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `446` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `143` *(Base + INT×2)* |
| **ATK** | `207` *(Formula Ranged)* | **Action Speed** | `95` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `100.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `17.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `27.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `15.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `180.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `135.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.10%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.60%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.92%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Eclipse Talon** | `11 Dark` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Void Feather** | `05 Air` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Curse 30%))` |
| **Dark Sky Dive** | `05 Air` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25 (Curse 30%))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Dark Sky Dive, Lowest HP%
State === Taunt: Void Feather, Random
Turn % 2 == 0: Void Feather, Random
Always: Eclipse Talon, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Light: 150%, Void: 50%, Wind: 75%
* **Resistensi Status:** Curse: 50%
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
