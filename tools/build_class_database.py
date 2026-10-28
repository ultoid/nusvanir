"""
Script otomatis untuk menyusun database Class Nusvanir menggunakan sistem Turn-Based RPG:
- 6 Base Stats (STR, INT, DEX, LUK, AGI, VIT)
- Stat Turunan (Derived Stats): Max HP, Max MP, Max SP, ATK, DEF, MAT, MDF, Action Speed, HIT, EVA, CRI, CEV, CDMG, GRD, HRG, MRG, TRG
- Fixed Stat Growth per Class Level
- Database Skill Lengkap dari Excel (NUSV-SKILL & MV SKILLS)
"""

import os
import openpyxl

EXCEL_PATH = r"e:\Ananto\Emulatoid\Nusvanir\Database\NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx"
OUTPUT_DIR = r"e:\Ananto\Emulatoid\Nusvanir\06_Sistem Game & Ekonomi\Class"

CLASS_BRANCH_MAP = {
    # Jalur Fisik
    'Fighter': ('01_Jalur_Fisik', '01_Fighter.md', 'Jalur Fisik (Melee / Tank)', 1, 10, '—', 'Warrior, Squire, Brawler', 'Petarung Pemula', False),
    'Warrior': ('01_Jalur_Fisik', '02_Warrior.md', 'Jalur Fisik (Melee / Tank)', 2, 30, 'Fighter', 'Mercenary', 'Bruiser / Offense Frontliner', False),
    'Squire': ('01_Jalur_Fisik', '03_Squire.md', 'Jalur Fisik (Melee / Tank)', 2, 30, 'Fighter', 'Knight', 'Shield Tank / Protector', False),
    'Brawler': ('01_Jalur_Fisik', '04_Brawler.md', 'Jalur Fisik (Melee / Tank)', 2, 30, 'Fighter', 'Martial Artist', 'Dodge / Combo Fighter', False),
    'Mercenary': ('01_Jalur_Fisik', '05_Mercenary.md', 'Jalur Fisik (Melee / Tank)', 3, 40, 'Warrior', 'Dragoon', 'Aggressive Heavy Bruiser', False),
    'Knight': ('01_Jalur_Fisik', '06_Knight.md', 'Jalur Fisik (Melee / Tank)', 3, 40, 'Squire', 'Champion, Paladin', 'Tank / Counter Protector', False),
    'Martial Artist': ('01_Jalur_Fisik', '07_Martial_Artist.md', 'Jalur Fisik (Melee / Tank)', 3, 40, 'Brawler', 'Monk', 'Dodge / Combo / Chi Striker', False),
    'Champion': ('01_Jalur_Fisik', '08_Champion.md', 'Jalur Fisik (Melee / Tank)', 4, 50, 'Knight', 'Holy Knight / Berserker (Tier 5)', 'Offensive Juggernaut Tank', False),
    'Dragoon': ('01_Jalur_Fisik', '09_Dragoon.md', 'Jalur Fisik (Melee / Tank)', 4, 50, 'Mercenary', 'Sky Sovereign (Tier 5)', 'Aerial Lancer / Boss Killer', False),
    'Paladin': ('01_Jalur_Fisik', '10_Paladin.md', 'Jalur Fisik (Melee / Tank)', 4, 50, 'Knight', 'Holy Knight (Tier 5)', 'Holy Defensive Protector', False),
    'Monk': ('01_Jalur_Fisik', '11_Monk.md', 'Jalur Fisik (Melee / Tank)', 4, 50, 'Martial Artist', 'Brahma-Kera (Tier 5)', 'Evasion / Chi Burst Master', False),

    # Jalur Sihir
    'Apprentice': ('02_Jalur_Sihir', '01_Apprentice.md', 'Jalur Sihir (Magic / Support)', 1, 10, '—', 'Magician, Acolyte, Occultist', 'Inisiat Sihir Pemula', False),
    'Magician': ('02_Jalur_Sihir', '02_Magician.md', 'Jalur Sihir (Magic / Support)', 2, 30, 'Apprentice', 'Mage', 'General Elemental Caster', False),
    'Acolyte': ('02_Jalur_Sihir', '03_Acolyte.md', 'Jalur Sihir (Magic / Support)', 2, 30, 'Apprentice', 'Cleric', 'Healer / Holy Support', False),
    'Occultist': ('02_Jalur_Sihir', '04_Occultist.md', 'Jalur Sihir (Magic / Support)', 2, 30, 'Apprentice', 'Cultist', 'Dark Caster / Early Summoner', False),
    'Mage': ('02_Jalur_Sihir', '05_Mage.md', 'Jalur Sihir (Magic / Support)', 3, 40, 'Magician', 'Elementalist (8 Cabang)', 'Advanced Elemental Specialist', False),
    'Cleric': ('02_Jalur_Sihir', '06_Cleric.md', 'Jalur Sihir (Magic / Support)', 3, 40, 'Acolyte', 'Priest', 'Healer / Cleanse / Protection', False),
    'Cultist': ('02_Jalur_Sihir', '07_Cultist.md', 'Jalur Sihir (Magic / Support)', 3, 40, 'Occultist', 'Necromancer', 'Dark Summoner / Soul Sacrifice', False),
    'Priest': ('02_Jalur_Sihir', '08_Priest.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Cleric', 'High Priest (Tier 5)', 'Endgame Healer / Holy Vanguard', False),
    'Necromancer': ('02_Jalur_Sihir', '09_Necromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Cultist', 'Warlock / Death Knight (Tier 5)', 'Undead Overlord / Dark Resource', False),
    'Elementalist - Pyromancer': ('02_Jalur_Sihir', '10_Elementalist_Pyromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Fire Burst & Burn Specialist', False),
    'Elementalist - Hydromancer': ('02_Jalur_Sihir', '11_Elementalist_Hydromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Water Control & Sustain Caster', False),
    'Elementalist - Geomancer': ('02_Jalur_Sihir', '12_Elementalist_Geomancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage / Shaman (Tier 5)', 'Earth Barrier & Control Caster', False),
    'Elementalist - Aeromancer': ('02_Jalur_Sihir', '13_Elementalist_Aeromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Wind Evasion & Swift Caster', False),
    'Elementalist - Electromancer': ('02_Jalur_Sihir', '14_Elementalist_Electromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Lightning Burst & Voltage Stack', False),
    'Elementalist - Cryomancer': ('02_Jalur_Sihir', '15_Elementalist_Cryomancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Ice Control & Freeze Specialist', False),
    'Elementalist - Ferromancer': ('02_Jalur_Sihir', '16_Elementalist_Ferromancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Metal Shard & Armored Battle Caster', False),
    'Elementalist - Echomancer': ('02_Jalur_Sihir', '17_Elementalist_Echomancer.md', 'Jalur Sihir (Magic / Support)', 4, 50, 'Mage', 'Archmage (Tier 5)', 'Sonic Vibration & Disruption Utility', False),

    # Jalur Lincah
    'Scout': ('03_Jalur_Lincah', '01_Scout.md', 'Jalur Lincah (Ranged / Assassin)', 1, 10, '—', 'Archer, Thief', 'Pengintai Cekatan Pemula', True),
    'Archer': ('03_Jalur_Lincah', '02_Archer.md', 'Jalur Lincah (Ranged / Assassin)', 2, 30, 'Scout', 'Ranger', 'Precision Ranged Marksman', True),
    'Thief': ('03_Jalur_Lincah', '03_Thief.md', 'Jalur Lincah (Ranged / Assassin)', 2, 30, 'Scout', 'Rogue', 'Stealth / Speed / Utility Infiltrator', True),
    'Ranger': ('03_Jalur_Lincah', '04_Ranger.md', 'Jalur Lincah (Ranged / Assassin)', 3, 40, 'Archer', 'Sniper', 'Wilderness Survival & Trap Master', True),
    'Rogue': ('03_Jalur_Lincah', '05_Rogue.md', 'Jalur Lincah (Ranged / Assassin)', 3, 40, 'Thief', 'Assassin', 'Evasive Dual-Blade & Bleed Striker', True),
    'Sniper': ('03_Jalur_Lincah', '06_Sniper.md', 'Jalur Lincah (Ranged / Assassin)', 4, 50, 'Ranger', 'Windrunner (Tier 5)', 'Extreme Range Precision Executioner', True),
    'Assassin': ('03_Jalur_Lincah', '07_Assassin.md', 'Jalur Lincah (Ranged / Assassin)', 4, 50, 'Rogue', 'Shadow Walker (Tier 5)', 'Lethal Poison & Shadow Executioner', True)
}

CLASS_BASE_STATS = {
    # T1
    'Fighter': {'str': 9, 'int': 1, 'dex': 3, 'luk': 4, 'agi': 4, 'vit': 7, 'growth': '+2 STR, +1 VIT', 'ranks': 'STR: A | INT: E | DEX: C | LUK: C | AGI: C | VIT: B'},
    'Apprentice': {'str': 1, 'int': 9, 'dex': 5, 'luk': 4, 'agi': 3, 'vit': 3, 'growth': '+2 INT, +1 DEX', 'ranks': 'STR: E | INT: A | DEX: B | LUK: C | AGI: C | VIT: D'},
    'Scout': {'str': 3, 'int': 1, 'dex': 8, 'luk': 5, 'agi': 8, 'vit': 3, 'growth': '+1 DEX, +1 AGI, +1 LUK', 'ranks': 'STR: D | INT: E | DEX: A | LUK: B | AGI: A | VIT: D'},

    # T2 Fisik
    'Warrior': {'str': 18, 'int': 2, 'dex': 7, 'luk': 5, 'agi': 8, 'vit': 12, 'growth': '+2 STR, +1 VIT', 'ranks': 'STR: A+ | INT: E | DEX: C | LUK: C | AGI: C | VIT: B+'},
    'Squire': {'str': 10, 'int': 2, 'dex': 5, 'luk': 5, 'agi': 5, 'vit': 20, 'growth': '+2 VIT, +1 STR', 'ranks': 'STR: B | INT: E | DEX: C | LUK: C | AGI: D | VIT: A+'},
    'Brawler': {'str': 14, 'int': 2, 'dex': 8, 'luk': 6, 'agi': 14, 'vit': 8, 'growth': '+1 STR, +1 AGI, +1 DEX', 'ranks': 'STR: A | INT: E | DEX: B | LUK: C | AGI: A | VIT: C'},

    # T2 Sihir
    'Magician': {'str': 2, 'int': 18, 'dex': 10, 'luk': 6, 'agi': 6, 'vit': 5, 'growth': '+2 INT, +1 DEX', 'ranks': 'STR: E | INT: A | DEX: B | LUK: C | AGI: C | VIT: D'},
    'Acolyte': {'str': 3, 'int': 16, 'dex': 6, 'luk': 7, 'agi': 5, 'vit': 10, 'growth': '+2 INT, +1 VIT', 'ranks': 'STR: E | INT: A | DEX: C | LUK: B | AGI: C | VIT: C'},
    'Occultist': {'str': 2, 'int': 17, 'dex': 7, 'luk': 11, 'agi': 5, 'vit': 6, 'growth': '+2 INT, +1 LUK', 'ranks': 'STR: E | INT: A | DEX: C | LUK: A | AGI: C | VIT: D'},

    # T2 Lincah
    'Archer': {'str': 6, 'int': 2, 'dex': 16, 'luk': 7, 'agi': 12, 'vit': 6, 'growth': '+2 DEX, +1 AGI', 'ranks': 'STR: C | INT: E | DEX: A | LUK: B | AGI: B | VIT: D'},
    'Thief': {'str': 6, 'int': 2, 'dex': 12, 'luk': 10, 'agi': 16, 'vit': 5, 'growth': '+2 AGI, +1 DEX', 'ranks': 'STR: C | INT: E | DEX: B | LUK: A | AGI: A | VIT: D'},

    # T3 Fisik
    'Mercenary': {'str': 34, 'int': 3, 'dex': 14, 'luk': 8, 'agi': 14, 'vit': 22, 'growth': '+2 STR, +1 VIT, +1 DEX', 'ranks': 'STR: S | INT: E | DEX: B | LUK: C | AGI: B | VIT: A'},
    'Knight': {'str': 20, 'int': 4, 'dex': 12, 'luk': 8, 'agi': 10, 'vit': 38, 'growth': '+2 VIT, +1 STR, +1 DEX', 'ranks': 'STR: A | INT: E | DEX: B | LUK: C | AGI: C | VIT: S'},
    'Martial Artist': {'str': 26, 'int': 5, 'dex': 18, 'luk': 10, 'agi': 28, 'vit': 16, 'growth': '+2 AGI, +1 STR, +1 DEX', 'ranks': 'STR: A | INT: E | DEX: A | LUK: B | AGI: S | VIT: B'},

    # T3 Sihir
    'Mage': {'str': 4, 'int': 36, 'dex': 18, 'luk': 10, 'agi': 12, 'vit': 12, 'growth': '+2 INT, +1 DEX, +1 VIT', 'ranks': 'STR: E | INT: S | DEX: A | LUK: B | AGI: C | VIT: C'},
    'Cleric': {'str': 6, 'int': 32, 'dex': 12, 'luk': 12, 'agi': 10, 'vit': 22, 'growth': '+2 INT, +1 VIT, +1 LUK', 'ranks': 'STR: D | INT: S | DEX: B | LUK: B | AGI: C | VIT: A'},
    'Cultist': {'str': 4, 'int': 34, 'dex': 14, 'luk': 20, 'agi': 10, 'vit': 14, 'growth': '+2 INT, +1 LUK, +1 VIT', 'ranks': 'STR: E | INT: S | DEX: B | LUK: S | AGI: C | VIT: C'},

    # T3 Lincah
    'Ranger': {'str': 12, 'int': 4, 'dex': 34, 'luk': 12, 'agi': 24, 'vit': 14, 'growth': '+2 DEX, +1 AGI, +1 VIT', 'ranks': 'STR: C | INT: E | DEX: S | LUK: B | AGI: A | VIT: C'},
    'Rogue': {'str': 12, 'int': 4, 'dex': 24, 'luk': 18, 'agi': 32, 'vit': 10, 'growth': '+2 AGI, +1 DEX, +1 LUK', 'ranks': 'STR: C | INT: E | DEX: A | LUK: A | AGI: S | VIT: D'},

    # T4 Fisik
    'Champion': {'str': 52, 'int': 5, 'dex': 20, 'luk': 12, 'agi': 18, 'vit': 50, 'growth': '+2 VIT, +2 STR, +1 DEX', 'ranks': 'STR: S | INT: E | DEX: A | LUK: B | AGI: B | VIT: S'},
    'Dragoon': {'str': 56, 'int': 6, 'dex': 22, 'luk': 12, 'agi': 36, 'vit': 30, 'growth': '+2 STR, +2 AGI, +1 DEX', 'ranks': 'STR: S | INT: E | DEX: A | LUK: B | AGI: S | VIT: A'},
    'Paladin': {'str': 38, 'int': 18, 'dex': 18, 'luk': 12, 'agi': 16, 'vit': 55, 'growth': '+2 VIT, +1 STR, +1 INT, +1 DEX', 'ranks': 'STR: A | INT: C | DEX: B | LUK: B | AGI: C | VIT: S+'},
    'Monk': {'str': 45, 'int': 14, 'dex': 24, 'luk': 15, 'agi': 45, 'vit': 28, 'growth': '+2 AGI, +1 STR, +1 INT, +1 DEX', 'ranks': 'STR: S | INT: C | DEX: A | LUK: B | AGI: S+ | VIT: A'},

    # T4 Sihir
    'Priest': {'str': 10, 'int': 52, 'dex': 20, 'luk': 18, 'agi': 18, 'vit': 40, 'growth': '+2 INT, +2 VIT, +1 LUK', 'ranks': 'STR: D | INT: S+ | DEX: A | LUK: A | AGI: B | VIT: S'},
    'Necromancer': {'str': 8, 'int': 56, 'dex': 22, 'luk': 32, 'agi': 16, 'vit': 24, 'growth': '+2 INT, +2 LUK, +1 VIT', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: S+ | AGI: C | VIT: B'},
    'Elementalist - Pyromancer': {'str': 8, 'int': 60, 'dex': 25, 'luk': 15, 'agi': 22, 'vit': 25, 'growth': '+3 INT, +1 DEX, +1 VIT', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: B | AGI: B | VIT: B'},
    'Elementalist - Hydromancer': {'str': 8, 'int': 56, 'dex': 22, 'luk': 16, 'agi': 20, 'vit': 32, 'growth': '+3 INT, +1 VIT, +1 DEX', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: B | AGI: B | VIT: A'},
    'Elementalist - Geomancer': {'str': 14, 'int': 54, 'dex': 18, 'luk': 14, 'agi': 16, 'vit': 42, 'growth': '+2 INT, +2 VIT, +1 STR', 'ranks': 'STR: C | INT: S+ | DEX: B | LUK: B | AGI: C | VIT: S'},
    'Elementalist - Aeromancer': {'str': 8, 'int': 56, 'dex': 25, 'luk': 16, 'agi': 36, 'vit': 20, 'growth': '+3 INT, +2 AGI', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: B | AGI: S | VIT: C'},
    'Elementalist - Electromancer': {'str': 8, 'int': 62, 'dex': 26, 'luk': 18, 'agi': 28, 'vit': 18, 'growth': '+3 INT, +1 AGI, +1 DEX', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: A | AGI: A | VIT: C'},
    'Elementalist - Cryomancer': {'str': 8, 'int': 56, 'dex': 22, 'luk': 16, 'agi': 20, 'vit': 32, 'growth': '+3 INT, +1 VIT, +1 DEX', 'ranks': 'STR: E | INT: S+ | DEX: A | LUK: B | AGI: B | VIT: A'},
    'Elementalist - Ferromancer': {'str': 18, 'int': 52, 'dex': 20, 'luk': 14, 'agi': 16, 'vit': 40, 'growth': '+2 INT, +2 VIT, +1 STR', 'ranks': 'STR: B | INT: S | DEX: B | LUK: B | AGI: C | VIT: S'},
    'Elementalist - Echomancer': {'str': 8, 'int': 58, 'dex': 28, 'luk': 18, 'agi': 26, 'vit': 22, 'growth': '+3 INT, +1 DEX, +1 AGI', 'ranks': 'STR: E | INT: S+ | DEX: A+ | LUK: A | AGI: A | VIT: B'},

    # T4 Lincah
    'Sniper': {'str': 18, 'int': 6, 'dex': 64, 'luk': 20, 'agi': 35, 'vit': 20, 'growth': '+3 DEX, +1 AGI, +1 LUK', 'ranks': 'STR: C | INT: E | DEX: S+ | LUK: A | AGI: A | VIT: C'},
    'Assassin': {'str': 20, 'int': 6, 'dex': 40, 'luk': 32, 'agi': 52, 'vit': 16, 'growth': '+2 AGI, +2 DEX, +1 LUK', 'ranks': 'STR: B | INT: E | DEX: S | LUK: S | AGI: S+ | VIT: C'}
}

T1_SKILLS_DATA = {
    'Fighter': [
        {'lvl': 1, 'name': 'Dash', 'type': 'Physical', 'cost': '10 SP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Manuver lari cepat untuk menutup celah atau mengatur posisi bertarung.'},
        {'lvl': 1, 'name': 'Charge Attack', 'type': 'Physical', 'cost': '15 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.3 - b.def * 0.4)', 'desc': 'Tebasan keras terarah yang memanfaatkan bobot tubuh.'},
        {'lvl': 1, 'name': 'Weapon Mastery', 'type': 'Passive', 'cost': '0 SP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Keahlian bawaan yang meningkatkan Physical Attack secara permanen.'},
        {'lvl': 1, 'name': 'Vitality Mastery', 'type': 'Passive', 'cost': '0 SP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Keahlian ketahanan tubuh yang meningkatkan P.DEF dan M.DEF.'},
        {'lvl': 3, 'name': 'Cyclone Sweep', 'type': 'Physical', 'cost': '25 SP', 'scope': 'All Enemies', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.1 - b.def * 0.3)', 'desc': 'Ayunan senjata memutar yang melukai seluruh musuh di sekitar.'},
        {'lvl': 5, 'name': 'Fatal Blow', 'type': 'Physical', 'cost': '20 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.6 - b.def * 0.35) (Crit Rate +20%)', 'desc': 'Hantaman presisi pada titik lemah target dengan peluang kritikal tinggi.'},
        {'lvl': 7, 'name': 'Impact Wave', 'type': 'Physical', 'cost': '30 SP', 'scope': '1 Target', 'elem': 'Earth', 'formula': 'Math.max(0, a.atk * 1.4 + a.vit * 0.5 - b.def * 0.3)', 'desc': 'Menghantamkan senjata ke tanah untuk melepaskan gelombang kejut.'},
        {'lvl': 9, 'name': 'Provoke', 'type': 'Support', 'cost': '15 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': '-', 'desc': 'Meneriakkan tantangan untuk menarik target rate (TGR) musuh ke diri sendiri.'}
    ],
    'Apprentice': [
        {'lvl': 1, 'name': 'Heal', 'type': 'White Magic', 'cost': '12 MP', 'scope': '1 Ally', 'elem': 'Holy', 'formula': 'Math.max(0, a.mat * 2.0 + a.int * 1.5)', 'desc': 'Menyalurkan energi spiritual untuk memulihkan luka diri atau sekutu.'},
        {'lvl': 1, 'name': 'Fireball', 'type': 'Black Magic', 'cost': '10 MP', 'scope': '1 Target', 'elem': 'Fire', 'formula': 'Math.max(0, a.mat * 1.4 - b.mdf * 0.4)', 'desc': 'Melontarkan gumpalan api magis ke arah musuh (Peluang Burn 20%).'},
        {'lvl': 1, 'name': 'Spell Mastery', 'type': 'Passive', 'cost': '0 MP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Pemahaman pola mantra dasar yang meningkatkan MP Regen (MRG).'},
        {'lvl': 1, 'name': 'Elemental Mastery', 'type': 'Passive', 'cost': '0 MP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Meningkatkan kapasitas Max MP dan efektivitas mantra elemen.'},
        {'lvl': 3, 'name': 'Aqua Blast', 'type': 'Black Magic', 'cost': '14 MP', 'scope': 'All Enemies', 'elem': 'Water', 'formula': 'Math.max(0, a.mat * 1.15 - b.mdf * 0.35)', 'desc': 'Gelombang air melingkar yang menekan posisi musuh.'},
        {'lvl': 5, 'name': 'Fire Bolt', 'type': 'Black Magic', 'cost': '18 MP', 'scope': '1 Target', 'elem': 'Fire', 'formula': 'Math.max(0, a.mat * 1.8 - b.mdf * 0.4)', 'desc': 'Tombak api pekat dengan daya tembus tinggi pada target tunggal.'},
        {'lvl': 7, 'name': 'Sonic Boom', 'type': 'Black Magic', 'cost': '16 MP', 'scope': '1 Target', 'elem': 'Sound', 'formula': 'Math.max(0, a.mat * 1.3 - b.mdf * 0.3)', 'desc': 'Gelombang kejut frekuensi tinggi yang dapat menyebabkan Paralyze (20%).'},
        {'lvl': 9, 'name': 'Holy Veil', 'type': 'White Magic / Support', 'cost': '25 MP', 'scope': 'Self', 'elem': 'Holy', 'formula': '-', 'desc': 'Menciptakan perisai cahaya suci penahan serangan lawan.'}
    ],
    'Scout': [
        {'lvl': 1, 'name': 'Quick Shot', 'type': 'Physical', 'cost': '4 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.15 - b.def * 0.5) (Priority +2)', 'desc': 'Tembakan kilat yang dilepas dengan kecepatan tinggi sebelum musuh bertindak.'},
        {'lvl': 1, 'name': 'Hunter\'s Mark', 'type': 'Support', 'cost': '6 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': '-', 'desc': 'Menandai target untuk meningkatkan akurasi dan damage serangan berikutnya.'},
        {'lvl': 3, 'name': 'Eagle Eye', 'type': 'Passive', 'cost': '0 SP', 'scope': 'Self', 'elem': 'Neutral', 'formula': '-', 'desc': 'Pandangan tajam penjelajah yang meningkatkan HIT dan CRI secara permanen.'},
        {'lvl': 5, 'name': 'Piercing Arrow', 'type': 'Physical', 'cost': '8 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.4 - b.def * 0.25)', 'desc': 'Anak panah berhulu runcing yang mengabaikan sebagian pertahanan armor lawan.'},
        {'lvl': 7, 'name': 'Scatter Shot', 'type': 'Physical', 'cost': '12 SP', 'scope': '3 Random Enemies', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 0.85 - b.def * 0.2) per hit', 'desc': 'Melepaskan beberapa anak panah sekaligus ke arah sekelompok musuh.'},
        {'lvl': 9, 'name': 'Poison Arrow', 'type': 'Physical', 'cost': '10 SP', 'scope': '1 Target', 'elem': 'Neutral', 'formula': 'Math.max(0, a.atk * 1.2 - b.def * 0.4) (Poison 50%)', 'desc': 'Panah berlumur racun hutan yang menimbulkan kerusakan berulang tiap giliran.'}
    ]
}

def calculate_derived_stats(p, is_ranged=False):
    s = p['str']
    i = p['int']
    d = p['dex']
    l = p['luk']
    a = p['agi']
    v = p['vit']

    # Derived Stats Formulas
    hp = 50 + (v * 15) + (s * 5)
    mp = 20 + (i * 8)
    sp = 20 + (v * 5) + (s * 2)

    if is_ranged:
        atk = (d * 2) + (s * 0.5)
    else:
        atk = (s * 2) + (d * 0.5)

    df = (v * 1.5) + (s * 0.5)
    mat = (i * 2)
    mdf = (i * 1.2) + (v * 0.8)
    spd = (a * 1.5)

    hit = min(1.0, 0.85 + (d * 0.002))
    eva = min(0.8, 0.02 + (a * 0.002) + (l * 0.0005))
    cri = min(0.85, 0.03 + (d * 0.002) + (l * 0.001))
    cev = (l * 0.0015) + (v * 0.001)
    cdmg = 1.5 + (s * 0.003) + (d * 0.002)
    grd = 1.0 + (v * 0.005)
    hrg = v * 0.0003
    mrg = i * 0.0003
    trg = 0.03 + (a * 0.0004) + (v * 0.0002)

    return {
        'hp': int(round(hp)),
        'mp': int(round(mp)),
        'sp': int(round(sp)),
        'atk': int(round(atk)),
        'def': int(round(df)),
        'mat': int(round(mat)),
        'mdf': int(round(mdf)),
        'spd': int(round(spd)),
        'hit': hit * 100.0,
        'eva': eva * 100.0,
        'cri': cri * 100.0,
        'cev': cev * 100.0,
        'cdmg': cdmg * 100.0,
        'grd': grd * 100.0,
        'hrg': hrg * 100.0,
        'mrg': mrg * 100.0,
        'trg': trg * 100.0
    }

def load_data():
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    
    # CLASS TRAIT SUMMARY
    ws_summary = wb['CLASS TRAIT SUMMARY']
    summary_dict = {}
    for r in range(2, ws_summary.max_row + 1):
        cname = ws_summary.cell(r, 3).value
        if cname:
            cname_str = str(cname).strip()
            summary_dict[cname_str] = {
                'id': int(ws_summary.cell(r, 1).value or 0),
                'tier': int(ws_summary.cell(r, 2).value or 2),
                'promotion_from': str(ws_summary.cell(r, 4).value or '—').strip(),
                'primary_role': str(ws_summary.cell(r, 5).value or '').strip(),
                'innate_trait': str(ws_summary.cell(r, 6).value or '').strip(),
                'chassis': str(ws_summary.cell(r, 7).value or '').strip(),
                'xs_param': str(ws_summary.cell(r, 8).value or '').strip(),
                'skill_types': str(ws_summary.cell(r, 9).value or '').strip(),
                'equip': str(ws_summary.cell(r, 10).value or '').strip(),
                'weakness': str(ws_summary.cell(r, 11).value or '').strip()
            }

    # NUSV-CLASS TRAIT
    ws_nusv = wb['NUSV-CLASS TRAIT']
    nusv_dict = {}
    curr_c = None
    for r in range(3, ws_nusv.max_row + 1):
        cname = ws_nusv.cell(r, 1).value
        if cname:
            curr_c = str(cname).strip()
            nusv_dict[curr_c] = {
                'exp_curve': str(ws_nusv.cell(r, 2).value or '').strip(),
                'param_ranks': str(ws_nusv.cell(r, 3).value or '').strip(),
                'desc': str(ws_nusv.cell(r, 9).value or '').strip(),
                'weapons': [],
                'armors': [],
                'param_traits': []
            }
        if curr_c:
            cat = str(ws_nusv.cell(r, 5).value or '').strip()
            ttype = str(ws_nusv.cell(r, 6).value or '').strip()
            target = str(ws_nusv.cell(r, 7).value or '').strip()
            val = ws_nusv.cell(r, 8).value
            if cat == 'Equip':
                if 'Weapon' in ttype and target:
                    nusv_dict[curr_c]['weapons'].append(target)
                elif 'Armor' in ttype and target:
                    nusv_dict[curr_c]['armors'].append(target)
            elif cat == 'Param' and target:
                nusv_dict[curr_c]['param_traits'].append(f"{target}: {val if val is not None else ''}")

    # MV SKILLS
    ws_skills = wb['MV SKILLS']
    skills_by_class = {}
    for r in range(2, ws_skills.max_row + 1):
        cname = ws_skills.cell(r, 5).value
        sname = ws_skills.cell(r, 7).value
        if cname and sname:
            cname_str = str(cname).strip()
            if cname_str not in skills_by_class:
                skills_by_class[cname_str] = []
            
            mp = ws_skills.cell(r, 11).value or 0
            tp = ws_skills.cell(r, 12).value or 0
            mp_val = int(mp) if isinstance(mp, (int, float)) else str(mp)
            sp_val = int(tp) if isinstance(tp, (int, float)) else str(tp)
            
            cost_parts = []
            if mp_val and mp_val != 0: cost_parts.append(f"{mp_val} MP")
            if sp_val and sp_val != 0: cost_parts.append(f"{sp_val} SP")
            cost_str = " / ".join(cost_parts) if cost_parts else "0 SP"

            skills_by_class[cname_str].append({
                'skill_id': int(ws_skills.cell(r, 1).value or 0),
                'lvl': ws_skills.cell(r, 6).value,
                'name': str(sname).strip(),
                'design_type': str(ws_skills.cell(r, 8).value or 'Skill').strip(),
                'skill_type': str(ws_skills.cell(r, 10).value or 'Physical').strip(),
                'cost': cost_str,
                'scope': str(ws_skills.cell(r, 15).value or 'One Enemy').strip(),
                'damage_type': str(ws_skills.cell(r, 17).value or 'HP Damage').strip(),
                'hit_type': str(ws_skills.cell(r, 19).value or 'Physical Attack').strip(),
                'element': str(ws_skills.cell(r, 20).value or 'Neutral').strip(),
                'formula': str(ws_skills.cell(r, 21).value or '-').strip(),
                'effects': str(ws_skills.cell(r, 29).value or '').strip(),
                'desc': str(ws_skills.cell(r, 35).value or '').strip()
            })

    return summary_dict, nusv_dict, skills_by_class

def generate_class_md(cname, summary_dict, nusv_dict, skills_by_class):
    binfo = CLASS_BRANCH_MAP[cname]
    subfolder, fname, branch, tier, lvl_cap, prom_from, prom_to, role_desc, is_ranged = binfo
    
    # Summary info
    sinfo = summary_dict.get(cname, {})
    cid = sinfo.get('id', tier * 10)
    p_from = sinfo.get('promotion_from', prom_from)
    role = sinfo.get('primary_role', role_desc)
    innate_trait = sinfo.get('innate_trait', '—')
    skill_types = sinfo.get('skill_types', 'Physical, Support, Passive' if 'Fisik' in branch else 'Magic, Support, Passive')
    equip_archetype = sinfo.get('equip', '—')
    weakness = sinfo.get('weakness', 'Standar kelemahan arketipe')

    # NUSV info
    ninfo = nusv_dict.get(cname, {})
    exp_curve = ninfo.get('exp_curve', f'Tier {tier}')
    lore_desc = ninfo.get('desc', f'Profesi petualang tingkat {tier} di dunia Nusvanir.')
    weapons_list = ninfo.get('weapons', [])
    armors_list = ninfo.get('armors', [])
    
    weapons_str = ", ".join(weapons_list) if weapons_list else equip_archetype
    armors_str = ", ".join(armors_list) if armors_list else "Light Armor / Clothing"

    # Base Stats & Derived calculation
    p_stat = CLASS_BASE_STATS.get(cname, {'str': 10, 'int': 10, 'dex': 10, 'luk': 10, 'agi': 10, 'vit': 10, 'growth': '+1 STR, +1 VIT, +1 DEX', 'ranks': 'Semua C'})
    derived = calculate_derived_stats(p_stat, is_ranged)

    md = []
    # Frontmatter
    md.append("---")
    md.append(f"title: {cname}")
    md.append(f"class_id: {cid}")
    md.append(f"tier: {tier}")
    md.append(f"branch: {branch}")
    md.append(f"level_cap: {lvl_cap}")
    md.append(f"primary_role: {role}")
    md.append("tags:")
    md.append("  - Class_Database")
    md.append(f"  - Tier_{tier}")
    md.append(f"  - {branch.split()[1]}")
    md.append("---\n")

    # Header
    md.append(f"# 🛡️ Database Kelas: {cname}")
    md.append(f"> **Cabang:** `{branch}` | **Tingkat:** `Tier {tier}` | **Batas Level:** `Lv. 1 – {lvl_cap}`\n")
    md.append(f"{lore_desc}\n")
    md.append("---\n")

    # 1. Profil & Identitas Peran
    md.append("## 1. Profil & Identitas Peran")
    md.append("| Atribut Kelas | Rincian / Status |")
    md.append("| :--- | :--- |")
    md.append(f"| **Nama Resmi** | **{cname}** |")
    md.append(f"| **Class ID Database** | `CID: {cid}` |")
    md.append(f"| **Tier Penguasaan** | `Tier {tier}` *(Level Cap: {lvl_cap})* |")
    md.append(f"| **Promosi Dari** | `{p_from}` |")
    md.append(f"| **Promosi Lanjutan** | `{prom_to}` |")
    md.append(f"| **Peran Utama** | `{role}` |")
    md.append(f"| **Kelemahan Taktis** | *{weakness}* |\n")

    # 2. Parameter Pertumbuhan & Karakteristik
    md.append("## 2. Parameter Pertumbuhan & Karakteristik (Turn-Based RPG)\n")
    
    # 2.A Base Stats
    md.append("### A. 6 Base Stats (Atribut Dasar Kelas)")
    md.append("| STR | INT | DEX | LUK | AGI | VIT |")
    md.append("| :---: | :---: | :---: | :---: | :---: | :---: |")
    md.append(f"| **{p_stat['str']}** | **{p_stat['int']}** | **{p_stat['dex']}** | **{p_stat['luk']}** | **{p_stat['agi']}** | **{p_stat['vit']}** |\n")
    md.append(f"* **Peringkat Atribut Dasar:** `{p_stat['ranks']}`")
    md.append(f"* **Pertumbuhan Stat Alami (Fixed Stat Growth per Class Level):** `{p_stat['growth']}`")
    md.append(f"* **Kurva Kebutuhan EXP:** `{exp_curve}`\n")

    # 2.B Derived Stats
    md.append("### B. Stat Turunan Awal (Baseline Derived Stats)")
    md.append("*Nilai di bawah dihitung deterministik dari 6 Base Stats awal kelas menggunakan formula resmi Nusvanir (sebelum bonus perlengkapan & alokasi poin pemain):*\n")

    md.append("#### 1. Sumber Daya Vital & Tempur Utama")
    md.append("| Parameter | Nilai Baseline | Formula / Perhitungan Resmi |")
    md.append("| :--- | :---: | :--- |")
    md.append(f"| **Max HP** | `{derived['hp']}` | `Base 50 + (VIT {p_stat['vit']} * 15) + (STR {p_stat['str']} * 5)` |")
    md.append(f"| **Max MP** | `{derived['mp']}` | `Base 20 + (INT {p_stat['int']} * 8)` |")
    md.append(f"| **Max SP** | `{derived['sp']}` | `Base 20 + (VIT {p_stat['vit']} * 5) + (STR {p_stat['str']} * 2)` *(Preserved antar battle)* |")
    atk_label = "Ranged/Finesse" if is_ranged else "Melee"
    atk_form = f"(DEX {p_stat['dex']} * 2) + (STR {p_stat['str']} * 0.5)" if is_ranged else f"(STR {p_stat['str']} * 2) + (DEX {p_stat['dex']} * 0.5)"
    md.append(f"| **ATK** | `{derived['atk']}` | `{atk_form}` *({atk_label})* |")
    md.append(f"| **DEF** | `{derived['def']}` | `Base + (VIT {p_stat['vit']} * 1.5) + (STR {p_stat['str']} * 0.5)` |")
    md.append(f"| **MAT** | `{derived['mat']}` | `Base + (INT {p_stat['int']} * 2)` |")
    md.append(f"| **MDF** | `{derived['mdf']}` | `Base + (INT {p_stat['int']} * 1.2) + (VIT {p_stat['vit']} * 0.8)` |")
    md.append(f"| **Action Speed** | `{derived['spd']}` | `Base + (AGI {p_stat['agi']} * 1.5)` |\n")

    md.append("#### 2. Presisi, Kritikal & Regenerasi Giliran (X-Param & S-Param)")
    md.append("| Parameter | Nilai (%) | Formula Perhitungan |")
    md.append("| :--- | :---: | :--- |")
    md.append(f"| **Hit Rate (HIT)** | `{derived['hit']:.1f}%` | `0.85 + (DEX {p_stat['dex']} * 0.002)` (Cap 100%) |")
    md.append(f"| **Evasion Rate (EVA)** | `{derived['eva']:.1f}%` | `0.02 + (AGI {p_stat['agi']} * 0.002) + (LUK {p_stat['luk']} * 0.0005)` (Cap 80%) |")
    md.append(f"| **Critical Rate (CRI)** | `{derived['cri']:.1f}%` | `0.03 + (DEX {p_stat['dex']} * 0.002) + (LUK {p_stat['luk']} * 0.001)` (Cap 85%) |")
    md.append(f"| **Critical Evasion (CEV)** | `{derived['cev']:.1f}%` | `(LUK {p_stat['luk']} * 0.0015) + (VIT {p_stat['vit']} * 0.001)` |")
    md.append(f"| **Critical Damage (CDMG)** | `{derived['cdmg']:.1f}%` | `1.5 + (STR {p_stat['str']} * 0.003) + (DEX {p_stat['dex']} * 0.002)` |")
    md.append(f"| **Guard Efficiency (GRD)** | `{derived['grd']:.1f}%` | `1.0 + (VIT {p_stat['vit']} * 0.005)` *(Mitigasi saat bertahan)* |")
    md.append(f"| **HP Regen / Turn (HRG)** | `{derived['hrg']:.2f}%` | `VIT {p_stat['vit']} * 0.0003` |")
    md.append(f"| **MP Regen / Turn (MRG)** | `{derived['mrg']:.2f}%` | `INT {p_stat['int']} * 0.0003` |")
    md.append(f"| **SP Regen / Turn (TRG)** | `{derived['trg']:.2f}%` | `0.03 + (AGI {p_stat['agi']} * 0.0004) + (VIT {p_stat['vit']} * 0.0002)` |\n")

    # 2.C Karakteristik & Peralatan
    md.append("### C. Karakteristik, Sasis & Peralatan")
    md.append(f"* **Innate Trait:** `{innate_trait}`")
    md.append(f"* **Senjata yang Dapat Digunakan:** `{weapons_str}`")
    md.append(f"* **Zirah & Pelindung:** `{armors_str}`")
    md.append(f"* **Tipe Skill yang Dibuka:** `{skill_types}`\n")

    # 3. Database Skill & Learnings
    md.append("## 3. Daftar Lengkap Skill & Pembelajaran (Learnings)")
    md.append("*Seluruh skill di bawah ini otomatis terbuka saat mencapai Class Level yang ditentukan.*\n")

    skills_list = []
    if tier == 1:
        skills_list = T1_SKILLS_DATA.get(cname, [])
    else:
        skills_list = skills_by_class.get(cname, [])

    if skills_list:
        md.append("| Level | Nama Skill | Tipe / Elemen | Biaya | Target | Formula / Efek Matematis | Deskripsi & Catatan |")
        md.append("| :---: | :--- | :--- | :---: | :--- | :--- | :--- |")
        for sk in skills_list:
            lvl_display = sk.get('lvl', 1)
            s_name = sk.get('name', '')
            s_type = sk.get('skill_type', sk.get('type', 'Physical'))
            elem = sk.get('element', sk.get('elem', 'Neutral'))
            cost = sk.get('cost', '0 SP')
            scope = sk.get('scope', '1 Target')
            formula = sk.get('formula', '-')
            desc = sk.get('desc', '')
            effects = sk.get('effects', '')
            if effects and effects != 'None' and effects not in desc:
                desc += f" *(Efek: {effects})*"
            
            md.append(f"| **{lvl_display}** | **{s_name}** | `{s_type}` / `{elem}` | `{cost}` | {scope} | `{formula}` | {desc} |")
    else:
        md.append("> *Daftar skill tingkat lanjut untuk kelas ini sedang dalam tahap perancangan akhir.*\n")

    md.append("\n---\n")

    # 4. Pohon Evolusi (Advancement Tree)
    md.append("## 4. Alur Evolusi & Percabangan Kelas")
    md.append("```mermaid")
    md.append("graph LR")
    if 'Fisik' in branch:
        md.append('    Fighter["Fighter (T1)"] --> Warrior["Warrior (T2: Offense)"]')
        md.append('    Fighter --> Squire["Squire (T2: Defense)"]')
        md.append('    Fighter --> Brawler["Brawler (T2: Agility)"]')
        md.append('    Warrior --> Mercenary["Mercenary (T3)"]')
        md.append('    Squire --> Knight["Knight (T3)"]')
        md.append('    Brawler --> MartialArtist["Martial Artist (T3)"]')
        md.append('    Mercenary --> Dragoon["Dragoon (T4: Aerial)"]')
        md.append('    Knight --> Champion["Champion (T4: Tank Juggernaut)"]')
        md.append('    Knight --> Paladin["Paladin (T4: Holy Guard)"]')
        md.append('    MartialArtist --> Monk["Monk (T4: Chi Burst)"]')
    elif 'Sihir' in branch:
        md.append('    Apprentice["Apprentice (T1)"] --> Magician["Magician (T2: Caster)"]')
        md.append('    Apprentice --> Acolyte["Acolyte (T2: Healer)"]')
        md.append('    Apprentice --> Occultist["Occultist (T2: Dark)"]')
        md.append('    Magician --> Mage["Mage (T3)"]')
        md.append('    Acolyte --> Cleric["Cleric (T3)"]')
        md.append('    Occultist --> Cultist["Cultist (T3)"]')
        md.append('    Mage --> Elementalist["Elementalist (T4: 8 Cabang Elemen)"]')
        md.append('    Cleric --> Priest["Priest (T4: Holy Vanguard)"]')
        md.append('    Cultist --> Necromancer["Necromancer (T4: Dark Summoner)"]')
    else: # Lincah
        md.append('    Scout["Scout (T1)"] --> Archer["Archer (T2: Bow)"]')
        md.append('    Scout --> Thief["Thief (T2: Dagger & Stealth)"]')
        md.append('    Archer --> Ranger["Ranger (T3: Trap & Wilderness)"]')
        md.append('    Thief --> Rogue["Rogue (T3: Ambush & Dual Blade)"]')
        md.append('    Ranger --> Sniper["Sniper (T4: Absolute Precision)"]')
        md.append('    Rogue --> Assassin["Assassin (T4: Fatal Execution)"]')
    md.append("```")

    return subfolder, fname, "\n".join(md)

def run():
    print("Membaca database Excel NUSV...")
    summary_dict, nusv_dict, skills_by_class = load_data()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for folder in ['01_Jalur_Fisik', '02_Jalur_Sihir', '03_Jalur_Lincah']:
        os.makedirs(os.path.join(OUTPUT_DIR, folder), exist_ok=True)

    generated_count = 0
    index_records = []
    
    for cname in CLASS_BRANCH_MAP.keys():
        subfolder, fname, content = generate_class_md(cname, summary_dict, nusv_dict, skills_by_class)
        filepath = os.path.join(OUTPUT_DIR, subfolder, fname)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        generated_count += 1
        binfo = CLASS_BRANCH_MAP[cname]
        p_stat = CLASS_BASE_STATS.get(cname, {})
        index_records.append({
            'name': cname,
            'tier': binfo[3],
            'branch': binfo[2],
            'level_cap': binfo[4],
            'role': binfo[7],
            'growth': p_stat.get('growth', '-'),
            'path': f"{subfolder}/{fname}"
        })
        print(f"[OK] Re-generated (Turn-Based): {subfolder}/{fname}")

    # Generate master README.md
    readme = []
    readme.append("# ⚔️ Master Database Kelas & Profesi Nusvanir (Turn-Based RPG)\n")
    readme.append("Direktori ini memuat dokumentasi resmi, parameter pertumbuhan 6 Base Stats, perhitungan Stat Turunan (Derived Stats), karakteristik traits, dan daftar skill lengkap untuk seluruh **35 Kelas Petualang** di dunia Nusvanir (Tier 1 hingga Tier 4).\n")
    readme.append("---")
    readme.append("## 🧭 Struktur Direktori Kelas")
    readme.append("* **[01_Jalur_Fisik/](01_Jalur_Fisik/)**: 11 Kelas Melee, Tank, dan Bela Diri (Fighter, Warrior, Squire, Brawler, Mercenary, Knight, Martial Artist, Champion, Dragoon, Paladin, Monk).")
    readme.append("* **[02_Jalur_Sihir/](02_Jalur_Sihir/)**: 17 Kelas Magis, Healer, Elemen, dan Kegelapan (Apprentice, Magician, Acolyte, Occultist, Mage, Cleric, Cultist, Priest, Necromancer, serta 8 Cabang Elementalist).")
    readme.append("* **[03_Jalur_Lincah/](03_Jalur_Lincah/)**: 7 Kelas Ranged, Assassin, dan Stealth (Scout, Archer, Thief, Ranger, Rogue, Sniper, Assassin).\n")
    readme.append("---")
    readme.append("## 📊 Matriks Daftar Kelas & Pertumbuhan Stat Alami\n")
    readme.append("| Tier | Nama Kelas | Jalur Profesi | Batas Level | Peran Utama | Fixed Stat Growth | Tautan Berkas |")
    readme.append("| :---: | :--- | :--- | :---: | :--- | :--- | :--- |")
    
    for rec in sorted(index_records, key=lambda x: (x['tier'], x['branch'], x['name'])):
        readme.append(f"| **T{rec['tier']}** | **{rec['name']}** | {rec['branch'].split()[1]} | Lv. {rec['level_cap']} | {rec['role']} | `{rec['growth']}` | [{rec['name']}]({rec['path']}) |")

    readme_path = os.path.join(OUTPUT_DIR, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(readme))
    print("[OK] Generated Master README.md")

    print(f"\nSelesai! Berhasil menyusun ulang {generated_count} file markdown database kelas + 1 Master README sesuai sistem 6 Base Stats & Derived Stats Turn-Based RPG!")

if __name__ == '__main__':
    run()
