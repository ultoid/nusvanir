---
title: Ksatria Vayu
tags:
  - Bestiary
  - Boss
---

# Ksatria Vayu

## Deskripsi

Ksatria Avalerion yang membelah formasi dengan badai bercahaya dan perubahan arah yang cepat. Ia dikenal dari hembusan yang datang sebelum sosoknya melintas. Gerakannya membantu menghubungkan bagian medan yang terpisah, membawa tekanan ke titik yang terbuka atau memberi ruang bagi rekan yang harus bergerak mundur.

## Bentuk

Siluetnya lebih ramping daripada penjaga berperisai besar. Zirah berlapis mengikuti dada dan paha, dengan sambungan lentur pada pinggang serta lutut. Kain pendek terikat di belakang bahu, memperlihatkan arah angin ketika tubuh berhenti. Cahaya tipis berpilin di sekitar lengan dan kaki saat hembusan dikumpulkan. Ketika melesat, garis cahaya tertinggal sesaat seperti pita yang ditarik dari udara. Perlengkapannya memberi keleluasaan untuk bergerak cepat di antara posisi penjagaan.

## Kepribadian dan Sikap

Vayu sigap dan waspada, dengan kebiasaan berbicara singkat saat bertugas. Ia memperhatikan perubahan suasana dan cepat menyadari ketika seorang rekan tertinggal atau enggan meminta bantuan. Kesabarannya mudah diuji oleh perdebatan yang berlarut, terutama ketika ada pesan penting yang harus disampaikan. Meski begitu, ia berusaha memastikan orang lain memahami arahannya sebelum bergerak. Di luar keadaan genting, ia lebih santai dan senang mendengar kabar dari petugas yang baru kembali. Ia bangga pada kecepatannya, tetapi lebih mengutamakan keselamatan rekan daripada kesempatan membuktikan diri melalui pengejaran yang berisiko.

## Lokasi Benteng

Outpost Bayu di tebing dekat kanopi Astradipa menjadi tempat tugas Vayu. Pos ini berfokus pada mobilitas udara, serangan cepat, dan dukungan logistik, kadang dibantu Garuda dari Nusa Sayendra. Tepian pelataran serta jalur penghubung di tebing cocok untuk kegiatan pengawasan. Nama Vayu tidak memastikan bahwa ia komandan Bayu, dan catatan lama tentang pos selatan belum mendapatkan pemetaan arah yang pasti.

## Kisah — Pesan Sebelum Badai

Angin berubah saat seorang pembawa pesan mencapai pelataran Bayu. Kain penandanya menegang ke arah berbeda dari awan, dan petugas di tepi tebing menghentikan keberangkatan rombongan. Vayu menunggu satu hembusan lewat sambil memperhatikan pucuk-pucuk kanopi.

Ia kemudian bergerak menuju pelataran penghubung, membawa pesan agar rombongan berikutnya bertahan di tempat terlindung. Cahaya melintas pendek di antara batu, lalu hilang di balik dinding pos. Ketika badai menutup pandangan, tidak ada orang yang masih berdiri menunggu di tepian terbuka. Hari itu kecepatannya berguna untuk menyampaikan peringatan sebelum orang lain harus berlari.

> Acuan: [Outpost Bayu](../../03_Region/03_Avalerion/Cities%20%26%20Town/Outpost_Bayu.md); [Senopati Prabha](../../03_Region/03_Avalerion/Faksi%20%26%20Institusi/Senopati_Prabha.md); [Avalerion](../../03_Region/03_Avalerion/Avalerion.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `52.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Assassin` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T4 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Wind` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Earth` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Holy, Wind` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **35** | **7** | **12** | **32** | **35** | **18** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `990` *(Base 545 + VIT×15 + STR×5)* | **DEF** | `44` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `57` *(Base 1 + INT×8)* | **MDF** | `43` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `180` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `54` *(Base + INT×2)* |
| **ATK** | `76` *(Formula Melee)* | **Action Speed** | `52` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `10.6%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `8.6%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `6.6%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `162.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `109.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.54%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.21%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.76%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Quick Shot** | `01 Neutral` / Physical Attack | `4 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.5 (Priority +2))` |
| **Aero Slash** | `05 Air` / Magical Attack | `12 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 2.1 - b.mdef * 0.2 (Float 50%))` |
| **Piercing Arrow** | `01 Neutral` / Physical Attack | `6 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.atk * 1.5 - b.def * 0.3 (Ignore 20% DEF))` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Piercing Arrow, Lowest HP%
State === Taunt: Aero Slash, Random
Turn % 2 == 0: Aero Slash, Random
Always: Quick Shot, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Earth: 150%, Light: 50%, Wind: 75%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `260` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `195` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `80` | Mata uang resmi penjelajahan |
| **Drop 1** | `Silver` (`25%`) | Material alam / crafting |
| **Drop 2** | `Mana Crystal` (`20%`) | Komponen sekunder |
