---
title: Vraka The Wrathful
tags:
  - Bestiary
  - Boss
---

# Vraka The Wrathful

## Deskripsi

Panglima Amarah dan penjaga Fortress of Wrath. Vraka dahulu seorang jenderal Hanorok yang dieksekusi karena taktik perang terlalu brutal; Sangrahal menarik jiwanya dan membentuknya kembali sebagai Bhuta. Kini ia memimpin gelombang invasi Jenggala menuju Swargaloka, membawa dendam lama ke dalam setiap pertempuran.

## Bentuk

Vraka adalah monster mutan berotot dengan empat lengan, masing-masing menggenggam kapak jagal raksasa yang meneteskan lava. Api neraka membakar tubuhnya tanpa padam oleh air biasa. Sisa rupa Hanorok masih terbaca pada rahang, postur, dan gerak memanjat, tetapi telah dipelintir oleh pembentukan ulang. Bekas rantai eksekusi melingkari sebagian lengan sebagai pengingat pengkhianatan yang tidak pernah ia lepaskan.

## Kepribadian dan Sikap

Vraka mudah murka, frontal, dan memandang belas kasihan sebagai penghinaan. Ia mempertahankan kecerdasan seorang jenderal, tetapi dendam membuat strateginya berpusat pada penghancuran total, terutama terhadap Hanorok dan Panglima Wukong. Ia memancing lawan marah agar kehilangan disiplin, karena pertumpahan darah memperkuat benteng serta dirinya. Di balik ledakan emosinya terdapat ingatan yang terus dipelihara; ia memilih menafsirkan setiap penolakan sebagai pengulangan pengkhianatan masa lalu.

## Kedudukan dan Benteng

Fortress of Wrath berdiri di atas kolam darah mendidih dan berbentuk Arena Jagal Merah. Di sana Jenggala diadu sampai mati, sementara pengaruh Bloodlust mengikis kendali pengunjung. Vraka menjaga kawah benteng sekaligus memimpin serangan berat ke Nusa Sayendra. Lokasi ini menggambarkan masa sebelum Hector menghancurkan komandan dan peradaban Raksamala.

## Kisah - Nama yang Tidak Dimaafkan

Seorang tawanan Hanorok dibawa ke arena dan menyebut nama lama Vraka, berharap ingatan masa lalu menghentikan kapaknya. Sang panglima justru mendengar ejekan dari mereka yang pernah menjatuhkan hukuman. Api pada empat bilahnya membesar.

Tawanan itu menolak membalas kemarahan dengan makian. Ia berkata bahwa kekejaman lama tidak menjadi benar hanya karena pengkhianatan yang diterima Vraka juga salah. Sesaat sang panglima berhenti. Lalu ia menghantam arena, bukan karena telah memaafkan, melainkan karena jawaban tersebut mencapai bagian dirinya yang belum sepenuhnya menjadi amarah.

> Acuan: [Vraka The Wrathful](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Vraka%20The%20Wrathful.md); [Fortress of Wrath](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Wrath.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `70.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Berserker` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Dark/Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Frenzy, Large, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **167** | **26** | **68** | **70** | **77** | **79** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `24200` *(Base 22180 + VIT×15 + STR×5)* | **DEF** | `202` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `208` *(INT×8)* | **MDF** | `189` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `749` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `183` *(Base + INT×2)* |
| **ATK** | `368` *(Formula Melee)* | **Action Speed** | `116` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `98.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `23.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `18.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `213.7%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `139.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.37%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.78%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.66%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Raging Blow** | `01 Neutral` / Physical Attack | `8 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.9 - b.def * 0.3)` |
| **Frenzy** | `01 Neutral` / Certain Hit | `25 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Executioner's Wrath** | `01 Neutral` / Physical Attack | `40 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.atk * 1.55 - b.def * 0.10 per hit (3 hits; ignores 15% DEF) (Bleed))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Executioner's Wrath, All Foes
Turn % 3 == 0: Frenzy, Highest ATK
HP% <= 50%: Executioner's Wrath, Lowest HP%
Always: Raging Blow, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Fire: 75%, Light: 150%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Root: 75%, Stun: 40%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `8500` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `6375` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `2200` | Mata uang resmi penjelajahan |
| **Drop 1** | `Kala Crystal` (`25%`) | Material alam / crafting |
| **Drop 2** | `Spirit Thread` (`15%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`10%`) | Rampasan langka |
| **Boss / Unique Drop** | `Wrathbound Carapace` (`5%`) | Rampasan unik / piala bos |
