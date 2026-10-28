---
title: Grok Tulang-Besi
tags:
  - Bestiary
  - Boss
---

# Grok Tulang-Besi

## Deskripsi

Kepala Suku Troliogoro sekaligus shaman Animisme Batu. Grok memimpin ritual penyusunan cairn untuk menenangkan roh Gunung Arkananta dan menjaga keselamatan kaumnya. Julukan Tulang-Besi merujuk pada tubuh Troliogoro yang telah menyatu dengan logam serta kekokohan pemimpin yang memilih mempertahankan gua daripada mencari perang di luar wilayahnya.

## Bentuk

Grok bertubuh raksasa dengan punggung yang dipenuhi pertumbuhan kristal gua. Kulit tebalnya menyimpan lapisan logam hasil evolusi buatan Troliogoro, sedangkan kedua tangan dibalut potongan logam dari reruntuhan kuno. Susunannya tidak sepenuhnya simetris: beberapa lempeng menutup buku jari, sementara bagian lain mengikuti lengan seperti bekas tempaan yang tumbuh bersama tubuh. Ia membawa tongkat ritual berat untuk memukul batu dan membangunkan gema pemujaan. Ketika berdiri diam di antara cairn, siluetnya menyerupai bagian dari dinding kristal.

## Kepribadian dan Sikap

Grok keras, curiga kepada orang luar, dan sangat menjaga tata ruang sakral. Kemarahannya mudah muncul ketika cairn dipindahkan atau dirusak, sebab tindakan itu ia anggap membahayakan seluruh suku. Meski dikenal brutal, ia tidak mencari pertempuran terbuka tanpa alasan. Ia lebih suka menutup akses, mengamati niat pendatang, lalu menuntut mereka memperbaiki kerusakan yang dibuat. Sebagai shaman, ia sabar saat memimpin ritual dan mampu menunggu lama demi membaca perubahan gunung. Kesetiaannya kepada tradisi dapat membuatnya menolak gagasan baru sebelum memahami manfaatnya.

## Kedudukan dan Wilayah

Grok memimpin Suku Troliogoro dari Gua Agnigarba di dataran tinggi Arkananta. Lorong besarnya menjulur menuju pusat magma serta menampung pemukiman, bengkel logam, dan susunan cairn yang digunakan dalam ritual. Lokasi Bestiary lama menyebut Lembah Batu Arkananta; lembah tersebut dipertahankan sebagai bagian wilayah patroli dan pengumpulan batu, sedangkan pusat kekuasaannya berada di gua sukunya. Hubungannya dengan Krom tegang karena sengketa batas dan perbedaan cara hidup.

## Kisah — Batu yang Harus Dikembalikan

Seorang pedagang yang tersesat mengambil batu pipih dari sebuah cairn untuk menahan roda gerobaknya. Ketika Grok menemukannya, ia mengangkat tongkat ritual dan meminta seluruh rombongan menjauh. Pedagang itu mengira emas dapat menyelesaikan masalah, tetapi tawarannya justru membuat wajah sang shaman semakin keras.

Grok menyuruhnya mengembalikan batu ke susunan semula. Pedagang itu tidak mengingat posisinya, sehingga para Troliogoro membimbingnya menyusun ulang cairn dari dasar. Pekerjaan berlangsung sampai gema pukulan batu kembali terdengar benar. Grok akhirnya membuka jalan keluar. Ia tidak menerima koin; bagi pemimpin itu, pelajaran untuk menghormati batu jauh lebih berharga daripada pembayaran yang dibawa orang asing.

> Acuan: [Grok Tulang-Besi](../../05_Karakter%20%26%20Tokoh%20Penting/05_Arkananta/Grok%20Tulang-Besi.md); [Troliogoro (Troll)](../../04_Ras/02_Wuru%20Loka/Troliogoro_%28Troll%29.md); [Gua Agnigarba](../../03_Region/05_Arkananta/Cities%20%26%20Town/Gua%20Agnigarba.md); [Religion](../../03_Region/05_Arkananta/Religion.md); [Economy](../../03_Region/05_Arkananta/Economy.md); [Pegunungan Arkananta](../../03_Region/05_Arkananta/Arkananta.md).

---

# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)

### 1. Klasifikasi Tempur
| Parameter | Nilai | Sumber / Keterangan |
| :--- | :--- | :--- |
| **Database ID** | `57.0` | Sheet `NUSV-ENEMIES` |
| **Ras / Taksonomi** | `Humanoid` | Kategori taksonomi Nusvanir |
| **Class / Archetype** | `Tank` | Pola peran tempur turn-based |
| **Tier / Threat Rank** | `T5 (Boss)` | Skala ancaman encounter |
| **Tipe Serangan Dasar** | `Melee` | Formula serangan dasar |
| **Elemen Utama** | `Earth/Iron` | Afinitas serangan alami |
| **Kelemahan (Weakness)** | `Fire & Lightning` | Menerima pengganda kerusakan 2.0x |
| **Combat Tags** | `Armored, Large, Shielded` | Penanda taktis unit |

### 2. Parameter Atribut

#### A. 6 Base Stats (Atribut Dasar)
| STR | INT | DEX | LUK | AGI | VIT |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **50** | **11** | **18** | **38** | **31** | **57** |

#### B. Stat Turunan Utama (Vital & Combat)
| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |
| :--- | :--- | :--- | :--- |
| **Max HP** | `6500` *(Base 5395 + VIT×15 + STR×5)* | **DEF** | `110` *(Base + VIT×1.5 + STR×0.5)* |
| **Max MP** | `86` *(INT×8)* | **MDF** | `89` *(Base + INT×1.2 + VIT×0.8)* |
| **Max SP** | `405` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `79` *(Base + INT×2)* |
| **ATK** | `109` *(Formula Melee)* | **Action Speed** | `46` *(Base + AGI×1.5)* |

#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)
| Parameter | Nilai (%) | Formula Perhitungan |
| :--- | :---: | :--- |
| **Hit Rate (HIT)** | `88.6%` | `0.85 + (DEX * 0.002)` (Cap 100%) |
| **Evasion Rate (EVA)** | `10.1%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |
| **Critical Rate (CRI)** | `10.4%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |
| **Critical Evasion (CEV)** | `11.4%` | `(LUK * 0.0015) + (VIT * 0.001)` |
| **Critical Damage (CDMG)** | `168.6%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |
| **Guard Efficiency (GRD)** | `128.5%` | `1.0 + (VIT * 0.005)` |
| **HP Regen / Turn (HRG)** | `1.71%` | `VIT * 0.0003` |
| **MP Regen / Turn (MRG)** | `0.33%` | `INT * 0.0003` |
| **SP Regen / Turn (TRG)** | `5.38%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |

### 3. Skill & Pola Aksi Giliran (AI Actions)

#### A. Daftar Skill & Syarat Pemicu
*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*

| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |
| :--- | :--- | :--- | :--- | :--- |
| **Shield Breaker** | `01 Neutral` / Physical Attack | `15 SP` | Always (Prioritas 5.0) | `Math.max(1, a.atk * 1.15 - b.def * 0.1 (Vulnerable 30%))` |
| **Iron Fortress** | `04 Earth` / Magical Attack | `24 SP` | Turn 2+ / 50% chance (Prioritas 4.0) | `-` |
| **Fortified Line** | `01 Neutral` / Certain Hit | `30 SP` | HP <= 50% (Prioritas 6.0) | `-` |

#### B. Konfigurasi AI Taktis (YEP_BattleAICore)
* **AI Behavioral Tier:** `Tier 3: Mastermind AI (Pengendali Arena Multifase)`
* **Jumlah Aksi per Giliran:** `2 Aksi per Giliran`
* **Logika Penargetan:** Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.
* **Notetag Engine (Salin ke Database RPG Maker MV):**
```text
<Action Times: 2>
<AI Priority>
HP% <= 30%: Fortified Line, All Foes
Turn % 3 == 0: Iron Fortress, Highest ATK
HP% <= 50%: Fortified Line, Lowest HP%
Always: Shield Breaker, Lowest DEF
</AI Priority>
```

### 4. Traits & Resistensi Khusus
* **Resistensi Elemen:** Earth: 75%, Fire: 150%, Iron: 75%, Lightning: 150%
* **Resistensi Status:** Freeze: 50%, Paralyze: 50%, Root: 75%, Stun: 50%
* **Karakteristik / Passive:** Preserve SP (Stamina tersimpan antar battle)

### 5. Ekonomi & Rampasan (Combat Rewards)
| Jenis Hadiah | Jumlah / Peluang | Keterangan |
| :--- | :--- | :--- |
| **Base EXP** | `1540` | Akumulasi Base Level (+3 Stat Point bebas) |
| **Class EXP** | `1155` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |
| **Saka (Gold)** | `455` | Mata uang resmi penjelajahan |
| **Drop 1** | `Butoraksa Bone` (`35%`) | Material alam / crafting |
| **Drop 2** | `Adamantine` (`15%`) | Komponen sekunder |
| **Drop 3** | `Spirit Stone` (`12%`) | Rampasan langka |
| **Boss / Unique Drop** | `Grok Ironbone Helm / Ironbone Warplate / Ironbone Greaves` (`5%`) | Rampasan unik / piala bos |
