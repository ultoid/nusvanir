# ⚔️ Master Database Kelas & Profesi Nusvanir (Turn-Based RPG)

Direktori ini memuat dokumentasi resmi, parameter pertumbuhan 6 Base Stats, perhitungan Stat Turunan (Derived Stats), karakteristik traits, dan daftar skill lengkap untuk seluruh **35 Kelas Petualang** di dunia Nusvanir (Tier 1 hingga Tier 4).

---
## 🧭 Struktur Direktori Kelas
* **[01_Jalur_Fisik/](01_Jalur_Fisik/)**: 11 Kelas Melee, Tank, dan Bela Diri (Fighter, Warrior, Squire, Brawler, Mercenary, Knight, Martial Artist, Champion, Dragoon, Paladin, Monk).
* **[02_Jalur_Sihir/](02_Jalur_Sihir/)**: 17 Kelas Magis, Healer, Elemen, dan Kegelapan (Apprentice, Magician, Acolyte, Occultist, Mage, Cleric, Cultist, Priest, Necromancer, serta 8 Cabang Elementalist).
* **[03_Jalur_Lincah/](03_Jalur_Lincah/)**: 7 Kelas Ranged, Assassin, dan Stealth (Scout, Archer, Thief, Ranger, Rogue, Sniper, Assassin).

---
## 📊 Matriks Daftar Kelas & Pertumbuhan Stat Alami

| Tier | Nama Kelas | Jalur Profesi | Batas Level | Peran Utama | Fixed Stat Growth | Tautan Berkas |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
| **T1** | **Fighter** | Fisik | Lv. 10 | Petarung Pemula | `+2 STR, +1 VIT` | [Fighter](01_Jalur_Fisik/01_Fighter.md) |
| **T1** | **Scout** | Lincah | Lv. 10 | Pengintai Cekatan Pemula | `+1 DEX, +1 AGI, +1 LUK` | [Scout](03_Jalur_Lincah/01_Scout.md) |
| **T1** | **Apprentice** | Sihir | Lv. 10 | Inisiat Sihir Pemula | `+2 INT, +1 DEX` | [Apprentice](02_Jalur_Sihir/01_Apprentice.md) |
| **T2** | **Brawler** | Fisik | Lv. 30 | Dodge / Combo Fighter | `+1 STR, +1 AGI, +1 DEX` | [Brawler](01_Jalur_Fisik/04_Brawler.md) |
| **T2** | **Squire** | Fisik | Lv. 30 | Shield Tank / Protector | `+2 VIT, +1 STR` | [Squire](01_Jalur_Fisik/03_Squire.md) |
| **T2** | **Warrior** | Fisik | Lv. 30 | Bruiser / Offense Frontliner | `+2 STR, +1 VIT` | [Warrior](01_Jalur_Fisik/02_Warrior.md) |
| **T2** | **Archer** | Lincah | Lv. 30 | Precision Ranged Marksman | `+2 DEX, +1 AGI` | [Archer](03_Jalur_Lincah/02_Archer.md) |
| **T2** | **Thief** | Lincah | Lv. 30 | Stealth / Speed / Utility Infiltrator | `+2 AGI, +1 DEX` | [Thief](03_Jalur_Lincah/03_Thief.md) |
| **T2** | **Acolyte** | Sihir | Lv. 30 | Healer / Holy Support | `+2 INT, +1 VIT` | [Acolyte](02_Jalur_Sihir/03_Acolyte.md) |
| **T2** | **Magician** | Sihir | Lv. 30 | General Elemental Caster | `+2 INT, +1 DEX` | [Magician](02_Jalur_Sihir/02_Magician.md) |
| **T2** | **Occultist** | Sihir | Lv. 30 | Dark Caster / Early Summoner | `+2 INT, +1 LUK` | [Occultist](02_Jalur_Sihir/04_Occultist.md) |
| **T3** | **Knight** | Fisik | Lv. 40 | Tank / Counter Protector | `+2 VIT, +1 STR, +1 DEX` | [Knight](01_Jalur_Fisik/06_Knight.md) |
| **T3** | **Martial Artist** | Fisik | Lv. 40 | Dodge / Combo / Chi Striker | `+2 AGI, +1 STR, +1 DEX` | [Martial Artist](01_Jalur_Fisik/07_Martial_Artist.md) |
| **T3** | **Mercenary** | Fisik | Lv. 40 | Aggressive Heavy Bruiser | `+2 STR, +1 VIT, +1 DEX` | [Mercenary](01_Jalur_Fisik/05_Mercenary.md) |
| **T3** | **Ranger** | Lincah | Lv. 40 | Wilderness Survival & Trap Master | `+2 DEX, +1 AGI, +1 VIT` | [Ranger](03_Jalur_Lincah/04_Ranger.md) |
| **T3** | **Rogue** | Lincah | Lv. 40 | Evasive Dual-Blade & Bleed Striker | `+2 AGI, +1 DEX, +1 LUK` | [Rogue](03_Jalur_Lincah/05_Rogue.md) |
| **T3** | **Cleric** | Sihir | Lv. 40 | Healer / Cleanse / Protection | `+2 INT, +1 VIT, +1 LUK` | [Cleric](02_Jalur_Sihir/06_Cleric.md) |
| **T3** | **Cultist** | Sihir | Lv. 40 | Dark Summoner / Soul Sacrifice | `+2 INT, +1 LUK, +1 VIT` | [Cultist](02_Jalur_Sihir/07_Cultist.md) |
| **T3** | **Mage** | Sihir | Lv. 40 | Advanced Elemental Specialist | `+2 INT, +1 DEX, +1 VIT` | [Mage](02_Jalur_Sihir/05_Mage.md) |
| **T4** | **Champion** | Fisik | Lv. 50 | Offensive Juggernaut Tank | `+2 VIT, +2 STR, +1 DEX` | [Champion](01_Jalur_Fisik/08_Champion.md) |
| **T4** | **Dragoon** | Fisik | Lv. 50 | Aerial Lancer / Boss Killer | `+2 STR, +2 AGI, +1 DEX` | [Dragoon](01_Jalur_Fisik/09_Dragoon.md) |
| **T4** | **Monk** | Fisik | Lv. 50 | Evasion / Chi Burst Master | `+2 AGI, +1 STR, +1 INT, +1 DEX` | [Monk](01_Jalur_Fisik/11_Monk.md) |
| **T4** | **Paladin** | Fisik | Lv. 50 | Holy Defensive Protector | `+2 VIT, +1 STR, +1 INT, +1 DEX` | [Paladin](01_Jalur_Fisik/10_Paladin.md) |
| **T4** | **Assassin** | Lincah | Lv. 50 | Lethal Poison & Shadow Executioner | `+2 AGI, +2 DEX, +1 LUK` | [Assassin](03_Jalur_Lincah/07_Assassin.md) |
| **T4** | **Sniper** | Lincah | Lv. 50 | Extreme Range Precision Executioner | `+3 DEX, +1 AGI, +1 LUK` | [Sniper](03_Jalur_Lincah/06_Sniper.md) |
| **T4** | **Elementalist - Aeromancer** | Sihir | Lv. 50 | Wind Evasion & Swift Caster | `+3 INT, +2 AGI` | [Elementalist - Aeromancer](02_Jalur_Sihir/13_Elementalist_Aeromancer.md) |
| **T4** | **Elementalist - Cryomancer** | Sihir | Lv. 50 | Ice Control & Freeze Specialist | `+3 INT, +1 VIT, +1 DEX` | [Elementalist - Cryomancer](02_Jalur_Sihir/15_Elementalist_Cryomancer.md) |
| **T4** | **Elementalist - Echomancer** | Sihir | Lv. 50 | Sonic Vibration & Disruption Utility | `+3 INT, +1 DEX, +1 AGI` | [Elementalist - Echomancer](02_Jalur_Sihir/17_Elementalist_Echomancer.md) |
| **T4** | **Elementalist - Electromancer** | Sihir | Lv. 50 | Lightning Burst & Voltage Stack | `+3 INT, +1 AGI, +1 DEX` | [Elementalist - Electromancer](02_Jalur_Sihir/14_Elementalist_Electromancer.md) |
| **T4** | **Elementalist - Ferromancer** | Sihir | Lv. 50 | Metal Shard & Armored Battle Caster | `+2 INT, +2 VIT, +1 STR` | [Elementalist - Ferromancer](02_Jalur_Sihir/16_Elementalist_Ferromancer.md) |
| **T4** | **Elementalist - Geomancer** | Sihir | Lv. 50 | Earth Barrier & Control Caster | `+2 INT, +2 VIT, +1 STR` | [Elementalist - Geomancer](02_Jalur_Sihir/12_Elementalist_Geomancer.md) |
| **T4** | **Elementalist - Hydromancer** | Sihir | Lv. 50 | Water Control & Sustain Caster | `+3 INT, +1 VIT, +1 DEX` | [Elementalist - Hydromancer](02_Jalur_Sihir/11_Elementalist_Hydromancer.md) |
| **T4** | **Elementalist - Pyromancer** | Sihir | Lv. 50 | Fire Burst & Burn Specialist | `+3 INT, +1 DEX, +1 VIT` | [Elementalist - Pyromancer](02_Jalur_Sihir/10_Elementalist_Pyromancer.md) |
| **T4** | **Necromancer** | Sihir | Lv. 50 | Undead Overlord / Dark Resource | `+2 INT, +2 LUK, +1 VIT` | [Necromancer](02_Jalur_Sihir/09_Necromancer.md) |
| **T4** | **Priest** | Sihir | Lv. 50 | Endgame Healer / Holy Vanguard | `+2 INT, +2 VIT, +1 LUK` | [Priest](02_Jalur_Sihir/08_Priest.md) |