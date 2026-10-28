---
title: Fighter
class_id: 10
tier: 1
branch: Jalur Fisik (Melee / Tank)
level_cap: 10
primary_role: Petarung Pemula
tags:
  - Class_Database
  - Tier_1
  - Fisik
---

# 🛡️ Database Kelas: Fighter
> **Cabang:** `Jalur Fisik (Melee / Tank)` | **Tingkat:** `Tier 1` | **Batas Level:** `Lv. 1 – 10`

Petarung yang mengandalkan keberanian, latihan dasar, dan naluri tempur untuk menghadapi bahaya Nusvanir.

---

## 1. Profil & Identitas Peran
| Atribut Kelas | Rincian / Status |
| :--- | :--- |
| **Nama Resmi** | **Fighter** |
| **Class ID Database** | `CID: 10` |
| **Tier Penguasaan** | `Tier 1` *(Level Cap: 10)* |
| **Promosi Dari** | `—` |
| **Promosi Lanjutan** | `Warrior, Squire, Brawler` |
| **Peran Utama** | `Petarung Pemula` |
| **Kelemahan Taktis** | *Standar kelemahan arketipe* |

## 2. Parameter Pertumbuhan & Karakteristik (Turn-Based RPG)

### A. 6 Base Stats (Atribut Dasar Kelas)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **9** | **1** | **3** | **4** | **4** | **7** |

* **Peringkat Atribut Dasar:** `STR: A | INT: E | DEX: C | LUK: C | AGI: C | VIT: B`
* **Pertumbuhan Stat Alami (Fixed Stat Growth per Class Level):** `+2 STR, +1 VIT`
* **Kurva Kebutuhan EXP:** `Tier 1 [25, 15, 20, 20]`

### B. Stat Turunan Awal (Baseline Derived Stats)
*Nilai di bawah dihitung deterministik dari 6 Base Stats awal kelas menggunakan formula resmi Nusvanir (sebelum bonus perlengkapan & alokasi poin pemain):*

#### 1. Sumber Daya Vital & Tempur Utama
| Parameter | Nilai Baseline | Formula / Perhitungan Resmi |
| :--- | :---: | :--- |
| **Max HP** | `200` | `Base 50 + (VIT 7 * 15) + (STR 9 * 5)` |
| **Max MP** | `28` | `Base 20 + (INT 1 * 8)` |
| **Max SP** | `73` | `Base 20 + (VIT 7 * 5) + (STR 9 * 2)` *(Preserved antar battle)* |
| **ATK** | `20` | `(STR 9 * 2) + (DEX 3 * 0.5)` *(Melee)* |
| **DEF** | `15` | `Base + (VIT 7 * 1.5) + (STR 9 * 0.5)` |
| **MAT** | `2` | `Base + (INT 1 * 2)` |
| **MDF** | `7` | `Base + (INT 1 * 1.2) + (VIT 7 * 0.8)` |
| **Action Speed** | `6` | `Base + (AGI 4 * 1.5)` |

#### 2. Presisi, Kritikal & Regenerasi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `85.6%` | `0.85 + (DEX 3 * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `3.0%` | `0.02 + (AGI 4 * 0.002) + (LUK 4 * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `4.0%` | `0.03 + (DEX 3 * 0.002) + (LUK 4 * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `1.3%` | `(LUK 4 * 0.0015) + (VIT 7 * 0.001)` |
| **Critical Damage (CDMG)** | `153.3%` | `1.5 + (STR 9 * 0.003) + (DEX 3 * 0.002)` |
| **Guard Efficiency (GRD)** | `103.5%` | `1.0 + (VIT 7 * 0.005)` *(Mitigasi saat bertahan)* |
| **HP Regen / Turn (HRG)** | `0.21%` | `VIT 7 * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT 1 * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.30%` | `0.03 + (AGI 4 * 0.0004) + (VIT 7 * 0.0002)` |

### C. Karakteristik, Sasis & Peralatan
* **Innate Trait:** `—`
* **Senjata yang Dapat Digunakan:** `Sword, Long Sword, Gloves, Spear, Axe`
* **Zirah & Pelindung:** `Basic Armor, Light Armor, Light Shield`
* **Tipe Skill yang Dibuka:** `Physical, Support, Passive`

## 3. Daftar Lengkap Skill & Pembelajaran (Learnings)
*Seluruh skill di bawah ini otomatis terbuka saat mencapai Class Level yang ditentukan.*

| Level | Nama Skill | Tipe / Elemen | Biaya | Target | Formula / Efek Matematis | Deskripsi & Catatan |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
| **1** | **Dash** | `Physical` / `Neutral` | `10 SP` | Self | `-` | Manuver lari cepat untuk menutup celah atau mengatur posisi bertarung. |
| **1** | **Charge Attack** | `Physical` / `Neutral` | `15 SP` | 1 Target | `Math.max(0, a.atk * 1.3 - b.def * 0.4)` | Tebasan keras terarah yang memanfaatkan bobot tubuh. |
| **1** | **Weapon Mastery** | `Passive` / `Neutral` | `0 SP` | Self | `-` | Keahlian bawaan yang meningkatkan Physical Attack secara permanen. |
| **1** | **Vitality Mastery** | `Passive` / `Neutral` | `0 SP` | Self | `-` | Keahlian ketahanan tubuh yang meningkatkan P.DEF dan M.DEF. |
| **3** | **Cyclone Sweep** | `Physical` / `Neutral` | `25 SP` | All Enemies | `Math.max(0, a.atk * 1.1 - b.def * 0.3)` | Ayunan senjata memutar yang melukai seluruh musuh di sekitar. |
| **5** | **Fatal Blow** | `Physical` / `Neutral` | `20 SP` | 1 Target | `Math.max(0, a.atk * 1.6 - b.def * 0.35) (Crit Rate +20%)` | Hantaman presisi pada titik lemah target dengan peluang kritikal tinggi. |
| **7** | **Impact Wave** | `Physical` / `Earth` | `30 SP` | 1 Target | `Math.max(0, a.atk * 1.4 + a.vit * 0.5 - b.def * 0.3)` | Menghantamkan senjata ke tanah untuk melepaskan gelombang kejut. |
| **9** | **Provoke** | `Support` / `Neutral` | `15 SP` | 1 Target | `-` | Meneriakkan tantangan untuk menarik target rate (TGR) musuh ke diri sendiri. |

---

## 4. Alur Evolusi & Percabangan Kelas
```mermaid
graph LR
    Fighter["Fighter (T1)"] --> Warrior["Warrior (T2: Offense)"]
    Fighter --> Squire["Squire (T2: Defense)"]
    Fighter --> Brawler["Brawler (T2: Agility)"]
    Warrior --> Mercenary["Mercenary (T3)"]
    Squire --> Knight["Knight (T3)"]
    Brawler --> MartialArtist["Martial Artist (T3)"]
    Mercenary --> Dragoon["Dragoon (T4: Aerial)"]
    Knight --> Champion["Champion (T4: Tank Juggernaut)"]
    Knight --> Paladin["Paladin (T4: Holy Guard)"]
    MartialArtist --> Monk["Monk (T4: Chi Burst)"]
```