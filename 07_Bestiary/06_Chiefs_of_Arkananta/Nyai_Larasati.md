---
title: Nyai Larasati
tags:
  - Bestiary
  - Boss
---

# Nyai Larasati

## Deskripsi

Pemimpin Rakshorien buangan yang memilih kehidupan damai di gua tersembunyi Arkananta. Nyai Larasati mengembangkan botani bawah tanah, Pemujaan Spora, serta ramuan penetral gas beracun. Sihir air dan getaran alam membantunya merawat kebun jamur sekaligus melindungi komunitas yang menolak jalan kekerasan Rakshorien lain.

## Bentuk

Larasati adalah Dark Elf yang sangat sepuh dengan tubuh ramping dan kulit pucat gelap. Kedua matanya berwarna ungu terang sepenuhnya, hasil kehidupan panjang dalam kegelapan gua. Telinganya meruncing, sedangkan kuku hitam yang diwarisi fisiologi Rakshorien dijaga tetap pendek agar tidak merusak tanaman obat. Ia mengenakan jubah dari tenunan serat dan jamur yang berpendar lembut. Botol ramuan tergantung pada sabuknya, dan sebuah tongkat bercabang membantu mengarahkan aliran air serta getaran melalui lantai batu.

## Kepribadian dan Sikap

Larasati tenang, penuh pertimbangan, dan protektif kepada para pelarian yang mempercayakan hidup kepadanya. Ia tidak mudah menerima orang luar ke kebun spora, tetapi memilih bertanya sebelum menghakimi. Pengalaman panjang membuat tutur katanya lembut sekaligus sulit dibantah. Ia membenci kekerasan yang dilakukan hanya demi kesenangan, sehingga menjaga jarak dari faksi Rakshorien yang memilih jalan bandit. Dalam barter ia berhati-hati dan merahasiakan hubungan dagangnya dengan Krom. Ketika komunitasnya terancam, kelembutan itu berubah menjadi ketegasan seorang pemimpin yang memahami racun, penyembuhan, dan medan guanya.

## Kedudukan dan Wilayah

Larasati memimpin komunitas kecil Rakshorien damai di Gua Wisamaya, wilayah gelap yang dipenuhi tumbuhan, jamur, dan spora beracun. Kebun spora serta jamur penyembuh menjadi sumber pangan, obat, ritual, dan barter. Gua Air Mata Air Arkananta pada catatan lama ditempatkan sebagai ruang mata air di dalam kompleks gua, tempat Larasati mengumpulkan air untuk ramuan dan melatih sihirnya. Penempatan ini menyelaraskan lokasi lama tanpa menciptakan permukiman Rakshorien kedua.

## Kisah — Barter di Bawah Cahaya Jamur

Krom datang melalui jalur tersembunyi dengan bungkusan daging monster. Larasati telah menyiapkan jamur obat, tetapi menemukan noda busuk pada salah satu potongan. Pengawal Rakshorien meraih senjata, mengira Butoraksa mencoba menipu mereka.

Larasati meminta semua orang menunggu. Ia memperlihatkan perubahan warna pada serat daging dan menjelaskan racun gas yang terserap selama perjalanan. Krom memerintahkan bagian itu dibuang, lalu menambah kulit samak sebagai pengganti. Barter selesai tanpa pertumpahan darah. Sebelum berpisah, Larasati memberinya sedikit ramuan untuk jalur pulang. Hubungan mereka tetap rahasia dan penuh kewaspadaan, tetapi malam itu pengetahuan sang Nyai mencegah kedua suku mengubah kesalahan menjadi perang.

> Acuan: [Nyai Larasati](../../05_Karakter%20%26%20Tokoh%20Penting/05_Arkananta/Nyai%20Larasati.md); [Rakshorien (Dark Elf)](../../04_Ras/02_Wuru%20Loka/Rakshorien_%28Dark_Elf%29.md); [Gua Wisamaya](../../03_Region/05_Arkananta/Cities%20%26%20Town/Gua%20Wisamaya.md); [Religion](../../03_Region/05_Arkananta/Religion.md); [Economy](../../03_Region/05_Arkananta/Economy.md); [Pegunungan Arkananta](../../03_Region/05_Arkananta/Arkananta.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `59.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Controller` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T5 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Magic` | Formula serangan dasar |
| **Elemen Utama** | `Water/Sound` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Caster, Water, Sonic` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **42** | **16** | **16** | **47** | **38** | **41** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `4940` *(Base 4115 + VIT×15 + STR×5)* | **DEF** | `83` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `130` *(Base 2 + INT×8)* | **MDF** | `89` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `309` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `121` *(Base + INT×2)* |
| **ATK** | `92` *(Formula Magic)* | **Action Speed** | `57` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `88.2%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `11.9%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `10.9%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `11.2%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `165.8%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `120.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.23%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.48%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.34%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Aqua Jet** | `Water` / Magical Attack | `12 SP` | Always (Prioritas 5.0) | `a.mat * 1.9 - b.mdef * 0.2 (Soaked 50%)` |
| **Ultrasonic Pulse** | `Sound` / Magical Attack | `22 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `a.mat * 1.3 - b.mdf * 0.3` |
| **Tidal Resonance** | `Water` / Certain Hit | `30 SP` | HP <= 50% (Prioritas 6.0) | `-` |

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Lightning: 150%, Sound: 75%, Water: 75%
* **Resistensi Status:** Freeze: 50%, Paralyze: 50%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1540` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1155` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `455` | Mata uang resmi penjelajahan |
| **Drop 1** | `Spirit Stone` (`25%`) | Material alam / crafting |
| **Drop 2** | `Mana Crystal` (`20%`) | Komponen sekunder |
| **Drop 3** | `Astradipa Silk` (`15%`) | Rampasan langka |
| **Boss / Unique Drop** | `Larasati Tide Robe / Larasati Waterglass Ring / Larasati Resonance Relic` (`5%`) | Rampasan unik / piala bos |
