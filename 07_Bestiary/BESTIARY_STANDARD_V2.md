# Bestiary Standard V2

## Status persetujuan menyeluruh — 2026-09-17

Seluruh 80 entri narasi Bestiary telah disetujui pemilik proyek. Persetujuan terakhir mencakup 28 entri pada Agnitra, Arkananta, Nusa Sayendra, Raksamala, dan Laut Rangkaruna. Penanda `PROPOSED_ADDITIONS` pada catatan penerapan di bawah menggambarkan tahap sebelum persetujuan dan dipertahankan sebagai riwayat pengerjaan.

Persetujuan narasi tidak menetapkan jawaban bagi konflik sumber yang masih terbuka dan tidak mengesahkan angka permainan. Data teknis tetap berada dalam JSON, sedangkan status kalibrasi dan balance tetap `BLOCKED`.

## Penerapan fauna Rangkaruna — 2026-09-17

Sepuluh fauna memakai pola **Deskripsi, Bentuk, Tingkah Laku, Habitat, Kisah**. Entri JSON lama tanpa identitas standar diberi `id`, `title`, dan metadata pemisahan lore/data; seluruh objek lama tetap tersimpan utuh dalam `legacy_values`. Kejadian Prologue diringkas tanpa mengubahnya menjadi durasi state, immunity, atau rumus serangan.

## Penerapan komandan Raksamala — 2026-09-17

Tujuh tokoh berakal memakai **Kepribadian dan Sikap** serta **Kedudukan dan Benteng**. Profil tokoh mengatur identitas, bentuk utama, dan relasi; dokumen Fortress of Sins mengatur wilayah serta godaan psikologis. Kontrak nyawa kepada Sangrahal dicatat tanpa menghapus perbedaan kepribadian setiap komandan.

Efek naratif seperti tidur abadi, Bloodlust, pencurian kemampuan, perisai ego, transformasi, dan kekebalan tidak otomatis menjadi state atau immunity game. Seluruh data teknis tetap JSON dan balance BLOCKED. Narasi membedakan benteng sebelum penyerangan Hector dari keadaan Raksamala yang kemudian runtuh.

## Penerapan Sentinel Nusa Sayendra — 2026-09-17

Empat tokoh Garuda menggunakan bagian **Kepribadian dan Sikap** serta **Kedudukan dan Kuil Penjagaan**. Profil karakter khusus menjadi sumber utama bila tersedia; entri Bestiary lama memasok kemampuan dan lokasi. Rincian baru yang tidak memiliki profil tokoh tetap ditandai usulan.

Kuil arah mata angin diperlakukan sebagai pos penjagaan yang terhubung dengan Puncak Emas Swargaloka. Deskripsi tidak mengubah klaim lore menjadi angka kecepatan, immunity, jarak serangan, atau aturan AI. Data game tetap di JSON dengan status kalibrasi BLOCKED.

## Penerapan kepala suku Arkananta — 2026-09-17

Tokoh berakal memakai **Kepribadian dan Sikap** serta **Kedudukan dan Wilayah** sebagai pengganti pola perilaku/habitat fauna. JSON menyimpan ras, sumber profil karakter, status narasi, snapshot runtime, dan blokir kalibrasi. Profil tokoh menjadi sumber utama identitas; entri Bestiary lama tetap arsip data game.

Grok–Troliogoro, Krom–Butoraksa, dan Larasati–Rakshorien adalah pemetaan canon existing. Rincian visual tambahan dan tiga vignette baru berstatus usulan. Lokasi yang belum memiliki dokumen sendiri diselaraskan sebagai bagian dari kompleks pemukiman, bukan permukiman baru.

## Penguatan material nest Agnitra ? 2026-09-17

Atas arahan pemilik, setiap naga kini mewakili satu nest/material: Blackhorn?Adamantine (zirah dan peredaman sihir, barat), Orichalor?Orichalcum (konduktivitas sihir, selatan kawah), Argentfang?Silver (dingin dan pemurnian, utara), Mithralis?Mithril (ringan dan kuat, timur). Bentuk, kepribadian, ujian, lokasi, serta kisah diselaraskan. Argentfang menjadi penjaga pemurnian, bukan pembunuh yang menguji dengan kematian.

Pemetaan ini menggantikan kehati-hatian afiliasi pada catatan sebelumnya. JSON `lore_identity` menyimpan identitas terkini; field legacy dan snapshot runtime tetap utuh untuk jejak historis. Lokasi Orichalor berpindah dari puncak timur ke Orichalcum selatan; Argentfang dari gua tanpa koordinat ke Silver utara; Mithralis bersarang di Mithril timur dengan jelajah kawah. Tidak ada perubahan stat, drop, recipe, atau runtime. Rincian narasi tetap PROPOSED_ADDITIONS sampai disetujui.

## Batch narasi Agnitra ? 2026-09-17

Empat pasangan Blackhorn, Orichalor, Argentfang, dan Mithralis memakai Deskripsi, Bentuk, Kepribadian dan Sikap, Lokasi Nest, serta Kisah. Narasi baru berstatus PROPOSED_ADDITIONS. Lokasi legacy dipertahankan; klan dan jabatan pemimpin tidak disimpulkan dari warna, nama, atau kemampuan. Kisah baru menampilkan naga berakal sesuai Nagarasven, bukan menetapkan mereka Feral.

Blackhorn tetap di lereng bawah Mahasvara, Orichalor di puncak timur, Argentfang di Gua Gelap Agnitra yang belum dipetakan, dan Mithralis di langit kawah. Mikrohabitat istirahat merupakan usulan. Sarang regional dipakai sebagai konteks, bukan pemetaan otomatis: Orichalcum berada di selatan, Mithril di timur, Silver di utara, Adamantine di dasar lereng barat.

Angka, ID, kelas, dan field legacy dipertahankan. VERIFIED Blackhorn/Orichalor diganti BLOCKED; perbedaan elemen Blackhorn dan label serangan Orichalor terhadap runtime dicatat tanpa rekonsiliasi sepihak. Snapshot runtime hanya observasi. Tidak ada perubahan runtime, item, skill, spawn, atau batch sebelumnya. Arsip: `_audit/pre_agnitra_narrative.json` dan `_audit/pre_agnitra_hashes.json`; hasil: `_audit/agnitra_verification.json`. Pemeriksaan: `python tools/verify_agnitra_lore.py`, audit inventaris, verifier workspace, dan `git diff --check`. Tidak dilakukan simulasi balance atau playtest.

## Persetujuan seluruh narasi Thalantira ? 2026-09-17

Pemilik menegaskan persetujuan seluruh usulan 18 entri Thalantira. Narasi, rincian visual/perilaku, habitat tambahan, dan kisah kini APPROVED. Penanda usulan dihapus; sumber dipertahankan. Bukti persetujuan dan hash Markdown tersimpan di `_audit/thalantira_lore_approval.json`. Pernyataan usulan atau status Thalantira belum berubah pada catatan terdahulu merupakan riwayat sebelum konfirmasi ini. Pertanyaan canon yang belum dijawab tetap terbuka; angka, runtime, serta status balance BLOCKED tidak berubah.

## Persetujuan penjaga Avalerion ? 2026-09-17

Pemilik menyetujui seluruh usulan empat penjaga Avalerion, termasuk kepribadian dan sikap, lokasi benteng, serta kisah. Penanda usulan dihapus dari narasi; sumber dipertahankan. JSON berstatus APPROVED dengan bukti dan hash Markdown di `_audit/avalerion_lore_approval.json`. Race tetap Asevari sesuai permintaan. Konflik kelas Vayu, identitas komandan, dan pemetaan arah yang belum dijawab tetap terbuka; balance tetap BLOCKED dan runtime tidak berubah. Pernyataan usulan Avalerion di bagian terdahulu merupakan riwayat sebelum persetujuan. Status Thalantira tidak berubah.

## Penerapan penjaga Avalerion — 2026-09-17

Empat entri kategori 04 memakai Deskripsi, Bentuk, Kepribadian dan Sikap, Lokasi Benteng, dan Kisah. Untuk penjaga berakal, Lokasi Benteng menjelaskan wilayah tugas dan pos, sedangkan Kepribadian dan Sikap menjelaskan watak, cara berkomunikasi, hubungan dengan orang lain, serta sikap saat tertekan. JSON mempertahankan format legacy dengan metadata presentation/lore_review/runtime_observation/balance_review. Tambahan lore berstatus PROPOSED_ADDITIONS; angka tidak dikalibrasi ulang dan balance BLOCKED.

Pos bernama merupakan usulan penempatan berdasarkan kecocokan peran. Arah mata angin lama belum otomatis identik dengan lokasi pos regional. Nama ksatria tidak menetapkan komandan, jabatan baru, atau kelas yang bertentangan dengan arsip. Seluruh kisah batch ini merupakan vignette baru, bukan penambahan kejadian pada Prologue.

## Penerapan Thalantira — 2026-09-17

Seluruh 18 pasangan `03_Thalantira` mengikuti format lima bagian narasi: Deskripsi, Bentuk, Tingkah Laku, Habitat, dan Kisah. JSON memakai tambahan root `presentation`, `lore_review`, `runtime_observation`, dan `balance_review` seperti batch Jenggala. ID, angka, serta field lama dipertahankan selain label status kalibrasi/sumber. Deskripsi JSON lama adalah arsip; Markdown menjadi sumber narasi terkini. Data game hanya berada di JSON.

Tambahan Thalantira berstatus `PROPOSED_ADDITIONS`, dengan approval null. Persetujuan Wildlife dan Jenggala tetap berlaku untuk batch masing-masing. Kisah Treant, Golem, Hydra, Behemoth, serta Void Wyrm merangkum kejadian Prologue; kisah lain dan rincian visual/ekologis baru diberi penanda usulan serta tautan sumber.

Perilaku penjaga membedakan pertemuan awal, pengaruh kristal/Uru saat pengungkapan, dan penampilan sadar berikutnya. Kuil Api pada masa Hector tidak disamakan dengan Kuil Udara. Nama Void/Phantom, ketahanan naratif, dan pembekuan tidak menjadi dasar otomatis untuk elemen, ras, immunity, atau state game baru. Seluruh balance tetap `BLOCKED`; snapshot runtime hanya observasi.

> **Persetujuan Jenggala 2026-09-17:** seluruh narasi batch 15 Jenggala telah disetujui. `presentation.narrative_status` kini APPROVED dan `presentation.approval` memuat keputusan pemilik. Pernyataan PROPOSED_ADDITIONS pada dokumentasi batch sebelumnya adalah riwayat. Persetujuan lore tidak mengubah kalibrasi game.

## Penerapan Jenggala — batch narasi 2026-09-17

Kelima belas pasangan Jenggala mengikuti pemisahan Markdown lore / JSON game. Untuk mempertahankan format JSON lama secara sederhana, batch ini menambahkan `presentation`, `lore_review`, `runtime_observation`, dan `balance_review` pada root JSON, tanpa mewajibkan migrasi penuh ke objek `v2` Wildlife. Key lama dan angka tetap arsip; narasi terkini ada di Markdown. `presentation.narrative_status` adalah PROPOSED_ADDITIONS dan approval null, terpisah dari BLOCKED pada balance. Persetujuan Wildlife sebelumnya tidak diasumsikan mencakup tambahan baru Jenggala.

`lore_review` menyimpan sumber, lokasi arsip dan keputusan yang belum selesai. `runtime_observation` menyimpan enemy, skill dan item existing sebagai observasi saja. Tidak ada stat atau resep baru dihitung. Pemeriksaan khusus: `python tools/verify_jenggala_lore.py`; sinkronisasi tidak menulis data teknis kembali ke Markdown.

> **Persetujuan 2026-09-17:** seluruh pengembangan narasi pada 15 entri Alam Liar sudah disetujui pemilik. Markdown merupakan lore terkini; metadata persetujuan tersimpan di `v2.presentation.lore_approval`. Ketentuan penandaan usulan di bawah berlaku untuk tambahan baru yang belum disetujui, bukan untuk narasi batch ini. Persetujuan lore tidak mengubah status kalibrasi game.

## Gaya narasi — pengayaan 2026-09-17

Markdown memakai lima bagian: **Deskripsi**, **Bentuk**, **Tingkah Laku**, **Habitat**, dan **Kisah**. Deskripsi bergaya ensiklopedia fauna/Pokédex: ringkas, khas, dan menjelaskan cara mengenali makhluk. Bentuk menggambarkan siluet, tubuh, permukaan, warna, dan bagian khas secara konkret. Tingkah Laku menggantikan Ciri-ciri, membedakan sikap normal, berburu, menghindar, melindungi anak, dan respons terhadap ancaman.

Habitat harus membedakan lokasi existing dari rekomendasi yang diturunkan dari geografi regional. Kisah merupakan vignette baru yang menempatkan fauna dalam kehidupan Nusvanir, bukan catatan peristiwa canon yang sudah disetujui. Rincian visual/perilaku tambahan dan penempatan baru diberi satu catatan usulan beserta tautan sumber pada akhir entri. Pengayaan cerita tidak mengubah database game atau menetapkan kemampuan magis baru secara tersirat.

## Format sederhana — keputusan pemilik, 2026-09-17

Aturan ini menggantikan aturan mirror Markdown/JSON pada revisi sebelumnya.

- **Markdown:** sumber narasi yang diedit langsung oleh penulis. Berisi deskripsi, bentuk, ciri-ciri, habitat, dan lore sesuai informasi yang tersedia. Bagian yang belum memiliki isi boleh dihilangkan; jangan mengarang ciri atau asal-usul untuk melengkapinya.
- **JSON:** sumber data game, meliputi identity/ID, klasifikasi, stat, elemen, skill, AI, spawn, drop, progression, status balance, sumber runtime, dan arsip. Tidak perlu menyalin seluruh JSON ke Markdown.
- `v2.presentation` mencatat path pasangan dan kebijakan tersebut. Teks worldbuilding lama di JSON adalah konteks historis; Markdown menjadi sumber narasi terkini.
- Validasi pasangan memeriksa identitas, path sumber, dan pemisahan konten; tidak lagi mengharuskan isi kedua file identik. `--render-wildlife` melewati entri `lore_only` agar narasi tidak tertimpa data game.

Sudah diterapkan pada 15 entri Alam Liar. Isi Markdown sebelumnya diarsipkan dalam `_audit/pre_lore_split_markdown.json`; nilai game tidak diubah. Format ini menjadi acuan untuk batch kategori berikutnya.

## Revisi implementasi 2.1 — 2026-09-17

Bagian ini berlaku di atas draft skema awal di bawah. Runtime lokal **sudah tersedia**. Empat status balance yang sah hanya BLOCKED, PROVISIONAL, CALIBRATED, VALIDATED; `legacy_candidate` adalah label arsip, `OBSERVED_ONLY` adalah status bukti, keduanya bukan status balance.

Konvensi migrasi aman: sumber structured V2 adalah key `v2` dalam pasangan JSON. `tools/bestiary_audit.py:render` menghasilkan salinan lengkap di bagian Markdown bertanda `BESTIARY V2 START/END`. Narasi dan metadata lama dipertahankan sebagai arsip dengan pemberitahuan; tidak boleh dipakai mengalahkan record V2. Jangan menjalankan skrip massal lama. Perubahan berikutnya dilakukan pada JSON V2 dahulu lalu render ulang hanya bagian bertanda, tidak seluruh prose. ID existing dan canonical_slug tetap stem existing, bukan ID enemy MV; pemetaan runtime eksplisit ada di `runtime_observation.enemy.id`.

| Kelompok V2 | Field wajib / makna |
|---|---|
| identity | id, name, alternative_names, canonical_slug, species, creature_family, origin, faction, region, biome, sub_area |
| classification | creature_type, basis, encounter_type, encounter_type_basis, threat_rank, spawn_rarity, sentience_level, civilization_status |
| gameplay | progression_point, recommended_level, combat_role, design_status, attack_type, primary_element, secondary_element, element_basis, ai_archetype, intended_counterplay, troop_context, balance_status |
| balance | stat_status, balance_version, stats(mhp/mmp/atk/def/mat/mdf/agi/luk), source_dependencies, source_sha256, party_reference(LOW/EXPECTED/HIGH), target_encounter_duration, target_pressure, assumptions, calculation_summary, simulation_result, playtest_evidence, unresolved_blockers |
| combat | basic_attack_skill_id, active_skill_ids, passive, special_mechanic, ai_conditions, action_priority, target_selection, resource_use, enrage_behavior, elemental_affinity, status_resistances, state_registry, pending_effect_skill_ids |
| spawn | region, biome, sub_area, source_habitat, time, weather, spawn_weight, pack_size, aggression, encounter_conditions, diet, predators, prey, migration_or_territory, status |
| rewards | status, exp, saka, common_drop, uncommon_drop, rare_drop, unique_drop, quest_drop, drops(database/id/name/rarity/runtime_denominator/description/source_note/uses/canon_review), drop_slot_note, economy_risk |
| worldbuilding | description, lore, origin, ecology, behavior, diet, predators, prey, relationship_with_civilization, cultural_significance, economic_value, known_uses, historical_notes, quest_relevance, story_relevance, proposal, proposal_status, source, regional_sources |
| runtime_observation | status OBSERVED_ONLY, source, enemy (entire unmodified database object), skills (entire referenced objects), meaning |
| legacy | source snapshot, values, status legacy_candidate, prior_stat_status, compatibility |

Tidak ada field kebutuhan yang sengaja dibuang: summary direpresentasikan description, origin_story oleh worldbuilding.origin, predator_prey dipecah, crafting/forge/alchemy/summoning use melalui drop.uses. Null berarti belum diketahui/ditetapkan, daftar kosong berarti belum tercatat, **bukan** bukti tidak ada. Proposal non-numerik tidak memakai status balance PROVISIONAL. Usulan bioma/role/counterplay tidak otomatis menjadi canon. Threat rank dan spawn rarity null sampai kamus disetujui; jangan mengambil item rarity atau guild rank sebagai penggantinya. Noncombat boleh memiliki encounter_type/role null.

### Elemen dan state dalam engine lokal

| Istilah lore | System element ID / nama |
|---|---|
| Netral (non-atribut) | 1 / Neutral; primary_element null |
| Api | 2 / Fire |
| Air (air cair) | 3 / Water |
| Tanah | 4 / Earth |
| Udara | 5 / Air; alias notetag Wind |
| Listrik | 6 / Electric; alias notetag Lightning |
| Es | 7 / Ice |
| Besi | 8 / Steel |
| Suara | 9 / Sound |
| Cahaya | 10 / Holy; alias notetag Light |
| Kegelapan | 11 / Dark |

Terjemahan **Air** wajib memperhatikan konteks bahasa. Void/All bukan ID elemen baru. Trait MV code 11 menyimpan element rate, code 13 state rate, code 14 immunity; simpan dataId/value asli sebagai observasi, jangan mengekspor modifier ke parameter mentah. Source runtime attack trait code 31 bukan otomatis seluruh affinity atau semua skill. Skill damage.elementId dan plugin dual-element harus dibaca sendiri. State harus memakai ID/name dari States.json; tidak menyimpulkan effect dari nama skill. Status/rarity dropout diturunkan dari sumber, bukan urutan slot drop MV.

Boss kelak menambahkan `boss_design` dengan identity/story/progression/party, phases, thresholds, adds, arena, break/stagger, enrage, telegraph/counterplay, affinities/states, reward links, per-phase evidence dan full-encounter evidence. Semua ambang numerik null sebelum gerbang balance lolos; null bukan mekanik yang sudah diimplementasikan.

Validasi: parse JSON, ID unik dan stabil, referensi lokal, snapshot runtime, state/skill/drop IDs, serta kesamaan seluruh objek V2 Markdown/JSON. Agregat/wiki belum diregenerasi karena generator belum diketahui. Full canon parity arsip lama masih mempunyai konflik yang dicatat di audit.

## Draft skema awal (lihat pemetaan revisi 2.1 di atas)

## Tujuan

Dokumen ini menetapkan skema kanonik yang dapat dipakai oleh penulis lore dan implementer game untuk memastikan entri bestiary Nusvanir tetap konsisten secara canon, ekologi, dan gameplay.

Pada saat ini, repository belum memiliki database runtime RPG Maker MV aktif. Karena itu, semua bidang numerik harus tetap `null`, `TBD`, atau dibatasi pada nilai warisan yang jelas diberi status `LEGACY_CANDIDATE`. Tidak boleh ada angka final yang dibuat berdasarkan intuisi atau label seperti “boss” / “Thalantira” / “Tier 5”.

## 1. Skema standard

```yaml
id: "string"
name: "string"
alternative_name: "string | null"
canonical_slug: "string"
species: "string | null"
creature_family: "string | null"
origin: "string | null"
faction: "string | null"
region: "string | null"
biome: "string | null"
sub_area: "string | null"

creature_type: "Wildlife | Magical Beast | Spirit | Elemental | Jenggala | Drahkthar | Undead | Construct | Humanoid | Dragon | Divine Beast | Voidborn | Aberration | null"
encounter_type: "Normal | Elite | Rare | Mini Boss | Boss | Commander | World Boss | Story Boss | null"
threat_rank: "Low | Medium | High | Extreme | null"
rarity: "Common | Uncommon | Rare | Epic | Legendary | Mythic | null"
sentience_level: "Non-Sentient | Semi-Sentient | Sentient | Divine | null"
civilization_status: "Wild | Domesticated | Tribal | Civilized | Ruinbound | null"

recommended_level: "string | int | null"
combat_role: "Bruiser | Tank | Assassin | Skirmisher | Mage | Support | Controller | Summoner | Sniper | Swarm | null"
attack_type: "Melee | Ranged | Hybrid | null"
primary_element: "Api | Air | Tanah | Udara | Listrik | Es | Besi | Suara | Cahaya | Kegelapan | null"
secondary_element: "string | null"
ai_archetype: "string | null"
intended_counterplay: "string | null"
troop_context: "string | null"
balance_status: "BLOCKED | PROVISIONAL | CALIBRATED | VALIDATED"

mhp: null
mmp: null
atk: null
def: null
mat: null
mdf: null
agi: null
luk: null

stat_status: "BLOCKED | PROVISIONAL | CALIBRATED | VALIDATED"
balance_version: "string | null"
source_dependencies: []
party_reference: "string | null"
target_encounter_duration: "string | null"
assumptions: []
calculation_summary: "string | null"
simulation_result: "string | null"
playtest_evidence: "string | null"
unresolved_blockers: []

elemental_affinity: []
status_resistances: []
skills: []
passive: "string | null"
special_mechanic: "string | null"
ai_conditions: []
action_priority: "string | null"
target_selection: "string | null"
resource_use: "string | null"
enrage_behavior: "string | null"

region: "string | null"
biome: "string | null"
sub_area: "string | null"
time_of_day: "string | null"
weather: "string | null"
spawn_weight: "string | null"
pack_size: "string | null"
aggression: "string | null"
encounter_conditions: "string | null"
predator_prey: "string | null"
diet: "string | null"
migration_or_territory: "string | null"

exp: null
saka: null
common_drop: "string | null"
uncommon_drop: "string | null"
rare_drop: "string | null"
unique_drop: "string | null"
quest_drop: "string | null"
crafting_use: "string | null"

summary: "string"
lore: "string"
origin_story: "string | null"
ecology: "string | null"
behavior: "string | null"
relationship_with_civilization: "string | null"
known_uses: "string | null"
historical_notes: "string | null"
quest_relevance: "string | null"
story_relevance: "string | null"
```

## 2. Sumber elemen yang sah

Struktur elemen yang valid dan sah untuk dipakai saat ini mengikuti `06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md`:

- Api / Pyro
- Air / Hydro
- Tanah / Geo
- Udara / Aero
- Listrik / Electro
- Es / Cryo
- Besi / Ferro
- Suara / Sonic
- Cahaya / Holy
- Kegelapan / Dark

Catatan penting:

- Belum ada otoritas yang menetapkan `Void` sebagai elemen resmi sekunder.
- `Void` dapat muncul sebagai entitas, fenomena, atau ancaman kosmik, tetapi bukan elemen standar yang dipakai oleh tabel efektifitas 10-elemen.
- `Netral` tetap dipakai untuk makhluk yang tidak menonjolkan elemen tertentu, tetapi harus dipahami sebagai label non-atribut bukan multiplier otomatis.

## 3. Aturan validasi

- Jika jumlah data yang dibutuhkan tidak tersedia, semua bidang numerik harus diisi dengan `null` atau `TBD` dan diberi status `BLOCKED`.
- Angka legacy dapat dipertahankan untuk traceability, tetapi harus diberi label `LEGACY_CANDIDATE` dan tidak boleh dipakai sebagai angka final.
- Skema ini dibuat untuk mendukung penulisan lore dan game implementation, bukan untuk menebak balance.

## 4. Standar minimal untuk entri wildlife

Untuk fauna liar, entri minimal yang diperbolehkan:

- ID dan nama
- kategori/region/biome
- tipe makhluk
- perilaku makan dan habitat
- relasi dengan manusia dan peradaban setempat
- status balance dan data statistik yang jelas
- item drop yang sudah ada, jika diketahui

Semua nilai numerik yang belum dibuktikan harus tetap berstatus `BLOCKED`.
