# Tutorial Pengembangan Nusvanir: Tales of The Dark Time

Dokumen ini berisi panduan teknis yang mudah dipahami bagi Anda yang ingin menambah konten game sendiri tanpa harus mengkoding dari nol.

---

## 1. Panduan Membuat NPC Baru
NPC di game ini sangat fleksibel (`Scenes/npc.tscn`). Anda bisa membuatnya sekadar untuk cerita (*lore*), membuka toko (Merchant), atau penjaga gerbang (Portal).

### Langkah-langkah:
1. Buka *scene* di mana Anda ingin meletakkan NPC (contoh: `Scenes/maincity.tscn`).
2. Tarik (*drag and drop*) file `Scenes/npc.tscn` dari panel FileSystem ke dalam layar kerja 2D Anda.
3. **Mengganti Visual/Gambar NPC**:
   - Klik NPC yang baru Anda masukkan.
   - Centang opsi **Editable Children** (klik kanan pada node NPC -> centang *Editable Children*).
   - Klik node `Sprite2D` yang muncul di dalam NPC tersebut.
   - Di bagian Inspector sebelah kanan, pada properti **Texture**, tarik gambar/sprite karakter baru Anda ke sana.
4. **Mengubah Fungsi & Teks Percakapan NPC**:
   - Klik node utama NPC tersebut (yang bernama `NPC`).
   - Di panel Inspector paling atas, lihat bagian **Script Variables**.
   - `Npc Name`: Isi dengan nama karakter (misal: "Pak Tua").
   - `Dialogue Lines`: Klik tombol **Array**, lalu tambah elemen sesuai jumlah dialog. Isi setiap elemen dengan teks yang akan diucapkan NPC.
   - `Npc Type`: Ini adalah otak dari NPC tersebut!
     - Isi dengan `"Lore"` jika NPC hanya berfungsi untuk bercerita (setelah dialog selesai, tidak terjadi apa-apa).
     - Isi dengan `"Merchant"` jika Anda ingin memunculkan menu Toko (Beli/Jual) setelah dialog selesai.
     - Isi dengan `"Portal"` jika Anda ingin NPC ini memunculkan pilihan Yes/No untuk men-teleportasi (Warp) pemain ke Dungeon.

---

## 2. Panduan Membuat Musuh (Enemy) Baru
Musuh biasa diatur oleh `enemy.tscn` (tipe memukul/dekat) atau `ranged_enemy.tscn` (tipe menembak/jauh).

### Langkah-langkah (Contoh membuat monster baru):
1. Buka file `Scenes/enemy.tscn`. Di menu paling atas kiri, klik **Scene -> Save As...** dan simpan dengan nama baru, misalnya `Scenes/orc_enemy.tscn`.
2. Buka *scene* `orc_enemy.tscn` yang baru dibuat.
3. **Mengganti Sprite (Visual)**:
   - Klik node `Sprite2D` milik musuh tersebut, ganti **Texture**-nya dengan gambar Orc Anda.
   - Jangan lupa sesuaikan ukuran `CollisionShape2D` (bentuk kotak biru) agar ukurannya pas dengan gambar tubuh Orc tersebut.
4. **Mengatur Kekuatan Musuh**:
   - Klik node `Enemy` paling atas.
   - Di panel Inspector (Script Variables), Anda bisa mengatur sesuka hati:
     - `Speed`: Kecepatan bergerak/mengejar pemain.
     - `Max Health`: Darah musuh (semakin besar semakin tebal).
     - `Damage`: Kerusakan yang diberikan ke HP pemain saat bersentuhan.
     - `Coin Drop Amount`: Jumlah koin yang pasti dijatuhkan saat musuh ini mati.
5. **Memunculkannya di Map**:
   - Tarik file `orc_enemy.tscn` ke dalam peta `dungeon_2.tscn`.
   - Atau, klik node `GrindingCamp` di peta, lalu di properti `Enemy Scene` ganti dengan `orc_enemy.tscn` agar kamp tersebut menghasilkan Orc terus-menerus.

---

## 3. Panduan Membuat Boss Enemy & Pola Serangannya
Boss memiliki pergerakan yang lebih pintar dan serangan yang lebih berbahaya (`Scenes/boss_enemy.tscn`).

### Langkah-langkah:
1. Sama seperti musuh biasa, buka `Scenes/boss_enemy.tscn`, klik **Scene -> Save As...** menjadi `Scenes/boss_dragon.tscn`. Buka file tersebut.
2. Ganti `Sprite2D` menjadi gambar naga Anda.
3. **Membuat *Script* Khusus Boss**:
   - Agar *script* Boss asli tidak tertimpa, buka tab FileSystem, cari file `Scripts/boss_enemy.gd`, lalu **Klik Kanan -> Duplicate**. Beri nama `boss_dragon.gd`.
   - Di *scene* `boss_dragon.tscn` Anda, klik node Boss paling atas, lalu seret *script* `boss_dragon.gd` ke bagian paling bawah Inspector untuk mengganti *script* lamanya.
4. **Membuat Pola Serangan Baru (Contoh: Menembak Melingkar)**:
   - Buka *script* `boss_dragon.gd` tersebut.
   - Tambahkan fungsi baru ini di paling bawah kodingan:
     ```gdscript
     func cast_fireball_ring():
         var projectile_scene = load("res://Scenes/Skills/enemy_projectile.tscn")
         if not projectile_scene: return
         
         # Tembakkan 8 peluru melingkar (setiap 45 derajat)
         for i in range(8):
             var proj = projectile_scene.instantiate()
             proj.direction = Vector2.RIGHT.rotated(deg_to_rad(i * 45))
             proj.global_position = global_position
             get_tree().current_scene.call_deferred("add_child", proj)
     ```
   - Lalu, cari fungsi `_process(delta)` di dalam *script* tersebut. Di bagian bawah `_process`, ada sistem *cooldown* serangan (yang ada tulisan `if attack_timer <= 0:`).
   - Di bawah kondisi tersebut, panggil fungsi `cast_fireball_ring()` Anda tadi! Naga tersebut sekarang akan memuntahkan peluru melingkar setiap beberapa detik!
5. **Mengatur Jumlah Drop Hadiah Boss**:
   - Masih di *script* naga, cari fungsi `drop_loot()`.
   - Di dalam situ ada kode `for i in range(5):`. Angka 5 adalah jumlah koin yang jatuh. Ganti menjadi 20 jika Anda ingin Boss ini menjatuhkan lebih banyak koin emas!

---

## 4. Panduan Menambah Item Baru
Sistem item di game ini sangat mudah diperluas! Data item disimpan secara terpusat di skrip Autoload (Scripts/item_db.gd).

### Langkah-langkah (Contoh membuat item Elixir):
1. Buka file Scripts/item_db.gd.
2. Anda akan melihat *Dictionary* bernama items. Tambahkan item baru Anda di sana:
   `gdscript
   var items = {
       "potion": { "name": "Red Potion", "type": "consumable", "effect_amount": 50, "price": 10 },
       "ether": { "name": "Blue Ether", "type": "consumable", "effect_amount": 30, "price": 20 },
       "elixir": { "name": "Elixir", "type": "consumable", "effect_amount": 999, "price": 100 } # <-- Item Baru Anda
   }
   `
3. Buka file Scripts/global.gd untuk mendaftarkan item tersebut ke dalam tas (Inventory) awal pemain:
   `gdscript
   var inventory: Dictionary = {
       "potion": 5,
       "ether": 2,
       "elixir": 1 # <-- Beri pemain 1 Elixir di awal permainan
   }
   `
4. **Memberikan Efek Fungsi pada Item**:
   - Jika item digunakan melalui Quick Slot (Hotkey 5 atau 6), buka Scripts/player.gd dan cari fungsi _use_quick_item(slot_index: int).
   - Tambahkan efek unik dari item Anda di bagian bawah fungsi tersebut:
     `gdscript
     if item_id == "potion":
         restore_hp(heal_amt)
     elif item_id == "ether":
         restore_mp(heal_amt)
     elif item_id == "elixir": # <-- Efek Item Baru Anda!
         restore_hp(heal_amt)
         restore_mp(heal_amt)
         print("Pemain menggunakan Elixir, HP & MP pulih penuh!")
     `
5. **Selesai!** Item Elixir Anda otomatis akan muncul di layar Inventory (tombol B), bisa dipasang ke *Quick Slot*, dan akan memulihkan HP sekaligus MP saat dipakai!

---

## 5. Panduan Menambah Sihir (Skill) Baru
Sistem skill di game ini sudah mendukung sihir langsung (*instant*) maupun berbasis target area (*target_aoe*). Data skill diatur melalui `Scripts/skill_db.gd`.

### Langkah-langkah (Contoh membuat sihir "Ice Storm" tipe AoE):
1. **Tambahkan Data Skill**:
   - Buka file `Scripts/skill_db.gd`.
   - Tambahkan *Ice Storm* ke dalam Dictionary `skills`:
     ```gdscript
     "ice_storm": {
         "name": "Ice Storm",
         "description": "Menjatuhkan badai es di area target. Membutuhkan 25 MP.",
         "req_level": 3,
         "mp_cost": 25,
         "cast_time": 2.5,
         "type": "target_aoe",
         "range": 300,
         "aoe_radius": 50,
         "effect_multiplier": 2.0,
         "icon_color": Color(0.2, 0.8, 1.0)
     }
     ```

2. **Membuat Scene Proyektil/Ledakan (Opsional, untuk tipe AoE)**:
   - Jika sihir Anda adalah AoE, buat *scene* baru (misal `ice_storm.tscn` dengan script `ice_storm.gd`) yang berisi `Area2D` untuk mendeteksi *Enemy* yang tumpang tindih. (Anda bisa menduplikasi file `fireball.tscn` dan mengubah efek visual serta warnanya menjadi biru).

3. **Memicu Sihir di Player**:
   - Buka `Scripts/player.gd` lalu cari fungsi `_start_cast_skill()`.
   - Di bagian paling bawah fungsi tersebut (setelah pengecekan `elif skill_id == "fireball":`), tambahkan eksekusi untuk *Ice Storm*:
     ```gdscript
     elif skill_id == "ice_storm":
         var storm_scene = load("res://Scenes/ice_storm.tscn")
         if storm_scene and get_tree().current_scene:
             var storm = storm_scene.instantiate()
             storm.global_position = t_pos
             storm.damage = int(magic_attack * data.get("effect_multiplier", 2.0))
             storm.aoe_radius = data.get("aoe_radius", 50.0)
             get_tree().current_scene.add_child(storm)
     ```
4. **Selesai!** Jika pemain mencapai Level 3, ia bisa memasang "Ice Storm" dari menu Skill (tombol **K**). Saat *hotkey* ditekan, waktu otomatis melambat, memunculkan indikator target area biru, dan mengeksekusi *ice_storm.tscn* saat diklik!
