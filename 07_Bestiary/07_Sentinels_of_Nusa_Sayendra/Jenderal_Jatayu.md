---
title: Jenderal Jatayu
tags:
  - Bestiary
  - Boss
---

# Jenderal Jatayu

## Deskripsi

Komandan Pasukan Ksatria Sayap Garuda dan veteran perang udara paling berpengalaman di Nusa Sayendra. Jatayu memegang kendali operasional armada ketika Prabu Swarnapatra mulai kehilangan kewarasan akibat kutukan Feral. Petir yang dibawanya bukan sekadar kekuatan perang; di bawah kepemimpinannya, sambaran di langit menjadi isyarat bagi formasi Garuda untuk bergerak sebagai satu kesatuan.

## Bentuk

Jatayu adalah Garuda raksasa dengan sayap berwarna perunggu yang menyimpan banyak bekas patahan lama. Beberapa bulu tumbuh tidak rata di sepanjang garis luka, membuat bentangan sayapnya mudah dikenali dari jauh. Mata tajam berada di bawah helm berhias bulu badai. Cakar dan paruhnya tampak keemasan kusam, sedangkan listrik merambat sebagai garis putih-biru di antara bulu ketika ia bersiap terbang. Usia serta luka tidak mengurangi wibawanya; keduanya menjadi catatan hidup dari pertempuran yang telah dilalui.

## Kepribadian dan Sikap

Jatayu disiplin, penuh tanggung jawab, dan setia kepada rajanya bahkan ketika tugas itu menuntut keputusan berat. Ia berbicara singkat dalam operasi, tetapi mau mendengar laporan prajurit yang paling muda bila informasi mereka dapat menyelamatkan formasi. Pengalaman membuatnya berhati-hati terhadap keberanian yang tidak disertai rencana. Ia menghormati Ksatria Vayu dari Avalerion dan menjaga aliansi kedua wilayah melalui tindakan nyata. Di balik ketegasannya, ia menyimpan kegelisahan tentang kutukan Swarnapatra dan menolak menyerah mencari obat ke Tirta Amarta.

## Kedudukan dan Kuil Penjagaan

Kuil Angin Selatan Sayendra menjadi pos penjagaan Jatayu dalam entri lama. Dari sana ia mengatur jalur pendekatan armada serta hubungan dengan utusan Avalerion. Pusat komando dan kehidupan Garuda tetap terhubung dengan Puncak Emas Swargaloka, habitat melayang yang memiliki pelataran terbuka. Kuil selatan belum memiliki dokumen geografis tersendiri, sehingga bentuk bangunan, jarak, dan batas wilayahnya tidak diperinci.

## Kisah - Perintah di Tengah Petir

Awan gelap memutus pandangan antara dua sayap patroli. Seorang prajurit muda mengusulkan pengejaran cepat terhadap bayangan Jenggala yang melintas di bawah badai. Jatayu meminta seluruh formasi menahan posisi sampai kilat berikutnya memperlihatkan jalur.

Bayangan itu ternyata umpan; gerombolan lain menunggu di balik lapisan awan. Petir Jatayu membelah gelap sebagai tanda perubahan formasi, dan kedua sayap patroli menutup jalan bersama-sama. Setelah kembali, ia tidak menegur keberanian prajurit muda tersebut. Ia memintanya memimpin pembacaan cuaca berikutnya, agar keberanian itu belajar berjalan bersama kesabaran.

> Acuan: [Jenderal Jatayu](../../05_Karakter%20%26%20Tokoh%20Penting/07_Nusa%20Sayendra/Jenderal%20Jatayu.md); [Ksatria Vayu](../../05_Karakter%20%26%20Tokoh%20Penting/03_Avalerion/Ksatria%20Vayu.md); [Nusa Sayendra](../../03_Region/07_Nusa%20Sayendra/Nusa_Sayendra.md); [Garuda](../../04_Ras/02_Wuru%20Loka/Garuda.md); [Puncak Emas Swargaloka](../../03_Region/07_Nusa%20Sayendra/Cities%20%26%20Town/Puncak%20Emas%20Swargaloka.md); [Pasukan Ksatria Sayap Garuda](../../03_Region/07_Nusa%20Sayendra/Faksi%20%26%20Institusi/Pasukan%20Ksatria%20Sayap%20Garuda.md); [Sumpah Penjaga Langit](../../03_Region/07_Nusa%20Sayendra/Agama%20%26%20Kepercayaan/Sumpah%20Penjaga%20Langit.md); [Threat](../../03_Region/07_Nusa%20Sayendra/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `60.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Garuda` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T7 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Wind/Light` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Holy, Wind` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **114** | **22** | **44** | **58** | **60** | **89** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `16275` *(Base 14370 + VIT×15 + STR×5)* | **DEF** | `191` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `180` *(Base 4 + INT×8)* | **MDF** | `162` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `693` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `160` *(Base + INT×2)* |
| **ATK** | `250` *(Formula Melee)* | **Action Speed** | `90` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `16.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `17.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `17.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `193.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `144.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.67%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.66%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.18%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Piercing Shot** | `Neutral` / Physical Attack | `26 SP` | Always (Prioritas 5.0) | `a.atk * 2.7 - b.def * 0.1 (ignores 40% DEF)` |
| **Gale Force** | `Wind` / Magical Attack | `20 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.3 - b.mdef * 0.3` |
| **Forestbreaker Arrow** | `Neutral` / Physical Attack | `15 MP / 35 SP` | HP <= 50% (Prioritas 6.0) | `a.atk * 4.2 - b.def * 0.05` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Earth: 150%, Light: 50%, Wind: 50%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5600` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4200` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1500` | Mata uang resmi penjelajahan |
| **Drop 1** | `Garuda Storm Feather` (`35%`) | Material alam / crafting |
| **Drop 2** | `Garuda Golden Scale` (`20%`) | Komponen sekunder |
| **Drop 3** | `Spirit Thread` (`15%`) | Rampasan langka |
| **Boss / Unique Drop** | `Jatayu Stormcrown / Golden Sentinel Boots` (`5%`) | Rampasan unik / piala bos |
