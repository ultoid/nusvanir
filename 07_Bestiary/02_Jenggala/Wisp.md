---
title: Wisp
tags:
  - Bestiary
---

# Wisp

## Deskripsi

Api hantu penyesat jalan yang dikenal sebagai Kemamang. Wisp tampak seperti cahaya kecil yang dapat dijangkau dalam beberapa langkah, lalu menjauh ketika didekati. Bahayanya sering terungkap setelah pengelana tidak lagi mengenali jalan pulang, bukan ketika nyalanya pertama kali terlihat.

## Bentuk

Wujudnya kecil dan tidak padat, dengan inti cahaya pucat dikelilingi nyala yang berubah bentuk. Tepian apinya terurai seperti serabut, kemudian menyatu kembali ketika melayang. Dalam kabut, lingkaran cahaya dapat tampak lebih besar daripada sumbernya sehingga jaraknya sulit dinilai. Ia tidak diberi kaki, wajah tetap, atau pakaian untuk menjelaskan gerakannya; identitasnya tetap api hantu yang tercatat.

## Tingkah Laku

Tidak menunjukkan keganasan seperti hewan bertaring. Ia menarik perhatian dengan bergerak di batas pandangan, berhenti, lalu melanjutkan perjalanan ketika diikuti. Cahaya yang tampak memandu belum tentu membawa niat menolong. Belum dipastikan apakah penyesatan itu selalu dilakukan secara sadar atau bagaimana ia memilih korban. Wisp juga tidak otomatis menjadi bentuk muda Pyrowisp hanya karena keduanya berwujud api.

## Habitat

Rawa berkabut merupakan habitat yang tercatat yang belum memiliki region. Lahan basah berkabut di luar kawasan Valkindra menjadi tempat kemunculannya karena wilayah utara itu sudah mempunyai kabut mistis. Keberadaan rawa spesifik adalah pengembangan habitat, bukan pengubahan seluruh dataran Valkindra menjadi rawa.

## Kisah — Lampu yang Tidak Pulang

Seorang pengelana di luar Valkindra kehilangan pandangan terhadap rekannya dan melihat cahaya bergerak di depan. Ia mengikutinya sambil memanggil. Cahaya itu tidak menjawab, tetapi selalu berhenti ketika ia berhenti.

Ia baru sadar setelah pijakannya berubah menjadi lumpur dan tidak lagi menemukan bekas langkah rombongan. Dari kejauhan, panggilan rekannya datang dari arah berbeda. Pengelana itu bertahan di tanah yang masih keras sampai dijemput. Cahaya kecil tadi tetap menunggu di atas rawa, seolah perjalanan mereka belum selesai.

> Acuan: [Valkindra](../../03_Region/01_Mandala%20Kingdom/Cities%20%26%20Town/Valkindra.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `30.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Spirit` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T2 (Normal)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Water` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Flying, Burning, Caster` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **9** | **16** | **4** | **14** | **15** | **8** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `198` *(Base 33 + VIT×15 + STR×5)* | **DEF** | `17` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `26` *(INT×8)* | **MDF** | `20` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `78` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `31` *(Base + INT×2)* |
| **ATK** | `20` *(Formula Magic)* | **Action Speed** | `22` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `5.7%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `2.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `153.5%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `104.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.24%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.48%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.76%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Spirit Flame** | `02 Fire` / Magical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.15 - b.mdf * 0.45)` |
| **Wisp Pulse** | `02 Fire` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.45 - b.mdf * 0.35)` |
| **Flickering Burst** | `02 Fire` / Magical Attack | `0 SP` | HP <= 40% (Prioritas 4.0) | `Math.max(1, a.mat * 1.85 - b.mdf * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 1: Instinct-Driven AI (Naluri Alami)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran`
* **Logika Penargetan:** Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 40%: Flickering Burst, Lowest HP%
Turn 2+: Wisp Pulse, Random
Always: Spirit Flame, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Fire: 50%, Water: 150%
* **Resistensi Status:** Burn: 0%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `40` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `30` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `15` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Dust` (`50%`) | Material alam / crafting |
| **Drop 2** | `Wisp Core` (`25%`) | Komponen sekunder |
