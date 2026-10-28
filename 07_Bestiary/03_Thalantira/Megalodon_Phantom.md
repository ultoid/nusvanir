---
title: Megalodon Phantom
tags:
  - Bestiary
---

# Megalodon Phantom

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Hiu hantu Thalantira yang dapat menembus karang ketika memburu. Tempat berlindung yang menghentikan pemangsa lain tidak selalu memutus jalurnya. Siluetnya kadang hilang di balik batu sebelum muncul kembali dari sisi yang tidak memiliki celah cukup lebar untuk tubuh sebesar itu.

## Bentuk

Tubuhnya berbentuk torpedo dengan kepala berat, sirip punggung tinggi, dan ekor yang mendorong melalui kibasan lebar. Tepian tubuh tampak kabur seperti dilihat melalui air dengan kedalaman berbeda. Barisan gigi terlihat lebih jelas daripada kulit, membuat rahangnya seolah mendahului bagian lain saat muncul dari kegelapan. Ketika melewati karang, garis sirip dan punggung saling bertumpuk dengan batu tanpa memecahnya. Rupa menyerupai bayangan itu tidak dengan sendirinya menjelaskan apakah ia pernah hidup dalam bentuk lain.

## Tingkah Laku

Pemangsa buas yang terus mengikuti jalur mangsa melewati penghalang. Ia mengitari ruang sempit sebelum menerobos karang dari arah yang sulit diantisipasi. Ancaman yang mampu menghadapinya membuat hiu memperlebar putaran untuk mencari sisi terbuka. Gerak menghilang bukan selalu tanda mundur. Megalodon Phantom tercatat di antara makhluk air ketika keadaan asli Thalantira tersingkap; sebutan hantu tidak cukup untuk memasukkannya ke golongan Dhemit atau menyatakan asal arwahnya.

## Habitat

Perairan Thalantira, dengan labirin karang dan tepian jurang laut sebagai habitat tambahan yang sesuai. Di tempat tersebut, kemampuan menembus batu memberi jalur pendek di antara lorong berkelok. Ia tetap digambarkan sebagai penghuni air; kemunculan makhluk laut dalam kekacauan Prologue tidak mengubah seluruh kebiasaan hidupnya menjadi pemangsa daratan.

## Kisah — Jalan yang Tidak Terbuka

Seekor ikan besar menyelinap ke rongga karang setelah melihat sirip di belakangnya. Jalan masuk terlalu kecil bagi hiu. Ia berhenti di ruang gelap, sementara bayangan pemangsa lewat di luar lubang.

Lalu gigi muncul dari dinding. Batu tidak retak, dan tak ada pasir yang jatuh. Ikan itu melesat keluar melalui bukaan lain, kembali ke laut yang tadi ingin dihindarinya. Di belakangnya, hiu meluncur melewati karang seolah rongga tersebut tidak pernah memiliki dinding.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `40.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Mini Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Aquatic, Large, Stealth` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **122** | **29** | **48** | **80** | **87** | **69** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `9450` *(Base 7805 + VIT×15 + STR×5)* | **DEF** | `165` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `231` *(INT×8)* | **MDF** | `163` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `609` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `191` *(Base + INT×2)* |
| **ATK** | `268` *(Formula Melee)* | **Action Speed** | `131` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `94.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `23.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `20.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `18.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `196.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `134.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.07%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.87%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.86%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Phantom Bite** | `Void` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45)` |
| **Voidwake** | `11 Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Curse 30%))` |
| **Spectral Devour** | `Void` / Physical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Spectral Devour, Lowest HP%
State === Taunt: Voidwake, Random
Turn % 2 == 0: Voidwake, Random
Always: Phantom Bite, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Void: 50%, Water: 50%
* **Resistensi Status:** Curse: 50%, Freeze: 70%, Paralyze: 70%, Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `3400` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `2550` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `880` | Mata uang resmi penjelajahan |
| **Drop 1** | `Void Crystal` (`8%`) | Material alam / crafting |
| **Drop 2** | `Thalantira Primordial Stone` (`4%`) | Komponen sekunder |
| **Drop 3** | `Voidweave` (`5%`) | Rampasan langka |
