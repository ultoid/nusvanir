---
title: Luciferus
tags:
  - Bestiary
  - Boss
---

# Luciferus

## Deskripsi

Panglima Keangkuhan dan jenderal terkuat di bawah Sangrahal. Ia menguasai sihir kosmik serta ilusi yang menyerang harga diri. Luciferus menganggap manusia dan elf sebagai hama; hanya lawan yang mencapai takhtanya tanpa berlutut dianggap cukup berarti untuk menerima serangan langsung.

## Bentuk

Luciferus adalah Bhuta bersayap enam dengan cahaya emas yang telah terkorupsi. Wajahnya tampak sempurna dan tenang, sedangkan mata serta aura membuat orang di hadapannya merasa kecil. Zirah gelap mengikuti bentuk tubuh tanpa menutupi pangkal sayap. Listrik hitam-emas bergerak di antara bulu ketika sihir dihimpun. Cermin obsidian benteng memantulkan dirinya lebih terang daripada lingkungan, memperkuat ilusi bahwa seluruh menara dibangun untuk satu sosok.

## Kepribadian dan Sikap

Luciferus angkuh, menghina, dan menuntut pengakuan atas keunggulannya. Ia jarang meninggikan suara karena menganggap perintahnya tidak membutuhkan penjelasan. Penantang yang menolak tunduk menarik perhatiannya sekaligus melukai egonya. Ia bersaing dengan Ksatria Agung Galathius sebagai lawan yang cukup kuat untuk diakui, meski pengakuan itu selalu dibungkus penghinaan. Kesombongan memberinya keteguhan, tetapi juga membuatnya menunda tindakan sampai musuh membuktikan diri di hadapan takhtanya.

## Kedudukan dan Benteng

Fortress of Pride adalah menara utara berlapis cermin obsidian yang menampilkan kemegahan palsu. Luciferus menunggu di puncak Menara Tanpa Bayangan, setelah penyusup melewati ilusi kesempurnaan diri. Lokasi ini sesuai Benteng Pride Utara dalam data lama. Narasi benteng berlaku sebelum kehancuran peradaban Raksamala.

## Kisah - Mereka yang Tidak Berlutut

Seorang penantang mencapai ruang takhta dengan zirah rusak. Setiap cermin menampilkan dirinya sebagai raja, penyelamat, dan makhluk yang lebih agung daripada rekannya. Luciferus memintanya berlutut agar salah satu gambaran itu menjadi nyata.

Penantang tersebut menutup mata dan mengakui bahwa ia takut serta membutuhkan bantuan orang lain untuk tiba di sana. Cermin-cermin kehilangan sosok sempurna yang dapat ditelan. Luciferus akhirnya berdiri dari takhta. Ia membenci jawaban itu, sebab kerendahan hati telah membawa lawannya melewati ujian yang dirancang untuk kesombongan.

> Acuan: [Luciferus](../../05_Karakter%20%26%20Tokoh%20Penting/09_Raksamala/Luciferus.md); [Fortress of Pride](../../03_Region/10_Raksamala/Cities%20%26%20Town/Fortress%20of%20Pride.md); [Bhuta](../../04_Ras/04_Drahkthar/Bhuta.md); [Kerajaan Drahkthar](../../03_Region/10_Raksamala/Faksi%20%26%20Institusi/Kerajaan%20Drahkthar.md); [Threat](../../03_Region/10_Raksamala/Threat.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `68.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Demon` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Mage` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T8 (Commander)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Dark/Fire` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Light` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Demonic, Caster, Corrupted` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **90** | **170** | **36** | **70** | **73** | **97** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `19800` *(Base 17895 + VIT×15 + STR×5)* | **DEF** | `191` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `386` *(INT×8)* | **MDF** | `231` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `685` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `339` *(Base + INT×2)* |
| **ATK** | `198` *(Formula Magic)* | **Action Speed** | `110` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `92.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `20.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `17.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `20.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `184.2%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `148.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `2.91%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `5.10%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `7.86%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Dark Energy** | `11 Dark` / Magical Attack | `8 MP` | Always (Prioritas 5.0) | `Math.max(1, a.mat * 1.4 - b.mdf * 0.4 (Curse 25%))` |
| **Flame Burst** | `02 Fire` / Magical Attack | `12 MP` | Turn 2+ / 50% chance (Prioritas 4.0) | `Math.max(1, a.mat * 1.9 - b.mdf * 0.4 (Burn 50%))` |
| **Dark Purgatory** | `11 Dark` / Magical Attack | `25 MP` | HP <= 50% (Prioritas 6.0) | `Math.max(1, a.mat * 1.8 - b.mdf * 0.3)` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Dark Purgatory, All Foes
Turn % 3 == 0: Flame Burst, Highest ATK
HP% <= 50%: Dark Purgatory, Lowest HP%
Always: Dark Energy, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 50%, Fire: 75%, Light: 150%
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
| **Boss / Unique Drop** | `Crown of the Black Covenant / Black Covenant Signet` (`5%`) | Rampasan unik / piala bos |
