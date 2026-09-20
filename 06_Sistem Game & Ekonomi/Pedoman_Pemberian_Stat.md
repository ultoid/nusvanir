# Pedoman Pemberian Stat Nusvanir

> **Status:** Aturan wajib untuk penyusunan stat monster, NPC tempur, summon, elite, dan boss.
>
> **Tujuan:** Mencegah angka diberikan berdasarkan tebakan, intuisi semata, penyalinan dari entri lama, atau sekadar membuat boss memiliki HP sangat besar.
>
> **Lokasi yang disarankan di repository:** `06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md`

---

## 1. Prinsip utama

Stat **bukan titik awal desain**. Stat adalah hasil dari:

1. posisi encounter dalam progression;
2. kondisi party saat encounter terjadi;
3. rumus damage dan healing yang benar-benar dipakai game;
4. equipment yang tersedia pada tahap tersebut;
5. skill, passive, state, elemen, dan pola aksi musuh;
6. target durasi serta tingkat ancaman encounter;
7. hasil simulasi dan playtest.

Codex **dilarang** menetapkan angka final hanya dari deskripsi seperti “kuat”, “cepat”, “boss”, “Tier 5”, atau “berasal dari Thalantira”. Deskripsi tersebut hanya menentukan profil relatif, bukan angka.

Aturan inti:

> **Tidak ada sumber + tidak ada perhitungan + tidak ada pengujian = tidak boleh disebut stat final.**

---

## 2. Cakupan parameter

Pedoman ini berlaku untuk parameter utama RPG Maker MV:

| Parameter | Arti desain | Tidak boleh ditentukan hanya dari |
|---|---|---|
| MHP / HP | Daya tahan sebelum kalah | ukuran tubuh atau rank |
| MMP / MP | Anggaran penggunaan skill berbasis MP | status sebagai pengguna sihir |
| ATK | Daya serang fisik sebelum formula dan modifier | kesan “brutal” |
| DEF | Mitigasi terhadap formula fisik | armor visual |
| MAT | Daya serang/heal magis sebelum formula dan modifier | elemen atau class sihir |
| MDF | Mitigasi terhadap formula magis | sifat spiritual |
| AGI | Urutan dan frekuensi aksi sesuai sistem aktual | kesan “cepat” |
| LUK | Pengaruh keberuntungan/status sesuai implementasi aktual | rarity atau tingkat boss |

HP, MP, ATK, DEF, MAT, MDF, AGI, dan LUK harus berupa bilangan bulat saat dipindahkan ke database game. Pembulatan hanya dilakukan setelah perhitungan, bukan pada setiap langkah antara.

---

## 3. Hierarki sumber kebenaran

Jika beberapa sumber bertentangan, gunakan urutan berikut:

1. **Database dan kode runtime game yang sedang dipakai**
   - `data/System.json`
   - `data/Enemies.json`
   - `data/Actors.json`
   - `data/Classes.json`
   - `data/Skills.json`
   - `data/Weapons.json`
   - `data/Armors.json`
   - `data/States.json`
   - plugin dan kode yang mengubah formula, turn order, critical, hit/evasion, element rate, state rate, regeneration, atau parameter cap.
2. **Dokumen sistem terbaru yang telah disetujui**
   - class/job;
   - progression dan level cap;
   - equipment dan upgrade;
   - skill dan state;
   - elemen;
   - encounter dan boss;
   - ekonomi/reward.
3. **Baseline hasil pengukuran build game terbaru**
   - stat party pada level dan gear target;
   - damage, healing, akurasi, critical, dan action order aktual;
   - hasil simulasi atau playtest.
4. **Entri Bestiary lama** sebagai data historis, bukan sumber angka final.
5. **Asumsi desain**, hanya jika ditulis terang-terangan dan diberi status `PROVISIONAL`.

Nama file atau tanggal modifikasi saja tidak cukup untuk menentukan otoritas. Periksa referensi silang dan pemakaian aktual oleh game.

### Rujukan Nusvanir yang sudah tersedia

- `06_Sistem Game & Ekonomi/Mekanik_Class_Job.md` — sumber struktur class dan Tier. Dokumen ini bersifat kualitatif dan **belum menyediakan kurva parameter numerik**.
- `06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md` — sumber resmi matchup 10 elemen dan multiplier `2x`, `1x`, `0.5x`, serta immunity `0x`.
- `06_Sistem Game & Ekonomi/Sistem_Ekonomi_&_Crafting.md` — sumber hubungan drop, crafting, equipment, dan ekonomi; bukan dasar langsung untuk combat stat.
- `07_Bestiary/**` — sumber identitas, lore, lokasi, serta angka warisan. Angka di sini harus diaudit ulang sebelum dianggap final.

Pada audit 17 September 2026, repository lore Nusvanir belum memuat database runtime RPG Maker MV seperti `Enemies.json`, `Classes.json`, `Skills.json`, `Weapons.json`, `Armors.json`, dan `States.json`. Karena itu, angka Bestiary yang ada belum cukup untuk membentuk kurva balance final tanpa memasukkan project game/database terbaru.

---

## 4. Status validitas stat

Setiap stat block wajib memiliki salah satu status berikut:

| Status | Makna | Boleh masuk database rilis? |
|---|---|---:|
| `BLOCKED` | Data wajib belum tersedia; angka tidak boleh dibuat | Tidak |
| `PROVISIONAL` | Angka hasil model dengan asumsi yang dicatat, belum lolos playtest | Hanya build eksperimen |
| `CALIBRATED` | Dihitung dari database aktual dan lolos simulasi | Ya, untuk playtest |
| `VALIDATED` | Lolos playtest dalam konteks encounter sebenarnya | Ya |

Codex tidak boleh mengganti `BLOCKED` menjadi `PROVISIONAL` tanpa menuliskan seluruh asumsi. Codex tidak boleh menggunakan kata “final”, “balanced”, atau `VALIDATED` tanpa bukti playtest.

---

## 5. Gerbang wajib sebelum memberikan angka

Sebelum menghitung satu monster, isi checklist berikut.

### 5.1 Konteks progression

- [ ] Encounter terjadi pada chapter/area mana?
- [ ] Recommended level atau rentang level party diketahui?
- [ ] Ukuran party diketahui?
- [ ] Class/role party yang wajar diketahui?
- [ ] Tier dan kualitas equipment yang tersedia diketahui?
- [ ] Consumable, socket, upgrade, dan buff yang wajar diketahui?
- [ ] Apakah encounter wajib, opsional, rare, atau post-game?

### 5.2 Sistem perhitungan

- [ ] Formula setiap skill yang relevan dibaca dari database aktual?
- [ ] Critical rate dan critical multiplier diketahui?
- [ ] Hit, evasion, guard, PDR, MDR, recovery, variance, dan element rate diketahui?
- [ ] Sistem turn/action order dan jumlah aksi per giliran diketahui?
- [ ] State chance, resistance, durasi, dan stacking diketahui?
- [ ] Plugin yang mengubah parameter atau formula sudah diperiksa?

### 5.3 Target encounter

- [ ] Combat role musuh ditetapkan?
- [ ] Encounter type ditetapkan?
- [ ] Jumlah musuh dan komposisi troop diketahui?
- [ ] Target jumlah ronde/durasi pertarungan ditetapkan?
- [ ] Target tekanan terhadap HP/MP party ditetapkan?
- [ ] Mekanik phase, summon, heal, shield, revive, atau enrage sudah dihitung?

Jika salah satu informasi yang berdampak besar belum diketahui, jangan mengarang angka. Gunakan `BLOCKED`, sebutkan data yang kurang, lalu minta atau cari sumbernya.

---

## 6. Lembar acuan party

Stat musuh harus dihitung terhadap party acuan, bukan terhadap angka monster lain saja.

Buat sekurangnya tiga profil party pada titik progression yang sama:

| Profil | Tujuan | Contoh definisi |
|---|---|---|
| `LOW` | Pemain sedikit tertinggal tetapi masih valid | level bawah rentang, equipment minimum yang wajar |
| `EXPECTED` | Pengalaman utama yang ditargetkan | level rekomendasi, equipment dan upgrade median |
| `HIGH` | Pemain optimal tanpa eksploit | level atas rentang, build dan equipment kuat yang legal |

Untuk setiap profil, catat:

- MHP/MMP tiap anggota;
- ATK/DEF/MAT/MDF/AGI/LUK;
- PDR/MDR, element rate, state rate, guard, hit, evasion, critical;
- damage basic attack;
- damage skill berkelanjutan;
- burst damage yang tidak dapat digunakan setiap ronde;
- healing dan shielding berkelanjutan;
- jumlah aksi efektif per ronde;
- konsumsi MP/TP/item per ronde.

Jangan memakai satu karakter “rata-rata” jika encounter dirancang untuk party. Tank, damage dealer, support, dan karakter rapuh harus diuji terpisah.

---

## 7. Tentukan identitas tempur sebelum angka

Setiap musuh harus memiliki combat brief:

```yaml
combat_role: Bruiser | Tank | Assassin | Skirmisher | Mage | Support | Controller | Summoner | Sniper | Swarm
encounter_type: Normal | Elite | Rare | Mini Boss | Boss | Commander | World Boss | Story Boss
progression_point: "<chapter/area/level range>"
party_size: <integer>
troop_composition: "<jumlah dan jenis musuh>"
target_rounds: "<rentang yang telah disetujui>"
primary_pressure: HP | MP | Time | Status | Position | Resource
strengths: []
weaknesses: []
action_pattern: "<rotasi/kondisi AI>"
```

Role hanya menentukan **arah distribusi**, misalnya:

| Role | Cenderung tinggi | Cenderung rendah | Catatan |
|---|---|---|---|
| Tank | HP, DEF atau MDF | damage, AGI | Jangan menaikkan HP dan seluruh defense sekaligus tanpa target durasi |
| Bruiser | HP, ATK | utility atau speed | Ancaman konsisten, bukan burst assassin |
| Assassin | AGI, burst fisik | HP/DEF | Harus punya counterplay; hindari one-shot tak terbaca |
| Mage | MAT, MP | ATK/DEF | Nilai bergantung penuh pada formula dan biaya skill |
| Controller | AGI atau resource | raw damage | Kekuatan state harus masuk threat budget |
| Support | MP, MAT/MDF sesuai kit | damage mandiri | Heal, shield, cleanse, dan buff menambah effective HP/DPT troop |
| Summoner | MP, tempo | stat langsung | Nilai summon dihitung sebagai bagian action economy |
| Swarm | jumlah aksi kolektif | stat individu | Balance seluruh troop, bukan satu unit |

Tidak ada multiplier role universal sebelum baseline Nusvanir dikalibrasi.

---

## 8. Metode menghitung HP dan daya tahan

### 8.1 Hitung damage party aktual

Untuk setiap serangan representatif, evaluasi formula asli dari `Skills.json` dan seluruh modifier runtime.

Secara konseptual:

```text
damage_akhir = hasil_formula_skill
             × element_rate
             × physical_or_magical_rate
             × critical_modifier
             × guard_modifier
             × variance
             × modifier_plugin_lain
```

Urutan operasi harus mengikuti implementasi game aktual. Rumus di atas adalah daftar komponen, bukan pengganti kode runtime.

Hitung sekurangnya:

- damage minimum, expected, dan maksimum;
- peluang serangan mengenai target;
- peluang critical;
- frekuensi skill dapat digunakan;
- damage over time;
- damage yang hilang karena heal, shield, phase, invulnerability, summon, atau control.

### 8.2 Gunakan effective HP

HP tampilan bukan satu-satunya daya tahan.

```text
effective_HP = HP
             + healing_yang_realistis
             + shield_yang_realistis
             + nilai_summon_pelindung
             + damage_yang_dicegah_oleh_phase
```

Defense, resistance, evasion, counter, dan immunity juga meningkatkan waktu untuk mengalahkan musuh. Jangan menaikkan HP untuk menutup pengaruh mekanik tersebut dua kali.

### 8.3 Turunkan HP dari target durasi

Gunakan damage party per ronde yang benar-benar dapat dipertahankan:

```text
target_effective_HP = expected_party_net_damage_per_round × target_rounds
```

Lalu cari kombinasi HP, DEF/MDF, resistance, dan mekanik yang menghasilkan target tersebut. Jangan langsung menganggap seluruh target effective HP harus berupa raw HP.

Untuk troop berisi beberapa musuh:

```text
target_effective_HP_troop = total damage party selama target ronde
```

Bagikan budget itu menurut role dan prioritas target. Perhitungkan AoE; empat musuh tidak otomatis membutuhkan empat kali total HP.

---

## 9. Metode menghitung ATK, MAT, dan ancaman

Mulai dari hasil yang ingin dirasakan pemain, lalu selesaikan input stat melalui formula aktual.

### 9.1 Tetapkan target tekanan

Untuk setiap skill musuh, definisikan:

- target utama: tank, party median, atau karakter rapuh;
- expected damage sebagai angka dan persentase MHP target;
- frekuensi penggunaan;
- peluang hit dan critical;
- apakah damage single-target, AoE, DoT, counter, atau follow-up;
- telegraph dan kesempatan counterplay;
- kontribusi state/control.

### 9.2 Cari nilai ofensif

Gunakan formula skill aktual untuk mencari ATK/MAT yang menghasilkan target damage terhadap DEF/MDF profil `EXPECTED`. Jika formula kompleks, gunakan pencarian numerik atau simulasi; jangan menebak.

Setelah memperoleh kandidat:

1. uji terhadap profil `LOW`, `EXPECTED`, dan `HIGH`;
2. uji non-critical dan critical;
3. uji kondisi elemen `0.5x`, `1x`, dan `2x` yang mungkin terjadi;
4. uji buff/debuff yang legal;
5. periksa kombinasi skill dalam satu ronde;
6. periksa total damage seluruh troop.

Jika one-shot memang bagian desain, harus ditulis sebagai mekanik eksplisit dengan telegraph dan counterplay. One-shot akibat angka yang kebetulan terlalu tinggi dianggap gagal balance.

---

## 10. Metode menghitung DEF dan MDF

DEF/MDF harus diselesaikan dari formula damage aktual dan target durasi, bukan ditentukan sebagai persentase ATK monster.

Aturan:

- Hitung DEF terhadap beberapa skill fisik party, bukan basic attack saja.
- Hitung MDF terhadap beberapa skill magis party.
- Jangan memakai defense tinggi untuk membuat “kelemahan elemen” terasa perlu jika pemain mungkin tidak membawa elemen tersebut.
- Jangan menaikkan HP, DEF, MDF, resistance, evasion, heal, dan shield bersamaan tanpa menghitung effective HP total.
- Jika role hanya kuat terhadap satu tipe damage, tampilkan perbedaan DEF/MDF dengan jelas dan sediakan counterplay.
- Pastikan formula tidak menghasilkan damage nol atau negatif secara tidak sengaja pada build valid, kecuali immunity adalah mekanik yang disengaja.

---

## 11. Metode menghitung MP

MP berasal dari rotasi skill, bukan rank.

```text
MP_minimum = total biaya MP dari rotasi yang diharapkan
           + biaya respons kondisional yang mungkin dipakai
           + cadangan yang disengaja
```

Catat:

- perkiraan jumlah ronde hidup;
- urutan skill;
- cooldown atau syarat penggunaan;
- regenerasi MP;
- drain MP;
- phase reset;
- skill tanpa biaya;
- apakah kehabisan MP adalah counterplay yang sengaja dirancang.

Gunakan MP `0` jika musuh memang tidak memakai resource MP. Jangan memberi MP besar hanya karena monster adalah boss atau pengguna sihir.

---

## 12. Metode menghitung AGI

AGI ditentukan dari target urutan aksi terhadap distribusi AGI party `LOW`, `EXPECTED`, dan `HIGH`.

Dokumentasikan tujuan, misalnya:

- hampir selalu bergerak setelah tank;
- umumnya bergerak sebelum healer;
- bersaing dengan damage dealer cepat;
- selalu lebih dulu hanya saat skill telegraph tertentu aktif.

Periksa formula turn order dan random variance runtime. Jangan menyimpulkan bahwa AGI menggandakan jumlah aksi kecuali plugin/game memang menerapkannya.

Untuk musuh dengan multi-action, extra turn, counter, follow-up, summon, atau action speed modifier, masukkan semuanya ke action economy. AGI tinggi dan multi-action tidak boleh dihitung terpisah seolah salah satunya gratis.

---

## 13. Metode menghitung LUK dan status

LUK hanya boleh diberi bobot besar setelah implementasinya ditemukan di runtime. Periksa:

- formula pengaruh LUK terhadap application rate;
- state rate target;
- debuff rate;
- hit type skill;
- plugin yang mengganti luck effect;
- immunity dan resistance boss.

Nilai skill control mencakup giliran yang hilang, damage yang dicegah, setup combo, dan peluang aplikasinya. Musuh controller dengan raw damage rendah tetap dapat memiliki threat tinggi.

Jangan membuat boss kebal terhadap semua state sebagai solusi default. Tentukan salah satu:

- rentan penuh;
- resisten sebagian;
- durasi dipendekkan;
- diminishing return;
- kebal hanya pada state yang merusak mekanik;
- break/stagger khusus sebagai pengganti control biasa.

Gunakan hanya state yang ada atau telah disetujui di database Nusvanir.

---

## 14. Elemen: jangan dihitung dua kali

Ikuti `Mekanik_Efektivitas_Elemen.md` sebagai sumber matchup saat ini.

Aturan wajib:

1. Elemen mengubah **damage akhir melalui multiplier**, bukan menjadi alasan tersembunyi untuk menaikkan/menurunkan ATK, MAT, DEF, atau MDF lagi.
2. Uji seluruh matchup yang mungkin dibawa party pada titik progression tersebut.
3. Immunity `0x` harus memiliki alasan lore, komunikasi visual, dan jalur alternatif.
4. Dual-element harus mendefinisikan cara penentuan element rate di engine; jangan mengarang rata-rata atau menumpuk multiplier.
5. Cahaya vs Kegelapan mengikuti aturan mutual destruction yang ada, tetapi hasil damage tetap bergantung pada formula dan resource aktual.
6. Void tidak boleh diberi multiplier baru sebelum Void resmi masuk tabel elemen atau memiliki aturan tersendiri yang disetujui.

---

## 15. Encounter type dan boss

Label encounter tidak memberi multiplier stat otomatis. Label menentukan target pengalaman dan kebutuhan pengujian.

### Normal, Elite, dan Rare

- Hitung sebagai bagian troop dan area, bukan duel satu lawan satu.
- Elite/Rare boleh memiliki kit atau pressure lebih tinggi, tetapi kenaikannya harus terlihat pada target durasi/reward.
- Hindari menaikkan semua parameter sekaligus.

### Mini Boss dan Boss

Boss tidak boleh menjadi musuh biasa dengan HP sangat besar.

Perhitungan boss harus memasukkan:

- jumlah phase;
- HP gate;
- invulnerability;
- shield dan break bar;
- summon/adds;
- heal/regeneration;
- arena hazard;
- jumlah aksi per ronde;
- forced movement/control;
- dispel/cleanse;
- enrage dan batas waktu;
- perubahan resistance;
- checkpoint atau recovery antarfase.

Hitung tiap phase secara terpisah, lalu uji encounter utuh. Jika phase memakai HP bar yang sama, jangan melupakan recovery dan perubahan output party selama transisi.

### World Boss dan content ekstrem

- Tetapkan jumlah pemain/party dan aturan scaling lebih dulu.
- Bedakan scaling stat, scaling jumlah aksi, dan scaling mekanik.
- Jangan mengambil angka Thalantira lama sebagai baseline hanya karena nilainya besar.
- Nilai seperti HP `720000` pada Argentfang atau lonjakan HP makhluk Thalantira adalah **legacy candidate** sampai dapat dibuktikan oleh progression dan damage party aktual.

---

## 16. Reward bukan turunan langsung dari HP

EXP dan Saka dihitung dari progression economy dan waktu/risiko encounter, bukan sekadar persentase HP.

Pertimbangkan:

- waktu rata-rata mengalahkan encounter;
- konsumsi HP, MP, item, dan recovery;
- risiko wipe;
- aksesibilitas dan waktu respawn;
- kemudahan farming/automation;
- rarity encounter;
- nilai drop;
- target EXP dan Saka per menit pada area tersebut;
- potensi exploit melalui summon, AoE, elemental advantage, atau stun-lock.

Drop bernilai tinggi dapat menjadi bagian reward budget. Jangan memberikan EXP, Saka, dan drop maksimal secara bersamaan tanpa alasan.

---

## 17. Prosedur kerja wajib untuk Codex

Saat diminta membuat atau mengubah stat:

1. Cari seluruh referensi nama/ID target di repository.
2. Temukan database runtime dan plugin yang relevan.
3. Identifikasi versi sumber yang aktif.
4. Tulis combat brief.
5. Buat profil party `LOW`, `EXPECTED`, dan `HIGH`.
6. Ekstrak formula dan modifier aktual.
7. Tetapkan target ronde, pressure, dan action pattern.
8. Hitung kandidat stat dengan skrip/simulasi yang dapat diulang.
9. Uji skill, elemen, state, critical, AoE, heal, summon, dan seluruh troop.
10. Catat sumber, asumsi, hasil, serta status validitas.
11. Baru tulis angka ke Bestiary/database.
12. Jalankan pemeriksaan konsistensi setelah perubahan.

Codex **harus berhenti dan melaporkan kekurangan data** jika tidak dapat menemukan formula, baseline party, equipment, atau konteks progression yang diperlukan.

Codex tidak boleh:

- menyalin angka game lain;
- membuat kurva eksponensial tanpa persetujuan;
- menganggap `Tier class = Tier monster`;
- menganggap region akhir otomatis membutuhkan semua stat lebih tinggi;
- memakai multiplier tetap seperti “Elite ×2” atau “Boss ×10” tanpa kalibrasi;
- mempertahankan angka lama hanya demi kompatibilitas lore;
- menyembunyikan asumsi;
- mengubah ID database untuk keperluan balance tanpa audit referensi;
- menyebut stat seimbang hanya karena secara visual tampak rapi.

---

## 18. Format dokumentasi setiap stat block

Gunakan format minimum berikut:

```yaml
stat_status: BLOCKED | PROVISIONAL | CALIBRATED | VALIDATED
balance_version: "<versi/tanggal>"

subject:
  id: "<database id jika ada>"
  name: "<nama>"
  encounter_type: "<type>"
  combat_role: "<role>"
  progression_point: "<chapter/area/level range>"
  troop_context: "<komposisi>"

party_reference:
  size: null
  level_range: null
  equipment_tier: null
  profiles: [LOW, EXPECTED, HIGH]

targets:
  rounds: null
  pressure: "<deskripsi terukur>"
  intended_counterplay: []

stats:
  mhp: null
  mmp: null
  atk: null
  def: null
  mat: null
  mdf: null
  agi: null
  luk: null

dependencies:
  skill_formulas: []
  equipment_sources: []
  state_sources: []
  plugin_sources: []
  element_source: "06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md"

assumptions: []
calculation_summary: ""
simulation_result: ""
playtest_evidence: ""
unresolved: []
```

Semua angka harus dapat ditelusuri dari `dependencies`, `assumptions`, dan `calculation_summary`.

---

## 19. Laporan simulasi minimum

Sebelum status menjadi `CALIBRATED`, lampirkan tabel seperti berikut:

| Skenario | Party | Matchup | Hasil yang diukur | Target | Lulus? |
|---|---|---|---:|---:|---:|
| Sustain fisik | EXPECTED | 1x | ronde untuk menang | rentang desain | Ya/Tidak |
| Sustain magis | EXPECTED | 1x | ronde untuk menang | rentang desain | Ya/Tidak |
| Build rendah | LOW | 1x | ronde/risiko wipe | rentang desain | Ya/Tidak |
| Build optimal | HIGH | 1x | ronde untuk menang | batas bawah | Ya/Tidak |
| Kelemahan | EXPECTED | 2x | ronde untuk menang | target counterplay | Ya/Tidak |
| Resist | EXPECTED | 0.5x | ronde untuk menang | batas slog | Ya/Tidak |
| Burst musuh | EXPECTED | sesuai kit | damage per target/ronde | pressure target | Ya/Tidak |
| Worst case | LOW | crit + combo | survival/counterplay | aturan desain | Ya/Tidak |

Simulasi harus dapat diulang. Simpan input, seed bila relevan, versi database, dan script/perintah yang dipakai.

---

## 20. Kriteria kelulusan

Sebuah stat block hanya dapat menjadi `CALIBRATED` jika:

- semua sumber runtime yang relevan ditemukan;
- konteks party dan troop jelas;
- seluruh angka memiliki jejak perhitungan;
- target durasi dan pressure terpenuhi;
- elemen, critical, state, AoE, heal, dan action economy telah diuji;
- tidak ada one-shot atau soft-lock yang tidak disengaja;
- reward selaras dengan risiko dan waktu;
- hasil dapat direproduksi.

Status hanya dapat menjadi `VALIDATED` jika playtest nyata membuktikan encounter bekerja untuk profil pemain yang ditargetkan dan bukti playtest dicatat.

---

## 21. Kondisi repository Nusvanir saat pedoman dibuat

Temuan yang harus diperlakukan sebagai batasan, bukan diisi dengan asumsi:

1. `Mekanik_Class_Job.md` sudah menetapkan jalur dan Tier class, tetapi belum menyediakan growth curve parameter.
2. `Mekanik_Efektivitas_Elemen.md` sudah menetapkan multiplier matchup; aturan ini dapat digunakan setelah elemen target jelas.
3. Entri Alam Liar seperti Babi Hutan dan Beruang Madu Raksasa baru memiliki HP/MP, elemen, kelemahan, attack type, dan deskripsi singkat.
4. Entri boss seperti Argentfang memiliki HP/MP besar dan class, tetapi belum menunjukkan dasar perhitungan terhadap party, equipment, formula skill, phase, atau target durasi.
5. Database runtime RPG Maker MV dan spreadsheet sistem terbaru belum berada di repository lore yang diaudit.

Akibatnya:

> **Stat lama boleh dipakai sebagai hipotesis pembanding, tetapi tidak boleh dijadikan baseline final. Langkah pertama rework stat adalah memasukkan atau merujuk database game yang aktif, lalu membangun baseline party dan encounter.**

---

## 22. Instruksi singkat yang dapat ditempel ke prompt Codex

```text
Sebelum membuat atau mengubah stat apa pun, baca dan patuhi:
06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md

Stat lama adalah legacy candidate, bukan baseline final. Jangan memberikan angka
berdasarkan lore, Tier, region, role, atau encounter type saja. Temukan database
runtime, formula skill, equipment, states, plugin, baseline party, troop context,
dan target encounter. Gunakan status BLOCKED jika data wajib tidak tersedia;
gunakan PROVISIONAL hanya jika seluruh asumsi ditulis. Angka hanya boleh disebut
CALIBRATED setelah simulasi yang dapat diulang dan VALIDATED setelah playtest.
```

---

## 23. Keputusan yang masih perlu ditetapkan pemilik proyek

Pedoman ini sengaja tidak mengarang keputusan berikut:

- level cap dan kurva level;
- ukuran party utama;
- target ronde per encounter type;
- target damage/pressure per role;
- formula damage final;
- critical, hit/evasion, guard, dan action order final;
- equipment baseline per chapter;
- parameter cap;
- aturan multi-action dan boss scaling;
- target EXP/Saka per area atau per menit;
- definisi numerik threat rank.

Setelah keputusan tersebut tersedia, buat dokumen turunan `MONSTER_BALANCE_FRAMEWORK.md` berisi baseline numerik Nusvanir. Pedoman ini tetap menjadi aturan audit dan validasi di atas framework tersebut.
