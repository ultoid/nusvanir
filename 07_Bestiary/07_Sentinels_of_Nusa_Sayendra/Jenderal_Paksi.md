---
title: Jenderal Paksi
tags:
  - Bestiary
  - Boss
---

# Jenderal Paksi

## Deskripsi

Sentinel Garuda yang mengawasi langit timur dengan penglihatan tajam dan resonansi sonik suci. Paksi mengutamakan ketepatan: ia membaca jarak, arah angin, dan gema sebelum melepaskan serangan. Perannya membuat ancaman dapat dikenali saat masih jauh dari pusat Nusa Sayendra, memberi armada waktu untuk memilih tanggapan yang tepat.

## Bentuk

Tubuh Paksi lebih ramping daripada Garuda garis depan, dengan bulu emas pucat yang menggelap pada ujung sayap. Matanya berwarna terang dan terlindung tonjolan tulang halus agar tetap terbuka saat menembus angin kencang. Ia membawa busur panjang yang dapat digunakan ketika terbang; cahaya dan getaran suara berkumpul pada tali sebelum dilepaskan sebagai bidikan. Penutup dada dibuat rapat agar tidak mengganggu aliran udara. Ketika mendengarkan gema, bulu kecil di sekitar lehernya terangkat mengikuti perubahan tekanan.

## Kepribadian dan Sikap

Paksi teliti, pendiam, dan lebih nyaman menyampaikan kepastian daripada dugaan. Ia dapat terlihat lambat mengambil keputusan karena memeriksa informasi dari beberapa arah, tetapi setelah memilih sasaran ia bertindak tanpa ragu. Ia menghargai pengintai yang berani mengatakan bahwa mereka belum yakin. Sikap perfeksionisnya kadang membuat rekan merasa terus dinilai; ia perlu mengingat bahwa kesalahan latihan adalah bagian dari pembelajaran. Kepada pengunjung, ia sopan namun tidak mudah mengalihkan perhatian dari tugas pengawasan.

## Kedudukan dan Kuil Penjagaan

Kuil Angin Timur Sayendra adalah pos penjagaan Paksi. Arah timur mendapat cahaya awal dan ruang pandang luas, sesuai perannya sebagai pengamat serta pembidik jarak jauh. Ia berpatroli antara kuil dan jalur udara menuju Swargaloka, tetapi bukan berarti semua penerbangan sipil berada di bawah komandonya. Bentuk kuil dan koordinatnya belum mempunyai dokumen regional tersendiri.

## Kisah - Gema Sebelum Bayangan

Paksi mendengar gema yang kembali terlalu cepat dari awan timur. Pengintai lain tidak melihat apa pun dan mengira perubahan itu hanya akibat angin. Ia meminta mereka menyebar tanpa melepaskan serangan.

Ketika matahari naik, cahaya memperlihatkan makhluk yang terbang menempel di bawah lapisan awan. Paksi menembakkan resonansi ke ruang kosong di depannya, memaksa kawanan itu berbelok ke jalur yang telah dijaga. Para Sentinel menghalaunya sebelum mencapai Swargaloka. Paksi mencatat laporan tanpa menyebut dirinya paling dahulu mengetahui ancaman; baginya, pengamatan hanya berguna bila seluruh formasi sempat bertindak.

> Acuan: [Nusa Sayendra](../../03_Region/07_Nusa%20Sayendra/Nusa_Sayendra.md); [Garuda](../../04_Ras/02_Wuru%20Loka/Garuda.md); [Puncak Emas Swargaloka](../../03_Region/07_Nusa%20Sayendra/Cities%20%26%20Town/Puncak%20Emas%20Swargaloka.md); [Pasukan Ksatria Sayap Garuda](../../03_Region/07_Nusa%20Sayendra/Faksi%20%26%20Institusi/Pasukan%20Ksatria%20Sayap%20Garuda.md); [Sumpah Penjaga Langit](../../03_Region/07_Nusa%20Sayendra/Agama%20%26%20Kepercayaan/Sumpah%20Penjaga%20Langit.md); [Threat](../../03_Region/07_Nusa%20Sayendra/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `61.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Garuda` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Light` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Dark` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Holy, Light, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **94** | **22** | **38** | **58** | **48** | **114** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `19375` *(Base 17195 + VIT×15 + STR×5)* | **DEF** | `218` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `180` *(Base 4 + INT×8)* | **MDF** | `179` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `778` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `150` *(Base + INT×2)* |
| **ATK** | `207` *(Formula Melee)* | **Action Speed** | `72` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `14.5%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `16.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `20.1%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `185.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `157.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.42%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.66%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.20%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Bastion Smash** | `Neutral` / Physical Attack | `6 SP` | Always (Prioritas 5.0) | `a.def * 1.3 - b.def * 0.4` |
| **Bulwark of Light** | `Light` / Certain Hit | `14 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Aegis Retribution** | `Neutral` / Physical Attack | `24 SP` | HP <= 50% (Prioritas 6.0) | `a.atk * 0.9 + a.def * 1.8 - b.def * 0.2` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Light: 50%, Wind: 50%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5600` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4200` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1500` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Golden Scale` (`35%`) | Material alam / crafting |
| **Drop 2** | `Prabha Crystal` (`18%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Paksi Suncrest Helm` (`5%`) | Rampasan unik / piala bos |
