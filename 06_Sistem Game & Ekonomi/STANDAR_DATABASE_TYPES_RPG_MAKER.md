---
title: STANDAR_DATABASE_TYPES_RPG_MAKER
tags:
  - Sistem_Game_Ekonomi
  - Database_Standard
  - RPG_Maker_MV
  - Types_Config
---

# 📋 Konfigurasi Resmi Database Types RPG Maker MV (Nusvanir)

Dokumen ini adalah **sumber kebenaran tunggal (*Single Source of Truth*)** untuk konfigurasi tab **Types** pada Database RPG Maker MV proyek Nusvanir. Seluruh class, item, weapon, armor, dan skill wajib merujuk secara presisi pada ID dan nama yang tertera di sini.

---

## 1. Skill Types (5 Tipe Resmi)

Menu skill pemain dalam pertarungan hanya menampilkan **5 kategori utama** yang ramah pemain (*player-friendly*):

| ID | Nama Skill Type | Definisi Desain & Peran Gameplay | Sumber Daya Utama |
| :---: | :--- | :--- | :---: |
| **01** | **White Magic** | Sihir pemulihan (HP/MP/SP recovery), *cleanse/dispel* status negatif, pemberian buff pelindung (*barrier*), dan resureksi. | **MP** |
| **02** | **Black Magic** | Sihir ofensif murni manipulasi 10 elemen untuk menghasilkan damage sihir (*MAT vs MDF*) dan memberi status penyakit ke musuh. | **MP** |
| **03** | **Skill** | Teknik tempur fisik, bela diri (*Martial Arts*), manuver senjata, dan teknik *stance/taunt*. | **SP** |
| **04** | **Summon** | Pemanggilan entitas, roh alam, familiars, atau arwah kegelapan ke arena untuk membantu pertempuran. | **MP / SP** |
| **05** | **Ultimate** | Jurus pamungkas terkuat tiap kelas (*Apex/Mastery*), membutuhkan investasi resource tinggi atau syarat kondisi tertentu. | **SP Tinggi / MP Besar** |

> [!NOTE]
> **Bagaimana dengan Skill Pasif?**  
> Skill bertipe pasif dikelola langsung melalui plugin **`YEP_AutoPassiveStates`**. Skill pasif tidak membutuhkan slot pada menu pertarungan (tanpa Skill Type di menu) sehingga antarmuka pertempuran tetap bersih dan tidak membingungkan pemain.

---

## 2. Elements (11 Elemen Resmi)

Sesuai urutan ID engine dan matriks efektivitas di [Mekanik_Efektivitas_Elemen.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Mekanik_Efektivitas_Elemen.md):

| ID | Nama Elemen | Simbol / Nama Lore | Karakteristik Utama |
| :---: | :--- | :--- | :--- |
| **01** | **Neutral** | Tanpa Afinitas | Serangan fisik/magis standar non-elemen. |
| **02** | **Fire** | *Pyro / Pyrowisp* | Elemen alam dasar: Menang vs Tanah (Geo), Lemah vs Air (Hydro). |
| **03** | **Water** | *Hydro / Aqua* | Elemen alam dasar: Menang vs Api (Pyro), Lemah vs Udara (Aero). |
| **04** | **Earth** | *Geo / Terra* | Elemen alam dasar: Menang vs Udara & Petir, Lemah vs Api. |
| **05** | **Air** | *Aero / Vayu* | Elemen alam dasar: Menang vs Air, Kebal (0x) vs Tanah. |
| **06** | **Electric** | *Electro* | Turunan Api: Sangat efektif memanggang Besi (Steel), Lemah vs Es. |
| **07** | **Ice** | *Cryo* | Turunan Air: Mengisolasi Listrik, Lemah vs Suara & Api. |
| **08** | **Steel** | *Ferro* | Turunan Tanah: Menang vs Suara, Lemah vs Listrik & Api. |
| **09** | **Sound** | *Sonic / Echo* | Turunan Udara: Memecahkan struktur Es (Cryo), Diredam Besi (0x). |
| **10** | **Holy** | *Cahaya (Sang Hyang)* | Elemen kosmik: Menghancurkan Kegelapan (Dark). |
| **11** | **Dark** | *Kegelapan (Kala)* | Elemen kosmik: Menelan Cahaya (Holy). |

---

## 3. Weapon Types (10 Tipe Senjata Resmi)

Katalog detail seluruh 66 senjata dapat dilihat di [01_Weapons.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/01_Weapons.md).

| ID | Tipe Senjata | Scaling Stat Utama | Pengguna Utama |
| :---: | :--- | :--- | :--- |
| **01** | **Long Sword** | `STR` (Melee Berat / 2-Handed) | Warrior, Knight, Mercenary |
| **02** | **Sword** | `STR` (Melee Seimbang / 1-Handed) | Fighter, Squire, Paladin |
| **03** | **Gloves** | `STR / AGI` (Melee Lincah) | Brawler, Martial Artist, Monk |
| **04** | **Spear** | `STR / DEX` (Reach / Piercing) | Squire, Dragoon |
| **05** | **Axe** | `STR` (Burst Damage Tinggi) | Warrior, Berserker |
| **06** | **Staff** | `INT` (Katalis Sihir Alami) | Apprentice, Magician, Mage, Cleric |
| **07** | **Rune** | `INT` (Fokus Sihir Khusus) | Occultist, Necromancer, Cultist |
| **08** | **Long Bow** | `DEX` (Ranged Jarak Jauh) | Archer, Sniper, Ranger |
| **09** | **Crossbow** | `DEX` (Ranged Piercing) | Scout, Rogue |
| **10** | **Dagger** | `DEX / AGI` (Finesse / Critical) | Scout, Thief, Assassin |

---

## 4. Armor Types (6 Tipe Zirah Resmi)

Katalog detail seluruh 123 perlengkapan zirah, tameng, helm, boots, aksesoris, dan relik dapat dilihat di [02_Armors.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/02_Armors.md).

| ID | Tipe Zirah | Karakteristik Stat | Pengguna Utama |
| :---: | :--- | :--- | :--- |
| **01** | **Basic Clothes** | Stat minimal, tanpa penalti AGI | Semua kelas pemula (Novice) |
| **02** | **Magic Robe** | Pertahanan Magis tinggi (`MDF`), bonus MP/MAT | Magician, Mage, Cleric, Priest |
| **03** | **Light Armor** | Fleksibel, menjaga Evasion & Speed | Scout, Rogue, Brawler, Archer |
| **04** | **Heavy Armor** | Pertahanan Fisik masif (`DEF`), penalti AGI | Warrior, Knight, Paladin, Mercenary |
| **05** | **Light Shield** | Tambahan block rate & sedikit DEF | Fighter, Scout, Cleric |
| **06** | **Heavy Shield** | Tingkat mitigasi Guard (`GRD`) tinggi & Max DEF | Squire, Knight, Paladin |

---

## 5. Equipment Types (7 Slot Perlengkapan Resmi)

Menggunakan modul `YEP_EquipCore` dengan susunan 7 slot perlengkapan karakter:

| Slot ID | Nama Slot | Deskripsi |
| :---: | :--- | :--- |
| **01** | **Primary Weapon** | Senjata utama tangan kanan (atau senjata 2 tangan). |
| **02** | **Secondary Weapon** | Tameng (Shield), senjata kedua (*Dual Wield*), atau *Off-hand Focus*. |
| **03** | **Helm** | Pelindung kepala (Topi sihir, helm baja, bandana). |
| **04** | **Armor** | Pelindung tubuh (Jubah, baju kulit, zirah baja). |
| **05** | **Boots** | Alas kaki penambah AGI, Evasion, dan resistensi tanah/jebakan. |
| **06** | **Accessory** | Cincin, jimat, kalung status (*X-Param & S-Param boost*). |
| **07** | **Relic** | Artefak purba, intan jiwa, atau batu segel berkekuatan khusus. |

