---
title: Belphegor
tags:
  - Bestiary
  - Boss
---

# Belphegor

## Deskripsi

Panglima Kemalasan yang tidak pernah meninggalkan singgasana keraknya. Ia menguasai gravitasi, miasma, dan racun tidur sehingga lawan dikalahkan oleh berat tubuh serta hilangnya kemauan sebelum mencapai dirinya. Diamnya bukan ketidakmampuan; seluruh Fortress of Sloth berfungsi sebagai jangkauan serangannya.

## Bentuk

Belphegor berbentuk raksasa gemuk berbatu yang menyatu dengan singgasana. Lapisan kerak menutup punggung dan pinggang, sementara sulur berlendir tumbuh dari celah batu. Gas ungu keluar perlahan dari mulut serta pori tubuhnya. Matanya nyaris selalu tertutup, tetapi singgasana bergetar ketika ia menyadari penyusup. Batas antara tubuh, lumut, jamur, dan batu menjadi sulit dibedakan setelah ia berdiam terlalu lama.

## Kepribadian dan Sikap

Belphegor apatis, sabar, dan lebih suka membuat lawan menyerah daripada bergerak untuk menghentikan mereka. Ia berbicara seolah setiap tindakan tidak berguna, menanamkan keputusasaan melalui kata-kata yang lambat. Ia tidak mengejar penghinaan dan membiarkan pasukan menjadi sasaran selama benteng tetap bekerja. Sikap ini juga menjadi kelemahannya: ia meremehkan orang yang mampu mempertahankan tujuan di tengah kelelahan dan terlambat menanggapi perubahan cepat.

## Kedudukan dan Benteng

Fortress of Sloth adalah gua jamur berisi kabut spora ungu, tulang korban tertidur, dan ilusi tempat istirahat. Belphegor menyatu dengan singgasana di Gua Tidur Abadi, sejalan dengan lokasi lama Lorong Tidur Raksamala. Seluruh ruang menguras energi dan kemauan. Konteks ini menggambarkan benteng sebelum keruntuhan Raksamala.

## Kisah - Satu Langkah Lagi

Seorang penyusup melihat tempat tidur bersih di tengah kabut dan berjanji hanya akan duduk sebentar. Suara Belphegor menyebut perjalanan itu sia-sia dan menawarkan akhir tanpa rasa sakit. Lutut penyusup hampir menyentuh kasur.

Ia menjatuhkan ransel agar tubuh lebih ringan, lalu mengambil satu langkah. Setelah setiap langkah ia mengulang nama orang yang ingin diselamatkan. Belphegor tetap diam, yakin tekad itu akan habis. Ketika suara langkah mencapai ruang singgasana, untuk pertama kalinya batu di tubuh sang panglima bergerak.

> Acuan: [Belphegor](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Belphegor.md); [Fortress of Sloth](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Sloth.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `66.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Support` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Dark` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Caster, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **103** | **46** | **40** | **77** | **73** | **108** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `20900` *(Base 18765 + VIT×15 + STR×5)* | **DEF** | `214` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `372` *(Base 4 + INT×8)* | **MDF** | `252` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `766` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `300` *(Base + INT×2)* |
| **ATK** | `226` *(Formula Magic)* | **Action Speed** | `110` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `93.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.4%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `18.7%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `22.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `188.9%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `154.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `3.24%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `1.38%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `8.08%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Abyssal Shroud** | `11 Dark` / Magical Attack | `12 MP` | Always (Prioritas 5.0) | `-` |
| **Mana Corruption** | `01 Neutral` / Magical Attack | `0 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Soul Extract** | `01 Neutral` / Magical Attack | `12 MP` | HP <= 50% (Prioritas 6.0) | `-` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Soul Extract, All Foes
Turn % 3 == 0: Mana Corruption, Highest ATK
HP% <= 50%: Soul Extract, Lowest HP%
Always: Abyssal Shroud, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Light: 150%
* **Resistensi Status:** Freeze: 40%, Paralyze: 40%, Stun: 40%
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
