# Wildlife — hubungan regional, material dan pemanggilan

Status: **audit sumber dan proposal non-numerik**, 2026-09-17. Semua angka yang disebut sebagai ID menunjuk record existing, bukan perubahan balance. Record lengkap per creature ada di pasangan JSON/Markdown. Dokumen ini menghubungkan catatan lintas sumber tanpa mengubah canon regional atau database.

## Batas regional

Mandala bergantung pada pertanian dan perdagangan (`03_Region/01_Mandala Kingdom/Economy.md`). Sapi Perah, Bebek Danau dan Kelinci Lingkar Bumi memberi konteks fauna domestik, air tawar dan buruan; **usulan** quest perlindungan ternak/lahan harus lebih dahulu menentukan apakah hewan merupakan musuh, objek evakuasi atau sumber panen. Label habitat Pinggiran Jenggala pada Babi tidak menetapkan koordinat Mandala. Jangan mengubah semua satwa menjadi sumber Saka otomatis.

Astradipa mempunyai kanopi Asrivana, wilayah Hanorok, ancaman mutasi dari Raksamala, serta perdagangan tertutup di Wana Prasetya (`02_World/Astradipa.md`, Economy/Threat Astradipa). Habitat Rusa Tanduk-Cabang sudah menyebut hutan tersebut. Deer Hide yang menyebut Mandala masih konflik provenance item. **Usulan:** perburuan dan distribusi material harus memperhitungkan izin/akses hutan; belum ada quest atau izin baru dibuat. Macan/Serigala yang hanya menyebut tajuk/hutan tidak otomatis ditempatkan di Astradipa.

Arkananta mempunyai tebing, gua, mineral serta Butoraksa, Troliogoro dan Rakshorien (`02_World/Arkananta.md`, Economy/Threat Arkananta). Kambing pelompat tebing dan Arkananta Horn punya rantai forge nyata di catatan item/equipment. **Usulan:** biaya akses lintasan dapat membatasi panen; jangan menetapkan timer respawn atau tarif. Ekonomi lokal umumnya barter, tetapi Economy regional memberi pengecualian Troliogoro yang menghargai Saka Kencana; jangan menyalin klaim umum “semua tidak mengenal koin” tanpa pengecualian.

## Wilayah lain: batas batch berikutnya

| Wilayah / sumber | Hubungan yang harus dipertahankan |
|---|---|
| Avalerion — World + Threat | Guardian terkait benteng dan Avesari; bukan fauna generik. Class tokoh perlu dipisah dari rank encounter. |
| Cakrawala — World + Threat + Sistem Ekonomi | Pasar dan ancaman kriminal memberi jalur perdagangan material, bukan izin spawn fauna semua wilayah. |
| Tirta Amarta — World + Threat | Tidak ada invasi fisik menurut sumber regional; jangan menambahkan hunting hostile untuk melengkapi daftar encounter. |
| Nusa Sayendra — World + Threat | Garuda menjaga front udara dan bantuan Avalerion. Sentinel adalah jabatan/militer, bukan species. |
| Agnitra — World + Threat + profil Nagarasven | Vulkanisme dan hilangnya akal naga menjelaskan ancaman; boss nest bukan sekadar HP lebih tinggi. |
| Raksamala — World + Threat + profil Drahkthar | Hierarki Sangrahal/Bhuta/Dhemit, sumber jiwa dan tujuh fortress; summons memerlukan kontrol/kontrak yang dijelaskan. |
| Rangkaruna — `03_Region/09_Laut_Rangkaruna/Laut_Rangkaruna.md` | Karang dangkal, palung, badai dan rute kapal membedakan encounter; fauna air tawar bukan fauna laut. |
| Thalantira — World + Threat + Prologue 07–09 dan Untold Story 01 | Ilusi damai, penjaga kuil dan kondisi setelah pengungkapan harus dipisah per era. Void tidak diberi elemen atau inflasi stat baru. |

Semua baris di atas merupakan batas integrasi bersumber, belum rework boss/map. Geografi tidak menetapkan level band, spawn weight, makanan spesifik atau progression numerik.

## Creature → material → penggunaan → ekonomi

Sumber mekanis: `10_Game Project/Tales of The Dark Time/data/Enemies.json`, `Items.json`, `Weapons.json`, `Armors.json`. Enam item existing direferensikan; tidak ada item baru.

| Material | Creature runtime | Contoh penggunaan existing | Gap |
|---|---|---|---|
| Beast Bone (Items 99, Common) | Babi, Beruang, Buaya, Kambing, Kura-kura, Macan, Rusa, Sapi, Serigala | Leather Knuckles (Weapons 25), Beastbone Bracelet (Armors 13), Jenggala Charm (Items 289) | Recipe catatan; belum executable |
| Beast Fang (Items 100, Common) | Babi, Beruang, Buaya, Kelinci, Macan, Serigala, Piton | Steel Fang (Weapons 32), Obsidian Claws (Weapons 27), Beastbone Bracelet | Fang pada Kelinci pasif perlu konteks; fungsi overlap sengaja reuse material umum |
| Deer Hide (Items 60, Common) | Rusa | Deerhide Vest (Armors 5), Leather Knuckles | Asal Mandala vs habitat Astradipa perlu keputusan |
| Arkananta Horn (Items 102, Uncommon) | Kambing Arkananta | Arkananta Horn Spear (Weapons 21), Horn Totem (Armors 35) | Forge ada dalam catatan; akses bahan dan barter belum dikalibrasi |
| Clear Crystal (Items 74, Common) | Bebek, Ikan | Pine Staff (Weapons 37), Clear Rune (Weapons 43) | Asal Common Deposits vs drop satwa belum dijelaskan |
| Spirit Dust (Items 282, Common) | Ayam, Puyuh | Clear Rune (Weapons 43), Spirit Dust Talisman (Armors 16) | Item menyebut sisa Wisp; jangan mengarang unggas spiritual untuk membenarkan drop |

Rujuk snapshot tiap creature untuk daftar drop yang persis, denominator runtime dan seluruh output yang menyebut material. Tabel ini menunjukkan relasi database, bukan ratifikasi ekologi drop. EXP/Saka kalibrasi tetap null. Harga item bukan harga jual/kurva income yang otomatis sah. Audit farming kelak mencakup respawn, akses map, drop multiplier, penjualan, material sink, summon/revive kills, recovery cost dan kemampuan AoE/control; belum ada exploit yang dinyatakan terbukti.

`NUSV_ItemSynthesis.js` meminta blok `<Synthesis Recipe>` dengan ID bahan. Database yang diperiksa tidak memiliki blok itu; `<NUSV Craft Recipe: ...>` dan teks “Konsep recipe” tidak dikenali sebagai recipe oleh plugin tersebut. Jangan mengklaim material sudah bisa dicraft hanya karena namanya ditemukan. Jangan mengubah catatan menjadi recipe aktif sebelum biaya/progression disetujui.

## Occultist, Cultist, Necromancer

`Mekanik_Class_Job.md` menetapkan Occultist T2, Cultist T3, Necromancer T4; class runtime learnings menghubungkan skill berikut. Pemeriksaan ini mengidentifikasi **rancangan yang tersimpan**, bukan membuktikan pemanggilan berjalan.

| Class | Record skill / entitas | Resource/material yang tercatat | Batas implementasi |
|---|---|---|---|
| Occultist | Skill 98 Jenggala | MP cost pada skill; Items 289 Jenggala Charm mengacu Drakthar Essence + Beast Bone | Note hanya meminta summon plugin; recipe concept dan konsumsi catalyst belum terbukti |
| Cultist | Skills 136–139, Bhuta Dread-Mercenary/Hollow-Knight/Fallen-Cleric/Plague-Rogue | Items 290 Bloodbound Catalyst terkait Blood Sacrifice Pact; soul/essence terms sudah ada | Hubungan setiap bahan dengan skill harus dipetakan; tidak boleh menyimpulkan zero-cost karena mpCost 0 saja |
| Necromancer | Skills 248–251 Vanguard, 253–256 Sanctuary; skill 259 Summon Demon Lord Sangrahal | Bound Soul 286, Condensed Soul 287 dan covenant items 374–380 mempunyai catatan ritual | Asal Bhuta dan ketaatan pada Sangrahal harus cocok lore; summon Sangrahal memerlukan keputusan identitas/avatar/kontrak, tidak dijelaskan otomatis |

Lore Necromancer menyebut tengkorak/roh, sementara kit runtime menamai Bhuta dan Sangrahal. Drahkthar tidak boleh dianggap undead netral yang bebas dimiliki pemain. Prologue 10 membedakan portal Jenggala dari necromancy mayat. Kontrak Gadai Sukma dan kontrol mutlak Sangrahal tetap berlaku sampai pemilik menetapkan pengecualian.

`SRD_SummonCore` dan `SRD_SummonBattlerImages` enabled, tetapi note skill yang diperiksa hanya instruksi “Use summon plugin”, bukan konfigurasi summon aktor yang lengkap. Belum ada bukti jalur acquisition → recipe → consumption → summon entity untuk catalyst di atas. Audit lanjutan harus menentukan actor summon IDs, cost pay/check, durasi, kematian caster, maksimal summon dan penggunaan action economy. Jangan membuat tulang/jiwa/sigil baru karena kolom kosong; item konsep existing harus direuse.
