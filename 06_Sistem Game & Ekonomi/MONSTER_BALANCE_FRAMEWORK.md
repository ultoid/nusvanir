# Monster Balance Framework Nusvanir

## Pembaruan bukti 2026-09-17 — BLOCKED

**Runtime sudah ditemukan** di `10_Game Project/Tales of The Dark Time`. Bagian awal ini menggantikan alasan historis di bawah yang menyebut seluruh database hilang. Framework belum mempunyai baseline angka yang disetujui; tidak ada perubahan angka runtime.

| Input | Bukti tersedia | Yang masih harus ditentukan/diuji |
|---|---|---|
| Party | System.partyMembers 1/2/3; NUSV_PartySystem maksimum battle 4 | Roster per encounter, anggota cadangan dan summon legal |
| Level | Actors: Cassian/Hector/Jane mulai/maks 50; Rama mulai 30/maks 99; actor test berbeda | Level cap desain, chapter/area bands; jangan jadikan actor test baseline |
| Curves | Classes.json params, traits, EXP curve, learnings | Profil LOW/EXPECTED/HIGH per progression dan job yang legal |
| Equipment | Weapons/Armors params/traits/notetags | Availability, upgrade/socket/consumable budget per chapter |
| Formula | Skills.json; rpg_objects.js; damage/critical/parameter plugins | Pending skill effects dan semua modifier dalam urutan load aktual |
| Element/state | System/States/traits; YEP_ElementCore/BuffsStatesCore | Selisih 1.5/0.75 runtime vs chart lore, dual-element dan state interactions |
| Resource | MP/TP costs pada skills; traits regeneration | Rotasi sustain, item use, regen/plugin costs aktual |
| Turn/action | BattleEngine default dtb; CTB plugin juga enabled; AI Core enabled | Battle system yang dipilih event/save, multi-action, target selection dan AI notetag |
| Troop | Troops.json berisi empat troop, tiga nama tertinggal | Komposisi, map encounter access, adds/hazards dan target duration/pressure |
| Economy | EXP/gold/drop slots dan harga item tersedia | Satuan Saka/gold, target EXP/Saka per area/waktu, biaya recovery dan respawn |
| Validation | Belum ada bukti terhubung ke batch | Reproducible simulator dan playtest per encounter |

### Workbook yang siap diisi

Untuk setiap `encounter_id`, catat hash semua database, core JS, plugin enabled/config dan urutannya; progression, roster, gear, upgrade, socket, consumables, troop, battle mode. Tiga record profile LOW/EXPECTED/HIGH berisi stat tiap anggota, traits, legal actions, resource ledger dan target selection. Semua field belum terpilih tetap null. V2 Wildlife sudah menyediakan dependensi, hash sumber utama, dan nilai kalibrasi null. Hash semua data tersimpan di inventory; sebelum simulasi perlu menambahkan hash kode seluruh plugin.

Lembar `actions`: skill ID, formula persis, scope, hit type, repeats, MP/TP, element ID, effects, speed, critical, variance dan plugin modifiers. Lembar `rounds`: aksi aktual tiap unit, HP/MP/TP sebelum/sesudah, damage/heal/shield/regen, control kehilangan giliran, adds dan phase. Lembar `results`: victory/wipe/soft-lock, durasi, damage pressure per anggota, recovery cost, EXP/Saka dan nilai drop per waktu. Lembar `evidence`: seed, perintah simulator, input hash, hasil dan tautan playtest.

Gunakan pipeline runtime makeDamageValue beserta override plugin, bukan evaluasi formula polos. Secara konseptual effective HP mencakup HP + heal + shield + damage prevented; target effective HP = sustain net damage party × target rounds, lalu selesaikan defense/HP bersama. Resource budget berasal dari rotasi dan regen. Threat control dinilai dari aksi yang hilang; action economy menggabungkan summon, counter, multi-action, bukan AGI saja. Reward efficiency mencakup akses/respawn, recovery dan sale/crafting value, bukan persentase HP.

Matriks wajib sebelum CALIBRATED: sustain fisik/magis, LOW/EXPECTED/HIGH, matchup legal 0.5/1/2 jika ada, actual runtime rates, critical burst terburuk, full troop, AoE, heal, control, flee, phase/adds/regen/invulnerability. Catat expected versus measured dan pass/fail terhadap **target pemilik**, bukan target buatan simulator. Tidak ada simulator balance yang dijalankan pada batch ini; pemeriksaan snapshot/parity bukan simulasi.

Pertanyaan keputusan: encounter mana yang menjadi baseline pertama, roster dan gear apa yang legal, target durasi/pressure/recovery berapa, jadwal progression dan reward apa, chart atau runtime mana yang akan disejajarkan? Setelah jawabannya tersedia, implementasikan efek tertunda dan uji build sebelum menghitung kandidat. Runtime local adalah sumber perilaku; Pedoman tetap gerbang legitimasi angka.

## Arsip framework awal (pernyataan database hilang sudah kedaluwarsa)

## Status

Dokumen ini dibuat sebagai kerangka kerja yang sah menurut `Pedoman_Pemberian_Stat.md` dan statusnya saat ini adalah `BLOCKED`.

Alasan utama:

- Tidak ada database runtime RPG Maker MV aktif di workspace.
- Tidak ada `data/System.json`, `data/Enemies.json`, `data/Classes.json`, `data/Skills.json`, `data/Weapons.json`, `data/Armors.json`, `data/States.json`.
- Tidak ada baseline party progression, equipment, skill formula, atau hasil playtest yang dapat dijadikan sumber angka final.

## 1. Checklist input yang dibutuhkan

### Progression

- [ ] chapter/area level range
- [ ] level cap
- [ ] party size
- [ ] class distribution
- [ ] equipment available per level tier
- [ ] consumables and buffs

### Combat formulas

- [ ] skill damage and healing formulas
- [ ] hit / crit / evasion / guard data
- [ ] element matchup rates
- [ ] state resistances and stacks
- [ ] action order and multi-action behavior
- [ ] MP/TP costs and regeneration

### Encounter design

- [ ] target round duration
- [ ] enemy troop composition
- [ ] AI archetype
- [ ] trigger conditions for phase changes
- [ ] enrage or desperation behavior
- [ ] boss mechanics and hazard logic

### Economy

- [ ] EXP and Saka economy targets
- [ ] drop rarity rules
- [ ] crafting and upgrade chain
- [ ] market value by region

## 2. Format kerja yang disarankan

```yaml
stat_status: BLOCKED
balance_version: "TBD"
source_dependencies: []
party_reference: "TBD"
target_encounter_duration: "TBD"
assumptions: []
calculation_summary: "TBD"
simulation_result: "TBD"
playtest_evidence: "TBD"
unresolved_blockers: []
```

## 3. Struktur profil party

Untuk setiap progression point, di masa depan harus dibuat minimum 3 profil:

- `LOW`
- `EXPECTED`
- `HIGH`

Setiap profil harus mencatat:

- MHP, MMP
- ATK, DEF, MAT, MDF, AGI, LUK
- hit, crit, evasion, guard, PDR, MDR
- basic damage, skill damage, healing, shielding
- sustain per round
- burst per round
- party action economy

## 4. Poin yang harus diisi ketika data tersedia

- expected physical damage
- expected magical damage
- sustainable round pressure
- burst damage ceiling
- effective HP
- action economy per target
- element matchup outcome
- status effectiveness
- target duration for encounter
- reward efficiency

## 5. Pembatasan yang tidak boleh dilanggar

- Tidak boleh memakai shortcut seperti `Elite = Normal x2`.
- Tidak boleh memakai `Boss = Normal x10`.
- Tidak boleh mengambil `tier` atau `ukuran tubuh` sebagai pengganti matematika.
- Tidak boleh menambah `Void` menjadi elemen padahal repo belum menetapkannya sebagai elemen standar.
- Tidak boleh menilai `VALIDATED` tanpa playtest.

## 6. Legacy appendix

Angka lama seperti `HP 150` untuk `Babi Hutan`, `HP 850` untuk `Beruang Madu Raksasa`, atau angka besar pada boss Thalantira hanya boleh dipertahankan sebagai `LEGACY_CANDIDATE` untuk audit traceability. Tidak ada angka tersebut yang boleh diterima sebagai baseline final sebelum data progression diaktifkan.

## 7. Rekomendasi berikutnya

Langkah berikutnya yang paling aman adalah:

1. menyiapkan baseline game runtime dari project yang aktif;
2. memasukkan class curves dan equipment progression;
3. menetapkan party reference berdasarkan chapter dan area;
4. menghitung per-encounter duration target;
5. mengisi framework hanya setelah seluruh input terdokumentasi.

Sampai saat itu, seluruh numerik pada Bestiary harus tetap dibatasi pada `BLOCKED` atau `LEGACY_CANDIDATE`.
