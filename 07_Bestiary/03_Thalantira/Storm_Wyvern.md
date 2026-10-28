---
title: Storm Wyvern
tags:
  - Bestiary
---

# Storm Wyvern

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Naga terbang yang menguasai petir dan badai setempat di langit Thalantira. Ukurannya lebih kecil daripada para penjaga kolosal pulau, tetapi tetap cukup besar untuk mendominasi jalur angin. Kilat yang bergerak melawan arah awan dapat menandai kehadirannya sebelum bentuk sayap terlihat.

## Bentuk

Tubuhnya mengikuti wyvern: sepasang kaki belakang bercakar dan anggota depan yang membentang sebagai sayap. Leher melengkung menyangga kepala bertanduk pendek, sedangkan ekor panjang menjaga keseimbangan ketika tubuh membelok. Sisik kelabu kebiruan menebal di dada dan punggung. Sela duri pada tengkuk memantulkan kilat, dan selaput sayap tampak berurat ketika disinari dari dalam awan. Saat bertengger, ujung sayap dilipat rapat sehingga tubuhnya menyerupai punggung batu bergerigi.

## Tingkah Laku

Buas dan sangat mempertahankan jalur terbangnya. Ia berputar mengelilingi penyusup, memperkuat hembusan di sekitarnya, lalu menyambar dari batas awan. Ancaman yang mengejar ke tempat bertengger dapat memancing serangan petir sebelum ia kembali mengudara. Storm Wyvern termasuk penghuni langit yang tampak setelah ilusi pulau tersingkap. Kemiripan wujud dengan naga lain tidak menetapkan hubungan darah dengan Nagarasven maupun kedudukan sebagai keturunan Void Wyrm.

## Habitat

Langit Thalantira dan tebing tinggi yang bersentuhan dengan lapisan badai. Punggung lereng utara menjadi tempat bertenggernya, sementara perairan di sekitar benteng karang memberi ruang putar luas. Badai yang menyelimuti seluruh pulau tidak otomatis berasal dari satu Wyvern; batas pengaruh setiap individu belum diceritakan.

## Kisah — Kilat yang Berbelok

Seekor Wyvern mengitari tebing saat awan rendah mendesak masuk. Bayangan bersayap lain melintas terlalu dekat dengan batu tempatnya bertengger. Ia membuka sayap dan naik, mengikuti hembusan yang berputar ke laut.

Kilat menyala di sela awan, lalu berpindah mengikuti arah terbangnya. Sang pengganggu menukik menjauh dari tebing sebelum sambaran berikutnya. Wyvern menghentikan pengejaran di atas karang dan kembali ke lereng. Badai terus bergerak, tetapi tempat bertenggernya telah kosong dari bayangan lain.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [08 Ujian Para Pelindung](../../08_Story/02_Prologue/08_Ujian_Para_Pelindung.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `43.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Dragon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Flying, Large, Draconic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **138** | **28** | **54** | **70** | **73** | **107** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `16800` *(Base 14505 + VIT×15 + STR×5)* | **DEF** | `230` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `221` *(INT×8)* | **MDF** | `196` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `831` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `194` *(Base + INT×2)* |
| **ATK** | `303` *(Formula Melee)* | **Action Speed** | `110` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `95.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `20.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `21.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `202.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `153.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.21%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.84%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.06%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Storm Talon** | `05 Air` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45)` |
| **Thunder Dive** | `06 Electric` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Paralyze 30%))` |
| **Tempest Breath** | `Void` / Magical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Tempest Breath, All Foes
Turn % 3 == 0: Thunder Dive, Highest ATK
HP% <= 50%: Tempest Breath, Lowest HP%
Always: Storm Talon, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 150%, Void: 50%, Wind: 75%
* **Resistensi Status:** Curse: 50%, Fear: 50%, Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5950` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4462` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1540` | Mata uang resmi penjelajahan |
| **Drop 1** | `Storm Wyvern Fang` (`35%`) | Material alam / crafting |
| **Drop 2** | `Void Crystal` (`15%`) | Komponen sekunder |
| **Drop 3** | `Thalantira Primordial Stone` (`8%`) | Rampasan langka |
