---
title: Obsidian Crawler
tags:
  - Bestiary
---

# Obsidian Crawler

## Hakikat Entitas

Entitas ini bukan spesies biologis asli Thalantira, melainkan proyeksi Void yang diciptakan Uru. Tubuhnya dapat menyentuh materi, melukai, dan membunuh selama dipertahankan oleh kehendak Uru. Sikapnya dapat berubah dari tenang atau membantu menjadi buas ketika Uru menolak seorang tamu. Habitat yang dicatat di bawah menunjukkan tempat Uru biasa memproyeksikan wujud ini, bukan ekologi tetap atau populasi yang berkembang biak secara alami.

## Deskripsi

Kalajengking batu hitam sebesar rumah yang menyusuri daratan Thalantira. Tubuhnya dapat tersamarkan di antara bongkah vulkanik sampai kaki-kakinya membuka jalan. Bunyi gesekan batu sering mendahului kemunculannya, tetapi di dekat gunung api suara itu mudah tenggelam dalam gemuruh lereng.

## Bentuk

Punggungnya terbagi menjadi lempeng hitam berkilap, dengan tepi kasar menyerupai obsidian yang pecah. Kaki beruas keluar rendah dari sisi tubuh dan berakhir pada ujung keras untuk mencengkeram batu. Dua capit besar menggantung di depan, sementara ekor bersegmen melengkung di atas punggung menuju ujung runcing. Sambungan antarbagian tampak lebih gelap daripada lapisannya. Rupa kalajengking dipertahankan tanpa memastikan bahwa sengatnya membawa racun atau bahwa seluruh cangkang dapat diolah seperti batu tambang biasa.

## Tingkah Laku

Teritorial, cenderung menahan jalan sebelum menyerang. Ia membuka capit dan menaikkan ekor ketika gangguan mendekat, lalu maju dengan tubuh tetap rendah. Jika terdesak di antara batu, capit dapat dipakai mendorong penghalang atau menjepit apa pun yang berada di depannya. Gerak mundur memberinya ruang untuk mengarahkan kembali tubuh, sehingga bukan pertanda pasti menyerah. Crawler termasuk makhluk darat yang muncul dalam pengungkapan Prologue.

## Habitat

Darat Thalantira merupakan habitat sumber. Hamparan batu tandus di barat dan lereng luar gunung api menjadi tempat jelajahnya karena menyediakan celah serta permukaan yang menyamarkan cangkang. Lahar ungu tetap menjadi bahaya tersendiri; rupa batu tidak menjadi alasan untuk menganggapnya kebal terhadap aliran tersebut atau hidup di dasar kawah.

## Kisah — Lorong di Bawah Bongkah

Hujan mengisi sebuah celah dengan kerikil. Dari bawah bongkah hitam, capit muncul dan mendorong batu-batu kecil itu keluar. Seekor Crawler menarik tubuhnya ke permukaan, memperlihatkan bahwa yang terlihat seperti lantai gua ternyata punggungnya.

Makhluk yang bersembunyi di dekat mulut celah segera menyingkir. Crawler menahan posisi dengan ekor terangkat sampai jalan di depannya kosong. Setelah itu ia berjalan menuju hamparan batu, dan kilau hujan kembali menyamarkannya di antara bongkah lain.

> Acuan: [Threat](../../03_Region/11_Thalantira/Threat.md); [08 Ujian Para Pelindung](../../08_Story/02_Prologue/08_Ujian_Para_Pelindung.md); [09 Pesan dari Ketiadaan](../../08_Story/02_Prologue/09_Pesan_dari_Ketiadaan.md); [Kuil Udara Gunung Ungu](../../03_Region/11_Thalantira/Cities%20%26%20Town/Kuil%20Udara%20Gunung%20Ungu.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `42.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Alien-Void` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Void/Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Water` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Voidborn, Armored, Burrowing` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **75** | **18** | **28** | **53** | **46** | **90** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4750` *(Base 3025 + VIT×15 + STR×5)* | **DEF** | `172` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `143` *(INT×8)* | **MDF** | `142` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `620` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `119` *(Base + INT×2)* |
| **ATK** | `164` *(Formula Melee)* | **Action Speed** | `69` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `90.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `13.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `13.9%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `16.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `178.1%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `145.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.70%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.54%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `6.64%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Obsidian Claw** | `Earth` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45` |
| **Burrow Ambush** | `Void` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.atk * 1.45 - b.def * 0.35` |
| **Blackstone Carapace** | `Earth` / Certain Hit | `0 SP` | HP <= 40% (Prioritas 4.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Void: 50%, Water: 150%
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
