# 🧪 Database Item: Consumables (Barang Konsumsi)

Dokumen ini mencakup seluruh **Item Konsumsi (Consumables)** dalam dunia Nusvanir yang dapat digunakan oleh karakter selama pertempuran (*Turn-Based Combat*) maupun di luar pertempuran (*Field/Menu*).

> [!NOTE]
> **Aturan Mekanik Pertempuran Turn-Based Nusvanir:**
> - Menggunakan item dalam pertempuran mengonsumsi **1 Tindakan Giliran (Action Turn)** karakter.
> - Item pemulihan SP (*Focus Drop / Essence / Elixir*) sangat krusial bagi kelas fisik (*Fighter, Warrior, Rogue, Martial Artist*) karena sistem turn-based mempertahankan SP (*Preserve SP*) antar pertempuran.

---

## 1. Ramuan Pemulih HP (Health Recovery)

Memulihkan Hit Points secara instan dalam pertarungan turn-based atau saat eksplorasi menu.

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Potion** | ⚪ Common | 1 Ally | Always | 1R | 40T | Restore HP (small) |
| **Hi Potion** | 🟢 Uncommon | 1 Ally | Always | 1K | 40R | Restore HP (medium) |
| **Max Potion** | 🔵 Rare | 1 Ally | Always | 3K | 1K 20R | Restore HP 100% |


### 🔹 Potion
- **Kategori / Subkategori:** Consumable / `Recovery - HP`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Harga Beli Pasar:** 1 Rajata (100 Tamra)
- **Harga Jual Standar (40%):** 40 Tamra (40 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Restores a small amount of HP."*
- **Efek Mekanik Game:** **Restore HP (small)**
- **Sumber Perolehan:** Shop / Alchemy (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Hi Potion
- **Kategori / Subkategori:** Consumable / `Recovery - HP`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 1 Kencana (10,000 Tamra)
- **Harga Jual Standar (40%):** 40 Rajata (4,000 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Restores a moderate amount of HP."*
- **Efek Mekanik Game:** **Restore HP (medium)**
- **Sumber Perolehan:** Shop / Alchemy (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Max Potion
- **Kategori / Subkategori:** Consumable / `Recovery - HP`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 3 Kencana (30,000 Tamra)
- **Harga Jual Standar (40%):** 1 Kencana 20 Rajata (12,000 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Fully restores HP."*
- **Efek Mekanik Game:** **Restore HP 100%**
- **Sumber Perolehan:** Advanced Alchemy / Rare Shop (Major Cities)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 2. Ramuan Pemulih MP (Mana Recovery)

Memulihkan Mana Points untuk menjaga ketersediaan spellcaster (Mage, Cleric, Cultist).

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Ether** | ⚪ Common | 1 Ally | Always | 1R 20T | 48T | Restore MP (small) |
| **Hi Ether** | 🟢 Uncommon | 1 Ally | Always | 12R | 4R 80T | Restore MP (medium) |
| **Max Ether** | 🔵 Rare | 1 Ally | Always | 40R | 16R | Restore MP 100% |


### 🔹 Ether
- **Kategori / Subkategori:** Consumable / `Recovery - MP`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Harga Beli Pasar:** 1 Rajata 20 Tamra (120 Tamra)
- **Harga Jual Standar (40%):** 48 Tamra (48 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Restores a small amount of MP."*
- **Efek Mekanik Game:** **Restore MP (small)**
- **Sumber Perolehan:** Shop / Alchemy (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Hi Ether
- **Kategori / Subkategori:** Consumable / `Recovery - MP`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 12 Rajata (1,200 Tamra)
- **Harga Jual Standar (40%):** 4 Rajata 80 Tamra (480 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Restores a moderate amount of MP."*
- **Efek Mekanik Game:** **Restore MP (medium)**
- **Sumber Perolehan:** Shop / Alchemy (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Max Ether
- **Kategori / Subkategori:** Consumable / `Recovery - MP`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 40 Rajata (4,000 Tamra)
- **Harga Jual Standar (40%):** 16 Rajata (1,600 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Fully restores MP."*
- **Efek Mekanik Game:** **Restore MP 100%**
- **Sumber Perolehan:** Advanced Alchemy / Rare Shop (Major Cities)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 3. Ramuan Pemulih Campuran (Elixir HP + MP)

Pemulihan ganda darurat tingkat tinggi untuk skenario boss battle yang intens.

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Elixir** | 🔵 Rare | 1 Ally | Always | 60R | 24R | Restore HP + MP (large) |
| **Max Elixir** | 🟣 Epic | 1 Ally | Always | 2K 50R | 1K | Restore HP + MP 100% |


### 🔹 Elixir
- **Kategori / Subkategori:** Consumable / `Recovery - HP+MP`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 60 Rajata (6,000 Tamra)
- **Harga Jual Standar (40%):** 24 Rajata (2,400 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Restores a large amount of HP and MP."*
- **Efek Mekanik Game:** **Restore HP + MP (large)**
- **Sumber Perolehan:** Advanced Alchemy (Major Cities)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Max Elixir
- **Kategori / Subkategori:** Consumable / `Recovery - HP+MP`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Harga Beli Pasar:** 2 Kencana 50 Rajata (25,000 Tamra)
- **Harga Jual Standar (40%):** 1 Kencana (10,000 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Fully restores HP and MP."*
- **Efek Mekanik Game:** **Restore HP + MP 100%**
- **Sumber Perolehan:** Rare Reward / Master Alchemy (High-tier Regions)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 4. Ramuan Pemulih SP (Stamina Points Recovery)

Memulihkan Stamina Points (SP) karakter fisik untuk mengeksekusi skill jurus dan kombo fisik tanpa henti.

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Focus Drop** | ⚪ Common | 1 Ally | Battle Screen | 80T | 32T | Restore SP (small) |
| **Focus Essence** | 🟢 Uncommon | 1 Ally | Battle Screen | 6R | 2R 40T | Restore SP (medium) |
| **Focus Elixir** | 🔵 Rare | 1 Ally | Battle Screen | 30R | 12R | Restore SP 100% |


### 🔹 Focus Drop
- **Kategori / Subkategori:** Consumable / `Recovery - SP`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Harga Beli Pasar:** 80 Tamra (80 Tamra)
- **Harga Jual Standar (40%):** 32 Tamra (32 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Restores a small amount of Skill Points (SP)."*
- **Efek Mekanik Game:** **Restore SP (small)**
- **Sumber Perolehan:** Shop / Alchemy (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Focus Essence
- **Kategori / Subkategori:** Consumable / `Recovery - SP`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 6 Rajata (600 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata 40 Tamra (240 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Restores a moderate amount of Skill Points (SP)."*
- **Efek Mekanik Game:** **Restore SP (medium)**
- **Sumber Perolehan:** Alchemy (Mandala / Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Focus Elixir
- **Kategori / Subkategori:** Consumable / `Recovery - SP`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 30 Rajata (3,000 Tamra)
- **Harga Jual Standar (40%):** 12 Rajata (1,200 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Restores SP to maximum."*
- **Efek Mekanik Game:** **Restore SP 100%**
- **Sumber Perolehan:** Advanced Alchemy (High-tier Regions)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 5. Ramuan Kebangkitan (Revival & Anti-Death)

Membangkitkan sekutu dari status Death/Knockout dalam giliran tempur.

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Revive** | 🟢 Uncommon | 1 Ally (Dead) | Always | 15R | 6R | Remove Death; HP 10% |
| **Max Revive** | 🟣 Epic | 1 Ally (Dead) | Always | 2K | 80R | Remove Death; HP 100% |


### 🔹 Revive
- **Kategori / Subkategori:** Consumable / `Revival`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar (40%):** 6 Rajata (600 Tamra)
- **Target Penggunaan (Scope):** `1 Ally (Dead)`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Revives a fallen ally with 10% HP."*
- **Efek Mekanik Game:** **Remove Death; HP 10%**
- **Sumber Perolehan:** Shop / Alchemy (Major Cities)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Max Revive
- **Kategori / Subkategori:** Consumable / `Revival`
- **Tingkat Kelangkaan (Rarity):** 🟣 Epic
- **Harga Beli Pasar:** 2 Kencana (20,000 Tamra)
- **Harga Jual Standar (40%):** 80 Rajata (8,000 Tamra)
- **Target Penggunaan (Scope):** `1 Ally (Dead)`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Revives a fallen ally with full HP."*
- **Efek Mekanik Game:** **Remove Death; HP 100%**
- **Sumber Perolehan:** Rare Reward / Master Alchemy (High-tier Regions)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 6. Obat & Penawar Status Ailment

Menghilangkan status abnormal spesifik (Bleed, Burn, Poison, Chill, Paralyze, Confusion, Silence, Blind, Curse).

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Remedy** | 🟢 Uncommon | 1 Ally | Always | 5R | 2R | Cure Burn/Poison/Chill/Paralyze/Confusion |
| **Bandage** | ⚪ Common | 1 Ally | Always | 30T | 12T | Cure Bleed |
| **Clarity Tonic** | 🟢 Uncommon | 1 Ally | Always | 5R | 2R | Cure Silence/Blind |
| **Holy Water** | 🔵 Rare | 1 Ally | Always | 25R | 10R | Cure Cursed |


### 🔹 Remedy
- **Kategori / Subkategori:** Consumable / `Status Cure`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 5 Rajata (500 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata (200 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Cures Burn, Poison, Chill, Paralyze, and Confusion."*
- **Efek Mekanik Game:** **Cure Burn/Poison/Chill/Paralyze/Confusion**
- **Sumber Perolehan:** Alchemy (Mandala / Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Bandage
- **Kategori / Subkategori:** Consumable / `Status Cure`
- **Tingkat Kelangkaan (Rarity):** ⚪ Common
- **Harga Beli Pasar:** 30 Tamra (30 Tamra)
- **Harga Jual Standar (40%):** 12 Tamra (12 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Stops Bleeding."*
- **Efek Mekanik Game:** **Cure Bleed**
- **Sumber Perolehan:** Shop / Crafting (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Clarity Tonic
- **Kategori / Subkategori:** Consumable / `Status Cure`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 5 Rajata (500 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata (200 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Clears Silence and Blind."*
- **Efek Mekanik Game:** **Cure Silence/Blind**
- **Sumber Perolehan:** Alchemy (Mandala / Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Holy Water
- **Kategori / Subkategori:** Consumable / `Status Cure`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar (40%):** 10 Rajata (1,000 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Always`
- **Deskripsi Lore:** *"Purifies Cursed status."*
- **Efek Mekanik Game:** **Cure Cursed**
- **Sumber Perolehan:** Temple / Alchemy (Avalerion / Tirta Amarta)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 7. Tonik Penguat Tempur (Battle Stat Tonics)

Memberikan peningkatan atribut sementara (+25% / 1 Stage Buff) selama pertempuran (3-5 Turn).

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Might Tonic** | 🟢 Uncommon | 1 Ally | Battle Screen | 4R 50T | 1R 80T | Buff ATK |
| **Guard Tonic** | 🟢 Uncommon | 1 Ally | Battle Screen | 4R 50T | 1R 80T | Buff DEF |
| **Arcane Tonic** | 🟢 Uncommon | 1 Ally | Battle Screen | 5R | 2R | Buff MAT |
| **Ward Tonic** | 🟢 Uncommon | 1 Ally | Battle Screen | 5R | 2R | Buff MDF |
| **Swift Tonic** | 🟢 Uncommon | 1 Ally | Battle Screen | 5R 50T | 2R 20T | Buff AGI |
| **Fortune Tonic** | 🔵 Rare | 1 Ally | Battle Screen | 15R | 6R | Buff LUK |


### 🔹 Might Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 4 Rajata 50 Tamra (450 Tamra)
- **Harga Jual Standar (40%):** 1 Rajata 80 Tamra (180 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases ATK during battle."*
- **Efek Mekanik Game:** **Buff ATK**
- **Sumber Perolehan:** Combat Supply (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Guard Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 4 Rajata 50 Tamra (450 Tamra)
- **Harga Jual Standar (40%):** 1 Rajata 80 Tamra (180 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases DEF during battle."*
- **Efek Mekanik Game:** **Buff DEF**
- **Sumber Perolehan:** Combat Supply (Mandala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Arcane Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 5 Rajata (500 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata (200 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases MAT during battle."*
- **Efek Mekanik Game:** **Buff MAT**
- **Sumber Perolehan:** Combat Supply / Alchemy (Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Ward Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 5 Rajata (500 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata (200 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases MDF during battle."*
- **Efek Mekanik Game:** **Buff MDF**
- **Sumber Perolehan:** Combat Supply / Alchemy (Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Swift Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 5 Rajata 50 Tamra (550 Tamra)
- **Harga Jual Standar (40%):** 2 Rajata 20 Tamra (220 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases AGI during battle."*
- **Efek Mekanik Game:** **Buff AGI**
- **Sumber Perolehan:** Combat Supply / Alchemy (Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


### 🔹 Fortune Tonic
- **Kategori / Subkategori:** Consumable / `Battle Buff`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 15 Rajata (1,500 Tamra)
- **Harga Jual Standar (40%):** 6 Rajata (600 Tamra)
- **Target Penggunaan (Scope):** `1 Ally`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Temporarily increases LUK during battle."*
- **Efek Mekanik Game:** **Buff LUK**
- **Sumber Perolehan:** Rare Alchemy (Cakrawala)
- **Catatan Implementasi:** Craftable unless source/reward restriction applies.


## 8. Gulungan Sihir Tempur (Combat Magic Scrolls)

Memicu mantra sihir elemental langsung ke target musuh tanpa menghabiskan MP pengguna (skala MAT caster).

| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |
|---|---|---|---|---|---|---|
| **Fire Scroll** | 🟢 Uncommon | One Enemy | Battle Screen | 9R | 3R 60T | Basic Fire magic damage |
| **Water Scroll** | 🟢 Uncommon | One Enemy | Battle Screen | 9R | 3R 60T | Basic Water magic damage |
| **Wind Scroll** | 🟢 Uncommon | One Enemy | Battle Screen | 9R | 3R 60T | Basic Wind magic damage |
| **Earth Scroll** | 🟢 Uncommon | One Enemy | Battle Screen | 9R | 3R 60T | Basic Earth magic damage |
| **Light Scroll** | 🔵 Rare | One Enemy | Battle Screen | 25R | 10R | Basic Light magic damage |
| **Dark Scroll** | 🔵 Rare | One Enemy | Battle Screen | 25R | 10R | Basic Dark magic damage |


### 🔹 Fire Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 9 Rajata (900 Tamra)
- **Harga Jual Standar (40%):** 3 Rajata 60 Tamra (360 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Fire-element magic attack."*
- **Efek Mekanik Game:** **Basic Fire magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Fire`
- **Sumber Perolehan:** Scroll Crafting / Magic Shop (Nusvanir)
- **Catatan Implementasi:** Wuru Loka — Api (Pyrowisp). Craftable.


### 🔹 Water Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 9 Rajata (900 Tamra)
- **Harga Jual Standar (40%):** 3 Rajata 60 Tamra (360 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Water-element magic attack."*
- **Efek Mekanik Game:** **Basic Water magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Water`
- **Sumber Perolehan:** Scroll Crafting / Magic Shop (Nusvanir)
- **Catatan Implementasi:** Wuru Loka — Air (Aqua). Craftable.


### 🔹 Wind Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 9 Rajata (900 Tamra)
- **Harga Jual Standar (40%):** 3 Rajata 60 Tamra (360 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Wind-element magic attack."*
- **Efek Mekanik Game:** **Basic Wind magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Wind`
- **Sumber Perolehan:** Scroll Crafting / Magic Shop (Nusvanir)
- **Catatan Implementasi:** Wuru Loka — Udara (Vayu). Craftable.


### 🔹 Earth Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🟢 Uncommon
- **Harga Beli Pasar:** 9 Rajata (900 Tamra)
- **Harga Jual Standar (40%):** 3 Rajata 60 Tamra (360 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Earth-element magic attack."*
- **Efek Mekanik Game:** **Basic Earth magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Earth`
- **Sumber Perolehan:** Scroll Crafting / Magic Shop (Nusvanir)
- **Catatan Implementasi:** Wuru Loka — Tanah (Terra). Craftable.


### 🔹 Light Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar (40%):** 10 Rajata (1,000 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Light magic attack."*
- **Efek Mekanik Game:** **Basic Light magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Light`
- **Sumber Perolehan:** Sacred Scroll Crafting / Temple (Avalerion / Tirta Amarta)
- **Catatan Implementasi:** Poros Sang Hyang Cahaya. Craftable through sacred sources.


### 🔹 Dark Scroll
- **Kategori / Subkategori:** Consumable / `Magic Scroll`
- **Tingkat Kelangkaan (Rarity):** 🔵 Rare
- **Harga Beli Pasar:** 25 Rajata (2,500 Tamra)
- **Harga Jual Standar (40%):** 10 Rajata (1,000 Tamra)
- **Target Penggunaan (Scope):** `One Enemy`
- **Waktu Penggunaan (Occasion):** `Battle Screen`
- **Deskripsi Lore:** *"Unleashes a basic Dark magic attack."*
- **Efek Mekanik Game:** **Basic Dark magic damage**
- **Formula Efek / Damage:** `100 + a.mat * 2`
- **Elemen Kerusakan:** `Dark`
- **Sumber Perolehan:** Occult Scroll Crafting / Rare Drop (Raksamala)
- **Catatan Implementasi:** Poros Kala Laksana. Restricted occult crafting.

