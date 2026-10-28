---
title: Wendigo
tags:
  - Bestiary
---

# Wendigo

## Deskripsi

Raksasa ramping menjulang yang dikenal sebagai Begu Ganjang. Wendigo Nusvanir mengancam dengan kemampuan mencekik dari jauh, sehingga ruang kosong di antara tubuhnya dan korban bukan jaminan aman. Rupanya tidak mengikuti gambaran bertanduk rusa; identitas lokal dalam sumber adalah raksasa tinggi yang menyesakkan napas.

## Bentuk

Tubuhnya memanjang tidak wajar, dengan bahu sempit, dada cekung, dan lengan yang menggantung jauh ke bawah. Kepala kecil di ujung leher panjang membuat jarak tubuhnya sulit diperkirakan pada lereng berkabut. Kulit gelap pucat, jari-jari kurus, serta rambut jarang membentuk rupa yang menyerupai bayangan pohon mati. Ia tidak diberi tanduk, tengkorak hewan, atau ciri dingin yang tidak didukung entri Nusvanir.

## Tingkah Laku

Mengancam dan tidak perlu berlari untuk membuat pendatang merasa terpojok. Ia berdiri mengawasi jalur sebelum mengangkat tangan ke arah korban. Orang yang merasakan cekikan dapat salah mengira bahaya berasal dari seseorang di belakangnya. Jangkauan, penyebab, dan cara pasti memutus pengaruh itu belum ditetapkan sebagai aturan; kisah tidak memberikan jarak aman atau ritual penawar baru.

## Habitat

Puncak bukit Raksamala merupakan habitat yang tercatat. Jalur menanjak, tonjolan batu, dan punggung bukit terbuka cocok untuk siluetnya yang menjulang. Tidak ada benteng dosa tertentu yang ditetapkan sebagai pemilik atau wilayah kekuasaannya.

## Kisah — Orang Ketiga di Punggung Bukit

Dalam kisah perjalanan di Raksamala, dua pelintas berhenti ketika menghitung bayangan pada punggung bukit. Mereka hanya berdua, tetapi ada sosok ketiga yang jauh lebih tinggi. Salah seorang mulai menarik kerahnya, mengira pakaiannya tersangkut.

Rekannya tidak melihat tangan yang menyentuh leher itu. Ia menariknya mundur ke jalur tempat mereka datang, tanpa menunggu sosok tinggi tersebut melangkah. Setelah napas kembali, keduanya meninggalkan barang yang jatuh. Tidak ada yang mau naik lagi hanya untuk membuktikan ukuran bayangan tadi.

> Acuan: [Raksamala](../../03_Region/10_Raksamala/Raksamala.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `28.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Jenggala` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Berserker` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T4 (Mini Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Large, Frenzy, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **45** | **6** | **16** | **30** | **29** | **19** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `2420` *(Base 1910 + VIT×15 + STR×5)* | **DEF** | `51` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `48` *(INT×8)* | **MDF** | `47` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `205` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `48` *(Base + INT×2)* |
| **ATK** | `98` *(Formula Melee)* | **Action Speed** | `44` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `88.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `9.3%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `9.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `6.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `166.7%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `109.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.57%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.18%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.54%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Frosted Claw** | `Ice` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `a.atk * 1.15 - b.def * 0.45 (Chill 50%)` |
| **Hunger Howl** | `Dark` / Certain Hit | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Wendigo Frenzy** | `Dark` / Certain Hit | `0 SP` | HP <= 50% (Prioritas 6.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 75%, Light: 150%
* **Resistensi Status:** Freeze: 70%, Paralyze: 70%, Root: 75%, Stun: 70%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `520` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `390` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `160` | Mata uang resmi penjelajahan |
| **Drop 1** | `Beast Bone` (`40%`) | Material alam / crafting |
| **Drop 2** | `Wight Shroud` (`25%`) | Komponen sekunder |
