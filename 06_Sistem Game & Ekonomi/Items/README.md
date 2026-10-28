# 📦 Database Master Item & Inventaris Nusvanir

Selamat datang di repositori database resmi item, barang konsumsi, bahan baku penempaan, barang berharga, dan barang kunci untuk proyek **Nusvanir RPG (Turn-Based System)**.

Total seluruh item yang terdaftar dan terintegrasi dalam database adalah **398 Item**, yang bersumber langsung dari `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx`.

---

## 🗂️ Struktur Direktori Database Items

| File Dokumen | Kategori Item | Jumlah Item | Ruang Lingkup & Fungsi Utama |
|---|---|---|---|
| [01_Consumables.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/01_Consumables.md) | **Consumable** | 29 Item | Ramuan HP/MP/SP, Revive, Obat Status, Tonik Buff Tempur, dan Gulungan Sihir. |
| [02_Materials.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/02_Materials.md) | **Material** | 206 Item | Bijih tambang, kayu hutan, batuan, herbal, kulit, tulang, sisa arwah, hingga material naga purba. |
| [03_Forge_&_Enhancement.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) | **Forge** | 106 Item | Kristal soket stat (18 stat turn-based x 4 tier), kristal elemen, Enhance Stone, Socket Core, Upgrade Core. |
| [04_Valuables.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/04_Valuables.md) | **Valuable** | 36 Item | Trophy perburuan monster, emblem Chief Arkananta, lambang ksatria Avalerion, fosil langka. |
| [05_Key_Items.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/05_Key_Items.md) | **Key Item** | 21 Item | Jimat pemanggilan, segel komandan iblis, dan Demon Covenants untuk kontrak kelas Necromancer. |

---

## 🪙 Standarisasi Mata Uang & Valuasi Ekonomi (Saka)

Seluruh nilai item dalam game mengacu pada mata uang koin mineral resmi Nusvanir:

1. **Saka Tamra (Tembaga):** Koin dasar (1 Tamra). Dipakai untuk transaksi mikro dan kebutuhan dasar rakyat jelata.

2. **Saka Rajata (Perak):** Koin menengah (**1 Saka Rajata = 100 Saka Tamra**). Mata uang standar petualang dan perdagangan umum.

3. **Saka Kencana (Emas):** Koin tertinggi (**1 Saka Kencana = 100 Saka Rajata = 10,000 Saka Tamra**). Digunakan untuk senjata pusaka, material epik, dan transaksi makro bangsawan.


> [!TIP]
> **Aturan Penjualan Kembali (Sell Ratio):**
> - **Barang Biasa & Material:** Dijual seharga **50% (0.5x)** dari harga beli pasar.
> - **Item Konsumsi (Consumables):** Dijual seharga **40% (0.4x)** dari harga beli pasar guna mencegah arbitrase toko (*flipping*).
> - **Barang Kunci (Key Items):** Tidak memiliki harga jual (*Unsellable*).


---

## ⚔️ Integrasi Mekanik Turn-Based RPG

Setiap kategori item memiliki dampak langsung terhadap gameplay pertempuran berbasis giliran (*Turn-Based Combat*):

- **Sistem Stamina Points (SP):** Menggantikan sistem TP lama. Karakter fisik memerlukan SP untuk skill jurus. Penggunaan item seperti *Focus Drop* dan pemasangan *Focus Crystal* menjaga sustain SP karakter selama pertempuran panjang.

- **Konsumsi 1 Action Turn:** Penggunaan item pemulihan atau buff selama battle mengonsumsi giliran aksi karakter, menuntut perhitungan taktis antara menyerang, bertahan, atau memulihkan sekutu.

- **18 Kristal Soket Presisi:** Seluruh kristal soket pada [03_Forge_&_Enhancement.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) secara akurat memodifikasi 18 Parameter RPG Nusvanir: `Max HP`, `Max MP`, `ATK`, `DEF`, `MAT`, `MDF`, `Action Speed (AGI)`, `LUK`, `Hit Rate (HIT)`, `Evasion (EVA)`, `Magic Evasion (MEV)`, `Critical Rate (CRI)`, `Critical Evasion (CEV)`, `Magic Reflection (MRF)`, `Counter Attack (CNT)`, `HP Regen (HRG)`, `MP Regen (MRG)`, dan `SP Regen (TRG)`.

- **Sinergi Kontrak Necromancer:** Kontrak iblis pada [05_Key_Items.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/05_Key_Items.md) mengaktifkan cabang skill pemanggilan arwah bagi class Necromancer sesuai alur Dual Level System.
