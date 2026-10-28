# 🛡️ Database Induk Perlengkapan Petualang Nusvanir

Katalog resmi seluruh perlengkapan senjata, zirah pelindung, tameng, aksesoris, dan relik purba untuk game RPG *Turn-Based* Nusvanir.

Seluruh data pada direktori ini dihasilkan langsung dari spreadsheet master **`Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx`** dan diselaraskan dengan spesifikasi **[STANDAR_DATABASE_TYPES_RPG_MAKER.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md)**.

---

## 📑 Struktur Berkas Perlengkapan

| Berkas Dokumen | Kategori Perlengkapan | Jumlah Entri | Ruang Lingkup & Cakupan Utama |
|---|---|:---:|---|
| [01_Weapons.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/01_Weapons.md) | **Weapons (Senjata)** | **66 Senjata** | 10 Tipe Senjata resmi (Long Sword, Sword, Gloves, Spear, Axe, Staff, Rune, Bow, Crossbow, Dagger) dari Tier Common hingga Mythic. |
| [02_Armors.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/02_Armors.md) | **Armors & Gear (Zirah)** | **123 Perlengkapan** | Pelindung Tubuh (Armor), Tameng (Shields), Pelindung Kepala (Helm), Sepatu (Boots), Aksesoris, dan Relik Pusaka Purba dengan sistem Set Bonus. |

---

## ⚙️ Integrasi Sistem Tempur Turn-Based

1. **7 Slot Perlengkapan (`YEP_EquipCore`):**
   - `01 Primary Weapon`: Senjata utama tangan kanan (atau senjata 2 tangan).
   - `02 Secondary Weapon`: Tameng (Light/Heavy Shield), fokus magis, atau senjata kedua (*Dual Wield*).
   - `03 Helm`: Pelindung kepala.
   - `04 Armor`: Zirah tubuh (Basic Clothes, Magic Robe, Light Armor, Heavy Armor).
   - `05 Boots`: Sepatu penambah Action Speed (AGI) dan Evasion.
   - `06 Accessory`: Cincin, jimat, dan kalung stat sekunder.
   - `07 Relic`: Pusaka sakral penambah efek pasif unik tempur.

2. **Sinergi Soket Kristal & Tempa:**
   - Seluruh senjata dan zirah dapat dipasangi kristal soket stat dari [03_Forge_&_Enhancement.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) untuk meningkatkan 18 Parameter RPG secara presisi.
3. **Sistem Sinergi Set Bonus:**
   - Memasang perlengkapan dari seri yang sama (misal: *Mandala Guard, Deerhide, Ironwood, Sunken, Astral, Dragon Hunter*) mengaktifkan buff kumulatif 2-Set, 3-Set, 4-Set, hingga 5-Set.
