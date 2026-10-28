---
title: Ksatria Solarius
tags:
  - Bestiary
  - Boss
---

# Ksatria Solarius

## Deskripsi

Ksatria Avalerion yang menghadang kegelapan dengan perisai api suci. Nyala di hadapannya menjadi tanda bagi rekan di belakang untuk merapat, bukan alasan untuk maju tanpa perlindungan. Ia dikenal sebagai penjaga yang sanggup menerima tekanan di garis depan sambil membuka ruang bagi barisan lain untuk mengatur kembali langkah.

## Bentuk

Zirahnya menutup dada dan bahu dalam bidang lebar, dengan tepian keemasan yang menangkap cahaya api. Ketopong membingkai wajah seperti garis sinar yang menyebar dari dahi, sedangkan kain pelindung di belakang tubuh terikat agar tidak menyapu nyala. Perisainya tampak padat di bagian tengah dan dikelilingi lidah api terang pada pinggirannya. Ketika diangkat, pantulan pada lengan membuat batas antara logam dan cahaya sulit dibedakan. Api suci menjadi ciri utamanya, tanpa menetapkan bahwa semua perlengkapan yang dikenakan selalu terbakar.

## Kepribadian dan Sikap

Solarius disiplin dan terus terang. Ia menghargai kesiapan, ketepatan janji, serta keberanian mengakui kesalahan. Cara bicaranya tegas dan kadang terdengar kaku bagi orang yang baru mengenalnya, tetapi ia bersedia menjelaskan alasan di balik perintahnya. Ia menuntut banyak dari para prajurit karena menuntut hal yang sama dari dirinya sendiri. Ketika seorang rekan gagal, dorongan pertamanya adalah memberi teguran; ia harus menahan ketidaksabarannya agar tetap mendengar penjelasan mereka. Di hadapan ancaman ia memilih berdiri bersama barisan, sebab baginya tanggung jawab seorang penjaga harus terlihat melalui tindakan.

## Lokasi Benteng

Outpost Agni di dataran tinggi perbatasan Arkananta menjadi tempat tugas Solarius. Pos api ini berada dalam kesiagaan tinggi dan mengawasi pergerakan monster batu, Troliogoro, serta Rakshorien. Pelataran benteng dan jalan masuk berbatu mendukung perannya sebagai penahan serangan. Identitasnya belum dipastikan sebagai komandan Agni; sebutan pos timur dalam entri lama juga belum dihubungkan dengan arah geografis pos tersebut.

## Kisah — Nyala di Mulut Jalan

Patroli dari lereng Arkananta tiba di depan Agni ketika suara batu berguling menyusul dari belakang. Seorang prajurit tertinggal karena ikatan perlengkapannya tersangkut. Solarius bergerak ke mulut jalan dan mengangkat perisai; cahaya api memperlihatkan jalur di antara debu.

Ia menahan posisi sementara dua rekannya menarik prajurit itu ke pelataran. Ketika semua telah melewati pintu, barisan kembali rapat. Tidak ada sorak kemenangan. Solarius masih menghadap lereng, menunggu debu turun agar pasukan dapat membedakan bahaya yang sungguh mendekat dari bayangan yang dibesarkan kepanikan.

> Acuan: [Outpost Agni](../../03_Region/03_Avalerion/Cities%20%26%20Town/Outpost_Agni.md); [Senopati Prabha](../../03_Region/03_Avalerion/Faksi%20%26%20Institusi/Senopati_Prabha.md); [Avalerion](../../03_Region/03_Avalerion/Avalerion.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `50.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Fighter` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T5 (Elite)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Light` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Dark` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Holy, Light, Armored` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **51** | **9** | **20** | **34** | **37** | **38** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `1785` *(Base 960 + VIT×15 + STR×5)* | **DEF** | `82` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `74` *(Base 2 + INT×8)* | **MDF** | `69` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `312` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `72` *(Base + INT×2)* |
| **ATK** | `112` *(Formula Melee)* | **Action Speed** | `55` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `89.0%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `11.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `10.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `8.9%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `169.3%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `119.0%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.14%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.27%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.24%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Bastion Smash** | `01 Neutral` / Physical Attack | `6 SP` | Always (Prioritas 5.0) | `a.def * 1.3 - b.def * 0.4` |
| **Bulwark of Light** | `10 Holy` / Certain Hit | `14 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Holy Consecration** | `10 Holy` / Physical Attack | `22 SP` | HP <= 40% (Prioritas 4.0) | `a.def * 1.0 - b.mdef * 0.2` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 2: Tactical AI (Taktis Pasukan Elit)`
* **Jumlah Aksi per Giliran:** `1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)`
* **Logika Penargetan:** Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<AI Priority>
HP% <= 25%: Holy Consecration, Lowest HP%
State === Taunt: Bulwark of Light, Random
Turn % 2 == 0: Bulwark of Light, Random
Always: Bastion Smash, Highest TGR
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Dark: 150%, Light: 50%
* **Resistensi Status:** Resistensi standar (tanpa anomali status)
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `440` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `330` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `130` | Mata uang resmi penjelajahan |
| **Drop 1** | `Prabha Crystal` (`20%`) | Material alam / crafting |
| **Drop 2** | `Silver` (`25%`) | Komponen sekunder |
| **Drop 3** | `Mana Crystal` (`20%`) | Rampasan langka |
| **Boss / Unique Drop** | `Prabha Halohelm / Prabha Dawnplate / Prabha Dawnboots / Prabha Signet` (`5%`) | Rampasan unik / piala bos |
