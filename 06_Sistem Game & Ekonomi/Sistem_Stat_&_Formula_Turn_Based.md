---
title: Sistem_Stat_&_Formula_Turn_Based
tags:
  - Sistem_Game_Ekonomi
  - Stat_System
  - Turn_Based_RPG
---

# ⚔️ Sistem Atribut & Stat Turunan (Turn-Based RPG) Nusvanir

Dokumen ini adalah acuan resmi sistem atribut, stat turunan (*derived stats*), dan mekanik *Stamina Points (SP)* untuk game RPG *Turn-Based* Nusvanir. Untuk alur kalkulasi damage riil, giliran ATB, TGR, dan AI musuh, lihat [Sistem_Resolusi_Combat_&_AI.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Sistem_Resolusi_Combat_&_AI.md).

---

## 1. Enam Atribut Dasar (Base Stats)

Setiap entitas di dunia Nusvanir (Karakter Pemain, NPC Tempur, Monster, dan Boss) memiliki 6 atribut dasar utama:

| Atribut | Nama Lengkap | Peran Utama Desain |
| :---: | :--- | :--- |
| **STR** | *Strength* | Daya serang fisik jarak dekat, penambah HP dasar, batas kapasitas SP, dan pelipat *Critical Damage*. |
| **INT** | *Intelligence* | Daya hancur sihir (MAT), ketahanan sihir (MDF), batas kapasitas Mana (Max MP), dan regenerasi MP. |
| **DEX** | *Dexterity* | Akurasi serangan (HIT), serangan senjata lincah/jarak jauh (*Ranged/Finesse*), dan peluang *Critical Rate*. |
| **LUK** | *Luck* | Peluang serangan kritikal (CRI), penghindaran kritikal musuh (CEV), dan peluang menghindar sekunder. |
| **AGI** | *Agility* | Urutan giliran bertindak (*Action Speed / Turn Order*), peluang menghindar (EVA), dan regenerasi SP alami. |
| **VIT** | *Vitality* | Daya tahan fisik (DEF), kapasitas darah utama (Max HP), efisiensi pertahanan (GRD), dan kapasitas SP. |

### Mekanisme Poin Stat Karakter (Level Up)
* **Poin per Level:** Setiap kali karakter naik 1 *Base Level*, pemain memperoleh **3 Stat Points** (nilai default) yang bebas dialokasikan ke 6 Base Stats.
* **Fitur Reset Stat:** Terdapat mekanisme/layanan reset stat (melalui item khusus seperti *Tirta Penyucian* atau NPC Tetua/Gilda) untuk merombak kembali distribusi poin pemain.

---

## 2. Rumus Stat Turunan (Derived Stats)

Semua parameter tempur diturunkan secara deterministik dari 6 Base Stats menggunakan formula berikut:

### A. Sumber Daya Vital (Health, Mana, Stamina)
* **Max HP** = $\text{Base Class HP} + (\text{VIT} \times 15) + (\text{STR} \times 5) + \text{Flat HP Item}$
* **Max MP** = $\text{Base Class MP} + (\text{INT} \times 8) + \text{Flat MP Item}$
* **Max SP** = $\text{Base SP} + (\text{VIT} \times 5) + (\text{STR} \times 2) + \text{Flat SP Item}$

### B. Parameter Serangan & Pertahanan
* **ATK (Serangan Fisik):**
  * *Senjata Melee biasa:* $(\text{STR} \times 2) + (\text{DEX} \times 0.5) + \text{Weapon ATK}$
  * *Senjata Ranged / Finesse (Bow, Crossbow, Dagger):* $(\text{DEX} \times 2) + (\text{STR} \times 0.5) + \text{Weapon ATK}$
* **DEF (Pertahanan Fisik):**
  * $\text{Base DEF} + (\text{VIT} \times 1.5) + (\text{STR} \times 0.5) + \text{Armor DEF}$
* **MAT (Serangan Magis):**
  * $\text{Base MAT} + (\text{INT} \times 2) + \text{Equip MAT}$
* **MDF (Pertahanan Magis):**
  * $\text{Base MDF} + (\text{INT} \times 1.2) + (\text{VIT} \times 0.8) + \text{Equip MDF}$
* **Action Speed (Kecepatan Aksi / AGI):**
  * $\text{Base AGI} + (\text{AGI} \times 1.5) + \text{Equip AGI}$

### C. Parameter Presisi, Evasion, & Kritikal
* **Hit Rate (HIT):**
  * $0.85 + (\text{DEX} \times 0.002) + \text{Equip HIT}$ *(Maksimum Cap: 100%)*
* **Evasion Rate (EVA):**
  * $0.02 + (\text{AGI} \times 0.002) + (\text{LUK} \times 0.0005) + \text{Equip EVA}$ *(Maksimum Cap: 80%)*
* **Critical Rate (CRI):**
  * $0.03 + (\text{DEX} \times 0.002) + (\text{LUK} \times 0.001) + \text{Equip CRI}$ *(Maksimum Cap: 85%)*
* **Critical Evasion (CEV):**
  * $(\text{LUK} \times 0.0015) + (\text{VIT} \times 0.001) + \text{Equip CEV}$
* **Critical Damage (CDMG):**
  * $1.5 + (\text{STR} \times 0.003) + (\text{DEX} \times 0.002) + \text{Equip CDMG}$ *(Base multiplier: 150%)*
* **Guard Efficiency (GRD):**
  * $1.0 + (\text{VIT} \times 0.005) + \text{Equip GRD}$ *(Meningkatkan mitigasi saat melakukan Guard/Bertahan)*

### D. Parameter Regenerasi Per Giliran (Regen per Turn)
* **HP Regen (HRG):** $(\text{VIT} \times 0.0003) + \text{Equip HRG}$ *(0.03% HP per poin VIT)*
* **MP Regen (MRG):** $(\text{INT} \times 0.0003) + \text{Equip MRG}$ *(0.03% MP per poin INT)*
* **SP Regen (TRG):** $0.03 + (\text{AGI} \times 0.0004) + (\text{VIT} \times 0.0002) + \text{Equip TRG}$ *(Base 3% + 0.04% per AGI + 0.02% per VIT)*

---

## 3. Sistem Dua Tingkat Level (Dual Level System)

Sistem perkembangan karakter memisahkan progres personal dengan penguasaan profesi:

### 1. Base Level
* **Sumber Progres:** Diperoleh dari akumulasi **Base EXP** (pertempuran, penyelesaian misi/quest, dan eksplorasi).
* **Alokasi Poin Bebas:** Setiap kali karakter naik 1 *Base Level*, pemain memperoleh **3 Stat Points** yang bebas didistribusikan ke 6 Base Stats melalui modul sistem `NUSV_StatSystem`.
* **Karakteristik:** Base Level bersifat universal dan melekat pada karakter independen dari class apa pun yang sedang dipakai.

### 2. Class Level
* **Sumber Progres:** Diperoleh dari **Class EXP** saat bertarung menggunakan profesi/Class yang sedang aktif.
* **Progres Independen:** Setiap Class menyimpan level penguasaannya sendiri secara terpisah. Ketika pemain berganti Class (misal dari *Fighter* ke *Scout*), level *Fighter* tetap tersimpan dan tidak ter-reset.
* **Batas Maksimum Level (Level Cap) per Tier:**
  * **Tier 1 (Novice):** Level 1 – 10
  * **Tier 2 (Initiate):** Level 1 – 30
  * **Tier 3 (Adept):** Level 1 – 40
  * **Tier 4 (Master):** Level 1 – 50
  * **Tier 5 (Apex):** Level 1 – 60 *(Coming Soon / Endgame)*
* **Pertumbuhan Stat Alami (Fixed Stat Growth):** Selain poin bebas pemain, setiap kenaikan Class Level memberikan bonus Base Stat tetap yang spesifik sesuai karakter arketipe profesi tersebut (misal: *Warrior* menambah STR/VIT, *Magician* menambah INT, *Archer* menambah DEX/AGI).
* **Membuka Skill Baru (Learnings):** Kenaikan Class Level menjadi prasyarat pembuka skill aktif dan pasif baru pada daftar *Learnings* class di database.

---

## 4. Sistem SP (Stamina Points)

SP menggantikan sistem TP tradisional:
1. **Dinamis Berskala:** Nilai maksimum SP tidak lagi terkunci tetap di angka 100, melainkan berskala dinamis mengikuti stat fisik karakter: $\text{Base SP} + (\text{VIT} \times 5) + (\text{STR} \times 2) + \text{Item SP}$.
2. **Preserve SP (Disimpan Antar Battle):** SP tidak direset ke 0 saat pertempuran usai. Sisa SP karakter tetap tersimpan untuk pertempuran berikutnya, memungkinkan perencanaan combo skill fisik jarak jauh/panjang di dungeon.
3. **Pemulihan Penuh (Recover All):** Ketika beristirahat di Penginapan (*Inn*), berkemah (*Campfire*), atau memicu event *Recover All*, SP akan dipulihkan secara penuh 100% bersamaan dengan pemulihan HP dan MP.
4. **Aliran Skill:** Skill-skill kategori fisik, bela diri (*Martial Arts*), manuver senjata, dan teknik *stance* mengonsumsi SP, sementara sihir murni mengonsumsi MP.

