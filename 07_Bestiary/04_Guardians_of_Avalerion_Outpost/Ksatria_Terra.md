---
title: Ksatria Terra
tags:
  - Bestiary
  - Boss
---

# Ksatria Terra

## Deskripsi

Penjaga Avalerion dengan kulit menyerupai bebatuan bercahaya, terkenal karena kemampuannya bertahan di tempat yang harus tetap tertutup. Kehadirannya membuat sebuah celah dalam barisan terasa seperti gerbang yang kembali terkunci. Ia menjaga batas sekaligus orang-orang di belakangnya, sehingga keteguhannya berguna bahkan ketika tidak ada pertempuran.

## Bentuk

Tubuhnya lebar dan kokoh, dengan lapisan batu bercahaya yang mengikuti lengan, leher, serta bagian wajah yang tidak tertutup zirah. Permukaannya bersekat seperti lempeng mineral; cahaya lembut terlihat di sela-selanya ketika tubuh bergerak. Pelindung bahu dan dada menambah kesan benteng, sementara perisai besar menutup sebagian besar tubuh saat ditegakkan. Kaki diletakkan berjauhan untuk menjaga tumpuan. Asal lapisan batu tersebut belum diketahui, termasuk apakah terbentuk sejak lahir atau muncul melalui sihir.

## Kepribadian dan Sikap

Terra pendiam, sabar, dan lebih suka mendengarkan sampai seseorang selesai berbicara. Ia memperlakukan pengunjung yang gugup dengan tenang, menjelaskan aturan gerbang tanpa mempermalukan mereka di depan kerumunan. Rekannya mengenalnya sebagai orang yang dapat diandalkan untuk menepati janji, termasuk urusan kecil yang mudah dilupakan setelah pergantian jaga. Keteguhannya kadang berubah menjadi keras kepala: ia sulit menerima perubahan rencana sebelum memahami alasannya. Namun, ia bersedia mengalah ketika keselamatan orang lain menuntutnya. Saat keadaan kacau, ia berusaha memberi orang-orang satu arahan yang jelas untuk diikuti.

## Lokasi Benteng

Outpost Bumi di perbatasan darat Avalerion dan Mandala menjadi tempat tugas Terra. Pos ini merupakan gerbang diplomatik sekaligus pertahanan utama dengan infanteri berat dan perisai suci besar. Ambang gerbang serta jalur pemeriksaan merupakan lingkungan tugas yang masuk akal bagi Terra. Catatan pos utara dipertahankan sebagai lokasi historis yang arah pastinya belum dicocokkan; penempatan ini tidak menjadikannya penguasa gerbang atau komandan tanpa sumber.

## Kisah — Ruang untuk Satu Gerobak

Roda sebuah gerobak patah di jalur pemeriksaan Bumi. Orang-orang di belakang mulai mendesak, sementara kusir berusaha menahan muatan agar tidak jatuh mengenai rekannya. Terra menegakkan perisai di sisi jalan dan meminta barisan berhenti.

Dengan ruang yang kini kosong, para pengangkut dapat memindahkan peti satu per satu. Seorang pelintas mengeluh bahwa penjaga batu itu hanya memperlambat perjalanan. Lalu ikatan terakhir terlepas dan peti jatuh tepat di tempat kerumunan tadi berdiri. Terra menunggu serpihan disingkirkan sebelum membuka jalan kembali. Tidak ada musuh yang dikalahkan hari itu, tetapi tak seorang pun tertindih.

> Acuan: [Outpost Bumi](../../03_Region/03_Avalerion/Cities%20%26%20Town/Outpost_Bumi.md); [Senopati Prabha](../../03_Region/03_Avalerion/Faksi%20%26%20Institusi/Senopati_Prabha.md); [Avalerion](../../03_Region/03_Avalerion/Avalerion.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `51.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T4 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Wind` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Holy, Earth, Armored, Shielded` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **30** | **6** | **12** | **28** | **23** | **33** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `1375` *(Base 730 + VIT×15 + STR×5)* | **DEF** | `65` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `51` *(Base 3 + INT×8)* | **MDF** | `53` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `245` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `47` *(Base + INT×2)* |
| **ATK** | `66` *(Formula Melee)* | **Action Speed** | `34` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `87.4%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `8.0%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `8.2%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `7.5%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `161.4%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `116.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `0.99%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.18%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `4.58%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Shield Bash** | `Neutral` / Physical Attack | `10 SP` | Always (Prioritas 5.0) | `(a.atk * 0.6 + a.def * 0.8) - b.def * 0.5 (Stun 30%)` |
| **Shield Wall** | `Neutral` / Certain Hit | `18 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Granite Rampart** | `Earth` / Magical Attack | `24 SP` | HP <= 40% (Prioritas 4.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Earth: 75%, Light: 50%, Wind: 150%
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
