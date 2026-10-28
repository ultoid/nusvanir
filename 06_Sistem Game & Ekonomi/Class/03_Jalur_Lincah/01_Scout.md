---
title: Scout
class_id: 10
tier: 1
branch: Jalur Lincah (Ranged / Assassin)
level_cap: 10
primary_role: Pengintai Cekatan Pemula
tags:
  - Class_Database
  - Tier_1
  - Lincah
---

# 🛡️ Database Kelas: Scout
> **Cabang:** `Jalur Lincah (Ranged / Assassin)` | **Tingkat:** `Tier 1` | **Batas Level:** `Lv. 1 – 10`

Penjelajah cekatan yang mengandalkan pengamatan, gerak cepat, dan kemampuan membaca medan untuk menghindari bahaya.

---

## 1. Profil & Identitas Peran
| Atribut Kelas | Rincian / Status |
| :--- | :--- |
| **Nama Resmi** | **Scout** |
| **Class ID Database** | `CID: 10` |
| **Tier Penguasaan** | `Tier 1` *(Level Cap: 10)* |
| **Promosi Dari** | `—` |
| **Promosi Lanjutan** | `Archer, Thief` |
| **Peran Utama** | `Pengintai Cekatan Pemula` |
| **Kelemahan Taktis** | *Standar kelemahan arketipe* |

## 2. Parameter Pertumbuhan & Karakteristik (Turn-Based RPG)

### A. 6 Base Stats (Atribut Dasar Kelas)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **3** | **1** | **8** | **5** | **8** | **3** |

* **Peringkat Atribut Dasar:** `STR: D | INT: E | DEX: A | LUK: B | AGI: A | VIT: D`
* **Pertumbuhan Stat Alami (Fixed Stat Growth per Class Level):** `+1 DEX, +1 AGI, +1 LUK`
* **Kurva Kebutuhan EXP:** `Tier 1 [22, 14, 18, 18]`

### B. Stat Turunan Awal (Baseline Derived Stats)
*Nilai di bawah dihitung deterministik dari 6 Base Stats awal kelas menggunakan formula resmi Nusvanir (sebelum bonus perlengkapan & alokasi poin pemain):*

#### 1. Sumber Daya Vital & Tempur Utama
| Parameter | Nilai Baseline | Formula / Perhitungan Resmi |
| :--- | :---: | :--- |
| **Max HP** | `110` | `Base 50 + (VIT 3 * 15) + (STR 3 * 5)` |
| **Max MP** | `28` | `Base 20 + (INT 1 * 8)` |
| **Max SP** | `41` | `Base 20 + (VIT 3 * 5) + (STR 3 * 2)` *(Preserved antar battle)* |
| **ATK** | `18` | `(DEX 8 * 2) + (STR 3 * 0.5)` *(Ranged/Finesse)* |
| **DEF** | `6` | `Base + (VIT 3 * 1.5) + (STR 3 * 0.5)` |
| **MAT** | `2` | `Base + (INT 1 * 2)` |
| **MDF** | `4` | `Base + (INT 1 * 1.2) + (VIT 3 * 0.8)` |
| **Action Speed** | `12` | `Base + (AGI 8 * 1.5)` |

#### 2. Presisi, Kritikal & Regenerasi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `86.6%` | `0.85 + (DEX 8 * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `3.9%` | `0.02 + (AGI 8 * 0.002) + (LUK 5 * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `5.1%` | `0.03 + (DEX 8 * 0.002) + (LUK 5 * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `1.0%` | `(LUK 5 * 0.0015) + (VIT 3 * 0.001)` |
| **Critical Damage (CDMG)** | `152.5%` | `1.5 + (STR 3 * 0.003) + (DEX 8 * 0.002)` |
| **Guard Efficiency (GRD)** | `101.5%` | `1.0 + (VIT 3 * 0.005)` *(Mitigasi saat bertahan)* |
| **HP Regen / Turn (HRG)** | `0.09%` | `VIT 3 * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.03%` | `INT 1 * 0.0003` |
| **SP Regen / Turn (TRG)** | `3.38%` | `0.03 + (AGI 8 * 0.0004) + (VIT 3 * 0.0002)` |

### C. Karakteristik, Sasis & Peralatan
* **Innate Trait:** `—`
* **Senjata yang Dapat Digunakan (Weapon Types):** 08 Long Bow, 09 Crossbow, 10 Dagger
* **Zirah & Pelindung (Armor Types):** 01 Basic Clothes, 03 Light Armor
* **Tipe Skill yang Dibuka (Skill Types):** `03 Skill, 05 Ultimate` *(Skill pasif aktif otomatis via YEP_AutoPassiveStates)*

## 3. Daftar Lengkap Skill & Pembelajaran (Learnings)
*Seluruh skill di bawah ini otomatis terbuka saat mencapai Class Level yang ditentukan.*

| Level | Nama Skill | Skill Type | MP / SP Cost | Scope | Hit Type / Repeat | Damage (Type, Element, Formula, Crit) | Effects & Description |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :--- |
| **Lv 1** | **Swift Stab** | `03 Skill` | `0 MP / 15 SP` | 1 Enemy | Physical Attack / 2 | **Type:** HP Damage<br>**Element:** 01 Neutral<br>**Formula:** `Math.max(1, (a.atk * 0.8) - (b.def * 0.5))`<br>**Crit:** Yes | **Efek:** -<br>**Deskripsi:** Tusukan belati kilat berturut-turut yang dirancang untuk mengoyak pertahanan cepat musuh. |
| **Lv 4** | **Fleet Footed** | `Passive` | `0 MP / 0 SP` | None | Certain Hit / 1 | **Type:** None<br>**Formula:** None | **Efek:** Auto-Passive State [0301+] (Evasion +10%, Agility +5%)<br>**Deskripsi:** Kelincahan gerak alami yang membuat penggunanya lebih mudah menghindari serangan. |
| **Lv 7** | **Poison Edge** | `03 Skill` | `10 MP / 10 SP` | 1 Enemy | Physical Attack / 1 | **Type:** HP Damage<br>**Element:** 01 Neutral<br>**Formula:** `Math.max(1, (a.atk * 1.2) - (b.def * 0.75))`<br>**Crit:** Yes | **Efek:** Add State: [0203] Poison 50% (3 Turns)<br>**Deskripsi:** Serangan berlapis racun mematikan yang menggerogoti HP target perlahan di setiap giliran. |
| **Lv 10** | **Shadow Dash** | `05 Ultimate` | `20 MP / 20 SP` | All Enemies | Physical Attack / 1 | **Type:** HP Damage<br>**Element:** 01 Neutral<br>**Formula:** `Math.max(1, (a.atk * 1.5) - (b.def * 0.75))`<br>**Crit:** Yes | **Efek:** Add State (ke diri sendiri): [0223] Shadow Mark / Stealth (2 Turns)<br>**Deskripsi:** Melesat menembus bayangan untuk menyerang seluruh musuh sekaligus menyamarkan keberadaan diri. |

---

## 4. Alur Evolusi & Percabangan Kelas
```mermaid
graph LR
    Scout["Scout (T1)"] --> Archer["Archer (T2: Bow)"]
    Scout --> Thief["Thief (T2: Dagger & Stealth)"]
    Archer --> Ranger["Ranger (T3: Trap & Wilderness)"]
    Thief --> Rogue["Rogue (T3: Ambush & Dual Blade)"]
    Ranger --> Sniper["Sniper (T4: Absolute Precision)"]
    Rogue --> Assassin["Assassin (T4: Fatal Execution)"]
```