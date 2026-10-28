---
title: Armors_Database
tags:
  - Sistem_Game_Ekonomi
  - Equipment
  - Armor_Database
  - Turn_Based_RPG
---

# 🛡️ Database Perlengkapan: Armors & Protective Gear (Zirah & Pelindung)

Dokumen ini memuat seluruh **123 Perlengkapan Zirah & Pelindung** di dunia Nusvanir yang mencakup Body Armor, Shields, Helms, Boots, Accessories, dan Relics sesuai [STANDAR_DATABASE_TYPES_RPG_MAKER.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md).

> [!NOTE]
> **Aturan Sistem Zirah & Set Bonus Nusvanir:**
> - **6 Tipe Zirah Resmi:** `01 Basic Clothes`, `02 Magic Robe`, `03 Light Armor`, `04 Heavy Armor`, `05 Light Shield`, `06 Heavy Shield`.
> - **6 Slot Perlengkapan:** `Primary Weapon`, `Secondary Weapon`, `Helm`, `Armor`, `Boots`, `Accessory`, `Relic`.
> - **Sistem Set Bonus:** Memasang 2, 3, 4, hingga 5 bagian dari set zirah yang sama (misal: *Mandala Guard Set, Raksawana Scout Set, Silkweaver Set*) membuka efek sinergi pasif kuat.
> - **Mitigasi Guard:** Tameng secara drastis meningkatkan efisiensi parameter Guard Efficiency ($GRD$) saat karakter memilih aksi bertahan.

---

## 🛡️ 1. Pelindung Tubuh (Body Armor)

*Zirah utama penentu pertahanan fisik dan magis tubuh. Terbagi menjadi Basic Clothes, Magic Robe, Light Armor, dan Heavy Armor.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **04** | **Cotton Robe** | `Magic Robe` | ⚪ Common | - | `+6` | `+12` | MMP +8 | 25R | 12R 50T | Cotton Fiber ×4 + Clear Crystal ×1 |
| **05** | **Deerhide Vest** | `Light Armor` | ⚪ Common | - | `+8` | `+0` | AGI +2 | 25R | 12R 50T | Deer Hide ×4 + Flax Fiber ×1 |
| **06** | **Iron Brigandine** | `01 Basic Clothes` | ⚪ Common | Mandala Guard | `+12` | `+0` | MHP +15 | 25R | 12R 50T | Iron Ore ×4 + Deer Hide ×2 |
| **07** | **Leather Jerkin** | `Light Armor` | ⚪ Common | - | `+9` | `+0` | AGI +2 | 25R | 12R 50T | Deer Hide ×3 + Flax Fiber ×1 |
| **21** | **Gremlin Scrapcoat** | `01 Basic Clothes` | 🟢 Uncommon | - | `+16` | `+0` | AGI +1 | 1K | 50R | Steel ×2 + Lycan Hide ×2 |
| **22** | **Lycan Hidecoat** | `Light Armor` | 🟢 Uncommon | Arkananta Trail | `+18` | `+0` | AGI +3 | 1K | 50R | Lycan Hide ×3 + Black Iron Ore ×1 |
| **23** | **Steel Lamellar** | `Heavy Armor` | 🟢 Uncommon | - | `+25` | `+0` | MHP +35, AGI -2 | 1K | 50R | Steel ×4 + Ironwood ×1 |
| **24** | **Wight Shroud Robe** | `Magic Robe` | 🟢 Uncommon | - | `+9` | `+19` | MMP +12 | 1K | 50R | Wight Shroud ×4 + Cave Crystal ×1 |
| **41** | **Astradipa Silk Robe** | `Magic Robe` | 🔵 Rare | - | `+14` | `+29` | MMP +18, MAT +5 | 3K | 1K 50R | Astradipa Silk ×4 + Mana Crystal ×1 |
| **42** | **Basilisk Scale Vest** | `Light Armor` | 🔵 Rare | - | `+27` | `+10` | AGI +4 | 3K | 1K 50R | Crystal Basilisk Hide ×3 + Mana Crystal ×1 |
| **43** | **Butoraksa Boneplate** | `Heavy Armor` | 🔵 Rare | - | `+40` | `+0` | MHP +60, AGI -3 | 3K | 1K 50R | Butoraksa Bone ×3 + Platinum ×2 |
| **44** | **Platinum Guardplate** | `Heavy Armor` | 🔵 Rare | Avalerion Guardian | `+38` | `+0` | MHP +55, AGI -2 | 3K | 1K 50R | Platinum ×4 + Mana Crystal ×1 |
| **45** | **Sylvana Warden Garb** | `Light Armor` | 🔵 Rare | Sylvana Warden | `+28` | `+0` | AGI +5 | 3K | 1K 50R | Astradipa Silk ×3 + Raksawana Hardwood ×2 |
| **63** | **Blackhorn Scaleplate** | `Heavy Armor` | 🟣 Epic | Blackhorn Drake | `+58` | `+0` | MHP +90, AGI -4 | 10K | 5K | Adamantine ×4 + Adamantine Scale ×2 + Mithril Dragon Fang ×1 |
| **64** | **Ironbone Warplate** | `Heavy Armor` | 🟣 Epic | Ironbone | `+56` | `+0` | MHP +80, AGI -4 | 10K | 5K | Adamantine ×4 + Butoraksa Bone ×2 + Spirit Stone ×1 |
| **65** | **Larasati Tide Robe** | `Magic Robe` | 🟣 Epic | Larasati Tide | `+21` | `+43` | MMP +30, MAT +12 | 10K | 5K | Nyai Larasati |
| **66** | **Moonfang Shadowcoat** | `Light Armor` | 🟣 Epic | Moonfang Drake | `+37` | `+0` | AGI +9 | 10K | 5K | Lightweb Silk ×2 + Mithril ×2 + Moonfang ×1 |
| **67** | **Stonewind Battle Garb** | `Light Armor` | 🟣 Epic | Stonewind | `+36` | `+0` | AGI +8 | 10K | 5K | Lightweb Silk ×2 + Adamantine ×2 + Spirit Stone ×1 |
| **68** | **Vriskapala Vestment** | `Magic Robe` | 🟣 Epic | Vriskapala Grace | `+22` | `+45` | MMP +32, MAT +14 | 10K | 5K | Vriskapala Silk ×3 + Vriskapala Crystal ×2 |
| **89** | **Astral Vestment** | `Magic Robe` | 🟡 Legendary | Astral Communion | `+31` | `+64` | MMP +45, MAT +20 | 50K | 25K | Spirit Thread ×2 + Astral Crystal ×2 + Orichalcum ×1 |
| **90** | **Goldenscale Aegisplate** | `Heavy Armor` | 🟡 Legendary | Golden Drake | `+84` | `+28` | MHP +130, AGI -3 | 50K | 25K | Orichalcum ×4 + Garuda Golden Scale ×2 + Astral Crystal ×1 |
| **91** | **Prabha Dawnplate** | `Heavy Armor` | 🟡 Legendary | Prabha Aegis | `+80` | `+25` | MHP +120, AGI -3 | 50K | 25K | Orichalcum ×4 + Prabha Crystal ×2 + Prabha Thread ×1 |
| **92** | **Sempati Skyguard** | `Light Armor` | 🟡 Legendary | Golden Sentinel | `+48` | `+22` | AGI +12 | 50K | 25K | Jenderal Sempati |
| **93** | **Silverwing Mantle** | `Light Armor` | 🟡 Legendary | Silverwing | `+50` | `+25` | AGI +13 | 50K | 25K | Spirit Thread ×2 + Orichalcum ×2 + Astral Crystal ×1 |
| **94** | **Suparna Golden Mantle** | `Magic Robe` | 🟡 Legendary | Golden Sentinel | `+30` | `+61` | MMP +40, MAT +18 | 50K | 25K | Jenderal Suparna |
| **112** | **Coreweave of the False Eden** | `Magic Robe` | 🔴 Mythic | False Eden | `+48` | `+92` | MHP +50, MMP +90, MAT +35 | 0T | 0T | NOT CRAFTABLE |
| **113** | **Mantle of Mahasvara** | `Heavy Armor` | 🔴 Mythic | Mahasvara Sovereign | `+110` | `+35` | MHP +170, AGI -4 | 0T | 0T | NOT CRAFTABLE |
| **114** | **Rootsilk Vestment** | `Magic Robe` | 🔴 Mythic | Maharuha Grace | `+45` | `+88` | MMP +80, MAT +30 | 0T | 0T | NOT CRAFTABLE |
| **115** | **Wrathbound Carapace** | `Heavy Armor` | 🔴 Mythic | Wrathbound | `+115` | `+0` | MHP +180, ATK +15, AGI -6 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [04] Cotton Robe
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +6, MDF +12, MMP +8
- **Harga Pasar (Beli):** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar:** 12 Rajata 50 Tamra (1,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Cotton Fiber ×4 + Clear Crystal ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** MMP +8; DEF +6; MDF +12
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [05] Deerhide Vest
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +8, AGI +2
- **Harga Pasar (Beli):** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar:** 12 Rajata 50 Tamra (1,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Deer Hide ×4 + Flax Fiber ×1`
- **Monster Drop Source:** `Rusa Tanduk Cabang`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** DEF +8; AGI +2
- **Asal Wilayah / Budaya:** Alam Liar


### 🛡️ [06] Iron Brigandine
- **Slot Perlengkapan & Tipe:** `Armor` | `01 Basic Clothes`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Bagian dari Set:** ⚜️ **Mandala Guard**
- **Parameter Stat Pertahanan:** DEF +12, MHP +15
- **Harga Pasar (Beli):** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar:** 12 Rajata 50 Tamra (1,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×4 + Deer Hide ×2`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** MHP +15; DEF +12
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +3%
  * **[3 Set]:** MHP +5%
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [07] Leather Jerkin
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +9, AGI +2
- **Harga Pasar (Beli):** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar:** 12 Rajata 50 Tamra (1,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Deer Hide ×3 + Flax Fiber ×1`
- **Monster Drop Source:** `Babi Hutan / Rusa Tanduk Cabang`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +9; AGI +2
- **Asal Wilayah / Budaya:** Mandala / Alam Liar


### 🛡️ [21] Gremlin Scrapcoat
- **Slot Perlengkapan & Tipe:** `Armor` | `01 Basic Clothes`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +16, AGI +1
- **Harga Pasar (Beli):** 1 Kencana (10,000 Tamra)
- **Harga Jual Standar:** 50 Rajata (5,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Steel ×2 + Lycan Hide ×2`
- **Monster Drop Source:** `Gremlin`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** LUK +2
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [22] Lycan Hidecoat
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Bagian dari Set:** ⚜️ **Arkananta Trail**
- **Parameter Stat Pertahanan:** DEF +18, AGI +3
- **Harga Pasar (Beli):** 1 Kencana (10,000 Tamra)
- **Harga Jual Standar:** 50 Rajata (5,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Lycan Hide ×3 + Black Iron Ore ×1`
- **Monster Drop Source:** `Lycan`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** EVA +2%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +3%
  * **[3 Set]:** EVA +3%
- **Asal Wilayah / Budaya:** Arkananta / Jenggala


### 🛡️ [23] Steel Lamellar
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +25, MHP +35, AGI -2
- **Harga Pasar (Beli):** 1 Kencana (10,000 Tamra)
- **Harga Jual Standar:** 50 Rajata (5,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Steel ×4 + Ironwood ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** GRD +3%
- **Asal Wilayah / Budaya:** Mandala / Hermindar


### 🛡️ [24] Wight Shroud Robe
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +9, MDF +19, MMP +12
- **Harga Pasar (Beli):** 1 Kencana (10,000 Tamra)
- **Harga Jual Standar:** 50 Rajata (5,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Wight Shroud ×4 + Cave Crystal ×1`
- **Monster Drop Source:** `Wight`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MRG +1%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [41] Astradipa Silk Robe
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +14, MDF +29, MMP +18, MAT +5
- **Harga Pasar (Beli):** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 50 Rajata (15,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Astradipa Silk ×4 + Mana Crystal ×1`
- **Monster Drop Source:** `Banshee / Wight`
- **Metode Perolehan:** Normal Craft / Elite Drop
- **Traits Bawaan:** MRG +2%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [42] Basilisk Scale Vest
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +27, MDF +10, AGI +4
- **Harga Pasar (Beli):** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 50 Rajata (15,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Crystal Basilisk Hide ×3 + Mana Crystal ×1`
- **Monster Drop Source:** `Crystal Basilisk`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** Petrify State Rate 60%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [43] Butoraksa Boneplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +40, MHP +60, AGI -3
- **Harga Pasar (Beli):** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 50 Rajata (15,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Butoraksa Bone ×3 + Platinum ×2`
- **Monster Drop Source:** `Butoraksa`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** GRD +7%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [44] Platinum Guardplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Avalerion Guardian**
- **Parameter Stat Pertahanan:** DEF +38, MHP +55, AGI -2
- **Harga Pasar (Beli):** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 50 Rajata (15,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Platinum ×4 + Mana Crystal ×1`
- **Monster Drop Source:** `Ksatria Terra`
- **Metode Perolehan:** Guardian Drop / Craft
- **Traits Bawaan:** GRD +6%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +5%
  * **[3 Set]:** Dark Damage Taken -5%
- **Asal Wilayah / Budaya:** Avalerion Outpost


### 🛡️ [45] Sylvana Warden Garb
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Sylvana Warden**
- **Parameter Stat Pertahanan:** DEF +28, AGI +5
- **Harga Pasar (Beli):** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 50 Rajata (15,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Astradipa Silk ×3 + Raksawana Hardwood ×2`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Normal Craft / Elite Drop
- **Traits Bawaan:** EVA +4%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +5%
  * **[3 Set]:** EVA +5%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [63] Blackhorn Scaleplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Blackhorn Drake**
- **Parameter Stat Pertahanan:** DEF +58, MHP +90, AGI -4
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×4 + Adamantine Scale ×2 + Mithril Dragon Fang ×1`
- **Monster Drop Source:** `Blackhorn`
- **Metode Perolehan:** Dragon Boss Drop / Special Craft
- **Traits Bawaan:** GRD +12%; PDR 94%
- **Efek Khusus 1:** Physical Damage Taken -6%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [64] Ironbone Warplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Ironbone**
- **Parameter Stat Pertahanan:** DEF +56, MHP +80, AGI -4
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×4 + Butoraksa Bone ×2 + Spirit Stone ×1`
- **Monster Drop Source:** `Grok Tulang-Besi`
- **Metode Perolehan:** Chief Drop / Special Craft
- **Traits Bawaan:** GRD +10%; PDR 95%
- **Efek Khusus 1:** Physical Damage Taken -5%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [65] Larasati Tide Robe
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Larasati Tide**
- **Parameter Stat Pertahanan:** DEF +21, MDF +43, MMP +30, MAT +12
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Monster Drop Source:** `Nyai Larasati`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** MEV +6%
- **Efek Khusus 1:** Water Damage +10%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Water Magic +10%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [66] Moonfang Shadowcoat
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Moonfang Drake**
- **Parameter Stat Pertahanan:** DEF +37, AGI +9
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Lightweb Silk ×2 + Mithril ×2 + Moonfang ×1`
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Boss Drop / Special Craft
- **Traits Bawaan:** EVA +6%
- **Efek Khusus 1:** Critical Damage +10%
- **Efek Sinergi Set:**
  * **[2 Set]:** CRI +5%
  * **[3 Set]:** Critical Damage +10%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [67] Stonewind Battle Garb
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Stonewind**
- **Parameter Stat Pertahanan:** DEF +36, AGI +8
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Lightweb Silk ×2 + Adamantine ×2 + Spirit Stone ×1`
- **Monster Drop Source:** `Krom Batugilang`
- **Metode Perolehan:** Chief Drop / Special Craft
- **Traits Bawaan:** EVA +6%; Action Speed +8
- **Efek Khusus 1:** Action Speed +8
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +6%
  * **[3 Set]:** Earth/Wind Damage +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [68] Vriskapala Vestment
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Vriskapala Grace**
- **Parameter Stat Pertahanan:** DEF +22, MDF +45, MMP +32, MAT +14
- **Harga Pasar (Beli):** 10 Kencana (100,000 Tamra)
- **Harga Jual Standar:** 5 Kencana (50,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Vriskapala Silk ×3 + Vriskapala Crystal ×2`
- **Monster Drop Source:** `Vriskapala`
- **Metode Perolehan:** Special Craft / Elite Drop
- **Traits Bawaan:** MRG +4%
- **Efek Khusus 1:** Nature Damage +12%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Nature Damage +10%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [89] Astral Vestment
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Astral Communion**
- **Parameter Stat Pertahanan:** DEF +31, MDF +64, MMP +45, MAT +20
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Thread ×2 + Astral Crystal ×2 + Orichalcum ×1`
- **Monster Drop Source:** `Silverwing / Goldenscale`
- **Metode Perolehan:** Rare Craft / Boss Drop
- **Traits Bawaan:** MEV +9%; MCR 92%
- **Efek Khusus 1:** All Element Damage +8%
- **Efek Khusus 2:** MP Cost -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** MAT +8%
  * **[3 Set]:** MMP +10%
  * **[4 Set]:** All Element Damage +10%
- **Asal Wilayah / Budaya:** Agnitra / Avalerion


### 🛡️ [90] Goldenscale Aegisplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Drake**
- **Parameter Stat Pertahanan:** DEF +84, MDF +28, MHP +130, AGI -3
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×4 + Garuda Golden Scale ×2 + Astral Crystal ×1`
- **Monster Drop Source:** `Goldenscale`
- **Metode Perolehan:** Dragon Lord Drop / Rare Craft
- **Traits Bawaan:** GRD +16%; Light Rate 85%; PDR 92%
- **Efek Khusus 1:** Light Damage Taken -15%
- **Efek Khusus 2:** Physical Damage Taken -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +8%
  * **[3 Set]:** Light Damage +12%
  * **[4 Set]:** All Element Rate 95%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [91] Prabha Dawnplate
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** DEF +80, MDF +25, MHP +120, AGI -3
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×4 + Prabha Crystal ×2 + Prabha Thread ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Rare Craft / Guardian Reward
- **Traits Bawaan:** GRD +15%; Dark Rate 85%; REC 110%
- **Efek Khusus 1:** Dark Damage Taken -15%
- **Efek Khusus 2:** Healing Received +10%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [92] Sempati Skyguard
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +48, MDF +22, AGI +12
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Monster Drop Source:** `Jenderal Sempati`
- **Metode Perolehan:** General Drop
- **Traits Bawaan:** EVA +8%; Wind Rate 85%; Action Speed +12
- **Efek Khusus 1:** Wind Damage Taken -15%
- **Efek Khusus 2:** Action Speed +12
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [93] Silverwing Mantle
- **Slot Perlengkapan & Tipe:** `Armor` | `Light Armor`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Silverwing**
- **Parameter Stat Pertahanan:** DEF +50, MDF +25, AGI +13
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Thread ×2 + Orichalcum ×2 + Astral Crystal ×1`
- **Monster Drop Source:** `Silverwing`
- **Metode Perolehan:** Dragon Lord Drop / Rare Craft
- **Traits Bawaan:** EVA +9%; Wind Rate 85%; Action Speed +12
- **Efek Khusus 1:** Wind Damage Taken -15%
- **Efek Khusus 2:** Action Speed +12
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +12%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [94] Suparna Golden Mantle
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +30, MDF +61, MMP +40, MAT +18
- **Harga Pasar (Beli):** 50 Kencana (500,000 Tamra)
- **Harga Jual Standar:** 25 Kencana (250,000 Tamra)
- **Monster Drop Source:** `Jenderal Suparna`
- **Metode Perolehan:** General Drop
- **Traits Bawaan:** MEV +8%; MCR 94%
- **Efek Khusus 1:** Light/Wind Damage +10%
- **Efek Khusus 2:** MP Cost -6%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [112] Coreweave of the False Eden
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **False Eden**
- **Parameter Stat Pertahanan:** DEF +48, MDF +92, MHP +50, MMP +90, MAT +35
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Thalantira / Uru`
- **Metode Perolehan:** Endgame Core Reward
- **Traits Bawaan:** All Element Rate 80%; MCR 88%
- **Efek Khusus 1:** Void Damage +20%
- **Efek Khusus 2:** MP Cost -12%
- **Signature Effect:** ✨ **Reality Fracture: every fourth magic skill creates a Void Echo that repeats 40% of the skill's damage/effect.**
- **Efek Sinergi Set:**
  * **[2 Set]:** MAT +10%
  * **[3 Set]:** Void Damage +15%
  * **[4 Set]:** All Element Pierce +10%
  * **[5 Set]:** False Eden: first lethal hit each battle leaves wearer at 1 HP
- **Asal Wilayah / Budaya:** Thalantira
- **Catatan / Lore:** *"Extraterrestrial artifact tied to Uru."*


### 🛡️ [113] Mantle of Mahasvara
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Mahasvara Sovereign**
- **Parameter Stat Pertahanan:** DEF +110, MDF +35, MHP +170, AGI -4
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Agnitra Lord / Mahasvara Trial`
- **Metode Perolehan:** Nagarasven Lord Reward
- **Traits Bawaan:** Fire Rate 70%; GRD +20%
- **Efek Khusus 1:** GRD +20%
- **Efek Khusus 2:** Fire Damage +20%
- **Signature Effect:** ✨ **Molten Sovereignty: below 40% HP, attacks against the wearer can trigger a magma counter once per turn.**
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [114] Rootsilk Vestment
- **Slot Perlengkapan & Tipe:** `Armor` | `Magic Robe`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Maharuha Grace**
- **Parameter Stat Pertahanan:** DEF +45, MDF +88, MMP +80, MAT +30
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Astradipa / Maharuha`
- **Metode Perolehan:** Sacred Quest Reward
- **Traits Bawaan:** MRG +6%; MCR 90%
- **Efek Khusus 1:** Nature/Wind Damage +18%
- **Efek Khusus 2:** MP Cost -10%
- **Signature Effect:** ✨ **Living Canopy: every third spell grants a barrier to the lowest-HP ally.**
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [115] Wrathbound Carapace
- **Slot Perlengkapan & Tipe:** `Armor` | `Heavy Armor`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Wrathbound**
- **Parameter Stat Pertahanan:** DEF +115, MHP +180, ATK +15, AGI -6
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Vraka The Wrathful`
- **Metode Perolehan:** Commander Drop
- **Traits Bawaan:** GRD +18%; PDR 88%
- **Efek Khusus 1:** Physical Damage Taken -12%
- **Efek Khusus 2:** ATK +10% below 50% HP
- **Signature Effect:** ✨ **Wrath Incarnate: damage taken builds Wrath; at max stacks, the next physical skill ignores part of DEF.**
- **Asal Wilayah / Budaya:** Raksamala


## 🛡️ 2. Pelindung Tangan / Tameng (Shields)

*Tameng ringan (Light Shield) dan tameng berat (Heavy Shield) penambah mitigasi Guard (GRD) dan penangkis serangan.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **10** | **Iron Buckler** | `Light Shield` | ⚪ Common | Mandala Guard | `+8` | `+0` | - | 20R | 10R | Iron Ore ×2 + Deer Hide ×1 |
| **11** | **Iron Tower Shield** | `Heavy Shield` | ⚪ Common | - | `+12` | `+0` | MHP +10, AGI -1 | 20R | 10R | Iron Ore ×4 + Pine Wood ×1 |
| **12** | **Pine Round Shield** | `Light Shield` | ⚪ Common | - | `+6` | `+0` | - | 20R | 10R | Pine Wood ×2 + Deer Hide ×1 |
| **28** | **Black Iron Bulwark** | `Heavy Shield` | 🟢 Uncommon | - | `+19` | `+0` | MHP +20, AGI -2 | 80R | 40R | Black Iron Ore ×4 + Ironwood ×1 |
| **29** | **Ironwood Ward** | `Light Shield` | 🟢 Uncommon | Arkananta Trail | `+11` | `+6` | - | 80R | 40R | Ironwood ×3 + Cave Crystal ×1 |
| **30** | **Steel Kite Shield** | `Light Shield` | 🟢 Uncommon | - | `+13` | `+3` | - | 80R | 40R | Steel ×3 + Ironwood ×1 |
| **49** | **Platinum Tower Shield** | `Heavy Shield` | 🔵 Rare | Avalerion Guardian | `+29` | `+0` | MHP +40, AGI -2 | 2K 40R | 1K 20R | Platinum ×4 + Mana Crystal ×1 |
| **50** | **Silver Wardshield** | `Light Shield` | 🔵 Rare | - | `+19` | `+10` | - | 2K 40R | 1K 20R | Silver ×3 + Mana Crystal ×1 |
| **51** | **Solarius Dawnshield** | `Light Shield` | 🔵 Rare | Avalerion Guardian | `+18` | `+13` | - | 2K 40R | 1K 20R | Silver ×2 + Mana Crystal ×2 |
| **52** | **Sylvana Leafward** | `Light Shield` | 🔵 Rare | Sylvana Warden | `+17` | `+8` | AGI +2 | 2K 40R | 1K 20R | Raksawana Hardwood ×2 + Astradipa Silk ×1 + Mana Crystal ×1 |
| **73** | **Blackhorn Scale Bulwark** | `Heavy Shield` | 🟣 Epic | Blackhorn Drake | `+46` | `+0` | MHP +70, AGI -3 | 8K | 4K | Adamantine ×3 + Mithril Dragon Fang ×1 + Mahasvara Crystal ×1 |
| **74** | **Ironbone Bulwark** | `Heavy Shield` | 🟣 Epic | Ironbone | `+43` | `+0` | MHP +60, AGI -3 | 8K | 4K | Adamantine ×3 + Butoraksa Bone ×2 + Spirit Stone ×1 |
| **75** | **Moonfang Crescent Guard** | `Light Shield` | 🟣 Epic | Moonfang Drake | `+25` | `+14` | AGI +6 | 8K | 4K | Moonfang |
| **76** | **Stonewind Guard** | `Light Shield` | 🟣 Epic | Stonewind | `+28` | `+14` | AGI +5 | 8K | 4K | Krom Batugilang |
| **77** | **Tideglass Ward** | `Light Shield` | 🟣 Epic | Larasati Tide | `+24` | `+24` | MMP +18 | 8K | 4K | Nyai Larasati |
| **99** | **Abyssal Shellguard** | `Heavy Shield` | 🟡 Legendary | - | `+60` | `+28` | MHP +85, AGI -3 | 40K | 20K | Orichalcum ×3 + Primordial Crystal ×1 + Spirit Thread ×1 |
| **100** | **Goldenscale Bastion** | `Heavy Shield` | 🟡 Legendary | Golden Drake | `+64` | `+22` | MHP +90, AGI -3 | 40K | 20K | Orichalcum ×3 + Garuda Golden Scale ×2 + Astral Crystal ×1 |
| **101** | **Jatayu Stormguard** | `Light Shield` | 🟡 Legendary | Golden Sentinel | `+38` | `+22` | AGI +9 | 40K | 20K | Garuda Storm Feather ×2 + Orichalcum ×2 + Spirit Thread ×1 |
| **102** | **Prabha Aegis Shield** | `Heavy Shield` | 🟡 Legendary | Prabha Aegis | `+61` | `+24` | MHP +80, AGI -2 | 40K | 20K | Orichalcum ×3 + Prabha Crystal ×2 + Prabha Thread ×1 |
| **103** | **Silverwing Gale Shield** | `Light Shield` | 🟡 Legendary | Silverwing | `+40` | `+25` | AGI +10 | 40K | 20K | Orichalcum ×2 + Spirit Thread ×1 + Astral Crystal ×1 |
| **117** | **Abyssal Tidewall** | `Light Shield` | 🔴 Mythic | Abyssal Tide | `+58` | `+52` | MHP +70, MMP +40, AGI +8 | 0T | 0T | NOT CRAFTABLE |
| **118** | **Aegis of First Dawn** | `Heavy Shield` | 🔴 Mythic | First Dawn | `+84` | `+42` | MHP +120, AGI -2 | 0T | 0T | NOT CRAFTABLE |
| **119** | **Worldwall of Arkananta** | `Heavy Shield` | 🔴 Mythic | - | `+92` | `+28` | MHP +150, AGI -5 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [10] Iron Buckler
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Bagian dari Set:** ⚜️ **Mandala Guard**
- **Parameter Stat Pertahanan:** DEF +8
- **Harga Pasar (Beli):** 20 Rajata (2,000 Tamra)
- **Harga Jual Standar:** 10 Rajata (1,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×2 + Deer Hide ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +8
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +3%
  * **[3 Set]:** MHP +5%
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [11] Iron Tower Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +12, MHP +10, AGI -1
- **Harga Pasar (Beli):** 20 Rajata (2,000 Tamra)
- **Harga Jual Standar:** 10 Rajata (1,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×4 + Pine Wood ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** MHP +10; DEF +12; AGI -1
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [12] Pine Round Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +6
- **Harga Pasar (Beli):** 20 Rajata (2,000 Tamra)
- **Harga Jual Standar:** 10 Rajata (1,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Pine Wood ×2 + Deer Hide ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +6
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [28] Black Iron Bulwark
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +19, MHP +20, AGI -2
- **Harga Pasar (Beli):** 80 Rajata (8,000 Tamra)
- **Harga Jual Standar:** 40 Rajata (4,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Black Iron Ore ×4 + Ironwood ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** MHP +20; DEF +19; AGI -2; GRD +3%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [29] Ironwood Ward
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Bagian dari Set:** ⚜️ **Arkananta Trail**
- **Parameter Stat Pertahanan:** DEF +11, MDF +6
- **Harga Pasar (Beli):** 80 Rajata (8,000 Tamra)
- **Harga Jual Standar:** 40 Rajata (4,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Ironwood ×3 + Cave Crystal ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** DEF +11; MDF +6; Earth Rate 97%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +3%
  * **[3 Set]:** EVA +3%
- **Asal Wilayah / Budaya:** Astradipa / Arkananta


### 🛡️ [30] Steel Kite Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +13, MDF +3
- **Harga Pasar (Beli):** 80 Rajata (8,000 Tamra)
- **Harga Jual Standar:** 40 Rajata (4,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Steel ×3 + Ironwood ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** DEF +13; MDF +3; EVA +1%
- **Asal Wilayah / Budaya:** Mandala / Hermindar


### 🛡️ [49] Platinum Tower Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Avalerion Guardian**
- **Parameter Stat Pertahanan:** DEF +29, MHP +40, AGI -2
- **Harga Pasar (Beli):** 2 Kencana 40 Rajata (24,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 20 Rajata (12,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Platinum ×4 + Mana Crystal ×1`
- **Monster Drop Source:** `Ksatria Terra`
- **Metode Perolehan:** Guardian Drop / Craft
- **Traits Bawaan:** MHP +40; DEF +29; AGI -2; GRD +7%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +5%
  * **[3 Set]:** Dark Damage Taken -5%
- **Asal Wilayah / Budaya:** Avalerion Outpost
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/04_Guardians_of_Avalerion_Outpost"*


### 🛡️ [50] Silver Wardshield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +19, MDF +10
- **Harga Pasar (Beli):** 2 Kencana 40 Rajata (24,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 20 Rajata (12,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Silver ×3 + Mana Crystal ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** DEF +19; MDF +10; MEV +3%
- **Asal Wilayah / Budaya:** Mandala / Avalerion


### 🛡️ [51] Solarius Dawnshield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Avalerion Guardian**
- **Parameter Stat Pertahanan:** DEF +18, MDF +13
- **Harga Pasar (Beli):** 2 Kencana 40 Rajata (24,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 20 Rajata (12,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Silver ×2 + Mana Crystal ×2`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Guardian Drop / Craft
- **Traits Bawaan:** DEF +18; MDF +13; Light Rate 92%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +5%
  * **[3 Set]:** Dark Damage Taken -5%
- **Asal Wilayah / Budaya:** Avalerion Outpost
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/04_Guardians_of_Avalerion_Outpost"*


### 🛡️ [52] Sylvana Leafward
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Sylvana Warden**
- **Parameter Stat Pertahanan:** DEF +17, MDF +8, AGI +2
- **Harga Pasar (Beli):** 2 Kencana 40 Rajata (24,000 Tamra)
- **Harga Jual Standar:** 1 Kencana 20 Rajata (12,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Raksawana Hardwood ×2 + Astradipa Silk ×1 + Mana Crystal ×1`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Normal Craft / Elite Drop
- **Traits Bawaan:** DEF +17; MDF +8; AGI +2; EVA +4%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +5%
  * **[3 Set]:** EVA +5%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [73] Blackhorn Scale Bulwark
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Blackhorn Drake**
- **Parameter Stat Pertahanan:** DEF +46, MHP +70, AGI -3
- **Harga Pasar (Beli):** 8 Kencana (80,000 Tamra)
- **Harga Jual Standar:** 4 Kencana (40,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×3 + Mithril Dragon Fang ×1 + Mahasvara Crystal ×1`
- **Monster Drop Source:** `Blackhorn`
- **Metode Perolehan:** Dragon Boss Drop / Special Craft
- **Traits Bawaan:** MHP +70; DEF +46; AGI -3; GRD +13%
- **Efek Khusus 1:** Damage vs Large Taken -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Agnitra
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/05_Dragons_of_Agnitra_Nest"*


### 🛡️ [74] Ironbone Bulwark
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Ironbone**
- **Parameter Stat Pertahanan:** DEF +43, MHP +60, AGI -3
- **Harga Pasar (Beli):** 8 Kencana (80,000 Tamra)
- **Harga Jual Standar:** 4 Kencana (40,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×3 + Butoraksa Bone ×2 + Spirit Stone ×1`
- **Monster Drop Source:** `Grok Tulang-Besi`
- **Metode Perolehan:** Chief Drop / Special Craft
- **Traits Bawaan:** MHP +60; DEF +43; AGI -3; GRD +12%; PDR 95%
- **Efek Khusus 1:** Physical Damage Taken -5%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/06_Chiefs_of_Arkananta"*


### 🛡️ [75] Moonfang Crescent Guard
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Moonfang Drake**
- **Parameter Stat Pertahanan:** DEF +25, MDF +14, AGI +6
- **Harga Pasar (Beli):** 8 Kencana (80,000 Tamra)
- **Harga Jual Standar:** 4 Kencana (40,000 Tamra)
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Boss Drop
- **Traits Bawaan:** DEF +25; MDF +14; AGI +6; EVA +6%; CRI +5%
- **Efek Khusus 1:** CRI +5%
- **Efek Sinergi Set:**
  * **[2 Set]:** CRI +5%
  * **[3 Set]:** Critical Damage +10%
- **Asal Wilayah / Budaya:** Agnitra
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/05_Dragons_of_Agnitra_Nest"*


### 🛡️ [76] Stonewind Guard
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Stonewind**
- **Parameter Stat Pertahanan:** DEF +28, MDF +14, AGI +5
- **Harga Pasar (Beli):** 8 Kencana (80,000 Tamra)
- **Harga Jual Standar:** 4 Kencana (40,000 Tamra)
- **Monster Drop Source:** `Krom Batugilang`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** DEF +28; MDF +14; AGI +5; EVA +6%; Earth/Wind Rate 92%
- **Efek Khusus 1:** Earth/Wind Damage Taken -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +6%
  * **[3 Set]:** Earth/Wind Damage +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/06_Chiefs_of_Arkananta"*


### 🛡️ [77] Tideglass Ward
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Larasati Tide**
- **Parameter Stat Pertahanan:** DEF +24, MDF +24, MMP +18
- **Harga Pasar (Beli):** 8 Kencana (80,000 Tamra)
- **Harga Jual Standar:** 4 Kencana (40,000 Tamra)
- **Monster Drop Source:** `Nyai Larasati`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** DEF +24; MDF +24; MMP +18; MEV +6%; Water Rate 90%
- **Efek Khusus 1:** Water Damage Taken -10%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Water Magic +10%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/06_Chiefs_of_Arkananta"*


### 🛡️ [99] Abyssal Shellguard
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Parameter Stat Pertahanan:** DEF +60, MDF +28, MHP +85, AGI -3
- **Harga Pasar (Beli):** 40 Kencana (400,000 Tamra)
- **Harga Jual Standar:** 20 Kencana (200,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×3 + Primordial Crystal ×1 + Spirit Thread ×1`
- **Monster Drop Source:** `Naga Laut Penghancur / Hydra`
- **Metode Perolehan:** Sea Boss Drop / Rare Craft
- **Traits Bawaan:** MHP +85; DEF +60; MDF +28; AGI -3; Water Rate 82%; GRD +15%; State Rates 90%
- **Efek Khusus 1:** GRD +15%
- **Efek Khusus 2:** State Rate 90%
- **Asal Wilayah / Budaya:** Laut Rangkaruna
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/09_Laut_Rangkaruna"*


### 🛡️ [100] Goldenscale Bastion
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Drake**
- **Parameter Stat Pertahanan:** DEF +64, MDF +22, MHP +90, AGI -3
- **Harga Pasar (Beli):** 40 Kencana (400,000 Tamra)
- **Harga Jual Standar:** 20 Kencana (200,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×3 + Garuda Golden Scale ×2 + Astral Crystal ×1`
- **Monster Drop Source:** `Goldenscale`
- **Metode Perolehan:** Dragon Lord Drop / Rare Craft
- **Traits Bawaan:** MHP +90; DEF +64; MDF +22; AGI -3; GRD +18%; Light Rate 85%; PDR 92%
- **Efek Khusus 1:** Light Damage Taken -15%
- **Efek Khusus 2:** Physical Damage Taken -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +8%
  * **[3 Set]:** Light Damage +12%
  * **[4 Set]:** All Element Rate 95%
- **Asal Wilayah / Budaya:** Agnitra
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/05_Dragons_of_Agnitra_Nest"*


### 🛡️ [101] Jatayu Stormguard
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +38, MDF +22, AGI +9
- **Harga Pasar (Beli):** 40 Kencana (400,000 Tamra)
- **Harga Jual Standar:** 20 Kencana (200,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Garuda Storm Feather ×2 + Orichalcum ×2 + Spirit Thread ×1`
- **Monster Drop Source:** `Jenderal Jatayu`
- **Metode Perolehan:** General Drop / Rare Craft
- **Traits Bawaan:** DEF +38; MDF +22; AGI +9; EVA +8%; Wind Rate 85%; Action Speed +10
- **Efek Khusus 1:** Wind Damage Taken -15%
- **Efek Khusus 2:** Action Speed +10
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/07_Sentinels_of_Nusa_Sayendra"*


### 🛡️ [102] Prabha Aegis Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** DEF +61, MDF +24, MHP +80, AGI -2
- **Harga Pasar (Beli):** 40 Kencana (400,000 Tamra)
- **Harga Jual Standar:** 20 Kencana (200,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×3 + Prabha Crystal ×2 + Prabha Thread ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Rare Craft / Guardian Reward
- **Traits Bawaan:** MHP +80; DEF +61; MDF +24; AGI -2; GRD +18%; Dark Rate 85%; REC 110%
- **Efek Khusus 1:** Dark Damage Taken -15%
- **Efek Khusus 2:** Healing Received +10%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/04_Guardians_of_Avalerion_Outpost"*


### 🛡️ [103] Silverwing Gale Shield
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Silverwing**
- **Parameter Stat Pertahanan:** DEF +40, MDF +25, AGI +10
- **Harga Pasar (Beli):** 40 Kencana (400,000 Tamra)
- **Harga Jual Standar:** 20 Kencana (200,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×2 + Spirit Thread ×1 + Astral Crystal ×1`
- **Monster Drop Source:** `Silverwing`
- **Metode Perolehan:** Dragon Lord Drop / Rare Craft
- **Traits Bawaan:** DEF +40; MDF +25; AGI +10; EVA +9%; MEV +7%
- **Efek Khusus 1:** Wind Damage +10%
- **Efek Khusus 2:** MEV +7%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +12%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Agnitra
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/05_Dragons_of_Agnitra_Nest"*


### 🛡️ [117] Abyssal Tidewall
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Light Shield`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Abyssal Tide**
- **Parameter Stat Pertahanan:** DEF +58, MDF +52, MHP +70, MMP +40, AGI +8
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Krakentis Sang Pemutar Arus`
- **Metode Perolehan:** Sea Lord Drop
- **Traits Bawaan:** MHP +70; MMP +40; DEF +58; MDF +52; AGI +8; Water Rate 70%; MEV +10%
- **Efek Khusus 1:** MEV +10%
- **Efek Khusus 2:** Water Damage +18%
- **Signature Effect:** ✨ **Tidal Reversal: once per battle, completely nullify one magic attack and return 40% of its damage to the attacker.**
- **Asal Wilayah / Budaya:** Laut Rangkaruna
- **Catatan / Lore:** *"Bestiary: https://github.com/ultoid/nusvanir/tree/main/07_Bestiary/09_Laut_Rangkaruna"*


### 🛡️ [118] Aegis of First Dawn
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **First Dawn**
- **Parameter Stat Pertahanan:** DEF +84, MDF +42, MHP +120, AGI -2
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Avalerion / Senopati Prabha`
- **Metode Perolehan:** Main Story / Sacred Trial Reward
- **Traits Bawaan:** MHP +120; DEF +84; MDF +42; AGI -2; GRD +22%; Dark Rate 80%; State Resist Curse
- **Efek Khusus 1:** Dark Damage Taken -20%
- **Efek Khusus 2:** Curse Immunity
- **Signature Effect:** ✨ **First Light Bastion: once per battle, when an ally would receive lethal damage, intercept it and reduce that damage by 60%.**
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +10%
  * **[3 Set]:** Light Damage +15%
  * **[4 Set]:** Dark Damage Taken -15%
  * **[5 Set]:** First Dawn: party gains Holy Ward at battle start
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [119] Worldwall of Arkananta
- **Slot Perlengkapan & Tipe:** `Secondary Weapon` | `Heavy Shield`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Parameter Stat Pertahanan:** DEF +92, MDF +28, MHP +150, AGI -5
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Pegunungan Arkananta`
- **Metode Perolehan:** Ancient Arkananta Trial Reward
- **Traits Bawaan:** MHP +150; DEF +92; MDF +28; AGI -5; GRD +25%; PDR 85%
- **Efek Khusus 1:** Physical Damage Taken -15%
- **Efek Khusus 2:** Stagger Immunity
- **Signature Effect:** ✨ **Unmoving Mountain: after Guarding, the next hit taken is capped at 20% of Max HP.**
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


## 🪖 3. Pelindung Kepala (Helms & Headwear)

*Pelindung kepala penambah presisi, resistensi status mental/kebutaan, dan perlindungan vital.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **01** | **Boarhide Cap** | `Helm` | ⚪ Common | - | `+4` | `+0` | MHP +5 | 15R | 7R 50T | Boar Hide ×2 + Cotton Fiber ×1 |
| **02** | **Iron Guard Helm** | `Helm` | ⚪ Common | Mandala Guard | `+5` | `+2` | - | 15R | 7R 50T | Iron Ore ×2 + Deer Hide ×1 |
| **03** | **Traveler Hood** | `Helm` | ⚪ Common | - | `+2` | `+2` | AGI +1 | 15R | 7R 50T | Cotton Fiber ×2 + Flax Fiber ×1 |
| **18** | **Black Iron Hornhelm** | `Helm` | 🟢 Uncommon | Arkananta Trail | `+8` | `+3` | - | 60R | 30R | Black Iron Ore ×2 + Arkananta Horn ×1 |
| **19** | **Direboar Skullhelm** | `Helm` | 🟢 Uncommon | - | `+7` | `+0` | MHP +12 | 60R | 30R | Direboar Hide ×2 + Beast Bone ×1 |
| **20** | **Wight Hood** | `Helm` | 🟢 Uncommon | - | `+4` | `+7` | - | 60R | 30R | Wight Shroud ×2 + Cave Crystal ×1 |
| **37** | **Ahool Wingcrest** | `Helm` | 🔵 Rare | - | `+9` | `+7` | AGI +4 | 1K 80R | 90R | Ahool Hide ×2 + Mana Crystal ×1 |
| **38** | **Silver Knight Helm** | `Helm` | 🔵 Rare | Avalerion Guardian | `+13` | `+8` | - | 1K 80R | 90R | Silver ×2 + Mana Crystal ×1 |
| **39** | **Sylvana Leafguard** | `Helm` | 🔵 Rare | Sylvana Warden | `+10` | `+8` | - | 1K 80R | 90R | Raksawana Hardwood ×1 + Astradipa Silk ×1 + Mana Crystal ×1 |
| **40** | **Wendigo Bonehelm** | `Helm` | 🔵 Rare | - | `+12` | `+0` | MHP +20 | 1K 80R | 90R | Wendigo Hide ×2 + Beast Bone ×2 |
| **59** | **Blackhorn Cresthelm** | `Helm` | 🟣 Epic | Blackhorn Drake | `+20` | `+0` | MHP +30 | 6K | 3K | Blackhorn |
| **60** | **Grok Ironbone Helm** | `Helm` | 🟣 Epic | Ironbone | `+20` | `+8` | MHP +35 | 6K | 3K | Grok Tulang-Besi |
| **61** | **Krom Stonewind Crown** | `Helm` | 🟣 Epic | Stonewind | `+16` | `+10` | AGI +5 | 6K | 3K | Krom Batugilang |
| **62** | **Moonfang Nighthelm** | `Helm` | 🟣 Epic | Moonfang Drake | `+15` | `+12` | AGI +5 | 6K | 3K | Moonfang |
| **84** | **Goldenscale Crown** | `Helm` | 🟡 Legendary | Golden Drake | `+26` | `+18` | - | 30K | 15K | Goldenscale |
| **85** | **Jatayu Stormcrown** | `Helm` | 🟡 Legendary | Golden Sentinel | `+24` | `+14` | AGI +6 | 30K | 15K | Jenderal Jatayu |
| **86** | **Paksi Suncrest Helm** | `Helm` | 🟡 Legendary | Golden Sentinel | `+22` | `+18` | - | 30K | 15K | Jenderal Paksi |
| **87** | **Prabha Halohelm** | `Helm` | 🟡 Legendary | Prabha Aegis | `+22` | `+18` | - | 30K | 15K | Orichalcum ×2 + Prabha Crystal ×1 + Prabha Thread ×1 |
| **88** | **Silverwing Visor** | `Helm` | 🟡 Legendary | Silverwing | `+22` | `+20` | AGI +7 | 30K | 15K | Silverwing |
| **109** | **Crown of Drowned Hunger** | `Helm` | 🔴 Mythic | Drowned Hunger | `+34` | `+22` | MHP +90 | 0T | 0T | NOT CRAFTABLE |
| **110** | **Crown of First Dawn** | `Helm` | 🔴 Mythic | First Dawn | `+30` | `+30` | MMP +25 | 0T | 0T | NOT CRAFTABLE |
| **111** | **Crown of the Black Covenant** | `Helm` | 🔴 Mythic | Black Covenant | `+32` | `+30` | MHP +70, MMP +40 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [01] Boarhide Cap
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +4, MHP +5
- **Harga Pasar (Beli):** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar:** 7 Rajata 50 Tamra (750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Boar Hide ×2 + Cotton Fiber ×1`
- **Monster Drop Source:** `Babi Hutan`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** DEF +4; MHP +5
- **Asal Wilayah / Budaya:** Alam Liar


### 🛡️ [02] Iron Guard Helm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Bagian dari Set:** ⚜️ **Mandala Guard**
- **Parameter Stat Pertahanan:** DEF +5, MDF +2
- **Harga Pasar (Beli):** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar:** 7 Rajata 50 Tamra (750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×2 + Deer Hide ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +5; MDF +2
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +3%
  * **[3 Set]:** MHP +5%
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [03] Traveler Hood
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +2, MDF +2, AGI +1
- **Harga Pasar (Beli):** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar:** 7 Rajata 50 Tamra (750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Cotton Fiber ×2 + Flax Fiber ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +2; MDF +2; AGI +1
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [18] Black Iron Hornhelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Bagian dari Set:** ⚜️ **Arkananta Trail**
- **Parameter Stat Pertahanan:** DEF +8, MDF +3
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Black Iron Ore ×2 + Arkananta Horn ×1`
- **Monster Drop Source:** `Kambing Arkananta`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** MHP +2%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +3%
  * **[3 Set]:** EVA +3%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [19] Direboar Skullhelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +7, MHP +12
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Direboar Hide ×2 + Beast Bone ×1`
- **Monster Drop Source:** `Direboar`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MHP +3%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [20] Wight Hood
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +4, MDF +7
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Wight Shroud ×2 + Cave Crystal ×1`
- **Monster Drop Source:** `Wight`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** Dark Element Rate 95%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [37] Ahool Wingcrest
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +9, MDF +7, AGI +4
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Ahool Hide ×2 + Mana Crystal ×1`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** EVA +4%
- **Asal Wilayah / Budaya:** Astradipa / Jenggala


### 🛡️ [38] Silver Knight Helm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Avalerion Guardian**
- **Parameter Stat Pertahanan:** DEF +13, MDF +8
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Silver ×2 + Mana Crystal ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Guardian Drop / Craft
- **Traits Bawaan:** Light Element Rate 95%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +5%
  * **[3 Set]:** Dark Damage Taken -5%
- **Asal Wilayah / Budaya:** Avalerion Outpost


### 🛡️ [39] Sylvana Leafguard
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Sylvana Warden**
- **Parameter Stat Pertahanan:** DEF +10, MDF +8
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Raksawana Hardwood ×1 + Astradipa Silk ×1 + Mana Crystal ×1`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Normal Craft / Elite Drop
- **Traits Bawaan:** MEV +3%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +5%
  * **[3 Set]:** EVA +5%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [40] Wendigo Bonehelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +12, MHP +20
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Wendigo Hide ×2 + Beast Bone ×2`
- **Monster Drop Source:** `Wendigo`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** Chill State Rate 90%
- **Asal Wilayah / Budaya:** Arkananta


### 🛡️ [59] Blackhorn Cresthelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Blackhorn Drake**
- **Parameter Stat Pertahanan:** DEF +20, MHP +30
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Blackhorn`
- **Metode Perolehan:** Dragon Boss Drop
- **Traits Bawaan:** GRD +8%
- **Efek Khusus 1:** Damage vs Large +8%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [60] Grok Ironbone Helm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Ironbone**
- **Parameter Stat Pertahanan:** DEF +20, MDF +8, MHP +35
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Grok Tulang-Besi`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** GRD +8%; PDR 95%
- **Efek Khusus 1:** Physical Damage Taken -5%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [61] Krom Stonewind Crown
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Stonewind**
- **Parameter Stat Pertahanan:** DEF +16, MDF +10, AGI +5
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Krom Batugilang`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** EVA +5%; Earth/Wind Rate 92%
- **Efek Khusus 1:** Earth/Wind Damage Taken -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +6%
  * **[3 Set]:** Earth/Wind Damage +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [62] Moonfang Nighthelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Moonfang Drake**
- **Parameter Stat Pertahanan:** DEF +15, MDF +12, AGI +5
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Boss Drop
- **Traits Bawaan:** CRI +5%
- **Efek Khusus 1:** Dark Damage +10%
- **Efek Sinergi Set:**
  * **[2 Set]:** CRI +5%
  * **[3 Set]:** Critical Damage +10%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [84] Goldenscale Crown
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Drake**
- **Parameter Stat Pertahanan:** DEF +26, MDF +18
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Goldenscale`
- **Metode Perolehan:** Dragon Lord Drop
- **Traits Bawaan:** Light Rate 82%; GRD +8%
- **Efek Khusus 1:** Light Damage +12%
- **Efek Khusus 2:** GRD +8%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +8%
  * **[3 Set]:** Light Damage +12%
  * **[4 Set]:** All Element Rate 95%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [85] Jatayu Stormcrown
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +24, MDF +14, AGI +6
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Jenderal Jatayu`
- **Metode Perolehan:** General Drop
- **Traits Bawaan:** Wind Rate 85%; EVA +6%
- **Efek Khusus 1:** EVA +6%
- **Efek Khusus 2:** Wind Damage +12%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [86] Paksi Suncrest Helm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +22, MDF +18
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Jenderal Paksi`
- **Metode Perolehan:** General Drop
- **Traits Bawaan:** Light Rate 85%; State Resist Blind
- **Efek Khusus 1:** Blind Immunity
- **Efek Khusus 2:** Light Damage +12%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [87] Prabha Halohelm
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** DEF +22, MDF +18
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×2 + Prabha Crystal ×1 + Prabha Thread ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Rare Craft / Guardian Reward
- **Traits Bawaan:** Dark Rate 85%; Curse Rate 50%; MEV +5%
- **Efek Khusus 1:** Curse Resist +50%
- **Efek Khusus 2:** MEV +5%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [88] Silverwing Visor
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Silverwing**
- **Parameter Stat Pertahanan:** DEF +22, MDF +20, AGI +7
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Silverwing`
- **Metode Perolehan:** Dragon Lord Drop
- **Traits Bawaan:** EVA +7%; MEV +6%
- **Efek Khusus 1:** Wind Damage +12%
- **Efek Khusus 2:** MEV +6%
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +12%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [109] Crown of Drowned Hunger
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Drowned Hunger**
- **Parameter Stat Pertahanan:** DEF +34, MDF +22, MHP +90
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Paus Penelan Armada`
- **Metode Perolehan:** Sea Lord Drop
- **Traits Bawaan:** Water Rate 75%; HRG +4%
- **Efek Khusus 1:** HP Regen +4%
- **Efek Khusus 2:** Damage Taken -8% while HP >70%
- **Signature Effect:** ✨ **Devour the Tide: defeating an enemy restores 8% HP and 5% MP, up to three times per battle.**
- **Asal Wilayah / Budaya:** Laut Rangkaruna


### 🛡️ [110] Crown of First Dawn
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **First Dawn**
- **Parameter Stat Pertahanan:** DEF +30, MDF +30, MMP +25
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Avalerion / Senopati Prabha`
- **Metode Perolehan:** Main Story Reward
- **Traits Bawaan:** Dark Rate 75%; State Resist Curse
- **Efek Khusus 1:** Curse Immunity
- **Efek Khusus 2:** Light Damage +15%
- **Signature Effect:** ✨ **Dawnward: once per battle, lethal Dark damage leaves the wearer at 1 HP and grants Holy Ward.**
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +10%
  * **[3 Set]:** Light Damage +15%
  * **[4 Set]:** Dark Damage Taken -15%
  * **[5 Set]:** First Dawn: party gains Holy Ward at battle start
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [111] Crown of the Black Covenant
- **Slot Perlengkapan & Tipe:** `Helm` | `Helm`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Black Covenant**
- **Parameter Stat Pertahanan:** DEF +32, MDF +30, MHP +70, MMP +40
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Luciferus`
- **Metode Perolehan:** Commander/Lord Drop
- **Traits Bawaan:** State Resist Curse
- **Efek Khusus 1:** Curse Immunity
- **Efek Khusus 2:** Light Damage Taken +10%
- **Signature Effect:** ✨ **Sovereign Pact: once per battle, casting a Dark skill at critical HP restores 20% MP and applies a powerful self-buff for 2 turns.**
- **Efek Sinergi Set:**
  * **[2 Set]:** Dark Damage +10%
  * **[3 Set]:** Curse Potency +15%
  * **[4 Set]:** Dark Rate 75%
  * **[5 Set]:** Black Covenant: Dark skills gain lifesteal while HP <40%
- **Asal Wilayah / Budaya:** Raksamala


## 👢 4. Pelindung Kaki (Boots & Footwear)

*Alas kaki penunjang mobilitas, Action Speed (AGI), Evasion, serta pengurangan bahaya medan perang.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **08** | **Iron Greaves** | `Boots` | ⚪ Common | Mandala Guard | `+4` | `+0` | AGI +1 | 15R | 7R 50T | Iron Ore ×2 + Deer Hide ×1 |
| **09** | **Traveler Boots** | `Boots` | ⚪ Common | - | `+2` | `+0` | AGI +2 | 15R | 7R 50T | Deer Hide ×2 + Flax Fiber ×1 |
| **25** | **Arkananta Trail Boots** | `Boots` | 🟢 Uncommon | Arkananta Trail | `+5` | `+0` | AGI +4 | 60R | 30R | Lycan Hide ×2 + Ironwood ×1 |
| **26** | **Direboar Treads** | `Boots` | 🟢 Uncommon | - | `+5` | `+0` | AGI +3 | 60R | 30R | Direboar Hide ×2 + Ironwood ×1 |
| **27** | **Ironwood Boots** | `Boots` | 🟢 Uncommon | - | `+5` | `+0` | AGI +2 | 60R | 30R | Ironwood ×2 + Deer Hide ×1 |
| **46** | **Ahool Wingboots** | `Boots` | 🔵 Rare | - | `+7` | `+0` | AGI +8 | 1K 80R | 90R | Ahool Hide ×2 + Astradipa Silk ×1 |
| **47** | **Solarius Greaves** | `Boots` | 🔵 Rare | Avalerion Guardian | `+10` | `+6` | AGI +3 | 1K 80R | 90R | Silver ×2 + Mana Crystal ×1 |
| **48** | **Windstep Boots** | `Boots` | 🔵 Rare | Sylvana Warden | `+8` | `+0` | AGI +7 | 1K 80R | 90R | Astradipa Silk ×2 + Ahool Hide ×1 |
| **69** | **Blackhorn Sabatons** | `Boots` | 🟣 Epic | Blackhorn Drake | `+16` | `+0` | AGI -1 | 6K | 3K | Adamantine ×2 + Adamantine Scale ×1 |
| **70** | **Ironbone Greaves** | `Boots` | 🟣 Epic | Ironbone | `+15` | `+0` | AGI -1 | 6K | 3K | Adamantine ×2 + Butoraksa Bone ×1 |
| **71** | **Moonfang Stalkers** | `Boots` | 🟣 Epic | Moonfang Drake | `+11` | `+0` | AGI +10 | 6K | 3K | Moonfang |
| **72** | **Stonewind Boots** | `Boots` | 🟣 Epic | Stonewind | `+12` | `+0` | AGI +9 | 6K | 3K | Krom Batugilang |
| **95** | **Golden Sentinel Boots** | `Boots` | 🟡 Legendary | Golden Sentinel | `+18` | `+0` | AGI +12 | 30K | 15K | Garuda Storm Feather ×2 + Garuda Golden Scale ×1 + Spirit Thread ×1 |
| **96** | **Goldenscale Greaves** | `Boots` | 🟡 Legendary | Golden Drake | `+20` | `+12` | AGI +5 | 30K | 15K | Goldenscale |
| **97** | **Prabha Dawnboots** | `Boots` | 🟡 Legendary | Prabha Aegis | `+18` | `+10` | AGI +4 | 30K | 15K | Orichalcum ×2 + Prabha Thread ×1 + Prabha Crystal ×1 |
| **98** | **Silverwing Boots** | `Boots` | 🟡 Legendary | Silverwing | `+17` | `+0` | AGI +14 | 30K | 15K | Silverwing |
| **116** | **Talons of Golden Sky** | `Boots` | 🔴 Mythic | Golden Sky | `+24` | `+18` | AGI +18 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [08] Iron Greaves
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Bagian dari Set:** ⚜️ **Mandala Guard**
- **Parameter Stat Pertahanan:** DEF +4, AGI +1
- **Harga Pasar (Beli):** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar:** 7 Rajata 50 Tamra (750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×2 + Deer Hide ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +4; AGI +1
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +3%
  * **[3 Set]:** MHP +5%
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [09] Traveler Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +2, AGI +2
- **Harga Pasar (Beli):** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar:** 7 Rajata 50 Tamra (750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Deer Hide ×2 + Flax Fiber ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +2; AGI +2
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [25] Arkananta Trail Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Bagian dari Set:** ⚜️ **Arkananta Trail**
- **Parameter Stat Pertahanan:** DEF +5, AGI +4
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Lycan Hide ×2 + Ironwood ×1`
- **Monster Drop Source:** `Kambing Arkananta`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** Action Speed +2
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +3%
  * **[3 Set]:** EVA +3%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [26] Direboar Treads
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +5, AGI +3
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Direboar Hide ×2 + Ironwood ×1`
- **Monster Drop Source:** `Direboar`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MHP +2%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [27] Ironwood Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +5, AGI +2
- **Harga Pasar (Beli):** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar:** 30 Rajata (3,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Ironwood ×2 + Deer Hide ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** Earth Element Rate 97%
- **Asal Wilayah / Budaya:** Astradipa / Mandala


### 🛡️ [46] Ahool Wingboots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** DEF +7, AGI +8
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Ahool Hide ×2 + Astradipa Silk ×1`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** EVA +4%
- **Asal Wilayah / Budaya:** Astradipa / Jenggala


### 🛡️ [47] Solarius Greaves
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Avalerion Guardian**
- **Parameter Stat Pertahanan:** DEF +10, MDF +6, AGI +3
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Silver ×2 + Mana Crystal ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Guardian Drop / Craft
- **Traits Bawaan:** Blind State Rate 70%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +5%
  * **[3 Set]:** Dark Damage Taken -5%
- **Asal Wilayah / Budaya:** Avalerion Outpost


### 🛡️ [48] Windstep Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Bagian dari Set:** ⚜️ **Sylvana Warden**
- **Parameter Stat Pertahanan:** DEF +8, AGI +7
- **Harga Pasar (Beli):** 1 Kencana 80 Rajata (18,000 Tamra)
- **Harga Jual Standar:** 90 Rajata (9,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Astradipa Silk ×2 + Ahool Hide ×1`
- **Monster Drop Source:** `Ahool`
- **Metode Perolehan:** Normal Craft / Elite Drop
- **Traits Bawaan:** Action Speed +5
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +5%
  * **[3 Set]:** EVA +5%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [69] Blackhorn Sabatons
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Blackhorn Drake**
- **Parameter Stat Pertahanan:** DEF +16, AGI -1
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×2 + Adamantine Scale ×1`
- **Monster Drop Source:** `Blackhorn`
- **Metode Perolehan:** Dragon Boss Drop / Special Craft
- **Traits Bawaan:** GRD +5%
- **Efek Khusus 1:** Stagger Resist +20%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [70] Ironbone Greaves
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Ironbone**
- **Parameter Stat Pertahanan:** DEF +15, AGI -1
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Adamantine ×2 + Butoraksa Bone ×1`
- **Monster Drop Source:** `Grok Tulang-Besi`
- **Metode Perolehan:** Chief Drop / Special Craft
- **Traits Bawaan:** GRD +5%
- **Efek Khusus 1:** Stagger Resist +20%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +6%
  * **[3 Set]:** MHP +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [71] Moonfang Stalkers
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Moonfang Drake**
- **Parameter Stat Pertahanan:** DEF +11, AGI +10
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Boss Drop
- **Traits Bawaan:** EVA +6%; Action Speed +10
- **Efek Khusus 1:** Action Speed +10
- **Efek Sinergi Set:**
  * **[2 Set]:** CRI +5%
  * **[3 Set]:** Critical Damage +10%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [72] Stonewind Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Stonewind**
- **Parameter Stat Pertahanan:** DEF +12, AGI +9
- **Harga Pasar (Beli):** 6 Kencana (60,000 Tamra)
- **Harga Jual Standar:** 3 Kencana (30,000 Tamra)
- **Monster Drop Source:** `Krom Batugilang`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** EVA +5%; Action Speed +10
- **Efek Khusus 1:** Action Speed +10
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +6%
  * **[3 Set]:** Earth/Wind Damage +8%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [95] Golden Sentinel Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** DEF +18, AGI +12
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Garuda Storm Feather ×2 + Garuda Golden Scale ×1 + Spirit Thread ×1`
- **Monster Drop Source:** `Jenderal Jatayu / Jenderal Sempati`
- **Metode Perolehan:** Rare Craft / General Drop
- **Traits Bawaan:** EVA +6%; Wind Rate 85%; Action Speed +12
- **Efek Khusus 1:** Wind Rate 85%
- **Efek Khusus 2:** Action Speed +12
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [96] Goldenscale Greaves
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Drake**
- **Parameter Stat Pertahanan:** DEF +20, MDF +12, AGI +5
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Goldenscale`
- **Metode Perolehan:** Dragon Lord Drop
- **Traits Bawaan:** GRD +6%; Light Rate 85%
- **Efek Khusus 1:** Light Rate 85%
- **Efek Khusus 2:** Stagger Resist +25%
- **Efek Sinergi Set:**
  * **[2 Set]:** DEF +8%
  * **[3 Set]:** Light Damage +12%
  * **[4 Set]:** All Element Rate 95%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [97] Prabha Dawnboots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** DEF +18, MDF +10, AGI +4
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×2 + Prabha Thread ×1 + Prabha Crystal ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Rare Craft / Guardian Reward
- **Traits Bawaan:** MEV +5%; Blind Rate 50%; Action Speed +8
- **Efek Khusus 1:** Blind Resist +50%
- **Efek Khusus 2:** Action Speed +8
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [98] Silverwing Boots
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Silverwing**
- **Parameter Stat Pertahanan:** DEF +17, AGI +14
- **Harga Pasar (Beli):** 30 Kencana (300,000 Tamra)
- **Harga Jual Standar:** 15 Kencana (150,000 Tamra)
- **Monster Drop Source:** `Silverwing`
- **Metode Perolehan:** Dragon Lord Drop
- **Traits Bawaan:** EVA +7%; Wind Rate 85%; Action Speed +14
- **Efek Khusus 1:** Wind Rate 85%
- **Efek Khusus 2:** Action Speed +14
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +12%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [116] Talons of Golden Sky
- **Slot Perlengkapan & Tipe:** `Boots` | `Boots`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Golden Sky**
- **Parameter Stat Pertahanan:** DEF +24, MDF +18, AGI +18
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Jenderal Jatayu / Paksi / Sempati / Suparna`
- **Metode Perolehan:** Sacred General Trial Reward
- **Traits Bawaan:** EVA +10%; Action Speed +15
- **Efek Khusus 1:** Wind Damage +15%
- **Efek Khusus 2:** Action Speed +15
- **Signature Effect:** ✨ **Sky Dominion: after two successful evades, the next physical skill gains an extra hit.**
- **Asal Wilayah / Budaya:** Nusa Sayendra


## 💍 5. Aksesoris (Rings, Amulets, & Charms)

*Perhiasan berdaya magis yang melipatgandakan parameter sekunder (X-Param & S-Param) dan resistensi status.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **13** | **Beastbone Bracelet** | `Accessory` | ⚪ Common | - | `+1` | `+0` | ATK +2 | 13R | 6R 50T | Beast Bone ×1 + Beast Fang ×1 |
| **14** | **Clear Crystal Pendant** | `Accessory` | ⚪ Common | - | `+0` | `+2` | MMP +5, MAT +2 | 13R | 6R 50T | Clear Crystal ×2 + Cotton Fiber ×1 |
| **15** | **Iron Ring** | `Accessory` | ⚪ Common | - | `+2` | `+2` | - | 13R | 6R 50T | Iron Ore ×1 + Clear Crystal ×1 |
| **31** | **Cave Crystal Ring** | `Accessory` | 🟢 Uncommon | - | `+0` | `+3` | MAT +3 | 50R | 25R | Cave Crystal ×2 + Steel ×1 |
| **32** | **Jenggala Fang Charm** | `Accessory` | 🟢 Uncommon | - | `+0` | `+0` | ATK +3, AGI +1 | 50R | 25R | Jenggala Claw ×1 + Beast Fang ×1 |
| **33** | **Lycan Fang Pendant** | `Accessory` | 🟢 Uncommon | - | `+0` | `+0` | ATK +3, AGI +2 | 50R | 25R | Beast Fang ×1 + Lycan Hide ×1 + Cave Crystal ×1 |
| **34** | **Wightbone Ring** | `Accessory` | 🟢 Uncommon | - | `+0` | `+4` | LUK +2 | 50R | 25R | Wight Shroud ×1 + Beast Bone ×1 + Cave Crystal ×1 |
| **53** | **Basilisk Eye Ring** | `Accessory` | 🔵 Rare | - | `+0` | `+4` | MAT +5 | 1K 50R | 75R | Mana Crystal ×1 + Silver ×1 + Obsidian ×1 |
| **54** | **Mana Crystal Pendant** | `Accessory` | 🔵 Rare | - | `+0` | `+4` | MMP +12, MAT +5 | 1K 50R | 75R | Mana Crystal ×2 + Silver ×1 |
| **55** | **Moonfang Choker** | `Accessory` | 🔵 Rare | - | `+0` | `+0` | ATK +3, AGI +4 | 1K 50R | 75R | Moonfang ×1 + Astradipa Silk ×1 |
| **56** | **Moonfang Ring** | `Accessory` | 🔵 Rare | - | `+0` | `+0` | ATK +4, AGI +3 | 1K 50R | 75R | Moonfang ×1 + Silver ×1 |
| **78** | **Dragonfang Signet** | `Accessory` | 🟣 Epic | - | `+0` | `+0` | ATK +6, AGI +4 | 5K | 2K 50R | Mithril Dragon Fang ×1 + Mithril ×1 |
| **79** | **Larasati Waterglass Ring** | `Accessory` | 🟣 Epic | Larasati Tide | `+0` | `+6` | MMP +15, MAT +8 | 5K | 2K 50R | Nyai Larasati |
| **80** | **Mahasvara Ember Ring** | `Accessory` | 🟣 Epic | - | `+0` | `+0` | ATK +5, MAT +7 | 5K | 2K 50R | Mahasvara Crystal ×1 + Mithril ×1 |
| **81** | **Vriskapala Ring** | `Accessory` | 🟣 Epic | Vriskapala Grace | `+0` | `+8` | MAT +8 | 5K | 2K 50R | Vriskapala Crystal ×1 + Mithril ×1 |
| **104** | **Astral Signet** | `Accessory` | 🟡 Legendary | - | `+0` | `+10` | MMP +15, MAT +10 | 25K | 12K 50R | Astral Crystal ×1 + Orichalcum ×1 |
| **105** | **Garuda Storm Signet** | `Accessory` | 🟡 Legendary | Golden Sentinel | `+0` | `+0` | ATK +6, AGI +8 | 25K | 12K 50R | Garuda Storm Feather ×1 + Orichalcum ×1 |
| **106** | **Prabha Signet** | `Accessory` | 🟡 Legendary | Prabha Aegis | `+0` | `+8` | MAT +8, LUK +3 | 25K | 12K 50R | Orichalcum ×1 + Prabha Crystal ×1 |
| **120** | **Black Covenant Signet** | `Accessory` | 🔴 Mythic | Black Covenant | `+0` | `+16` | MAT +16, LUK +6 | 0T | 0T | NOT CRAFTABLE |
| **121** | **Ring of the Abyssal Tide** | `Accessory` | 🔴 Mythic | Abyssal Tide | `+0` | `+12` | MHP +40, MMP +30, MAT +12 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [13] Beastbone Bracelet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +1, ATK +2
- **Harga Pasar (Beli):** 13 Rajata (1,300 Tamra)
- **Harga Jual Standar:** 6 Rajata 50 Tamra (650 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Beast Bone ×1 + Beast Fang ×1`
- **Monster Drop Source:** `Beast`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** ATK +2; DEF +1
- **Asal Wilayah / Budaya:** Alam Liar


### 🛡️ [14] Clear Crystal Pendant
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** MDF +2, MMP +5, MAT +2
- **Harga Pasar (Beli):** 13 Rajata (1,300 Tamra)
- **Harga Jual Standar:** 6 Rajata 50 Tamra (650 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Clear Crystal ×2 + Cotton Fiber ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** MMP +5; MAT +2; MDF +2
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [15] Iron Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** DEF +2, MDF +2
- **Harga Pasar (Beli):** 13 Rajata (1,300 Tamra)
- **Harga Jual Standar:** 6 Rajata 50 Tamra (650 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Iron Ore ×1 + Clear Crystal ×1`
- **Metode Perolehan:** Normal Craft / Shop
- **Traits Bawaan:** DEF +2; MDF +2
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [31] Cave Crystal Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** MDF +3, MAT +3
- **Harga Pasar (Beli):** 50 Rajata (5,000 Tamra)
- **Harga Jual Standar:** 25 Rajata (2,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Cave Crystal ×2 + Steel ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** MMP +3%
- **Asal Wilayah / Budaya:** Mandala


### 🛡️ [32] Jenggala Fang Charm
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** ATK +3, AGI +1
- **Harga Pasar (Beli):** 50 Rajata (5,000 Tamra)
- **Harga Jual Standar:** 25 Rajata (2,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Jenggala Claw ×1 + Beast Fang ×1`
- **Monster Drop Source:** `Goblin / Gremlin / Lycan`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** CRI +1%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [33] Lycan Fang Pendant
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** ATK +3, AGI +2
- **Harga Pasar (Beli):** 50 Rajata (5,000 Tamra)
- **Harga Jual Standar:** 25 Rajata (2,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Beast Fang ×1 + Lycan Hide ×1 + Cave Crystal ×1`
- **Monster Drop Source:** `Lycan`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** CRI +2%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [34] Wightbone Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** MDF +4, LUK +2
- **Harga Pasar (Beli):** 50 Rajata (5,000 Tamra)
- **Harga Jual Standar:** 25 Rajata (2,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Wight Shroud ×1 + Beast Bone ×1 + Cave Crystal ×1`
- **Monster Drop Source:** `Wight`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** Dark Element Rate 97%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [53] Basilisk Eye Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** MDF +4, MAT +5
- **Harga Pasar (Beli):** 1 Kencana 50 Rajata (15,000 Tamra)
- **Harga Jual Standar:** 75 Rajata (7,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Mana Crystal ×1 + Silver ×1 + Obsidian ×1`
- **Monster Drop Source:** `Crystal Basilisk`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** Petrify State Rate 70%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [54] Mana Crystal Pendant
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** MDF +4, MMP +12, MAT +5
- **Harga Pasar (Beli):** 1 Kencana 50 Rajata (15,000 Tamra)
- **Harga Jual Standar:** 75 Rajata (7,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Mana Crystal ×2 + Silver ×1`
- **Metode Perolehan:** Normal Craft
- **Traits Bawaan:** MCR 97%
- **Asal Wilayah / Budaya:** Mandala / Astradipa


### 🛡️ [55] Moonfang Choker
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** ATK +3, AGI +4
- **Harga Pasar (Beli):** 1 Kencana 50 Rajata (15,000 Tamra)
- **Harga Jual Standar:** 75 Rajata (7,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Moonfang ×1 + Astradipa Silk ×1`
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Drop / Craft
- **Traits Bawaan:** CRI +3%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [56] Moonfang Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** ATK +4, AGI +3
- **Harga Pasar (Beli):** 1 Kencana 50 Rajata (15,000 Tamra)
- **Harga Jual Standar:** 75 Rajata (7,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Moonfang ×1 + Silver ×1`
- **Monster Drop Source:** `Moonfang`
- **Metode Perolehan:** Dragon Drop / Craft
- **Traits Bawaan:** CRI +3%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [78] Dragonfang Signet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Parameter Stat Pertahanan:** ATK +6, AGI +4
- **Harga Pasar (Beli):** 5 Kencana (50,000 Tamra)
- **Harga Jual Standar:** 2 Kencana 50 Rajata (25,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Mithril Dragon Fang ×1 + Mithril ×1`
- **Monster Drop Source:** `Blackhorn / Moonfang`
- **Metode Perolehan:** Dragon Drop / Special Craft
- **Traits Bawaan:** CRI +4%
- **Efek Khusus 1:** Damage vs Dragon +10%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [79] Larasati Waterglass Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Larasati Tide**
- **Parameter Stat Pertahanan:** MDF +6, MMP +15, MAT +8
- **Harga Pasar (Beli):** 5 Kencana (50,000 Tamra)
- **Harga Jual Standar:** 2 Kencana 50 Rajata (25,000 Tamra)
- **Monster Drop Source:** `Nyai Larasati`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** Silence State Rate 70%
- **Efek Khusus 1:** Silence Resist +30%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Water Magic +10%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [80] Mahasvara Ember Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Parameter Stat Pertahanan:** ATK +5, MAT +7
- **Harga Pasar (Beli):** 5 Kencana (50,000 Tamra)
- **Harga Jual Standar:** 2 Kencana 50 Rajata (25,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Mahasvara Crystal ×1 + Mithril ×1`
- **Metode Perolehan:** Special Craft
- **Efek Khusus 1:** Burn Potency +10%
- **Asal Wilayah / Budaya:** Agnitra


### 🛡️ [81] Vriskapala Ring
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Vriskapala Grace**
- **Parameter Stat Pertahanan:** MDF +8, MAT +8
- **Harga Pasar (Beli):** 5 Kencana (50,000 Tamra)
- **Harga Jual Standar:** 2 Kencana 50 Rajata (25,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Vriskapala Crystal ×1 + Mithril ×1`
- **Monster Drop Source:** `Vriskapala`
- **Metode Perolehan:** Special Craft / Elite Drop
- **Traits Bawaan:** MCR 95%
- **Efek Khusus 1:** MP Cost -5%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Nature Damage +10%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [104] Astral Signet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Parameter Stat Pertahanan:** MDF +10, MMP +15, MAT +10
- **Harga Pasar (Beli):** 25 Kencana (250,000 Tamra)
- **Harga Jual Standar:** 12 Kencana 50 Rajata (125,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Astral Crystal ×1 + Orichalcum ×1`
- **Monster Drop Source:** `Goldenscale / Silverwing`
- **Metode Perolehan:** Rare Craft / Dragon Drop
- **Traits Bawaan:** MRG +4%; MCR 95%
- **Efek Khusus 1:** All Element Damage +5%
- **Efek Khusus 2:** MP Cost -5%
- **Asal Wilayah / Budaya:** Agnitra / Avalerion


### 🛡️ [105] Garuda Storm Signet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Golden Sentinel**
- **Parameter Stat Pertahanan:** ATK +6, AGI +8
- **Harga Pasar (Beli):** 25 Kencana (250,000 Tamra)
- **Harga Jual Standar:** 12 Kencana 50 Rajata (125,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Garuda Storm Feather ×1 + Orichalcum ×1`
- **Monster Drop Source:** `Jenderal Jatayu / Jenderal Sempati`
- **Metode Perolehan:** General Drop / Rare Craft
- **Traits Bawaan:** CRI +5%; Action Speed +8
- **Efek Khusus 1:** CRI +5%
- **Efek Khusus 2:** Action Speed +8
- **Efek Sinergi Set:**
  * **[2 Set]:** AGI +8%
  * **[3 Set]:** Wind Damage +10%
  * **[4 Set]:** EVA +8%
- **Asal Wilayah / Budaya:** Nusa Sayendra


### 🛡️ [106] Prabha Signet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** MDF +8, MAT +8, LUK +3
- **Harga Pasar (Beli):** 25 Kencana (250,000 Tamra)
- **Harga Jual Standar:** 12 Kencana 50 Rajata (125,000 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Orichalcum ×1 + Prabha Crystal ×1`
- **Monster Drop Source:** `Ksatria Solarius`
- **Metode Perolehan:** Rare Craft / Guardian Reward
- **Traits Bawaan:** Dark Rate 90%; MCR 95%
- **Efek Khusus 1:** Dark Rate 90%
- **Efek Khusus 2:** MP Cost -5%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [120] Black Covenant Signet
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Black Covenant**
- **Parameter Stat Pertahanan:** MDF +16, MAT +16, LUK +6
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Luciferus / Asmodea`
- **Metode Perolehan:** Commander Drop
- **Traits Bawaan:** Dark Rate 75%
- **Efek Khusus 1:** Curse Potency +20%
- **Efek Khusus 2:** Dark Rate 75%
- **Signature Effect:** ✨ **Covenant Price: Dark skills cost 10% current HP instead of 50% of their MP cost while above 50% HP.**
- **Asal Wilayah / Budaya:** Raksamala


### 🛡️ [121] Ring of the Abyssal Tide
- **Slot Perlengkapan & Tipe:** `Accessory` | `Accessory`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Abyssal Tide**
- **Parameter Stat Pertahanan:** MDF +12, MHP +40, MMP +30, MAT +12
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Krakentis Sang Pemutar Arus`
- **Metode Perolehan:** Sea Lord Drop
- **Traits Bawaan:** Water Rate 70%
- **Efek Khusus 1:** Water Damage +18%
- **Efek Khusus 2:** Damage vs Sea Monsters +15%
- **Signature Effect:** ✨ **Tide Reversal: once per battle, a lethal magical hit is reduced to 1 damage and grants Water Ward.**
- **Asal Wilayah / Budaya:** Laut Rangkaruna


## 🔮 6. Relik Pusaka Purba (Relics & Artifacts)

*Artefak purba berkekuatan mistis yang memberikan efek pasif pengubah mekanik tempur.*

| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |
|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|
| **16** | **Spirit Dust Talisman** | `Relic` | ⚪ Common | - | `+0` | `+0` | MMP +4, MAT +1, LUK +1 | 19R | 9R 50T | Spirit Dust ×3 + Cotton Fiber ×1 |
| **17** | **Wisp Charm** | `Relic` | ⚪ Common | - | `+0` | `+0` | MMP +5, LUK +1 | 19R | 9R 50T | Spirit Dust ×2 + Clear Crystal ×1 |
| **35** | **Arkananta Horn Totem** | `Relic` | 🟢 Uncommon | - | `+3` | `+0` | MHP +10 | 75R | 37R 50T | Arkananta Horn ×1 + Wisp Core ×1 |
| **36** | **Wisp Core Totem** | `Relic` | 🟢 Uncommon | - | `+0` | `+3` | MMP +8 | 75R | 37R 50T | Wisp Core ×1 + Cave Crystal ×1 |
| **57** | **Gondarwa Spirit Idol** | `Relic` | 🔵 Rare | - | `+0` | `+6` | MHP +15, MMP +12 | 2K 25R | 1K 12R 50T | Spirit Stone ×1 + Mana Crystal ×1 + Beast Bone ×1 |
| **58** | **Spirit Stone Idol** | `Relic` | 🔵 Rare | - | `+0` | `+5` | MMP +12 | 2K 25R | 1K 12R 50T | Spirit Stone ×1 + Mana Crystal ×1 |
| **82** | **Larasati Resonance Relic** | `Relic` | 🟣 Epic | Larasati Tide | `+0` | `+8` | MMP +20, MAT +10 | 7K 50R | 3K 75R | Nyai Larasati |
| **83** | **Vriskapala Heartseed** | `Relic` | 🟣 Epic | Vriskapala Grace | `+0` | `+8` | MMP +25, MAT +10 | 7K 50R | 3K 75R | Vriskapala Crystal ×2 + Spirit Stone ×1 |
| **107** | **Avesari Dawn Relic** | `Relic` | 🟡 Legendary | Prabha Aegis | `+0` | `+10` | MMP +25, MAT +10 | 37K 50R | 18K 75R | Prabha Crystal ×2 + Astral Crystal ×1 + Prabha Thread ×1 |
| **108** | **Heart of the Primordial** | `Relic` | 🟡 Legendary | - | `+8` | `+8` | MHP +50, MMP +30 | 37K 50R | 18K 75R | Primordial Crystal ×1 + Spirit Thread ×1 |
| **122** | **Tirtanara Springheart** | `Relic` | 🔴 Mythic | Eternal Springs | `+0` | `+15` | MHP +60, MMP +60, MAT +15 | 0T | 0T | NOT CRAFTABLE |
| **123** | **Voidheart** | `Relic` | 🔴 Mythic | - | `+0` | `+0` | MHP +50, MMP +50, MAT +20, LUK +8 | 0T | 0T | NOT CRAFTABLE |


### 🛡️ [16] Spirit Dust Talisman
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** MMP +4, MAT +1, LUK +1
- **Harga Pasar (Beli):** 19 Rajata (1,900 Tamra)
- **Harga Jual Standar:** 9 Rajata 50 Tamra (950 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Dust ×3 + Cotton Fiber ×1`
- **Monster Drop Source:** `Wisp`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MMP +4; MAT +1; LUK +1
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [17] Wisp Charm
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Parameter Stat Pertahanan:** MMP +5, LUK +1
- **Harga Pasar (Beli):** 19 Rajata (1,900 Tamra)
- **Harga Jual Standar:** 9 Rajata 50 Tamra (950 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Dust ×2 + Clear Crystal ×1`
- **Monster Drop Source:** `Wisp`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MMP +5; LUK +1
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [35] Arkananta Horn Totem
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** DEF +3, MHP +10
- **Harga Pasar (Beli):** 75 Rajata (7,500 Tamra)
- **Harga Jual Standar:** 37 Rajata 50 Tamra (3,750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Arkananta Horn ×1 + Wisp Core ×1`
- **Monster Drop Source:** `Arkananta Beast`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** GRD +2%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [36] Wisp Core Totem
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Parameter Stat Pertahanan:** MDF +3, MMP +8
- **Harga Pasar (Beli):** 75 Rajata (7,500 Tamra)
- **Harga Jual Standar:** 37 Rajata 50 Tamra (3,750 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Wisp Core ×1 + Cave Crystal ×1`
- **Monster Drop Source:** `Wisp`
- **Metode Perolehan:** Monster Drop / Craft
- **Traits Bawaan:** MRG +1%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [57] Gondarwa Spirit Idol
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** MDF +6, MHP +15, MMP +12
- **Harga Pasar (Beli):** 2 Kencana 25 Rajata (22,500 Tamra)
- **Harga Jual Standar:** 1 Kencana 12 Rajata 50 Tamra (11,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Stone ×1 + Mana Crystal ×1 + Beast Bone ×1`
- **Monster Drop Source:** `Gondarwa`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** MRG +2%
- **Asal Wilayah / Budaya:** Jenggala


### 🛡️ [58] Spirit Stone Idol
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Parameter Stat Pertahanan:** MDF +5, MMP +12
- **Harga Pasar (Beli):** 2 Kencana 25 Rajata (22,500 Tamra)
- **Harga Jual Standar:** 1 Kencana 12 Rajata 50 Tamra (11,250 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Spirit Stone ×1 + Mana Crystal ×1`
- **Monster Drop Source:** `Gondarwa`
- **Metode Perolehan:** Elite Drop / Craft
- **Traits Bawaan:** MRG +2%
- **Asal Wilayah / Budaya:** Jenggala / Astradipa


### 🛡️ [82] Larasati Resonance Relic
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Larasati Tide**
- **Parameter Stat Pertahanan:** MDF +8, MMP +20, MAT +10
- **Harga Pasar (Beli):** 7 Kencana 50 Rajata (75,000 Tamra)
- **Harga Jual Standar:** 3 Kencana 75 Rajata (37,500 Tamra)
- **Monster Drop Source:** `Nyai Larasati`
- **Metode Perolehan:** Chief Drop
- **Traits Bawaan:** MRG +3%; MCR 92%
- **Efek Khusus 1:** Water/Sound Skill Cost -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Water Magic +10%
- **Asal Wilayah / Budaya:** Pegunungan Arkananta


### 🛡️ [83] Vriskapala Heartseed
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Bagian dari Set:** ⚜️ **Vriskapala Grace**
- **Parameter Stat Pertahanan:** MDF +8, MMP +25, MAT +10
- **Harga Pasar (Beli):** 7 Kencana 50 Rajata (75,000 Tamra)
- **Harga Jual Standar:** 3 Kencana 75 Rajata (37,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Vriskapala Crystal ×2 + Spirit Stone ×1`
- **Monster Drop Source:** `Vriskapala`
- **Metode Perolehan:** Elite Drop / Special Craft
- **Traits Bawaan:** MRG +4%
- **Efek Khusus 1:** Nature Skill Cost -8%
- **Efek Sinergi Set:**
  * **[2 Set]:** MMP +8%
  * **[3 Set]:** Nature Damage +10%
- **Asal Wilayah / Budaya:** Astradipa


### 🛡️ [107] Avesari Dawn Relic
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Bagian dari Set:** ⚜️ **Prabha Aegis**
- **Parameter Stat Pertahanan:** MDF +10, MMP +25, MAT +10
- **Harga Pasar (Beli):** 37 Kencana 50 Rajata (375,000 Tamra)
- **Harga Jual Standar:** 18 Kencana 75 Rajata (187,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Prabha Crystal ×2 + Astral Crystal ×1 + Prabha Thread ×1`
- **Monster Drop Source:** `Avalerion Guardians`
- **Metode Perolehan:** Sacred Quest / Guardian Reward
- **Traits Bawaan:** MRG +4%
- **Efek Khusus 1:** Light Damage +12%
- **Efek Khusus 2:** Once/battle remove 1 Curse at HP <30%
- **Efek Sinergi Set:**
  * **[2 Set]:** MDF +6%
  * **[3 Set]:** Dark Damage Taken -10%
  * **[4 Set]:** Curse Immunity
- **Asal Wilayah / Budaya:** Avalerion City / Avesari


### 🛡️ [108] Heart of the Primordial
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🟡 Legendary
- **Parameter Stat Pertahanan:** DEF +8, MDF +8, MHP +50, MMP +30
- **Harga Pasar (Beli):** 37 Kencana 50 Rajata (375,000 Tamra)
- **Harga Jual Standar:** 18 Kencana 75 Rajata (187,500 Tamra)
- **Resep Pembuatan (Craft Recipe):** `Primordial Crystal ×1 + Spirit Thread ×1`
- **Monster Drop Source:** `Hydra / Naga Laut Penghancur`
- **Metode Perolehan:** Rare Craft / Sea Boss Drop
- **Traits Bawaan:** HRG +2%; MRG +2%; Element/State Rates
- **Efek Khusus 1:** All Element Rate 92%
- **Efek Khusus 2:** State Rate 90%
- **Asal Wilayah / Budaya:** Laut Rangkaruna


### 🛡️ [122] Tirtanara Springheart
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Bagian dari Set:** ⚜️ **Eternal Springs**
- **Parameter Stat Pertahanan:** MDF +15, MHP +60, MMP +60, MAT +15
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Tirta Amarta`
- **Metode Perolehan:** Divine Revelation Reward
- **Traits Bawaan:** HRG +3%; MRG +3%
- **Efek Khusus 1:** Healing +20%
- **Efek Khusus 2:** All State Rate 90%
- **Signature Effect:** ✨ **Eternal Spring: once per battle, restore 30% HP and 20% MP when HP falls below 25%, then cleanse two negative states.**
- **Asal Wilayah / Budaya:** Tirta Amarta


### 🛡️ [123] Voidheart
- **Slot Perlengkapan & Tipe:** `Relic` | `Relic`
- **Tingkat Kelangkaan (Rarity):** 🔴 Mythic
- **Parameter Stat Pertahanan:** MHP +50, MMP +50, MAT +20, LUK +8
- **Harga Pasar (Beli):** 0 Saka (Tidak Dijual / Bebas)
- **Harga Jual Standar:** 0 Saka (Tidak Dijual / Bebas)
- **Resep Pembuatan (Craft Recipe):** `NOT CRAFTABLE`
- **Monster Drop Source:** `Thalantira / Uru`
- **Metode Perolehan:** Endgame Core Reward
- **Traits Bawaan:** All Element Rate 85%
- **Efek Khusus 1:** Void Damage +20%
- **Efek Khusus 2:** All Element Resistance Pierce +10%
- **Signature Effect:** ✨ **False Eden: once per battle, lethal damage leaves the wearer at 1 HP; the next skill gains extreme power but consumes 20% current HP.**
- **Asal Wilayah / Budaya:** Thalantira
- **Catatan / Lore:** *"Extraterrestrial artifact; intentionally outside Nusvanir cultural naming."*

