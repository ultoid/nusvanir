---
title: Void Panther
tags:
  - Bestiary
---

# Void Panther

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Macan kosmis yang berpindah seketika untuk menyergap dari arah tak terduga. Jejak kakinya dapat berakhir di tanah terbuka tanpa jalan keluar yang terlihat. Di hutan Thalantira, ketidakhadirannya di depan tidak berarti pemburu ini telah meninggalkan tempat perburuan.

## Bentuk

Tubuhnya rendah, panjang, dan lentur, dengan bahu kuat yang bergerak jelas di bawah bulu pendek. Warna hitam pekat memuat kilau ungu samar pada punggung, sedangkan mata terang tetap tampak ketika sisi tubuh lain menyatu dengan gelap. Ekor panjang membantu keseimbangan saat mendarat. Tepian siluet terlihat terurai sesaat sebelum perpindahan, seperti bayangan yang terpotong oleh air. Rahang dan cakar mempertahankan rupa pemangsa kucing besar, tanpa tanduk atau sayap tambahan.

## Tingkah Laku

Buas, mengintai, dan lebih memilih celah daripada pertarungan terbuka. Ia mendekat dari tutupan, berhenti ketika diperhatikan, lalu berpindah ke sisi yang tidak diawasi. Jika terluka atau terdesak, kemampuan serupa dipakai untuk melepaskan diri sebelum kembali menilai mangsa. Tubuh yang menghilang tidak selalu berarti serangan akan segera datang. Void Panther termasuk monster darat pada pengungkapan Prologue; kemiripan dengan Macan Kumbang tidak menetapkan bahwa ia hasil mutasi spesies tersebut.

## Habitat

Hutan daratan Thalantira adalah penempatan yang sesuai dengan kategori habitat lama. Jalur berakar, semak rapat, dan tepian bukit di antara pantai serta pusat pulau memberi banyak tempat muncul yang sulit dipantau sekaligus. Batas perpindahannya belum dijelaskan, sehingga tidak ditambahkan jalur teleportasi ke Mandala atau pulau lain.

## Kisah — Jejak yang Berhenti

Seekor hewan berhenti minum ketika melihat dua mata di sela akar. Ia mundur, menjaga kepala tetap menghadap pemangsa. Mata itu lenyap. Sesaat kemudian, ranting patah di belakangnya.

Panther telah muncul di sisi lain genangan. Hewan buruannya melompat ke semak sebelum cakar mencapai air. Percikan jatuh di atas jejak yang hanya terbentuk pada satu tepi. Panther tidak segera mengejar; ia menunduk, mendengarkan gerak daun, lalu menghilang lagi sebelum permukaan genangan kembali tenang.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [07 Tiga Kuil Penjaga](../../08_Story/02_Prologue/07_Tiga_Kuil_Penjaga.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `47.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Stealth` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **112** | **26** | **46** | **74** | **87** | **64** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4860` *(Base 3340 + VIT×15 + STR×5)* | **DEF** | `152` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `212` *(Base 4 + INT×8)* | **MDF** | `150` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `564` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `176` *(Base + INT×2)* |
| **ATK** | `247` *(Formula Melee)* | **Action Speed** | `131` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `94.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `23.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `19.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `17.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `192.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `132.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.92%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.78%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.76%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Phase Pounce** | `Void` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Void Claw** | `11 Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Curse 30%))` |
| **Eclipse Ambush** | `11 Dark` / Physical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Eclipse Ambush, Lowest HP%
State === Taunt: Void Claw, Random
Turn % 2 == 0: Void Claw, Random
Always: Phase Pounce, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%, Void: 50%
* **Resistensi Status:** Curse: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1700` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1275` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `440` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
