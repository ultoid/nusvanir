---
title: Paus Penelan Armada
tags:
  - Bestiary
  - Laut_Rangkaruna
---

# Paus Penelan Armada

## Deskripsi

Paus hitam sebesar gunung yang tidak sengaja memburu kapal, tetapi dapat menelan armada ketika membuka mulut untuk menyaring krill raksasa. Bahayanya lahir dari skala tubuh dan ketidakpedulian terhadap benda kecil di jalur makannya.

## Bentuk

Tubuhnya hitam kelam dengan punggung luas menyerupai pulau bergerak. Mulut memenuhi bagian depan kepala dan memiliki lempeng penyaring besar. Bekas teritip serta karang kecil tumbuh pada kulit tua. Sirip samping bergerak lambat, tetapi satu kibasan menggeser air dalam volume besar. Lubang napas menghasilkan semburan yang terlihat melampaui kabut.

## Tingkah Laku

Cenderung tenang dan tidak sengaja menyerang. Ia mengikuti kawanan krill, membuka mulut, lalu terus berenang tanpa membedakan organisme dan kapal. Benturan atau suara dekat kepala dapat membuatnya berubah arah secara mendadak, menciptakan gelombang tambahan. Menyerangnya dapat memperburuk bahaya bagi armada di sekitar.

## Habitat

Laut lepas Zona Badai Abadi, pada jalur migrasi krill raksasa dan air yang cukup dalam untuk tubuhnya. Ia menghindari Perairan Dangkal serta gugusan karang Kuburan Kapal.

## Kisah - Jalur Makan yang Berubah

Kawanan krill berpindah mengikuti arus malam. Paus besar berbelok bersama mereka, dan beberapa bangkai kapal hanyut tepat di depan mulutnya. Ia menelan semuanya tanpa memperlambat gerak. Setelah kawanan turun, paus menutup mulut dan menyelam; permukaan baru menunjukkan gelombang panjang setelah tubuhnya menghilang.

> Acuan: [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md); [Laut Rangkaruna](../../03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `78.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Aquatic` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Water` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Aquatic, Large, Ancient` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **114** | **28** | **44** | **70** | **59** | **137** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `20000` *(Base 17375 + VIT×15 + STR×5)* | **DEF** | `262` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `221` *(INT×8)* | **MDF** | `215` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `933` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `182` *(Base + INT×2)* |
| **ATK** | `250` *(Formula Melee)* | **Action Speed** | `88` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.8%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `17.3%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `18.8%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `24.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `193.0%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `168.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `4.11%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.84%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.10%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Hullbreaker Ram** | `03 Water` / Physical Attack | `0 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.45 (Stun 25%))` |
| **Abyssal Bellow** | `11 Dark` / Physical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.atk * 1.45 - b.def * 0.35 (Silence 35%))` |
| **Devour Armada** | `03 Water` / Physical Attack | `0 SP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.atk * 1.85 - b.def * 0.25)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Devour Armada, All Foes
Turn % 3 == 0: Abyssal Bellow, Highest ATK
HP% <= 50%: Devour Armada, Lowest HP%
Always: Hullbreaker Ram, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Water: 50%
* **Resistensi Status:** Freeze: 50%, Instant Death: 0%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `5950` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `4462` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `1540` | Mata uang resmi penjelajahan |
| **Drop 1** | `Primordial Crystal` (`25%`) | Material alam / crafting |
| **Drop 2** | `Spirit Stone` (`18%`) | Komponen sekunder |
| **Drop 3** | `Orichalcum` (`10%`) | Rampasan langka |
| **Boss / Unique Drop** | `Crown of Drowned Hunger` (`5%`) | Rampasan unik / piala bos |
