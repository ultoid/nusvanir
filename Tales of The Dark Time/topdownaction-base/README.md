# Tales of The Dark Time - Top Down Action Base

Repositori ini berisi dasar (base) dari game action RPG *top-down* bergaya Rogue-lite.

## Log Pembaruan (Update Log) - Sesi Terkini

### 1. Perombakan Sistem Antarmuka (UI Modular)
- **HUD Modular**: Pemecahan UI Monolitik (`hud.tscn`) menjadi beberapa file terpisah yang lebih bersih dan efisien:
  - `PlayerHUD.tscn`: UI Stat Pemain (HP, MP, EP, EXP) & Slot Cepat (Quickslot).
  - `BossHUD.tscn`: UI khusus pertarungan Boss (akan muncul saat Boss aktif).
  - `GameOverHUD.tscn`: Layar penutup saat pemain mati.

### 2. Layar Game Over & Ressurect (Bangkit Kembali)
- Sistem kematian pemain (*Game Over*) telah diperbarui. Saat mati, pemain disajikan 2 pilihan:
  - **Respawn di Town**: Mengulang dari awal (Main City) tanpa biaya.
  - **Ressurect (100 Koin)**: Bangkit kembali di lokasi kematian dengan 100% HP dan MP penuh, tapi mengorbankan 100 koin emas.

### 3. Ekstraksi dan Pembaruan Sistem Inventory (Tas)
- Pemisahan antarmuka *Inventory* dari menu profil karakter menjadi jendela tersendiri (tombol **B**).
- Fitur interaktif tas: Mengklik item akan menampilkan *Dropdown/Popup Menu* untuk 3 opsi:
  - **Gunakan**: Langsung mengonsumsi item dari tas.
  - **Quickslot**: Mendaftarkan item ke slot cepat agar bisa diakses lewat pintasan *keyboard* (tombol **5** atau **6**).
  - **Buang**: Membuang 1 item dari tas secara instan.

### 4. Sistem Slot Cepat (Quickslot) Potion & Skill
- Tersedia 4 slot cepat untuk *Skill/Job* (tombol 1-4) (akan datang).
- Tersedia 2 slot cepat untuk Item Potion (tombol 5-6). Item bisa didaftarkan langsung melalui menu *Inventory*.

### 5. Penyempurnaan Mekanik Karakter (Movement & Stamina)
- **Konsumsi Stamina Lari**: Aksi berlari menahan tombol **Shift** (Sprint) sekarang akan mengonsumsi **10 EP (Energy Points) per detik**.
- **Jeda Regenerasi**: Regenerasi otomatis EP akan diblokir dan berhenti sepenuhnya selama tombol Shift ditekan, menambah kesan taktis dan manajemen stamina.
- Efek Serangan & *Knockback* pemain dirancang menyesuaikan dengan status *Defense/VIT*.

### 6. Mode Debugging Pengembang
- **F1**: Instan *Level Up* +1 dan mendapatkan Stat Point.
- **F2**: Menambahkan +1000 Koin Emas.

### 7. Sistem Kemampuan (Skill & Sihir)
- **Sistem *Skill Tree***: Menu khusus untuk melihat dan memasang *skill* (tombol **K**).
- **Mekanik *Targeting* AoE**: Fitur membidik sihir area secara *real-time* dengan efek gerak lambat (*Slow Motion* 20%). 
  - Dilengkapi lingkaran batas aman (*max range*) biru dan lingkaran target proyektil merah.
  - Lingkaran akan berkedip (*blinking*) selama fase *casting*, mengunci posisi target tembakan di tanah sebagai zona aman.
- **Sihir *Fireball***: Skill tipe AoE yang memberikan ledakan bola api dan merusak banyak musuh sekaligus di dalam jangkauan ledakannya, serta meninggalkan noda gosong (*scorch mark*).
- **Sihir *Heal***: Skill tipe *instant* untuk menyembuhkan HP diri sendiri.
- **Pemolesan *Charge Attack***: *Heavy Attack* diganti menjadi *Charge Attack* yang memicu pergerakan menerjang (*lunge*) sejauh setengah *dash* dengan 200% *damage*.

### 8. Reorganisasi Struktur Proyek
- Pembersihan dan pengelompokan ulang file-file *Scene* (`.tscn`) ke dalam sub-direktori spesifik agar proyek lebih rapi dan profesional:
  - `Scenes/Maps/` (Peta Kota, Dungeon)
  - `Scenes/Entities/` (Player, Musuh, NPC)
  - `Scenes/UI/` (Seluruh HUD, Menu, dan Layar Dialog)
  - `Scenes/Items/` (Koin, Gem EXP)
  - `Scenes/Skills/` (Proyektil, Indikator Target)

### 9. Sistem Equipment & Profil Karakter Ala MMORPG Klasik
- **Antarmuka R.O Style**: Perombakan total pada layar profil karakter (tombol **C**) yang mengadaptasi tata letak status klasik bergaya Ragnarok Online, lengkap dengan *base stat + bonus*.
- **Slot Perlengkapan Dinamis**: Pemain kini bisa menggunakan (*equip*) dan mencopot (*unequip*) senjata, zirah, dan aksesoris yang memberikan dampak instan pada kekuatan serangan, pertahanan, hingga maksimum HP/MP.
- **Sistem Pengaman Copot Item**: Ditambahkan jendela konfirmasi (*pop-up*) saat hendak melepas perlengkapan untuk menghindari ketidaksengajaan.

### 10. Mobilitas Tempur Responsif (Roguelite Mobility)
- Karakter kini sepenuhnya dibebaskan untuk bergerak dan berlari secara bersamaan ketika sedang melancarkan *basic attack*.
- Arah tebasan dikunci secara stabil pada titik ayunan pertama, menjaga akurasi animasi sembari tetap mengizinkan mobilitas yang tinggi untuk menghindari serangan musuh.

---

## Panduan Modifikasi Game (Tutorial)
Jika Anda ingin berkreasi membuat karakter, NPC, Musuh, atau Bos naga buatan Anda sendiri tanpa perlu menyentuh bahasa pemrograman (coding) dari nol, silakan buka dan baca dokumen panduan lengkap yang telah disediakan.

🔗 **[Buka Tutorial Pengembangan Game (TUTORIAL_DEV.md)](./TUTORIAL_DEV.md)**
