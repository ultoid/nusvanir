---
title: Kamus_State_&_Status_Efek
tags:
  - Sistem_Game_Ekonomi
  - Combat_Engine
  - States_Database
  - Status_Effects
  - Turn_Based_RPG
---

# 📜 Kamus Status Efek & State Tempur Nusvanir (ID 201 – 477)

Dokumen ini adalah **kodifikasi resmi seluruh State, Status Efek, Buff, Debuff, Crowd Control (CC), dan Pasif** dalam game RPG *Turn-Based* Nusvanir.
Seluruh entri dikonfigurasi secara presisi sesuai dengan parameter engine pada spreadsheet **`MV STATES`** dan terintegrasi dengan plugin **`YEP_BuffsStatesCore`** serta **`YEP_AutoPassiveStates`**.

---

## 🧭 1. Arsitektur & Aturan Sistem State Nusvanir

### A. Pembagian 3 Kategori Besar State
1. **Status Effect & Canonical States (ID 201 – 226):** Status penyakit umum, DoT (*Damage over Time*), Hard CC, debuff kerentanan, dan penanda afinitas yang dapat diterapkan oleh berbagai mantra, item, maupun serangan monster.
2. **Skill Effect States (ID 301 – 477):** Efek temporer unik yang dipicu oleh skill spesifik kelas (*War Cry, Solid Stance, Iron Fortress, Barrier, Transformation*).
3. **Passive States (Auto-Passive System):** Keahlian pasif permanen berdasarkan Ras, Class Mastery, atau Peralatan yang aktif otomatis tanpa hitungan durasi turn.

### B. Parameter Mekanik Kunci
* **Priority (Prioritas Tampilan 50–95):** Menentukan urutan ikon yang ditampilkan di atas kepala unit. State dengan nilai prioritas tertinggi (misal: Petrify 95, Stun 90) akan menimpa tampilan status berprioritas rendah (Slow 50).
* **Restriction (Pembatasan Gerak):**
  * `None`: Unit bebas bertindak normal.
  * `Cannot Move`: Unit kehilangan giliran total (Stun, Freeze, Paralyze, Petrify).
  * `Attack Anyone`: Unit kalap dan menyerang target acak tanpa membedakan kawan atau lawan (Confusion).
* **Auto-Removal Timing:** Pengurangan durasi terjadi pada fase **Turn End** giliran unit.
* **Remove by Damage:** Beberapa state mental (seperti *Sleep* atau *Confusion*) memiliki peluang terlepas seketika apabila target menerima kerusakan fisik.
* **Boss Rule & Immunity:** Musuh berpangkat Boss memiliki imunitas bawaan (*State Rate = 0%*) terhadap *Instant Death* dan pengurangan durasi maksimal 1 turn untuk Hard CC.

---

## ☣️ 2. Status Efek Kanonikal (Canonical States: ID 201 – 226)

| ID | Nama State | Kategori | Prioritas | Pembatasan (Restriction) | Durasi (Turn) | Lepas Saat Dipukul | Pengaruh & Traits Mekanis |
|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **201** | **Burn** | `Status Effect` | `60` | `None` | `3 T` | `No` | HP Regen -2% Max HP/turn |
| **202** | **Severe Burn** | `Status Effect` | `70` | `None` | `2 T` | `No` | HP Regen -4% Max HP/turn; Healing Received -20% |
| **203** | **Poison** | `Status Effect` | `60` | `None` | `3 T` | `No` | HP Regen -4% Max HP/turn |
| **204** | **Bleed** | `Status Effect` | `60` | `None` | `3 T` | `No` | HP Regen -3% Max HP/turn |
| **205** | **Chill** | `Status Effect` | `55` | `None` | `2 T` | `No` | AGI ×85%; EVA ×90% |
| **206** | **Freeze** | `Hard CC` | `80` | `Cannot Move` | `1 T` | `Yes` | Cannot act; remove by damage 50% |
| **207** | **Paralyze** | `Hard CC` | `80` | `Cannot Move` | `1 T` | `No` | Cannot act |
| **208** | **Stun** | `Hard CC` | `90` | `Cannot Move` | `1 T` | `No` | Cannot act |
| **209** | **Root** | `Status Effect` | `55` | `None` | `2 T` | `No` | AGI ×70%; EVA ×85% |
| **210** | **Slow** | `Status Effect` | `50` | `None` | `3 T` | `No` | AGI ×75% |
| **211** | **Fear** | `Status Effect` | `60` | `None` | `2 T` | `No` | ATK ×85%; MAT ×85%; HIT ×90% |
| **212** | **Blind** | `Status Effect` | `60` | `None` | `2 T` | `No` | HIT ×50% |
| **213** | **Silence** | `Status Effect` | `70` | `None` | `2 T` | `No` | Seal Skill Types: Black Magic, White Magic, Dark Magic |
| **214** | **Confusion** | `Hard CC` | `75` | `Attack Anyone` | `2 T` | `Yes` | Restriction: Attack Anyone |
| **215** | **Vulnerable 30%** | `Status Effect` | `70` | `None` | `2 T` | `No` | Physical Damage Rate 130%; Magical Damage Rate 130% |
| **216** | **Vulnerable 60%** | `Status Effect` | `80` | `None` | `1 T` | `No` | Physical Damage Rate 160%; Magical Damage Rate 160% |
| **217** | **Vulnerable 100%** | `Status Effect` | `90` | `None` | `2 T` | `No` | Physical Damage Rate 200%; Magical Damage Rate 200% |
| **218** | **Soaked** | `Status Effect` | `55` | `None` | `3 T` | `No` | Fire Element Rate 80%; Lightning Element Rate 125% |
| **219** | **Shock** | `Status Effect` | `60` | `None` | `2 T` | `No` | AGI ×90%; Lightning Element Rate 120% |
| **220** | **Petrify** | `Hard CC` | `95` | `Cannot Move` | `1 T` | `No` | Cannot act; DEF ×130%; MDF ×130% |
| **221** | **Float** | `Tag / Status` | `50` | `None` | `3 T` | `No` | Tag state; optional EVA +5% |
| **222** | **Marked** | `Tag / Status` | `50` | `None` | `3 T` | `No` | Tag state only |
| **223** | **Shadow Mark** | `Stacking Tag` | `60` | `None` | `3 T` | `No` | Stacking tag, max 3 |
| **224** | **Taunt** | `Targeting` | `70` | `None` | `2 T` | `No` | Forced/weighted targeting toward caster |
| **225** | **Curse** | `Status Effect` | `55` | `None` | `3 T` | `No` | ATK ×90%; MAT ×90% |
| **226** | **Polarized** | `Tag / Status` | `50` | `None` | `3 T` | `No` | Tag state only |

### Rincian Mendalam 26 Status Efek Kanonikal

#### 🔹 [201] Burn
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** HP Regen -2% Max HP/turn
- **Aturan Boss:** ⚠️ **Bosses use normal state-rate resistance; do not add Instant Death.**
- **Catatan Desain & Lore:** *"Core DoT state."*


#### 🔹 [202] Severe Burn
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `70`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** HP Regen -4% Max HP/turn; Healing Received -20%
- **Aturan Boss:** ⚠️ **Bosses can resist; healing reduction needs custom logic.**
- **Catatan Desain & Lore:** *"Use only for Tier 4/rare effects."*


#### 🔹 [203] Poison
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** HP Regen -4% Max HP/turn
- **Aturan Boss:** ⚠️ **Bosses use reduced State Rate if needed.**
- **Catatan Desain & Lore:** *"Standard poison."*


#### 🔹 [204] Bleed
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** HP Regen -3% Max HP/turn
- **Aturan Boss:** ⚠️ **Bosses use reduced State Rate if needed.**
- **Catatan Desain & Lore:** *"Physical DoT."*


#### 🔹 [205] Chill
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `55`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** AGI ×85%; EVA ×90%
- **Aturan Boss:** ⚠️ **Bosses can receive Chill normally.**
- **Catatan Desain & Lore:** *"Soft control; not a lost turn."*


#### 🔹 [206] Freeze
- **Kategori & Prioritas:** `Hard CC` | Prioritas Tampilan: `80`
- **Pembatasan Aksi (*Restriction*):** `Cannot Move`
- **Durasi Giliran:** `1 – 1 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `Yes` (50.0%)
- **Mekanik & Pengaruh Parameter:** Cannot act; remove by damage 50%
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 35%.**
- **Catatan Desain & Lore:** *"Hard CC; short duration."*


#### 🔹 [207] Paralyze
- **Kategori & Prioritas:** `Hard CC` | Prioritas Tampilan: `80`
- **Pembatasan Aksi (*Restriction*):** `Cannot Move`
- **Durasi Giliran:** `1 – 1 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Cannot act
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 50%.**
- **Catatan Desain & Lore:** *"Low proc chance balances full action loss."*


#### 🔹 [208] Stun
- **Kategori & Prioritas:** `Hard CC` | Prioritas Tampilan: `90`
- **Pembatasan Aksi (*Restriction*):** `Cannot Move`
- **Durasi Giliran:** `1 – 1 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Cannot act
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 35%.**
- **Catatan Desain & Lore:** *"Do not extend beyond 1 turn by default."*


#### 🔹 [209] Root
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `55`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** AGI ×70%; EVA ×85%
- **Aturan Boss:** ⚠️ **Bosses can receive with normal resistance.**
- **Catatan Desain & Lore:** *"Turn-based root is soft control, not a stun."*


#### 🔹 [210] Slow
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `50`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** AGI ×75%
- **Aturan Boss:** ⚠️ **Bosses can receive with normal resistance.**
- **Catatan Desain & Lore:** *"Speed control."*


#### 🔹 [211] Fear
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** ATK ×85%; MAT ×85%; HIT ×90%
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 50%.**
- **Catatan Desain & Lore:** *"Avoid random forced actions to keep bosses readable."*


#### 🔹 [212] Blind
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** HIT ×50%
- **Aturan Boss:** ⚠️ **Bosses can receive with reduced State Rate.**
- **Catatan Desain & Lore:** *"Accuracy debuff."*


#### 🔹 [213] Silence
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `70`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Seal Skill Types: Black Magic, White Magic, Dark Magic
- **Aturan Boss:** ⚠️ **Bosses can have Silence State Rate 25–50%.**
- **Catatan Desain & Lore:** *"Configure Skill Type seals using IDs from MV CONFIG."*


#### 🔹 [214] Confusion
- **Kategori & Prioritas:** `Hard CC` | Prioritas Tampilan: `75`
- **Pembatasan Aksi (*Restriction*):** `Attack Anyone`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `Yes` (50.0%)
- **Mekanik & Pengaruh Parameter:** Restriction: Attack Anyone
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 25%.**
- **Catatan Desain & Lore:** *"Reduced boss chance prevents lockouts."*


#### 🔹 [215] Vulnerable 30%
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `70`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Physical Damage Rate 130%; Magical Damage Rate 130%
- **Aturan Boss:** ⚠️ **Bosses can receive normally unless encounter design says otherwise.**
- **Catatan Desain & Lore:** *"Use for Shield Breaker-tier effects."*


#### 🔹 [216] Vulnerable 60%
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `80`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `1 – 1 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Physical Damage Rate 160%; Magical Damage Rate 160%
- **Aturan Boss:** ⚠️ **Bosses: consider 50% State Rate.**
- **Catatan Desain & Lore:** *"High burst window."*


#### 🔹 [217] Vulnerable 100%
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `90`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Physical Damage Rate 200%; Magical Damage Rate 200%
- **Aturan Boss:** ⚠️ **Bosses: recommended 25% State Rate or scripted downgrade.**
- **Catatan Desain & Lore:** *"Tier 4 ultimate-only state."*


#### 🔹 [218] Soaked
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `55`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Fire Element Rate 80%; Lightning Element Rate 125%
- **Aturan Boss:** ⚠️ **Bosses can receive normally.**
- **Catatan Desain & Lore:** *"Element-combo setup."*


#### 🔹 [219] Shock
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** AGI ×90%; Lightning Element Rate 120%
- **Aturan Boss:** ⚠️ **Bosses can receive; ultimate-specific chance handled per skill.**
- **Catatan Desain & Lore:** *"Electromancer setup state."*


#### 🔹 [220] Petrify
- **Kategori & Prioritas:** `Hard CC` | Prioritas Tampilan: `95`
- **Pembatasan Aksi (*Restriction*):** `Cannot Move`
- **Durasi Giliran:** `1 – 1 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Cannot act; DEF ×130%; MDF ×130%
- **Aturan Boss:** ⚠️ **Boss State Rate recommended 25%.**
- **Catatan Desain & Lore:** *"Rare Tier 4 CC."*


#### 🔹 [221] Float
- **Kategori & Prioritas:** `Tag / Status` | Prioritas Tampilan: `50`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Tag state; optional EVA +5%
- **Aturan Boss:** ⚠️ **Ground immunity and special targeting require plugin/JS.**
- **Catatan Desain & Lore:** *"Used by Aeromancer conditional damage."*


#### 🔹 [222] Marked
- **Kategori & Prioritas:** `Tag / Status` | Prioritas Tampilan: `50`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Tag state only
- **Aturan Boss:** ⚠️ **Damage bonus from Archer/Ranger/Sniper skills requires plugin/JS.**
- **Catatan Desain & Lore:** *"Hunter's Mark family."*


#### 🔹 [223] Shadow Mark
- **Kategori & Prioritas:** `Stacking Tag` | Prioritas Tampilan: `60`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Stacking tag, max 3
- **Aturan Boss:** ⚠️ **Requires stack-aware plugin/JS.**
- **Catatan Desain & Lore:** *"Assassin resource; each stack handled by custom logic."*


#### 🔹 [224] Taunt
- **Kategori & Prioritas:** `Targeting` | Prioritas Tampilan: `70`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `2 – 2 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Forced/weighted targeting toward caster
- **Aturan Boss:** ⚠️ **Use taunt/aggro plugin or custom BattleManager target hook.**
- **Catatan Desain & Lore:** *"Vanilla TGR alone is not a guaranteed taunt."*


#### 🔹 [225] Curse
- **Kategori & Prioritas:** `Status Effect` | Prioritas Tampilan: `55`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** ATK ×90%; MAT ×90%
- **Aturan Boss:** ⚠️ **Bosses can receive with normal resistance.**
- **Catatan Desain & Lore:** *"General dark debuff."*


#### 🔹 [226] Polarized
- **Kategori & Prioritas:** `Tag / Status` | Prioritas Tampilan: `50`
- **Pembatasan Aksi (*Restriction*):** `None`
- **Durasi Giliran:** `3 – 3 Giliran (Turn End decay)`
- **Pelepasan Pertempuran:** Dihapus saat battle usai: `Yes` | Lepas jika terkena damage: `No` (0.0%)
- **Mekanik & Pengaruh Parameter:** Tag state only
- **Aturan Boss:** ⚠️ **Ferromancer conditional logic requires plugin/JS.**
- **Catatan Desain & Lore:** *"Polarity combo state."*


---

## ⚡ 3. Status Efek Skill Khusus & Pasif Kelas (ID 301 – 477)

Status efek berikut dipicu secara eksklusif oleh pohon skill profesi petualang atau auto-passive trait:

| ID | Nama State Efek Skill | Kategori | Prioritas | Pembatasan | Durasi | Efek Modifikasi Parameter & Mekanik |
|:---:|:---|:---:|:---:|:---:|:---:|:---|
| **301** | **PSV 1003 - Combat Mastery** | `Passive State` | `50` | `None` | `Permanen` | Attack +8% (Permanen) | Attack +8% (Permanen) |
| **302** | **FX 1004 - Battle Cry** | `Skill Effect State` | `50` | `None` | `3 T` | Buff ATK & DEF +12% (3 turns) | ATK +12% & DEF +12% (3 turns) |
| **303** | **PSV 1006 - Iron Discipline** | `Passive State` | `50` | `None` | `Permanen` | Max HP +8% & Fear Immunity | Max HP +8% & Fear Immunity |
| **304** | **FX 1008 - Solid Stance** | `Skill Effect State` | `50` | `None` | `2 T` | Buff DEF +25% & M.DEF +15% (2 turns) | DEF +25% & M.DEF +15% (2 turns) |
| **305** | **PSV 1011 - Guardian Armor** | `Passive State` | `50` | `None` | `Permanen` | Max HP +12%, Defense +7%, M.Defense +7% | Max HP +12%, Defense +7%, M.Defense +7% |
| **306** | **FX 1012 - Intercept** | `Skill Effect State` | `50` | `None` | `1 T` | Cover (1 turn); while covering, damage taken -20% | Cover 1 turn; damage taken -20% while Cover is active |
| **307** | **FX 1013 - Shield Wall** | `Skill Effect State` | `50` | `None` | `2 T` | Buff Defense +25% (2 turns) | DEF +25% (2 turns) |
| **308** | **FX 1015 - Suppressing Strike** | `Skill Effect State` | `50` | `None` | `2 T` | a.atk * 1.15 - b.def * 0.5; Enemy ATK -12% (2 turns) |
| **309** | **PSV 1016 - Unyielding Guard** | `Passive State` | `50` | `None` | `Permanen` | Stun/Fear Immunity; physical & magical damage taken -8% | Stun/Fear Immunity; physical & magical damage taken -8% |
| **310** | **FX 1017 - Fortified Line** | `Skill Effect State` | `50` | `None` | `2 T` | Party barrier = 12% of Squire Max HP for 2 turns | Party barrier equal to 12% of Squire Max HP for 2 turns |
| **311** | **PSV 1019 - Muscle Training** | `Passive State` | `50` | `None` | `Permanen` | Agility +8% & Evasion Rate +5% | Agility +8% & Evasion Rate +5% |
| **312** | **FX 1020 - Inner Focus** | `Skill Effect State` | `50` | `None` | `2 T` | Critical Rate +20% (2 turns) |
| **313** | **FX 1021 - Low Sweep** | `Skill Effect State` | `50` | `None` | `2 T` | a.atk * 1.1 - b.def * 0.5; Enemy AGI -15% (2 turns) |
| **314** | **PSV 1022 - Adrenaline Rush** | `Passive State` | `50` | `None` | `Permanen` | SP/TP Charge Rate +15% when dealing damage | SP/TP Charge Rate +15% when dealing damage |
| **315** | **FX 1023 - Counter Stance** | `Skill Effect State` | `50` | `None` | `1 T` | Counter Attack +30% (1 turn) |
| **316** | **PSV 1024 - Iron Fist** | `Passive State` | `50` | `None` | `Permanen` | Attack +12% & Ignore 8% DEF | Attack +12% & Ignore 8% DEF |
| **317** | **PSV 1027 - Bloodlust** | `Passive State` | `50` | `None` | `Permanen` | Lifesteal 10% of damage dealt | Lifesteal 10% of damage dealt |
| **318** | **PSV 1031 - Unstoppable Force** | `Passive State` | `50` | `None` | `Permanen` | ATK +15%, Control Resistance +40% | ATK +15%, Control Resistance +40% |
| **319** | **FX 1032 - Frenzy** | `Skill Effect State` | `50` | `None` | `3 T` | Berserker: ATK +25%, damage taken +15%, 3 turns | ATK +25%; damage taken +15% (3 turns) |
| **320** | **PSV 1034 - Desperate Fury** | `Passive State` | `50` | `None` | `Permanen` | When HP <25%: ATK +35%, AGI +20% | When HP <25%: ATK +35%, AGI +20% |
| **321** | **PSV 1037 - Fortified Guardian Armor** | `Passive State` | `50` | `None` | `Permanen` | Max HP +15%, DEF +8%, M.DEF +8% | Max HP +15%, DEF +8%, M.DEF +8% |
| **322** | **FX 1038 - War Cry** | `Skill Effect State` | `50` | `None` | `2 T` | Taunt all enemies; Enemy ATK -5%, Enemy DEF -8% (2 turns) |
| **323** | **FX 1039 - Knight’s Aegis** | `Skill Effect State` | `50` | `None` | `2 T` | Holy Veil: damage taken -40% for 2 turns | Damage taken -40% (2 turns) |
| **324** | **PSV 1040 - Shield Parry** | `Passive State` | `50` | `None` | `Permanen` | 10% chance to block physical damage and counterattack; counter scales from DEF | 10% chance to block physical damage and counterattack; counter scales from DEF |
| **325** | **FX 1042 - Vanguard Intercept** | `Skill Effect State` | `50` | `None` | `1 T` | Redirects 50% of target ally's incoming damage to self for 1 turn; 25% counter chance | Protects 1 ally for 1 turn; redirects 50% damage; 25% counter chance |
| **326** | **PSV 1043 - Will of Iron** | `Passive State` | `50` | `None` | `Permanen` | Physical Damage -20%, Fear Immunity, HP Regen 2% Max HP/turn | Physical Damage -20%, Fear Immunity, HP Regen 2% Max HP/turn |
| **327** | **PSV 1046 - Agile Footwork** | `Passive State` | `50` | `None` | `Permanen` | Agility +15%, Evasion +10%, Slow Immunity | Agility +15%, Evasion +10%, Slow Immunity |
| **328** | **PSV 1050 - Mind's Eye** | `Passive State` | `50` | `None` | `Permanen` | When an attack misses against the user, recover 4% Max SP and gain 10% counter chance for 1 turn | When an attack misses against the user, recover 4% Max SP and gain 10% counter chance for 1 turn |
| **329** | **FX 1051 - Dragon Stance** | `Skill Effect State` | `50` | `None` | `3 T` | ATK +25%, AGI +15%, SP Regen 4% Max SP/turn (3 turns) | ATK +25%, AGI +15%, SP Regen 4%/turn (3 turns) |
| **330** | **PSV 1053 - Feral Instinct** | `Passive State` | `50` | `None` | `Permanen` | Ignore 15% DEF, Crit Damage +30%, critical hits refund 3% Max SP | Ignore 15% DEF, Crit Damage +30%, critical hits refund 3% Max SP |
| **331** | **PSV 1055 - Dragon Hunter's Instinct** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **332** | **PSV 1058 - Scale Hardening** | `Passive State` | `50` | `None` | `Permanen` | Physical Damage -15%, Dragon/Boss Damage +10% | Physical Damage -15%, Dragon/Boss Damage +10% |
| **333** | **FX 1060 - Draconic Pact Transformation** | `Skill Effect State` | `50` | `None` | `3 T` | For 3 turns: ATK +25%, DEF +20%, gains Dragon element; damage taken +10% | Draconic Form: ATK +25%, DEF +20%, Dragon element; damage taken +10% (3 turns) |
| **334** | **FX 1062 - Wyvern Summon** | `Skill Effect State` | `50` | `None` | `4 T` | Wyvern auto-attack: a.atk * 1.0; duration 4 turns | Summons a Wyvern for 4 turns. Wyvern auto-attack deals a.atk * 1.0. |
| **335** | **PSV 1063 - Dragon's Wrath** | `Passive State` | `50` | `None` | `Permanen` | ATK +15%; attacks against Boss/Dragon targets gain +10% damage | ATK +15%; attacks against Boss/Dragon targets gain +10% damage |
| **336** | **PSV 1066 - Royal Vanguard Discipline** | `Passive State` | `50` | `None` | `Permanen` | Max HP +10%, ATK +8%, Control Resistance +20% | Max HP +10%, ATK +8%, Control Resistance +20% |
| **337** | **FX 1068 - King's Command** | `Skill Effect State` | `50` | `None` | `3 T` | ATK +20%, DEF +15%, Crit Rate +10% (3 turns) |
| **338** | **PSV 1069 - Unrelenting Offense** | `Passive State` | `50` | `None` | `Permanen` | ATK +12%; damage increases by 5% when HP is above 80% | ATK +12%; damage increases by 5% when HP is above 80% |
| **339** | **PSV 1074 - Savage Triumph** | `Passive State` | `50` | `None` | `Permanen` | Critical damage +25%; when defeating an enemy, recover 5% Max HP | Critical damage +25%; when defeating an enemy, recover 5% Max HP |
| **340** | **FX 1076 - Final Ignition** | `Skill Effect State` | `50` | `None` | `3 T` | Sacrifice 30% current HP. ATK +60%, Crit Rate +15%, Crit Damage +25%, AGI +20% for 3 turns; healing received -30%. | Berserk State (3 turns); healing received -30%. |
| **341** | **PSV 1078 - Guardian of Nusvanir** | `Passive State` | `50` | `None` | `Permanen` | Max HP +12%, Holy Resistance +20%, Taunt effects last +1 turn | Max HP +12%, Holy Resistance +20%, Taunt effects last +1 turn |
| **342** | **FX 1080 - Bulwark of Light** | `Skill Effect State` | `50` | `None` | `2 T` | Party barrier = 10% Paladin Max HP for 2 turns | Party barrier equal to 10% of Paladin Max HP for 2 turns |
| **343** | **PSV 1081 - Guardian's Resonating Vow** | `Passive State` | `50` | `None` | `Permanen` | When protecting an ally, damage taken -15% | When protecting an ally, damage taken -15% |
| **344** | **FX 1082 - Bulwark Stance** | `Skill Effect State` | `50` | `None` | `2 T` | DEF +30%, M.DEF +15%, AGI -10% (2 turns) |
| **345** | **FX 1084 - Sanctuary of Light** | `Skill Effect State` | `50` | `None` | `3 T` | Damage taken -30%; HP Regen 3% Max HP/turn (3 turns) | Damage taken -30% and HP Regen 3%/turn (3 turns) |
| **346** | **PSV 1086 - Absolute Fortitude** | `Passive State` | `50` | `None` | `Permanen` | Damage taken -10%; Stun and Knockback Resistance +30% | Damage taken -10%; Stun and Knockback Resistance +30% |
| **347** | **FX 1087 - Divine Citadel** | `Skill Effect State` | `50` | `None` | `3 T` | Party DEF +20%, M.DEF +20%, damage taken -10% (3 turns) |
| **348** | **FX 1088 - Avatar of Guardian: Garuda** | `Skill Effect State` | `50` | `None` | `3 T` | For 3 turns: DEF/M.DEF +55%, Max HP +20%, Regen 4% Max HP/turn; AGI -20%. | Garuda Guardian Form (3 turns). Cannot stack with other transformation states. |
| **349** | **PSV 1090 - Sang Hyang Blessing** | `Passive State` | `50` | `None` | `Permanen` | ATK +8%, M.DEF +8%, Holy Resistance +10% | ATK +8%, M.DEF +8%, Holy Resistance +10% |
| **350** | **PSV 1093 - Chi Mastery** | `Passive State` | `50` | `None` | `Permanen` | Max SP +15%, SP/TP Charge Rate +10% | Max SP +15%, SP/TP Charge Rate +10% |
| **351** | **PSV 1095 - Temple Blessing: Four Paths** | `Passive State` | `50` | `None` | `Permanen` | Choose one path after learning: Tiger (+10% ATK), Crane (+10% AGI), Tortoise (+10% DEF), Serpent (+10% Crit Rate). Permanent; only one path active. | Choose one path after learning: Tiger (+10% ATK), Crane (+10% AGI), Tortoise (+10% DEF), Serpent (+10% Crit Rate). Permanent; only one path active. |
| **352** | **FX 1096 - Chi Hyper-Burst** | `Skill Effect State` | `50` | `None` | `3 T` | ATK +25%, AGI +15%, SP Regen 5% Max SP/turn (3 turns); damage taken +10% | ATK +25%, AGI +15%, SP Regen 5%/turn, damage taken +10% (3 turns) |
| **353** | **FX 1098 - Iron Body** | `Skill Effect State` | `50` | `None` | `3 T` | Damage taken -35%, Stun/Knockback Resistance +50%, AGI -20% (3 turns) |
| **354** | **PSV 1100 - Chi Reflex** | `Passive State` | `50` | `None` | `Permanen` | Evasion +10%; when an attack misses, recover 2% Max SP | Evasion +10%; when an attack misses, recover 2% Max SP |
| **355** | **FX 1102 - Chi Life Transmutation** | `Skill Effect State` | `50` | `None` | `Permanen` | Sacrifice HP equal to 20% of Max HP to restore SP equal to 50% of Max SP; cannot reduce HP below 1. | HP sacrifice: 20% Max HP → restore 50% Max SP; cannot reduce HP below 1. |
| **356** | **PSV 1106 - Mana Amplification** | `Passive State` | `50` | `None` | `Permanen` | Mana Regen +3% Max MP/turn & Max MP +12% | Mana Regen +3% Max MP/turn & Max MP +12% |
| **357** | **FX 1108 - Magic Barrier** | `Skill Effect State` | `50` | `None` | `3 T` | Damage taken -15% (physical and magical, 3 turns) | Physical/Magic Damage taken -15% (3 turns) |
| **358** | **PSV 1109 - Elemental Mastery** | `Passive State` | `50` | `None` | `Permanen` | Elemental damage +10% | Elemental damage +10% |
| **359** | **PSV 1113 - Holy Protection** | `Passive State` | `50` | `None` | `Permanen` | M.DEF +8%; Poison/Curse/Silence Resistance +20% | M.DEF +8%; Poison/Curse/Silence Resistance +20% |
| **360** | **FX 1115 - Blessing** | `Skill Effect State` | `50` | `None` | `3 T` | ATK & M.ATK +12% (3 turns) |
| **361** | **PSV 1116 - Divine Grace** | `Passive State` | `50` | `None` | `Permanen` | Healing Power +12% | Healing Power +12% |
| **362** | **FX 1117 - Sanctuary** | `Skill Effect State` | `50` | `None` | `3 T` | Party: Regen 4% Max HP/turn (3 turns). Undead: a.mat * 0.8 - b.mdf * 0.2 | Party Regen 4% Max HP/turn for 3 turns |
| **363** | **FX 1118 - Armor of Light** | `Skill Effect State` | `50` | `None` | `2 T` | DEF & M.DEF +20% (2 turns) |
| **364** | **FX 1121 - Jenggala** | `Skill Effect State` | `50` | `None` | `3 T` | Summons 1 random Jenggala companion for 3 turns | Summons one random Jenggala companion for 3 turns. |
| **365** | **PSV 1122 - Blood Pact** | `Passive State` | `50` | `None` | `Permanen` | M.ATK +12%; Max HP -5% | M.ATK +12%; Max HP -5% |
| **366** | **FX 1124 - Abyssal Shroud** | `Skill Effect State` | `50` | `None` | `2 T` | Damage taken -20% (physical and magical, 2 turns) | Physical/Magic Damage taken -20% (2 turns) |
| **367** | **PSV 1125 - Soul Harvest** | `Passive State` | `50` | `None` | `Permanen` | Restore 6% Max MP when an enemy is defeated | Restore 6% Max MP when an enemy is defeated |
| **368** | **PSV 1132 - Arcane Elemental Mastery** | `Passive State` | `50` | `None` | `Permanen` | Elemental Magic Damage +20% | Elemental Magic Damage +20% |
| **369** | **FX 1133 - Mana Shield** | `Skill Effect State` | `50` | `None` | `3 T` | Absorbs 30% of incoming damage using MP; 3 turns | 30% of incoming damage is redirected to MP for 3 turns |
| **370** | **FX 1136 - Razor Shell** | `Skill Effect State` | `50` | `None` | `2 T` | Absorbs 35% physical damage and reflects 20% of blocked melee damage for 2 turns | Physical Damage Absorption 35%; melee reflect 20% (2 turns) |
| **371** | **PSV 1138 - Ether Conduit** | `Passive State` | `50` | `None` | `Permanen` | Ignore 15% M.DEF; MP Regen 3% Max MP/turn | Ignore 15% M.DEF; MP Regen 3% Max MP/turn |
| **372** | **FX 1140 - Time Distortion** | `Skill Effect State` | `50` | `None` | `5 T` | Enemy AGI -30%; user gains Extra Turn once. Cooldown 5 turns. | Enemy AGI -30%; grants one Extra Turn to user; cooldown 5 turns. |
| **373** | **PSV 1141 - Sorcerer's Rigor** | `Passive State` | `50` | `None` | `Permanen` | Max MP +25%, M.ATK +15%, 15% Double Cast Chance | Max MP +25%, M.ATK +15%, 15% Double Cast Chance |
| **374** | **PSV 1144 - Holy Blessing** | `Passive State` | `50` | `None` | `Permanen` | M.DEF +15%; Poison/Curse/Silence/Chaos Resistance +30% | M.DEF +15%; Poison/Curse/Silence/Chaos Resistance +30% |
| **375** | **FX 1146 - Sacred Sanctuary** | `Skill Effect State` | `50` | `None` | `3 T` | Party HP Regen 5% Max HP/turn & M.DEF +15% (3 turns) | Party Regen + M.DEF buff (3 turns). |
| **376** | **PSV 1147 - Devout Resolve** | `Passive State` | `50` | `None` | `Permanen` | MP Cost -10%, Silence & Confusion Immunity | MP Cost -10%, Silence & Confusion Immunity |
| **377** | **FX 1149 - Raise** | `Skill Effect State` | `50` | `None` | `Permanen` | Revive 1 fallen ally with 35% HP | Revives one fallen ally with 35% Max HP |
| **378** | **FX 1150 - Aegis of Faith** | `Skill Effect State` | `50` | `None` | `3 T` | DEF & M.DEF +25% (3 turns) |
| **379** | **PSV 1151 - Holy Aura** | `Passive State` | `50` | `None` | `Permanen` | When healing an ally, that ally gains DEF/M.DEF +8% for 2 turns; does not stack | When healing an ally, that ally gains DEF/M.DEF +8% for 2 turns; does not stack |
| **380** | **FX 1152 - Miracle Intervention** | `Skill Effect State` | `50` | `None` | `1 T` | Restores 55% Max HP and 30% Max MP to all allies; damage taken -40% for 1 turn | Party emergency recovery; damage taken -40% for 1 turn. Cooldown 4 turns. |
| **381** | **PSV 1154 - Blood Sacrifice Pact** | `Passive State` | `50` | `None` | `Permanen` | When HP falls below 50%, M.ATK +15% and damage taken +10% | When HP falls below 50%, M.ATK +15% and damage taken +10% |
| **382** | **PSV 1157 - Jenggala's Vow** | `Passive State` | `50` | `None` | `Permanen` | Jenggala summons gain +10% HP and +10% damage; caster damage taken +5% while a summon is active | Jenggala summons gain +10% HP and +10% damage; caster damage taken +5% while a summon is active |
| **383** | **FX 1158 - Umbral Veil** | `Skill Effect State` | `50` | `None` | `2 T` | Evasion +40% and damage taken -20% for 2 turns | Evasion +40%; damage taken -20% (2 turns) |
| **384** | **FX 1160 - Summon: Bhuta Hollow-Knight** | `Skill Effect State` | `50` | `None` | `3 T` | Hollow-Knight grants party DEF +15% for 3 turns; summon lasts 4 turns | Summons a defensive Bhuta for 4 turns; party DEF +15% while active. |
| **385** | **FX 1161 - Summon: Bhuta Fallen-Cleric** | `Skill Effect State` | `50` | `None` | `4 T` | Heals all allies for a.mat * 1.0 once on summon; summon lasts 4 turns | Summons a Fallen-Cleric for 4 turns; heals the party once on summon. |
| **386** | **PSV 1164 - Abyss Conduit** | `Passive State` | `50` | `None` | `Permanen` | Dark damage +15%; when a summon is defeated, recover 5% Max MP | Dark damage +15%; when a summon is defeated, recover 5% Max MP |
| **387** | **FX 1165 - Blood Pact: Demon Commander** | `Skill Effect State` | `50` | `None` | `3 T` | Costs 30% Current HP. Summons one selected Demon Commander for 3 turns; caster gains Commander Link while active. | Summons 1 selected Demon Commander for 3 turns. Maximum 1 Commander. Commander Link: caster damage +15% while commander is active. |
| **388** | **PSV 1173 - Heart of Flame** | `Passive State` | `50` | `None` | `Permanen` | Fire elemental damage +25%; fire damage taken -50%; Burn Immunity. | Fire elemental damage +25%; fire damage taken -50%; Burn Immunity. |
| **389** | **PSV 1176 - Flame Eater** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **390** | **FX 1178 - Flame Barrier** | `Skill Effect State` | `50` | `None` | `3 T` | Party Fire/Elemental Damage taken -40% for 3 turns; attacker suffers Burn 20% | Party elemental damage taken -40% (3 turns); fire attackers have 20% Burn chance |
| **391** | **FX 1180 - Blaze Resonance** | `Skill Effect State` | `50` | `None` | `3 T` | Fire Damage +20%; Burn chance +15%; damage taken +10% (3 turns) | Fire amplification stance (3 turns); damage taken +10%. |
| **392** | **PSV 1182 - Heart of Tides** | `Passive State` | `50` | `None` | `Permanen` | Water elemental damage +25%; water damage taken -50%; Chill Immunity. | Water elemental damage +25%; water damage taken -50%; Chill Immunity. |
| **393** | **PSV 1185 - Oceanic Mantle** | `Passive State` | `50` | `None` | `Permanen` | Burn/Chill/Freeze Immunity; Magic damage taken -10%; Regen 3% Max HP/turn during Rain. | Burn/Chill/Freeze Immunity; Magic damage taken -10%; Regen 3% Max HP/turn during Rain. |
| **394** | **FX 1186 - Aqua Prism** | `Skill Effect State` | `50` | `None` | `3 T` | Heals all allies for a.mat * 1.0; grants 12% Max HP shield for 3 turns | Party heal 1.0x MAT; 12% Max HP shield (3 turns) |
| **395** | **FX 1189 - Tidal Resonance** | `Skill Effect State` | `50` | `None` | `3 T` | Magic SP cost -15%; DEF/M.DEF +10%; party regen 4% Max HP/turn (3 turns) | Tidal Resonance (3 turns): magic SP cost -15%, DEF/M.DEF +10%, party regen 4% Max HP/turn. |
| **396** | **PSV 1191 - Heart of Stone** | `Passive State` | `50` | `None` | `Permanen` | Earth Damage +25%, DEF +20%, Stun/Knockback Resistance +30% | Earth Damage +25%, DEF +20%, Stun/Knockback Resistance +30% |
| **397** | **PSV 1194 - Earthen Resonance** | `Passive State` | `50` | `None` | `Permanen` | Magic SP cost -20%; Electric damage taken -50% | Magic SP cost -20%; Electric damage taken -50% |
| **398** | **FX 1196 - Granite Rampart** | `Skill Effect State` | `50` | `None` | `3 T` | DEF +45%; reflects 10% of incoming physical damage (3 turns) | DEF +45%; physical damage reflection 10% (3 turns) |
| **399** | **FX 1197 - Gravity** | `Skill Effect State` | `50` | `None` | `2 T` | All battlefield: AGI -25%, Flying/Float targets lose Float for 2 turns | AGI -25% globally; removes Float from affected targets for 2 turns |
| **400** | **PSV 1200 - Heart of Gale** | `Passive State` | `50` | `None` | `Permanen` | Wind Damage +25%, AGI +25%, Evasion +20% | Wind Damage +25%, AGI +25%, Evasion +20% |
| **401** | **PSV 1203 - Wind Walker** | `Passive State` | `50` | `None` | `Permanen` | Permanent Float; Ground immunity; Magic Crit Rate +10% | Permanent Float; Ground immunity; Magic Crit Rate +10% |
| **402** | **FX 1205 - Tailwind** | `Skill Effect State` | `50` | `None` | `3 T` | Party AGI +30%, Evasion +15% (3 turns) |
| **403** | **FX 1206 - Eye of the Storm** | `Skill Effect State` | `50` | `None` | `3 T` | Magic SP cost -20%; vs Float targets: Magic Crit +30%, Crit Damage +20% (3 turns) | Magic SP Cost -20%; vs Float: Magic Crit +30%, Crit Damage +20% (3 turns) |
| **404** | **FX 1207 - Zephyr Lift** | `Skill Effect State` | `50` | `None` | `2 T` | Party Float + Evasion +20% for 2 turns | Party Float and Evasion +20% (2 turns) |
| **405** | **PSV 1210 - Lightning Essence** | `Passive State` | `50` | `None` | `Permanen` | Lightning Damage +25%, AGI +20%, 15% Paralyze chance when casting electric magic | Lightning Damage +25%, AGI +20%, 15% Paralyze chance when casting electric magic |
| **406** | **PSV 1213 - Conductors** | `Passive State` | `50` | `None` | `Permanen` | Lightning Damage +15%; Metal accuracy against user -20%; Sleep Immunity; physical attackers have 15% Shock chance | Lightning Damage +15%; Metal accuracy against user -20%; Sleep Immunity; physical attackers have 15% Shock chance |
| **407** | **FX 1215 - Voltage Charge** | `Skill Effect State` | `50` | `None` | `Permanen` | Max 5 stacks. Each stack: Lightning Damage +15%, SP cost +8%. Electric skills consume all stacks and gain +10% bonus damage per stack. | Voltage stacks max 5; +15% Lightning Damage and +8% SP Cost per stack; consumed by electric skills for +10% bonus damage per stack. |
| **408** | **FX 1216 - Volt Phantom** | `Skill Effect State` | `50` | `None` | `3 T` | Sacrifice 15% Max HP. Decoy has 20% caster Max HP, absorbs 80% incoming damage, lasts up to 3 turns; destroyed decoy grants 1 Voltage stack. | Lightning Decoy: 20% caster Max HP, absorbs 80% damage, 3 turns; grants 1 Voltage stack when destroyed. |
| **409** | **PSV 1219 - Glacial Core** | `Passive State` | `50` | `None` | `Permanen` | Ice Damage +25%; Chill/Freeze resistance +30% | Ice Damage +25%; Chill/Freeze resistance +30% |
| **410** | **PSV 1222 - Snow Cloak** | `Passive State` | `50` | `None` | `Permanen` | Evasion +25%; damage taken from chilled targets -15% | Evasion +25%; damage taken from chilled targets -15% |
| **411** | **FX 1224 - Aurora Veil** | `Skill Effect State` | `50` | `None` | `3 T` | Magic Damage taken -25%; Chill attackers 30% chance (3 turns) | Magic Damage taken -25%; attackers have 30% Chill chance (3 turns) |
| **412** | **FX 1225 - Ice Mirror Illusion** | `Skill Effect State` | `50` | `None` | `3 T` | Evasion +50% for 3 turns; first avoided attack deals 1.5x MATK Ice counter | Evasion +50%; first avoided attack triggers an Ice counter (3 turns) |
| **413** | **PSV 1228 - Ferrous Dominance** | `Passive State` | `50` | `None` | `Permanen` | Metal Damage +20%; DEF +15%; gains Polarity mechanic | Metal Damage +20%; DEF +15%; gains Polarity mechanic |
| **414** | **PSV 1231 - Ironclad Bastion** | `Passive State` | `50` | `None` | `Permanen` | DEF +20%; physical damage taken -10% | DEF +20%; physical damage taken -10% |
| **415** | **FX 1233 - Iron Fortress** | `Skill Effect State` | `50` | `None` | `1 T` | Party damage taken -35% for 1 turn | Party Damage Taken -35% (1 turn) |
| **416** | **FX 1234 - Magnetic Repulsion** | `Skill Effect State` | `50` | `None` | `3 T` | Physical Evasion +30%, knockback/forced movement immunity (3 turns) | Physical Evasion +30%; forced-movement immunity (3 turns) |
| **417** | **FX 1236 - Iron Colossus** | `Skill Effect State` | `50` | `None` | `3 T` | Transformation 3 turns: DEF +60%, M.DEF +30%, ATK +20%, AGI -25%; attacks gain Metal element | Iron Colossus: DEF +60%, M.DEF +30%, ATK +20%, AGI -25%, Metal element (3 turns) |
| **418** | **PSV 1237 - Sonic Resonance** | `Passive State` | `50` | `None` | `Permanen` | Sonic Damage +25%; Hit Rate +10%; Silence Resistance +30% | Sonic Damage +25%; Hit Rate +10%; Silence Resistance +30% |
| **419** | **PSV 1240 - Active Echolocation** | `Passive State` | `50` | `None` | `Permanen` | Hit Rate +15%; reveals Stealth; Sonic skills ignore 15% Evasion | Hit Rate +15%; reveals Stealth; Sonic skills ignore 15% Evasion |
| **420** | **FX 1242 - Frequency Tuning** | `Skill Effect State` | `50` | `None` | `3 T` | Sonic Damage +25%; Skill Accuracy +20% (3 turns) |
| **421** | **FX 1243 - Infrasonic Suppression** | `Skill Effect State` | `50` | `None` | `3 T` | Enemy ATK/M.ATK -15% and Silence Resistance -20% (3 turns) |
| **422** | **FX 1245 - Absolute Vacuum Void** | `Skill Effect State` | `50` | `None` | `3 T` | a.mat * 7.5 - b.mdf * 0.0 | Sure Hit; creates Vacuum Field for 3 turns: enemy Hit Rate -15% and Sonic damage taken +15%. No extra collapse damage. |
| **423** | **PSV 1246 - Sacred Consecration** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **424** | **FX 1249 - Aegis Maxima** | `Skill Effect State` | `50` | `None` | `1 T` | Party damage taken -60% for 1 turn | Priority +5; party damage taken -60% for 1 turn. Cooldown 4 turns; can be dispelled. |
| **425** | **FX 1250 - Holy Nova** | `Skill Effect State` | `50` | `None` | `3 T` | Party Regen 5% Max HP/turn for 3 turns; Undead/Dark enemies take 4% Max HP damage per turn (Boss cap 2%) | Holy Field (3 turns): heals allies and damages Undead/Dark enemies. |
| **426** | **PSV 1251 - Divine Gift** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **427** | **PSV 1252 - Holy Barrier** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **428** | **FX 1253 - Sanctified Absolution** | `Skill Effect State` | `50` | `None` | `2 T` | Cleanses up to 5 negative states/debuffs from all allies; Status Resistance +25% for 2 turns | Mass cleanse + temporary status resistance. |
| **429** | **PSV 1255 - Martyr's Faith** | `Passive State` | `50` | `None` | `Permanen` | - | - |
| **430** | **FX 1256 - Celestial Grace** | `Skill Effect State` | `50` | `None` | `3 T` | Party Regen 8% Max HP/turn for 3 turns | Strong party regeneration for 3 turns; does not stack with itself. |
| **431** | **FX 1257 - Resurrection** | `Skill Effect State` | `50` | `None` | `1 T` | Revives 1 fallen ally with 70% Max HP | Revive 1 ally at 70% HP; grants damage taken -20% for 1 turn. |
| **432** | **FX 1258 - Avatar of Light** | `Skill Effect State` | `50` | `None` | `3 T` | Transformation 3 turns: healing +50%, Holy damage +30%, damage taken -30%, Status Resistance +50%; Dark damage taken +25%. | Avatar of Light (3 turns). Afterward: SP -30% and Healing Power -25% for 2 turns. |
| **433** | **PSV 1259 - Covenant of Demon Commanders (Luciferus)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **434** | **PSV 1260 - Covenant of Demon Commanders (Mamon)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **435** | **PSV 1261 - Covenant of Demon Commanders (Vraka)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **436** | **PSV 1262 - Covenant of Demon Commanders (Asmodea)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **437** | **PSV 1263 - Covenant of Demon Commanders (Beelzebub)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **438** | **PSV 1264 - Covenant of Demon Commanders (Belphegor)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **439** | **PSV 1265 - Covenant of Demon Commanders (Leviathanus)** | `Passive State` | `50` | `None` | `Permanen` | Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus. |
| **440** | **FX 1267 - Life Sacrifice** | `Skill Effect State` | `50` | `None` | `Permanen` | Sacrifice 10% caster Max HP to restore 30% summon Max HP | Sacrifice 10% caster Max HP to heal a summon for 30% of its Max HP |
| **441** | **FX 1268 - Soul Siphon** | `Skill Effect State` | `50` | `None` | `Permanen` | Sacrifice one active summon to restore 20% Max MP and gain 1 Soul | Dismisses one summon; restores 20% Max MP and grants 1 Soul |
| **442** | **FX 1270 - Necrotic Mana Corruption** | `Skill Effect State` | `50` | `None` | `Permanen` | Consumes 20% current MP; restores 25% Max HP | Converts MP into emergency healing; restores 25% Max HP |
| **443** | **PSV 1275 - Necrotic Mastery** | `Passive State` | `50` | `None` | `Permanen` | Dark Magic Damage +15%, Max MP +10%, summon costs reduced by 15% | Dark Magic Damage +15%, Max MP +10%, summon costs reduced by 15%; maximum 2 active summons. |
| **444** | **FX 1277 - Bhuta Manifestation: Sanctuary (Dark Priest)** | `Skill Effect State` | `50` | `None` | `4 T` | Heals all allies for a.mat * 0.9 + 20 on summon | Summons one Sanctuary Bhuta for 4 turns; maximum 2 active summons. |
| **445** | **PSV 1280 - Dual Demon Commander Contract** | `Passive State` | `50` | `None` | `Permanen` | Unlocks a second Commander contract option; only one Demon Commander may be active at a time. | Can equip two Commander contract options, but only one Commander can be active at a time. |
| **446** | **PSV 1285 - Eagle Eye** | `Passive State` | `50` | `None` | `Permanen` | Hit Rate +12% & Critical Rate +4% | Hit Rate +12% & Critical Rate +4% |
| **447** | **PSV 1288 - Swift Reflexes** | `Passive State` | `50` | `None` | `Permanen` | Agility +12% & Evasion +8% | Agility +12% & Evasion +8% |
| **448** | **PSV 1293 - Shadow Step** | `Passive State` | `50` | `None` | `Permanen` | Evasion +12% & Critical Rate +4% | Evasion +12% & Critical Rate +4% |
| **449** | **FX 1296 - Hide** | `Skill Effect State` | `50` | `None` | `1 T` | Shadow State: Evasion +70%, single-target damage taken -30%, 1 turn | Shadow State: Evasion +70%, single-target damage taken -30% (1 turn) |
| **450** | **PSV 1298 - Shadow Reflexes** | `Passive State` | `50` | `None` | `Permanen` | Agility +15% | Agility +15% |
| **451** | **FX 1300 - Shadow Lunge** | `Skill Effect State` | `50` | `None` | `1 T` | a.atk * 2.1 - b.def * 0.3 | Evasion +50% against the next physical attack (1 turn) |
| **452** | **PSV 1304 - Wild Stride** | `Passive State` | `50` | `None` | `Permanen` | AGI +12%, Move/Field Evasion +10% | AGI +12%, Move/Field Evasion +10% |
| **453** | **PSV 1307 - Hunter's Focus** | `Passive State` | `50` | `None` | `Permanen` | Damage +10% vs Marked targets; Crit Rate +8% | Damage +10% vs Marked targets; Crit Rate +8% |
| **454** | **PSV 1311 - Lupine Companion** | `Passive State` | `50` | `None` | `Permanen` | Summons Lupine companion for 5 turns; companion damage +10% while target is Marked | Summons Lupine companion for 5 turns; companion damage +10% while target is Marked |
| **455** | **PSV 1314 - Multi-Shot Mastery** | `Passive State` | `50` | `None` | `Permanen` | Multi-hit skills deal +10% total damage; no per-hit stacking | Multi-hit skills deal +10% total damage; no per-hit stacking |
| **456** | **PSV 1316 - Twin Blade Mastery** | `Passive State` | `50` | `None` | `Permanen` | Dual-wield damage +10%; Off-hand penalty reduced by 25% | Dual-wield damage +10%; Off-hand penalty reduced by 25% |
| **457** | **FX 1318 - Shadow Meld** | `Skill Effect State` | `50` | `None` | `2 T` | Evasion +40% and next single-target physical hit deals +20% damage (2 turns) | Evasion +40%; next single-target physical hit +20% (2 turns) |
| **458** | **PSV 1320 - Sadistic Executioner** | `Passive State` | `50` | `None` | `Permanen` | Damage +15% against targets below 40% HP | Damage +15% against targets below 40% HP |
| **459** | **FX 1321 - Phantom Decoy** | `Skill Effect State` | `50` | `None` | `2 T` | Creates a decoy with 15% Max HP; 50% chance to redirect a single-target attack for 2 turns | Decoy: 15% Max HP; 50% single-target redirect chance (2 turns) |
| **460** | **FX 1323 - Smokescreen** | `Skill Effect State` | `50` | `None` | `2 T` | Enemy Hit Rate -20% for 2 turns |
| **461** | **PSV 1324 - Shadow Ambush** | `Passive State` | `50` | `None` | `Permanen` | First attack against an unalerted target deals +20% damage and gains +15% Crit Rate | First attack against an unalerted target deals +20% damage and gains +15% Crit Rate |
| **462** | **PSV 1327 - Illusive Demise** | `Passive State` | `50` | `None` | `Permanen` | Evasion +15%; once per battle, survive a lethal hit at 1 HP | Evasion +15%; once per battle, survive a lethal hit at 1 HP |
| **463** | **PSV 1329 - Marksman Instinct** | `Passive State` | `50` | `None` | `Permanen` | First target hit becomes Marked for 3 turns; damage +8% and Hit Rate +10% vs Marked | First target hit becomes Marked for 3 turns; damage +8% and Hit Rate +10% vs Marked. |
| **464** | **FX 1330 - Focus Energy** | `Skill Effect State` | `50` | `None` | `1 T` | Focus: Crit Rate +20%, Hit Rate +20%, damage +10% for 1 turn | Crit Rate +20%, Hit Rate +20%, damage +10% (1 turn) |
| **465** | **FX 1331 - Nature Concealment** | `Skill Effect State` | `50` | `None` | `1 T` | Concealment: Evasion +60%, cannot be targeted by direct single-target attacks for 1 turn; ends after attacking | Concealment: Evasion +60%, untargetable by direct single-target attacks for 1 turn; ends after attacking |
| **466** | **PSV 1333 - Lupine Ride** | `Passive State` | `50` | `None` | `Permanen` | While riding Lupine: AGI +20%, Evasion +10%, ranged damage +10% | While riding Lupine: AGI +20%, Evasion +10%, ranged damage +10% |
| **467** | **PSV 1335 - Ambush Mastery** | `Passive State` | `50` | `None` | `Permanen` | Damage +10% against targets that have not acted; ignore 15% DEF | Damage +10% against targets that have not acted; ignore 15% DEF. |
| **468** | **PSV 1337 - Cold-Blooded Executioner** | `Passive State` | `50` | `None` | `Permanen` | Crit Damage +20%; +8% damage vs targets below 30% HP | Crit Damage +20%; +8% damage vs targets below 30% HP. |
| **469** | **FX 1338 - Enchant Elemental Arrow** | `Skill Effect State` | `50` | `None` | `3 T` | Choose Fire/Ice/Wind/Earth/Lightning/Metal/Sonic; attacks gain chosen element and +10% elemental damage for 3 turns | Elemental Arrow: choose one element; attacks gain that element and +10% elemental damage (3 turns) |
| **470** | **PSV 1340 - Phantom Thread** | `Passive State` | `50` | `None` | `Permanen` | Evasion +15%; damage from behind +15% | Evasion +15%; damage from behind +15% |
| **471** | **PSV 1341 - Shadow Mark** | `Passive State` | `50` | `None` | `Permanen` | Attacks can apply Shadow Mark, max 3 stacks; each stack +4% damage from Assassin; lasts 3 turns | Shadow Mark max 3 stacks; each stack +4% Assassin damage; lasts 3 turns. |
| **472** | **FX 1343 - Shadow Clone** | `Skill Effect State` | `50` | `None` | `2 T` | Creates 1 clone for 2 turns; clone has 30% caster Max HP and deals 35% of caster attack damage | Summons 1 Shadow Clone for 2 turns; clone deals 35% attack damage |
| **473** | **PSV 1344 - Toxic Coating** | `Passive State` | `50` | `None` | `Permanen` | Attacks have 30% Poison chance; Poison damage +15% | Attacks have 30% Poison chance; Poison damage +15%. |
| **474** | **FX 1345 - Shadow Cloak** | `Skill Effect State` | `50` | `None` | `1 T` | Evasion +70%, single-target damage taken -30%, duration 1 turn; ends after attacking | Evasion +70%, single-target damage taken -30% (1 turn); ends after attacking |
| **475** | **PSV 1347 - Phantom Executioner** | `Passive State` | `50` | `None` | `Permanen` | Damage +20% vs targets below 35% HP; execution bonus does not affect Bosses | Damage +20% vs targets below 35% HP; execution bonus does not affect Bosses |
| **476** | **FX 1348 - Toxic Smoke Bomb** | `Skill Effect State` | `50` | `None` | `2 T` | Poison 55% and Hit Rate -15% to all enemies for 2 turns; user Evasion +15% for 2 turns | Enemy Hit Rate -15% and user Evasion +15% (2 turns). |
| **477** | **PSV 1349 - Silent Killer** | `Passive State` | `50` | `None` | `Permanen` | Critical Rate +10%; attacks against Silenced targets deal +15% damage | Critical Rate +10%; attacks against Silenced targets deal +15% damage |

### Rincian Roster Efek Skill Per Kategori Kelas

#### 🔸 [301] PSV 1003 - Combat Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Attack +8% (Permanen) | Attack +8% (Permanen)
- **Catatan Implementasi:** Source Skill ID 1003; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [302] FX 1004 - Battle Cry
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Buff ATK & DEF +12% (3 turns) | ATK +12% & DEF +12% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1004; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [303] PSV 1006 - Iron Discipline
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max HP +8% & Fear Immunity | Max HP +8% & Fear Immunity
- **Catatan Implementasi:** Source Skill ID 1006; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [304] FX 1008 - Solid Stance
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Buff DEF +25% & M.DEF +15% (2 turns) | DEF +25% & M.DEF +15% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1008; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [305] PSV 1011 - Guardian Armor
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max HP +12%, Defense +7%, M.Defense +7% | Max HP +12%, Defense +7%, M.Defense +7%
- **Catatan Implementasi:** Source Skill ID 1011; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [306] FX 1012 - Intercept
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Cover (1 turn); while covering, damage taken -20% | Cover 1 turn; damage taken -20% while Cover is active
- **Catatan Implementasi:** Source Skill ID 1012; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [307] FX 1013 - Shield Wall
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Buff Defense +25% (2 turns) | DEF +25% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1013; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [308] FX 1015 - Suppressing Strike
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** a.atk * 1.15 - b.def * 0.5; Enemy ATK -12% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1015; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [309] PSV 1016 - Unyielding Guard
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Stun/Fear Immunity; physical & magical damage taken -8% | Stun/Fear Immunity; physical & magical damage taken -8%
- **Catatan Implementasi:** Source Skill ID 1016; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [310] FX 1017 - Fortified Line
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party barrier = 12% of Squire Max HP for 2 turns | Party barrier equal to 12% of Squire Max HP for 2 turns
- **Catatan Implementasi:** Source Skill ID 1017; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [311] PSV 1019 - Muscle Training
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Agility +8% & Evasion Rate +5% | Agility +8% & Evasion Rate +5%
- **Catatan Implementasi:** Source Skill ID 1019; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [312] FX 1020 - Inner Focus
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Critical Rate +20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1020; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [313] FX 1021 - Low Sweep
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** a.atk * 1.1 - b.def * 0.5; Enemy AGI -15% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1021; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [314] PSV 1022 - Adrenaline Rush
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** SP/TP Charge Rate +15% when dealing damage | SP/TP Charge Rate +15% when dealing damage
- **Catatan Implementasi:** Source Skill ID 1022; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [315] FX 1023 - Counter Stance
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Counter Attack +30% (1 turn)
- **Catatan Implementasi:** Source Skill ID 1023; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [316] PSV 1024 - Iron Fist
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Attack +12% & Ignore 8% DEF | Attack +12% & Ignore 8% DEF
- **Catatan Implementasi:** Source Skill ID 1024; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [317] PSV 1027 - Bloodlust
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Lifesteal 10% of damage dealt | Lifesteal 10% of damage dealt
- **Catatan Implementasi:** Source Skill ID 1027; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [318] PSV 1031 - Unstoppable Force
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +15%, Control Resistance +40% | ATK +15%, Control Resistance +40%
- **Catatan Implementasi:** Source Skill ID 1031; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [319] FX 1032 - Frenzy
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Berserker: ATK +25%, damage taken +15%, 3 turns | ATK +25%; damage taken +15% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1032; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [320] PSV 1034 - Desperate Fury
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** When HP <25%: ATK +35%, AGI +20% | When HP <25%: ATK +35%, AGI +20%
- **Catatan Implementasi:** Source Skill ID 1034; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [321] PSV 1037 - Fortified Guardian Armor
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max HP +15%, DEF +8%, M.DEF +8% | Max HP +15%, DEF +8%, M.DEF +8%
- **Catatan Implementasi:** Source Skill ID 1037; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [322] FX 1038 - War Cry
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Taunt all enemies; Enemy ATK -5%, Enemy DEF -8% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1038; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [323] FX 1039 - Knight’s Aegis
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Holy Veil: damage taken -40% for 2 turns | Damage taken -40% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1039; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [324] PSV 1040 - Shield Parry
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** 10% chance to block physical damage and counterattack; counter scales from DEF | 10% chance to block physical damage and counterattack; counter scales from DEF
- **Catatan Implementasi:** Source Skill ID 1040; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [325] FX 1042 - Vanguard Intercept
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Redirects 50% of target ally's incoming damage to self for 1 turn; 25% counter chance | Protects 1 ally for 1 turn; redirects 50% damage; 25% counter chance
- **Catatan Implementasi:** Source Skill ID 1042; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [326] PSV 1043 - Will of Iron
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Physical Damage -20%, Fear Immunity, HP Regen 2% Max HP/turn | Physical Damage -20%, Fear Immunity, HP Regen 2% Max HP/turn
- **Catatan Implementasi:** Source Skill ID 1043; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [327] PSV 1046 - Agile Footwork
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Agility +15%, Evasion +10%, Slow Immunity | Agility +15%, Evasion +10%, Slow Immunity
- **Catatan Implementasi:** Source Skill ID 1046; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [328] PSV 1050 - Mind's Eye
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** When an attack misses against the user, recover 4% Max SP and gain 10% counter chance for 1 turn | When an attack misses against the user, recover 4% Max SP and gain 10% counter chance for 1 turn
- **Catatan Implementasi:** Source Skill ID 1050; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [329] FX 1051 - Dragon Stance
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +25%, AGI +15%, SP Regen 4% Max SP/turn (3 turns) | ATK +25%, AGI +15%, SP Regen 4%/turn (3 turns)
- **Catatan Implementasi:** Source Skill ID 1051; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [330] PSV 1053 - Feral Instinct
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Ignore 15% DEF, Crit Damage +30%, critical hits refund 3% Max SP | Ignore 15% DEF, Crit Damage +30%, critical hits refund 3% Max SP
- **Catatan Implementasi:** Source Skill ID 1053; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [331] PSV 1055 - Dragon Hunter's Instinct
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1055; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [332] PSV 1058 - Scale Hardening
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Physical Damage -15%, Dragon/Boss Damage +10% | Physical Damage -15%, Dragon/Boss Damage +10%
- **Catatan Implementasi:** Source Skill ID 1058; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [333] FX 1060 - Draconic Pact Transformation
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** For 3 turns: ATK +25%, DEF +20%, gains Dragon element; damage taken +10% | Draconic Form: ATK +25%, DEF +20%, Dragon element; damage taken +10% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1060; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [334] FX 1062 - Wyvern Summon
- **Kategori & Durasi:** `Skill Effect State` | `4 – 4 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Wyvern auto-attack: a.atk * 1.0; duration 4 turns | Summons a Wyvern for 4 turns. Wyvern auto-attack deals a.atk * 1.0.
- **Catatan Implementasi:** Source Skill ID 1062; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [335] PSV 1063 - Dragon's Wrath
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +15%; attacks against Boss/Dragon targets gain +10% damage | ATK +15%; attacks against Boss/Dragon targets gain +10% damage
- **Catatan Implementasi:** Source Skill ID 1063; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [336] PSV 1066 - Royal Vanguard Discipline
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max HP +10%, ATK +8%, Control Resistance +20% | Max HP +10%, ATK +8%, Control Resistance +20%
- **Catatan Implementasi:** Source Skill ID 1066; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [337] FX 1068 - King's Command
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +20%, DEF +15%, Crit Rate +10% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1068; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [338] PSV 1069 - Unrelenting Offense
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +12%; damage increases by 5% when HP is above 80% | ATK +12%; damage increases by 5% when HP is above 80%
- **Catatan Implementasi:** Source Skill ID 1069; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [339] PSV 1074 - Savage Triumph
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Critical damage +25%; when defeating an enemy, recover 5% Max HP | Critical damage +25%; when defeating an enemy, recover 5% Max HP
- **Catatan Implementasi:** Source Skill ID 1074; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [340] FX 1076 - Final Ignition
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sacrifice 30% current HP. ATK +60%, Crit Rate +15%, Crit Damage +25%, AGI +20% for 3 turns; healing received -30%. | Berserk State (3 turns); healing received -30%.
- **Catatan Implementasi:** Source Skill ID 1076; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [341] PSV 1078 - Guardian of Nusvanir
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max HP +12%, Holy Resistance +20%, Taunt effects last +1 turn | Max HP +12%, Holy Resistance +20%, Taunt effects last +1 turn
- **Catatan Implementasi:** Source Skill ID 1078; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [342] FX 1080 - Bulwark of Light
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party barrier = 10% Paladin Max HP for 2 turns | Party barrier equal to 10% of Paladin Max HP for 2 turns
- **Catatan Implementasi:** Source Skill ID 1080; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [343] PSV 1081 - Guardian's Resonating Vow
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** When protecting an ally, damage taken -15% | When protecting an ally, damage taken -15%
- **Catatan Implementasi:** Source Skill ID 1081; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [344] FX 1082 - Bulwark Stance
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** DEF +30%, M.DEF +15%, AGI -10% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1082; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [345] FX 1084 - Sanctuary of Light
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage taken -30%; HP Regen 3% Max HP/turn (3 turns) | Damage taken -30% and HP Regen 3%/turn (3 turns)
- **Catatan Implementasi:** Source Skill ID 1084; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [346] PSV 1086 - Absolute Fortitude
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage taken -10%; Stun and Knockback Resistance +30% | Damage taken -10%; Stun and Knockback Resistance +30%
- **Catatan Implementasi:** Source Skill ID 1086; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [347] FX 1087 - Divine Citadel
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party DEF +20%, M.DEF +20%, damage taken -10% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1087; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [348] FX 1088 - Avatar of Guardian: Garuda
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** For 3 turns: DEF/M.DEF +55%, Max HP +20%, Regen 4% Max HP/turn; AGI -20%. | Garuda Guardian Form (3 turns). Cannot stack with other transformation states.
- **Catatan Implementasi:** Source Skill ID 1088; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [349] PSV 1090 - Sang Hyang Blessing
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +8%, M.DEF +8%, Holy Resistance +10% | ATK +8%, M.DEF +8%, Holy Resistance +10%
- **Catatan Implementasi:** Source Skill ID 1090; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [350] PSV 1093 - Chi Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max SP +15%, SP/TP Charge Rate +10% | Max SP +15%, SP/TP Charge Rate +10%
- **Catatan Implementasi:** Source Skill ID 1093; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [351] PSV 1095 - Temple Blessing: Four Paths
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Choose one path after learning: Tiger (+10% ATK), Crane (+10% AGI), Tortoise (+10% DEF), Serpent (+10% Crit Rate). Permanent; only one path active. | Choose one path after learning: Tiger (+10% ATK), Crane (+10% AGI), Tortoise (+10% DEF), Serpent (+10% Crit Rate). Permanent; only one path active.
- **Catatan Implementasi:** Source Skill ID 1095; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [352] FX 1096 - Chi Hyper-Burst
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK +25%, AGI +15%, SP Regen 5% Max SP/turn (3 turns); damage taken +10% | ATK +25%, AGI +15%, SP Regen 5%/turn, damage taken +10% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1096; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [353] FX 1098 - Iron Body
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage taken -35%, Stun/Knockback Resistance +50%, AGI -20% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1098; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [354] PSV 1100 - Chi Reflex
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +10%; when an attack misses, recover 2% Max SP | Evasion +10%; when an attack misses, recover 2% Max SP
- **Catatan Implementasi:** Source Skill ID 1100; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [355] FX 1102 - Chi Life Transmutation
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sacrifice HP equal to 20% of Max HP to restore SP equal to 50% of Max SP; cannot reduce HP below 1. | HP sacrifice: 20% Max HP → restore 50% Max SP; cannot reduce HP below 1.
- **Catatan Implementasi:** Source Skill ID 1102; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [356] PSV 1106 - Mana Amplification
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Mana Regen +3% Max MP/turn & Max MP +12% | Mana Regen +3% Max MP/turn & Max MP +12%
- **Catatan Implementasi:** Source Skill ID 1106; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [357] FX 1108 - Magic Barrier
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage taken -15% (physical and magical, 3 turns) | Physical/Magic Damage taken -15% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1108; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [358] PSV 1109 - Elemental Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Elemental damage +10% | Elemental damage +10%
- **Catatan Implementasi:** Source Skill ID 1109; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [359] PSV 1113 - Holy Protection
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** M.DEF +8%; Poison/Curse/Silence Resistance +20% | M.DEF +8%; Poison/Curse/Silence Resistance +20%
- **Catatan Implementasi:** Source Skill ID 1113; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [360] FX 1115 - Blessing
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** ATK & M.ATK +12% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1115; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [361] PSV 1116 - Divine Grace
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Healing Power +12% | Healing Power +12%
- **Catatan Implementasi:** Source Skill ID 1116; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [362] FX 1117 - Sanctuary
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party: Regen 4% Max HP/turn (3 turns). Undead: a.mat * 0.8 - b.mdf * 0.2 | Party Regen 4% Max HP/turn for 3 turns
- **Catatan Implementasi:** Source Skill ID 1117; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [363] FX 1118 - Armor of Light
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** DEF & M.DEF +20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1118; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [364] FX 1121 - Jenggala
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Summons 1 random Jenggala companion for 3 turns | Summons one random Jenggala companion for 3 turns.
- **Catatan Implementasi:** Source Skill ID 1121; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [365] PSV 1122 - Blood Pact
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** M.ATK +12%; Max HP -5% | M.ATK +12%; Max HP -5%
- **Catatan Implementasi:** Source Skill ID 1122; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [366] FX 1124 - Abyssal Shroud
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage taken -20% (physical and magical, 2 turns) | Physical/Magic Damage taken -20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1124; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [367] PSV 1125 - Soul Harvest
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Restore 6% Max MP when an enemy is defeated | Restore 6% Max MP when an enemy is defeated
- **Catatan Implementasi:** Source Skill ID 1125; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [368] PSV 1132 - Arcane Elemental Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Elemental Magic Damage +20% | Elemental Magic Damage +20%
- **Catatan Implementasi:** Source Skill ID 1132; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [369] FX 1133 - Mana Shield
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Absorbs 30% of incoming damage using MP; 3 turns | 30% of incoming damage is redirected to MP for 3 turns
- **Catatan Implementasi:** Source Skill ID 1133; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [370] FX 1136 - Razor Shell
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Absorbs 35% physical damage and reflects 20% of blocked melee damage for 2 turns | Physical Damage Absorption 35%; melee reflect 20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1136; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [371] PSV 1138 - Ether Conduit
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Ignore 15% M.DEF; MP Regen 3% Max MP/turn | Ignore 15% M.DEF; MP Regen 3% Max MP/turn
- **Catatan Implementasi:** Source Skill ID 1138; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [372] FX 1140 - Time Distortion
- **Kategori & Durasi:** `Skill Effect State` | `5 – 5 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Enemy AGI -30%; user gains Extra Turn once. Cooldown 5 turns. | Enemy AGI -30%; grants one Extra Turn to user; cooldown 5 turns.
- **Catatan Implementasi:** Source Skill ID 1140; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [373] PSV 1141 - Sorcerer's Rigor
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max MP +25%, M.ATK +15%, 15% Double Cast Chance | Max MP +25%, M.ATK +15%, 15% Double Cast Chance
- **Catatan Implementasi:** Source Skill ID 1141; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [374] PSV 1144 - Holy Blessing
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** M.DEF +15%; Poison/Curse/Silence/Chaos Resistance +30% | M.DEF +15%; Poison/Curse/Silence/Chaos Resistance +30%
- **Catatan Implementasi:** Source Skill ID 1144; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [375] FX 1146 - Sacred Sanctuary
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party HP Regen 5% Max HP/turn & M.DEF +15% (3 turns) | Party Regen + M.DEF buff (3 turns).
- **Catatan Implementasi:** Source Skill ID 1146; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [376] PSV 1147 - Devout Resolve
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** MP Cost -10%, Silence & Confusion Immunity | MP Cost -10%, Silence & Confusion Immunity
- **Catatan Implementasi:** Source Skill ID 1147; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [377] FX 1149 - Raise
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Revive 1 fallen ally with 35% HP | Revives one fallen ally with 35% Max HP
- **Catatan Implementasi:** Source Skill ID 1149; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [378] FX 1150 - Aegis of Faith
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** DEF & M.DEF +25% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1150; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [379] PSV 1151 - Holy Aura
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** When healing an ally, that ally gains DEF/M.DEF +8% for 2 turns; does not stack | When healing an ally, that ally gains DEF/M.DEF +8% for 2 turns; does not stack
- **Catatan Implementasi:** Source Skill ID 1151; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [380] FX 1152 - Miracle Intervention
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Restores 55% Max HP and 30% Max MP to all allies; damage taken -40% for 1 turn | Party emergency recovery; damage taken -40% for 1 turn. Cooldown 4 turns.
- **Catatan Implementasi:** Source Skill ID 1152; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [381] PSV 1154 - Blood Sacrifice Pact
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** When HP falls below 50%, M.ATK +15% and damage taken +10% | When HP falls below 50%, M.ATK +15% and damage taken +10%
- **Catatan Implementasi:** Source Skill ID 1154; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [382] PSV 1157 - Jenggala's Vow
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Jenggala summons gain +10% HP and +10% damage; caster damage taken +5% while a summon is active | Jenggala summons gain +10% HP and +10% damage; caster damage taken +5% while a summon is active
- **Catatan Implementasi:** Source Skill ID 1157; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [383] FX 1158 - Umbral Veil
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +40% and damage taken -20% for 2 turns | Evasion +40%; damage taken -20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1158; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [384] FX 1160 - Summon: Bhuta Hollow-Knight
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Hollow-Knight grants party DEF +15% for 3 turns; summon lasts 4 turns | Summons a defensive Bhuta for 4 turns; party DEF +15% while active.
- **Catatan Implementasi:** Source Skill ID 1160; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [385] FX 1161 - Summon: Bhuta Fallen-Cleric
- **Kategori & Durasi:** `Skill Effect State` | `4 – 4 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Heals all allies for a.mat * 1.0 once on summon; summon lasts 4 turns | Summons a Fallen-Cleric for 4 turns; heals the party once on summon.
- **Catatan Implementasi:** Source Skill ID 1161; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [386] PSV 1164 - Abyss Conduit
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Dark damage +15%; when a summon is defeated, recover 5% Max MP | Dark damage +15%; when a summon is defeated, recover 5% Max MP
- **Catatan Implementasi:** Source Skill ID 1164; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [387] FX 1165 - Blood Pact: Demon Commander
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Costs 30% Current HP. Summons one selected Demon Commander for 3 turns; caster gains Commander Link while active. | Summons 1 selected Demon Commander for 3 turns. Maximum 1 Commander. Commander Link: caster damage +15% while commander is active.
- **Catatan Implementasi:** Source Skill ID 1165; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [388] PSV 1173 - Heart of Flame
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Fire elemental damage +25%; fire damage taken -50%; Burn Immunity. | Fire elemental damage +25%; fire damage taken -50%; Burn Immunity.
- **Catatan Implementasi:** Source Skill ID 1173; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [389] PSV 1176 - Flame Eater
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1176; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [390] FX 1178 - Flame Barrier
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party Fire/Elemental Damage taken -40% for 3 turns; attacker suffers Burn 20% | Party elemental damage taken -40% (3 turns); fire attackers have 20% Burn chance
- **Catatan Implementasi:** Source Skill ID 1178; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [391] FX 1180 - Blaze Resonance
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Fire Damage +20%; Burn chance +15%; damage taken +10% (3 turns) | Fire amplification stance (3 turns); damage taken +10%.
- **Catatan Implementasi:** Source Skill ID 1180; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [392] PSV 1182 - Heart of Tides
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Water elemental damage +25%; water damage taken -50%; Chill Immunity. | Water elemental damage +25%; water damage taken -50%; Chill Immunity.
- **Catatan Implementasi:** Source Skill ID 1182; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [393] PSV 1185 - Oceanic Mantle
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Burn/Chill/Freeze Immunity; Magic damage taken -10%; Regen 3% Max HP/turn during Rain. | Burn/Chill/Freeze Immunity; Magic damage taken -10%; Regen 3% Max HP/turn during Rain.
- **Catatan Implementasi:** Source Skill ID 1185; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [394] FX 1186 - Aqua Prism
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Heals all allies for a.mat * 1.0; grants 12% Max HP shield for 3 turns | Party heal 1.0x MAT; 12% Max HP shield (3 turns)
- **Catatan Implementasi:** Source Skill ID 1186; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [395] FX 1189 - Tidal Resonance
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Magic SP cost -15%; DEF/M.DEF +10%; party regen 4% Max HP/turn (3 turns) | Tidal Resonance (3 turns): magic SP cost -15%, DEF/M.DEF +10%, party regen 4% Max HP/turn.
- **Catatan Implementasi:** Source Skill ID 1189; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [396] PSV 1191 - Heart of Stone
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Earth Damage +25%, DEF +20%, Stun/Knockback Resistance +30% | Earth Damage +25%, DEF +20%, Stun/Knockback Resistance +30%
- **Catatan Implementasi:** Source Skill ID 1191; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [397] PSV 1194 - Earthen Resonance
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Magic SP cost -20%; Electric damage taken -50% | Magic SP cost -20%; Electric damage taken -50%
- **Catatan Implementasi:** Source Skill ID 1194; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [398] FX 1196 - Granite Rampart
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** DEF +45%; reflects 10% of incoming physical damage (3 turns) | DEF +45%; physical damage reflection 10% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1196; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [399] FX 1197 - Gravity
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** All battlefield: AGI -25%, Flying/Float targets lose Float for 2 turns | AGI -25% globally; removes Float from affected targets for 2 turns
- **Catatan Implementasi:** Source Skill ID 1197; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [400] PSV 1200 - Heart of Gale
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Wind Damage +25%, AGI +25%, Evasion +20% | Wind Damage +25%, AGI +25%, Evasion +20%
- **Catatan Implementasi:** Source Skill ID 1200; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [401] PSV 1203 - Wind Walker
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Permanent Float; Ground immunity; Magic Crit Rate +10% | Permanent Float; Ground immunity; Magic Crit Rate +10%
- **Catatan Implementasi:** Source Skill ID 1203; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [402] FX 1205 - Tailwind
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party AGI +30%, Evasion +15% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1205; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [403] FX 1206 - Eye of the Storm
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Magic SP cost -20%; vs Float targets: Magic Crit +30%, Crit Damage +20% (3 turns) | Magic SP Cost -20%; vs Float: Magic Crit +30%, Crit Damage +20% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1206; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [404] FX 1207 - Zephyr Lift
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party Float + Evasion +20% for 2 turns | Party Float and Evasion +20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1207; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [405] PSV 1210 - Lightning Essence
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Lightning Damage +25%, AGI +20%, 15% Paralyze chance when casting electric magic | Lightning Damage +25%, AGI +20%, 15% Paralyze chance when casting electric magic
- **Catatan Implementasi:** Source Skill ID 1210; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [406] PSV 1213 - Conductors
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Lightning Damage +15%; Metal accuracy against user -20%; Sleep Immunity; physical attackers have 15% Shock chance | Lightning Damage +15%; Metal accuracy against user -20%; Sleep Immunity; physical attackers have 15% Shock chance
- **Catatan Implementasi:** Source Skill ID 1213; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [407] FX 1215 - Voltage Charge
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Max 5 stacks. Each stack: Lightning Damage +15%, SP cost +8%. Electric skills consume all stacks and gain +10% bonus damage per stack. | Voltage stacks max 5; +15% Lightning Damage and +8% SP Cost per stack; consumed by electric skills for +10% bonus damage per stack.
- **Catatan Implementasi:** Source Skill ID 1215; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [408] FX 1216 - Volt Phantom
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sacrifice 15% Max HP. Decoy has 20% caster Max HP, absorbs 80% incoming damage, lasts up to 3 turns; destroyed decoy grants 1 Voltage stack. | Lightning Decoy: 20% caster Max HP, absorbs 80% damage, 3 turns; grants 1 Voltage stack when destroyed.
- **Catatan Implementasi:** Source Skill ID 1216; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [409] PSV 1219 - Glacial Core
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Ice Damage +25%; Chill/Freeze resistance +30% | Ice Damage +25%; Chill/Freeze resistance +30%
- **Catatan Implementasi:** Source Skill ID 1219; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [410] PSV 1222 - Snow Cloak
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +25%; damage taken from chilled targets -15% | Evasion +25%; damage taken from chilled targets -15%
- **Catatan Implementasi:** Source Skill ID 1222; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [411] FX 1224 - Aurora Veil
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Magic Damage taken -25%; Chill attackers 30% chance (3 turns) | Magic Damage taken -25%; attackers have 30% Chill chance (3 turns)
- **Catatan Implementasi:** Source Skill ID 1224; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [412] FX 1225 - Ice Mirror Illusion
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +50% for 3 turns; first avoided attack deals 1.5x MATK Ice counter | Evasion +50%; first avoided attack triggers an Ice counter (3 turns)
- **Catatan Implementasi:** Source Skill ID 1225; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [413] PSV 1228 - Ferrous Dominance
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Metal Damage +20%; DEF +15%; gains Polarity mechanic | Metal Damage +20%; DEF +15%; gains Polarity mechanic
- **Catatan Implementasi:** Source Skill ID 1228; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [414] PSV 1231 - Ironclad Bastion
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** DEF +20%; physical damage taken -10% | DEF +20%; physical damage taken -10%
- **Catatan Implementasi:** Source Skill ID 1231; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [415] FX 1233 - Iron Fortress
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party damage taken -35% for 1 turn | Party Damage Taken -35% (1 turn)
- **Catatan Implementasi:** Source Skill ID 1233; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [416] FX 1234 - Magnetic Repulsion
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Physical Evasion +30%, knockback/forced movement immunity (3 turns) | Physical Evasion +30%; forced-movement immunity (3 turns)
- **Catatan Implementasi:** Source Skill ID 1234; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [417] FX 1236 - Iron Colossus
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Transformation 3 turns: DEF +60%, M.DEF +30%, ATK +20%, AGI -25%; attacks gain Metal element | Iron Colossus: DEF +60%, M.DEF +30%, ATK +20%, AGI -25%, Metal element (3 turns)
- **Catatan Implementasi:** Source Skill ID 1236; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [418] PSV 1237 - Sonic Resonance
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sonic Damage +25%; Hit Rate +10%; Silence Resistance +30% | Sonic Damage +25%; Hit Rate +10%; Silence Resistance +30%
- **Catatan Implementasi:** Source Skill ID 1237; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [419] PSV 1240 - Active Echolocation
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Hit Rate +15%; reveals Stealth; Sonic skills ignore 15% Evasion | Hit Rate +15%; reveals Stealth; Sonic skills ignore 15% Evasion
- **Catatan Implementasi:** Source Skill ID 1240; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [420] FX 1242 - Frequency Tuning
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sonic Damage +25%; Skill Accuracy +20% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1242; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [421] FX 1243 - Infrasonic Suppression
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Enemy ATK/M.ATK -15% and Silence Resistance -20% (3 turns)
- **Catatan Implementasi:** Source Skill ID 1243; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [422] FX 1245 - Absolute Vacuum Void
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** a.mat * 7.5 - b.mdf * 0.0 | Sure Hit; creates Vacuum Field for 3 turns: enemy Hit Rate -15% and Sonic damage taken +15%. No extra collapse damage.
- **Catatan Implementasi:** Source Skill ID 1245; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [423] PSV 1246 - Sacred Consecration
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1246; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [424] FX 1249 - Aegis Maxima
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party damage taken -60% for 1 turn | Priority +5; party damage taken -60% for 1 turn. Cooldown 4 turns; can be dispelled.
- **Catatan Implementasi:** Source Skill ID 1249; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [425] FX 1250 - Holy Nova
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party Regen 5% Max HP/turn for 3 turns; Undead/Dark enemies take 4% Max HP damage per turn (Boss cap 2%) | Holy Field (3 turns): heals allies and damages Undead/Dark enemies.
- **Catatan Implementasi:** Source Skill ID 1250; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [426] PSV 1251 - Divine Gift
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1251; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [427] PSV 1252 - Holy Barrier
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1252; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [428] FX 1253 - Sanctified Absolution
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Cleanses up to 5 negative states/debuffs from all allies; Status Resistance +25% for 2 turns | Mass cleanse + temporary status resistance.
- **Catatan Implementasi:** Source Skill ID 1253; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [429] PSV 1255 - Martyr's Faith
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** - | -
- **Catatan Implementasi:** Source Skill ID 1255; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [430] FX 1256 - Celestial Grace
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Party Regen 8% Max HP/turn for 3 turns | Strong party regeneration for 3 turns; does not stack with itself.
- **Catatan Implementasi:** Source Skill ID 1256; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [431] FX 1257 - Resurrection
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Revives 1 fallen ally with 70% Max HP | Revive 1 ally at 70% HP; grants damage taken -20% for 1 turn.
- **Catatan Implementasi:** Source Skill ID 1257; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [432] FX 1258 - Avatar of Light
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Transformation 3 turns: healing +50%, Holy damage +30%, damage taken -30%, Status Resistance +50%; Dark damage taken +25%. | Avatar of Light (3 turns). Afterward: SP -30% and Healing Power -25% for 2 turns.
- **Catatan Implementasi:** Source Skill ID 1258; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [433] PSV 1259 - Covenant of Demon Commanders (Luciferus)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1259; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [434] PSV 1260 - Covenant of Demon Commanders (Mamon)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1260; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [435] PSV 1261 - Covenant of Demon Commanders (Vraka)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1261; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [436] PSV 1262 - Covenant of Demon Commanders (Asmodea)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1262; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [437] PSV 1263 - Covenant of Demon Commanders (Beelzebub)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1263; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [438] PSV 1264 - Covenant of Demon Commanders (Belphegor)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1264; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [439] PSV 1265 - Covenant of Demon Commanders (Leviathanus)
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks this Demon Commander as a selectable contract. Only one Commander may be active at a time. | Unlocks one selectable Demon Commander contract; no direct combat stat bonus.
- **Catatan Implementasi:** Source Skill ID 1265; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [440] FX 1267 - Life Sacrifice
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sacrifice 10% caster Max HP to restore 30% summon Max HP | Sacrifice 10% caster Max HP to heal a summon for 30% of its Max HP
- **Catatan Implementasi:** Source Skill ID 1267; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [441] FX 1268 - Soul Siphon
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Sacrifice one active summon to restore 20% Max MP and gain 1 Soul | Dismisses one summon; restores 20% Max MP and grants 1 Soul
- **Catatan Implementasi:** Source Skill ID 1268; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [442] FX 1270 - Necrotic Mana Corruption
- **Kategori & Durasi:** `Skill Effect State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Consumes 20% current MP; restores 25% Max HP | Converts MP into emergency healing; restores 25% Max HP
- **Catatan Implementasi:** Source Skill ID 1270; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [443] PSV 1275 - Necrotic Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Dark Magic Damage +15%, Max MP +10%, summon costs reduced by 15% | Dark Magic Damage +15%, Max MP +10%, summon costs reduced by 15%; maximum 2 active summons.
- **Catatan Implementasi:** Source Skill ID 1275; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [444] FX 1277 - Bhuta Manifestation: Sanctuary (Dark Priest)
- **Kategori & Durasi:** `Skill Effect State` | `4 – 4 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Heals all allies for a.mat * 0.9 + 20 on summon | Summons one Sanctuary Bhuta for 4 turns; maximum 2 active summons.
- **Catatan Implementasi:** Source Skill ID 1277; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [445] PSV 1280 - Dual Demon Commander Contract
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Unlocks a second Commander contract option; only one Demon Commander may be active at a time. | Can equip two Commander contract options, but only one Commander can be active at a time.
- **Catatan Implementasi:** Source Skill ID 1280; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [446] PSV 1285 - Eagle Eye
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Hit Rate +12% & Critical Rate +4% | Hit Rate +12% & Critical Rate +4%
- **Catatan Implementasi:** Source Skill ID 1285; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [447] PSV 1288 - Swift Reflexes
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Agility +12% & Evasion +8% | Agility +12% & Evasion +8%
- **Catatan Implementasi:** Source Skill ID 1288; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [448] PSV 1293 - Shadow Step
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +12% & Critical Rate +4% | Evasion +12% & Critical Rate +4%
- **Catatan Implementasi:** Source Skill ID 1293; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [449] FX 1296 - Hide
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Shadow State: Evasion +70%, single-target damage taken -30%, 1 turn | Shadow State: Evasion +70%, single-target damage taken -30% (1 turn)
- **Catatan Implementasi:** Source Skill ID 1296; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [450] PSV 1298 - Shadow Reflexes
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Agility +15% | Agility +15%
- **Catatan Implementasi:** Source Skill ID 1298; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [451] FX 1300 - Shadow Lunge
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** a.atk * 2.1 - b.def * 0.3 | Evasion +50% against the next physical attack (1 turn)
- **Catatan Implementasi:** Source Skill ID 1300; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [452] PSV 1304 - Wild Stride
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** AGI +12%, Move/Field Evasion +10% | AGI +12%, Move/Field Evasion +10%
- **Catatan Implementasi:** Source Skill ID 1304; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [453] PSV 1307 - Hunter's Focus
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage +10% vs Marked targets; Crit Rate +8% | Damage +10% vs Marked targets; Crit Rate +8%
- **Catatan Implementasi:** Source Skill ID 1307; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [454] PSV 1311 - Lupine Companion
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Summons Lupine companion for 5 turns; companion damage +10% while target is Marked | Summons Lupine companion for 5 turns; companion damage +10% while target is Marked
- **Catatan Implementasi:** Source Skill ID 1311; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [455] PSV 1314 - Multi-Shot Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Multi-hit skills deal +10% total damage; no per-hit stacking | Multi-hit skills deal +10% total damage; no per-hit stacking
- **Catatan Implementasi:** Source Skill ID 1314; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [456] PSV 1316 - Twin Blade Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Dual-wield damage +10%; Off-hand penalty reduced by 25% | Dual-wield damage +10%; Off-hand penalty reduced by 25%
- **Catatan Implementasi:** Source Skill ID 1316; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [457] FX 1318 - Shadow Meld
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +40% and next single-target physical hit deals +20% damage (2 turns) | Evasion +40%; next single-target physical hit +20% (2 turns)
- **Catatan Implementasi:** Source Skill ID 1318; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [458] PSV 1320 - Sadistic Executioner
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage +15% against targets below 40% HP | Damage +15% against targets below 40% HP
- **Catatan Implementasi:** Source Skill ID 1320; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [459] FX 1321 - Phantom Decoy
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Creates a decoy with 15% Max HP; 50% chance to redirect a single-target attack for 2 turns | Decoy: 15% Max HP; 50% single-target redirect chance (2 turns)
- **Catatan Implementasi:** Source Skill ID 1321; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [460] FX 1323 - Smokescreen
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Enemy Hit Rate -20% for 2 turns
- **Catatan Implementasi:** Source Skill ID 1323; keep exact percentages from Phase 3. *(Engine: Vanilla)*


#### 🔸 [461] PSV 1324 - Shadow Ambush
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** First attack against an unalerted target deals +20% damage and gains +15% Crit Rate | First attack against an unalerted target deals +20% damage and gains +15% Crit Rate
- **Catatan Implementasi:** Source Skill ID 1324; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [462] PSV 1327 - Illusive Demise
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +15%; once per battle, survive a lethal hit at 1 HP | Evasion +15%; once per battle, survive a lethal hit at 1 HP
- **Catatan Implementasi:** Source Skill ID 1327; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [463] PSV 1329 - Marksman Instinct
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** First target hit becomes Marked for 3 turns; damage +8% and Hit Rate +10% vs Marked | First target hit becomes Marked for 3 turns; damage +8% and Hit Rate +10% vs Marked.
- **Catatan Implementasi:** Source Skill ID 1329; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [464] FX 1330 - Focus Energy
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Focus: Crit Rate +20%, Hit Rate +20%, damage +10% for 1 turn | Crit Rate +20%, Hit Rate +20%, damage +10% (1 turn)
- **Catatan Implementasi:** Source Skill ID 1330; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [465] FX 1331 - Nature Concealment
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Concealment: Evasion +60%, cannot be targeted by direct single-target attacks for 1 turn; ends after attacking | Concealment: Evasion +60%, untargetable by direct single-target attacks for 1 turn; ends after attacking
- **Catatan Implementasi:** Source Skill ID 1331; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [466] PSV 1333 - Lupine Ride
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** While riding Lupine: AGI +20%, Evasion +10%, ranged damage +10% | While riding Lupine: AGI +20%, Evasion +10%, ranged damage +10%
- **Catatan Implementasi:** Source Skill ID 1333; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [467] PSV 1335 - Ambush Mastery
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage +10% against targets that have not acted; ignore 15% DEF | Damage +10% against targets that have not acted; ignore 15% DEF.
- **Catatan Implementasi:** Source Skill ID 1335; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [468] PSV 1337 - Cold-Blooded Executioner
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Crit Damage +20%; +8% damage vs targets below 30% HP | Crit Damage +20%; +8% damage vs targets below 30% HP.
- **Catatan Implementasi:** Source Skill ID 1337; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [469] FX 1338 - Enchant Elemental Arrow
- **Kategori & Durasi:** `Skill Effect State` | `3 – 3 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Choose Fire/Ice/Wind/Earth/Lightning/Metal/Sonic; attacks gain chosen element and +10% elemental damage for 3 turns | Elemental Arrow: choose one element; attacks gain that element and +10% elemental damage (3 turns)
- **Catatan Implementasi:** Source Skill ID 1338; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [470] PSV 1340 - Phantom Thread
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +15%; damage from behind +15% | Evasion +15%; damage from behind +15%
- **Catatan Implementasi:** Source Skill ID 1340; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*


#### 🔸 [471] PSV 1341 - Shadow Mark
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Attacks can apply Shadow Mark, max 3 stacks; each stack +4% damage from Assassin; lasts 3 turns | Shadow Mark max 3 stacks; each stack +4% Assassin damage; lasts 3 turns.
- **Catatan Implementasi:** Source Skill ID 1341; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [472] FX 1343 - Shadow Clone
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Creates 1 clone for 2 turns; clone has 30% caster Max HP and deals 35% of caster attack damage | Summons 1 Shadow Clone for 2 turns; clone deals 35% attack damage
- **Catatan Implementasi:** Source Skill ID 1343; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [473] PSV 1344 - Toxic Coating
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Attacks have 30% Poison chance; Poison damage +15% | Attacks have 30% Poison chance; Poison damage +15%.
- **Catatan Implementasi:** Source Skill ID 1344; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [474] FX 1345 - Shadow Cloak
- **Kategori & Durasi:** `Skill Effect State` | `1 – 1 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Evasion +70%, single-target damage taken -30%, duration 1 turn; ends after attacking | Evasion +70%, single-target damage taken -30% (1 turn); ends after attacking
- **Catatan Implementasi:** Source Skill ID 1345; keep exact percentages from Phase 3. *(Engine: COMMON EVENT)*


#### 🔸 [475] PSV 1347 - Phantom Executioner
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Damage +20% vs targets below 35% HP; execution bonus does not affect Bosses | Damage +20% vs targets below 35% HP; execution bonus does not affect Bosses
- **Catatan Implementasi:** Source Skill ID 1347; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [476] FX 1348 - Toxic Smoke Bomb
- **Kategori & Durasi:** `Skill Effect State` | `2 – 2 Giliran` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Poison 55% and Hit Rate -15% to all enemies for 2 turns; user Evasion +15% for 2 turns | Enemy Hit Rate -15% and user Evasion +15% (2 turns).
- **Catatan Implementasi:** Source Skill ID 1348; keep exact percentages from Phase 3. *(Engine: PLUGIN/JS)*


#### 🔸 [477] PSV 1349 - Silent Killer
- **Kategori & Durasi:** `Passive State` | `Permanen (Auto-Passive)` | Prioritas: `50`
- **Efek Mekanik & Modifikator Stat:** Critical Rate +10%; attacks against Silenced targets deal +15% damage | Critical Rate +10%; attacks against Silenced targets deal +15% damage
- **Catatan Implementasi:** Source Skill ID 1349; keep exact percentages from Phase 3. *(Engine: Passive Plugin/Event)*

