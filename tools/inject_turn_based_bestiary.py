"""
Script untuk menyuntikkan Game Data Turn-Based RPG ke seluruh file Markdown Bestiary Nusvanir.
Mengacu pada:
- Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx
- 06_Sistem Game & Ekonomi/Sistem_Stat_&_Formula_Turn_Based.md
- 07_Bestiary/BESTIARY_STANDARD_V2.md
"""

import os
import glob
import openpyxl

EXCEL_PATH = r"e:\Ananto\Emulatoid\Nusvanir\Database\NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx"
BESTIARY_DIR = r"e:\Ananto\Emulatoid\Nusvanir\07_Bestiary"

def load_database():
    wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
    
    # Load Skills
    ws_skills = wb['NUSV-SKILL']
    skills_dict = {}
    for r in range(2, ws_skills.max_row + 1):
        sname = ws_skills.cell(r, 2).value
        if sname:
            sname_str = str(sname).strip()
            skills_dict[sname_str.lower()] = {
                'id': int(ws_skills.cell(r, 1).value or 0),
                'name': sname_str,
                'source_type': ws_skills.cell(r, 3).value or '',
                'source_owner': ws_skills.cell(r, 5).value or '',
                'mp_cost': int(ws_skills.cell(r, 9).value or 0),
                'sp_cost': int(ws_skills.cell(r, 10).value or 0),
                'scope': ws_skills.cell(r, 11).value or '1 Target',
                'damage_type': ws_skills.cell(r, 13).value or 'HP Damage',
                'element': ws_skills.cell(r, 14).value or 'Neutral',
                'formula': ws_skills.cell(r, 15).value or '-',
                'variance': ws_skills.cell(r, 16).value or 20,
                'critical': ws_skills.cell(r, 17).value or 'Yes',
                'hit_type': ws_skills.cell(r, 22).value or 'Physical Attack',
                'skill_effect': ws_skills.cell(r, 23).value or '',
                'status_effect': ws_skills.cell(r, 24).value or '',
                'desc': ws_skills.cell(r, 32).value or ''
            }
            
    # Load Traits
    ws_traits = wb['NUSV-ENEMYTRAITS']
    traits_dict = {}
    for r in range(2, ws_traits.max_row + 1):
        ename = ws_traits.cell(r, 1).value
        if ename:
            ename_str = str(ename).strip().lower()
            if ename_str not in traits_dict:
                traits_dict[ename_str] = []
            traits_dict[ename_str].append({
                'cat': ws_traits.cell(r, 2).value or '',
                'type': ws_traits.cell(r, 3).value or '',
                'target': ws_traits.cell(r, 4).value or '',
                'val': ws_traits.cell(r, 5).value,
                'notes': ws_traits.cell(r, 8).value or ''
            })

    # Load Enemies
    ws_enemies = wb['NUSV-ENEMIES']
    enemies_list = []
    for r in range(2, ws_enemies.max_row + 1):
        name = ws_enemies.cell(r, 2).value
        if name:
            enemies_list.append({
                'id': int(ws_enemies.cell(r, 1).value or 0),
                'name': str(name).strip(),
                'group': str(ws_enemies.cell(r, 3).value or '').strip(),
                'rank': str(ws_enemies.cell(r, 4).value or 'Normal').strip(),
                'type': str(ws_enemies.cell(r, 5).value or 'Beast').strip(),
                'archetype': str(ws_enemies.cell(r, 6).value or 'Balanced').strip(),
                'combat_tags': str(ws_enemies.cell(r, 7).value or '').strip(),
                'tier': str(ws_enemies.cell(r, 8).value or 'T1').strip(),
                'region': str(ws_enemies.cell(r, 9).value or '').strip(),
                'element': str(ws_enemies.cell(r, 10).value or 'Neutral').strip(),
                'weakness': str(ws_enemies.cell(r, 11).value or 'None').strip(),
                'mhp': float(ws_enemies.cell(r, 12).value or 100),
                'mmp': float(ws_enemies.cell(r, 13).value or 10),
                'atk': float(ws_enemies.cell(r, 14).value or 10),
                'def': float(ws_enemies.cell(r, 15).value or 10),
                'mat': float(ws_enemies.cell(r, 16).value or 10),
                'mdf': float(ws_enemies.cell(r, 17).value or 10),
                'agi': float(ws_enemies.cell(r, 18).value or 10),
                'luk': float(ws_enemies.cell(r, 19).value or 10),
                'exp': int(float(ws_enemies.cell(r, 20).value or 10)),
                'gold': int(float(ws_enemies.cell(r, 21).value or 5)),
                'attack_type': str(ws_enemies.cell(r, 22).value or 'Melee').strip(),
                'trait1': ws_enemies.cell(r, 23).value,
                'trait2': ws_enemies.cell(r, 24).value,
                'trait3': ws_enemies.cell(r, 25).value,
                'skill1': ws_enemies.cell(r, 26).value,
                'skill1_cond': ws_enemies.cell(r, 27).value or 'Selalu',
                'skill1_rating': ws_enemies.cell(r, 28).value or 5,
                'skill2': ws_enemies.cell(r, 30).value,
                'skill2_cond': ws_enemies.cell(r, 31).value or 'Turn 2+ / 50% Peluang',
                'skill2_rating': ws_enemies.cell(r, 32).value or 4,
                'skill3': ws_enemies.cell(r, 34).value,
                'skill3_cond': ws_enemies.cell(r, 35).value or 'HP <= 40% Desperation',
                'skill3_rating': ws_enemies.cell(r, 36).value or 4,
                'drop1': ws_enemies.cell(r, 38).value,
                'drop1_rate': ws_enemies.cell(r, 39).value,
                'drop2': ws_enemies.cell(r, 40).value,
                'drop2_rate': ws_enemies.cell(r, 41).value,
                'drop3': ws_enemies.cell(r, 42).value,
                'drop3_rate': ws_enemies.cell(r, 43).value,
                'boss_drop': ws_enemies.cell(r, 44).value,
                'boss_drop_rate': ws_enemies.cell(r, 45).value,
                'passive': ws_enemies.cell(r, 46).value
            })

    return enemies_list, skills_dict, traits_dict

def solve_stats(enemy):
    atk = enemy['atk']
    df = enemy['def']
    mat = enemy['mat']
    mdf = enemy['mdf']
    agi = enemy['agi']
    luk = enemy['luk']
    mhp = enemy['mhp']
    mmp = enemy['mmp']
    atk_type = enemy['attack_type']
    archetype = enemy['archetype']

    b_luk = max(1, int(round(luk)))
    b_agi = max(1, int(round(agi / 1.5))) if agi > 10 else max(1, int(round(agi)))
    
    # INT derived from MP and MAT
    b_int = max(1, int(round(mmp / 8.0)))
    if 'Mage' in archetype or 'Caster' in archetype:
        b_int = max(b_int, int(round(mat / 2.0)))

    # STR & DEX
    if 'Ranged' in atk_type or 'Sniper' in archetype or 'Scout' in archetype:
        b_dex = max(1, int(round(atk / 2.2)))
        b_str = max(1, int(round((atk - b_dex * 2) * 2)))
    else:
        b_str = max(1, int(round(atk / 2.2)))
        b_dex = max(1, int(round((atk - b_str * 2) * 2)))
        b_dex = max(1, b_dex)

    # VIT
    rem_def = df - (b_str * 0.5)
    b_vit = max(1, int(round(rem_def / 1.5))) if rem_def > 1.5 else max(1, int(round(df / 2.0)))

    # Derived Combat Stats:
    # Max HP: Base Class HP + (VIT * 15) + (STR * 5)
    calc_hp_from_stats = int(round(b_vit * 15 + b_str * 5))
    base_class_hp = max(0, int(round(mhp - calc_hp_from_stats)))
    final_hp = int(round(mhp))

    # Max MP: Base Class MP + (INT * 8)
    calc_mp_from_stats = int(round(b_int * 8))
    base_class_mp = max(0, int(round(mmp - calc_mp_from_stats)))
    final_mp = int(round(mmp))

    # Max SP: Base SP (20) + (VIT * 5) + (STR * 2)
    final_sp = int(round(20 + b_vit * 5 + b_str * 2))

    # ATK
    if 'Ranged' in atk_type or 'Sniper' in archetype or 'Scout' in archetype:
        calc_atk = int(round(b_dex * 2 + b_str * 0.5))
    else:
        calc_atk = int(round(b_str * 2 + b_dex * 0.5))
    final_atk = int(round(atk))

    # DEF & MDF & MAT
    final_def = int(round(df))
    final_mat = int(round(mat))
    final_mdf = int(round(mdf))
    final_spd = int(round(agi))

    # Precision & Turn Efficiency (X-Param & S-Param)
    hit = min(1.0, 0.85 + (b_dex * 0.002))
    eva = min(0.8, 0.02 + (b_agi * 0.002) + (b_luk * 0.0005))
    cri = min(0.85, 0.03 + (b_dex * 0.002) + (b_luk * 0.001))
    cev = (b_luk * 0.0015) + (b_vit * 0.001)
    cdmg = 1.5 + (b_str * 0.003) + (b_dex * 0.002)
    grd = 1.0 + (b_vit * 0.005)
    hrg = b_vit * 0.0003
    mrg = b_int * 0.0003
    trg = 0.03 + (b_agi * 0.0004) + (b_vit * 0.0002)

    return {
        'base': {
            'str': b_str, 'int': b_int, 'dex': b_dex, 'luk': b_luk, 'agi': b_agi, 'vit': b_vit
        },
        'derived': {
            'base_class_hp': base_class_hp, 'hp': final_hp,
            'base_class_mp': base_class_mp, 'mp': final_mp,
            'sp': final_sp,
            'atk': final_atk, 'def': final_def, 'mat': final_mat, 'mdf': final_mdf,
            'spd': final_spd
        },
        'xparam': {
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
    }

def format_game_data_markdown(enemy, skills_dict, traits_dict):
    st = solve_stats(enemy)
    b = st['base']
    d = st['derived']
    x = st['xparam']
    
    # Class EXP: 75% of Base EXP or min 5
    base_exp = enemy['exp']
    class_exp = max(5, int(round(base_exp * 0.75)))

    # Recommended Level & Tier
    tier_str = enemy['tier']
    rank_str = enemy['rank']
    role_str = enemy['archetype']
    
    # Resolve traits
    ename_lower = enemy['name'].lower()
    t_list = traits_dict.get(ename_lower, [])
    elem_traits = [f"{t['target']}: {int(t['val']*100)}%" for t in t_list if t['type'] == 'Element Rate']
    state_traits = [f"{t['target']}: {int(t['val']*100)}%" for t in t_list if t['type'] == 'State Rate']

    md = []
    md.append("\n---\n")
    md.append("# 📊 GAME DATA & RPG PARAMETERS (TURN-BASED)\n")
    
    # 1. Klasifikasi Tempur
    md.append("### 1. Klasifikasi Tempur")
    md.append("| Parameter | Nilai | Sumber / Keterangan |")
    md.append("| :--- | :--- | :--- |")
    md.append(f"| **Database ID** | `{enemy['id']}.0` | Sheet `NUSV-ENEMIES` |")
    md.append(f"| **Ras / Taksonomi** | `{enemy['type']}` | Kategori taksonomi Nusvanir |")
    md.append(f"| **Class / Archetype** | `{role_str}` | Pola peran tempur turn-based |")
    md.append(f"| **Tier / Threat Rank** | `{tier_str} ({rank_str})` | Skala ancaman encounter |")
    md.append(f"| **Tipe Serangan Dasar** | `{enemy['attack_type']}` | Formula serangan dasar |")
    md.append(f"| **Elemen Utama** | `{enemy['element']}` | Afinitas serangan alami |")
    md.append(f"| **Kelemahan (Weakness)** | `{enemy['weakness']}` | Menerima pengganda kerusakan 2.0x |")
    if enemy['combat_tags']:
        md.append(f"| **Combat Tags** | `{enemy['combat_tags']}` | Penanda taktis unit |")
    md.append("")

    # 2. Parameter Atribut
    md.append("### 2. Parameter Atribut\n")
    md.append("#### A. 6 Base Stats (Atribut Dasar)")
    md.append("| STR | INT | DEX | LUK | AGI | VIT |")
    md.append("| :---: | :---: | :---: | :---: | :---: | :---: |")
    md.append(f"| **{b['str']}** | **{b['int']}** | **{b['dex']}** | **{b['luk']}** | **{b['agi']}** | **{b['vit']}** |\n")

    md.append("#### B. Stat Turunan Utama (Vital & Combat)")
    md.append("| Parameter | Formula Dasar / Nilai | Parameter | Formula Dasar / Nilai |")
    md.append("| :--- | :--- | :--- | :--- |")
    hp_breakdown = f"`{d['hp']}` *(Base {d['base_class_hp']} + VIT×15 + STR×5)*" if d['base_class_hp'] > 0 else f"`{d['hp']}` *(VIT×15 + STR×5)*"
    mp_breakdown = f"`{d['mp']}` *(Base {d['base_class_mp']} + INT×8)*" if d['base_class_mp'] > 0 else f"`{d['mp']}` *(INT×8)*"
    md.append(f"| **Max HP** | {hp_breakdown} | **DEF** | `{d['def']}` *(Base + VIT×1.5 + STR×0.5)* |")
    md.append(f"| **Max MP** | {mp_breakdown} | **MDF** | `{d['mdf']}` *(Base + INT×1.2 + VIT×0.8)* |")
    md.append(f"| **Max SP** | `{d['sp']}` *(Base 20 + VIT×5 + STR×2)* | **MAT** | `{d['mat']}` *(Base + INT×2)* |")
    md.append(f"| **ATK** | `{d['atk']}` *(Formula {enemy['attack_type']})* | **Action Speed** | `{d['spd']}` *(Base + AGI×1.5)* |\n")

    md.append("#### C. Parameter Presisi & Efisiensi Giliran (X-Param & S-Param)")
    md.append("| Parameter | Nilai (%) | Formula Perhitungan |")
    md.append("| :--- | :---: | :--- |")
    md.append(f"| **Hit Rate (HIT)** | `{x['hit']:.1f}%` | `0.85 + (DEX * 0.002)` (Cap 100%) |")
    md.append(f"| **Evasion Rate (EVA)** | `{x['eva']:.1f}%` | `0.02 + (AGI * 0.002) + (LUK * 0.0005)` (Cap 80%) |")
    md.append(f"| **Critical Rate (CRI)** | `{x['cri']:.1f}%` | `0.03 + (DEX * 0.002) + (LUK * 0.001)` (Cap 85%) |")
    md.append(f"| **Critical Evasion (CEV)** | `{x['cev']:.1f}%` | `(LUK * 0.0015) + (VIT * 0.001)` |")
    md.append(f"| **Critical Damage (CDMG)** | `{x['cdmg']:.1f}%` | `1.5 + (STR * 0.003) + (DEX * 0.002)` |")
    md.append(f"| **Guard Efficiency (GRD)** | `{x['grd']:.1f}%` | `1.0 + (VIT * 0.005)` |")
    md.append(f"| **HP Regen / Turn (HRG)** | `{x['hrg']:.2f}%` | `VIT * 0.0003` |")
    md.append(f"| **MP Regen / Turn (MRG)** | `{x['mrg']:.2f}%` | `INT * 0.0003` |")
    md.append(f"| **SP Regen / Turn (TRG)** | `{x['trg']:.2f}%` | `0.03 + (AGI * 0.0004) + (VIT * 0.0002)` |")
    md.append("")

    # 3. Skill & Pola Aksi Giliran (AI Actions)
    md.append("### 3. Skill & Pola Aksi Giliran (AI Actions)")
    md.append("*Acuan resmi: `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx` (Sheet `NUSV-SKILL`)*\n")
    md.append("| Nama Skill | Elemen / Tipe | Biaya (MP/SP) | Syarat Pemicu AI & Rating | Formula Kerusakan / Efek |")
    md.append("| :--- | :--- | :--- | :--- | :--- |")

    for s_idx in [1, 2, 3]:
        sname = enemy.get(f'skill{s_idx}')
        scond = enemy.get(f'skill{s_idx}_cond')
        srating = enemy.get(f'skill{s_idx}_rating')
        if sname and str(sname).strip():
            sname_clean = str(sname).strip()
            sk = skills_dict.get(sname_clean.lower(), None)
            if sk:
                elem = sk['element']
                htype = sk['hit_type']
                cost_parts = []
                if sk['mp_cost'] > 0: cost_parts.append(f"{sk['mp_cost']} MP")
                if sk['sp_cost'] > 0: cost_parts.append(f"{sk['sp_cost']} SP")
                cost_str = " / ".join(cost_parts) if cost_parts else "0 SP"
                formula = sk['formula']
                if sk['status_effect'] and str(sk['status_effect']).strip():
                    formula += f" ({sk['status_effect']})"
                md.append(f"| **{sk['name']}** | `{elem}` / {htype} | `{cost_str}` | {scond} (Prioritas {srating}) | `{formula}` |")
            else:
                md.append(f"| **{sname_clean}** | `Netral` / Physical | `0 SP` | {scond} (Prioritas {srating}) | `a.atk * 1.15 - b.def * 0.45` |")
    md.append("")

    # 4. Traits & Resistensi Khusus
    md.append("### 4. Traits & Resistensi Khusus")
    elem_str = ", ".join(elem_traits) if elem_traits else f"{enemy['element']} 100%, {enemy['weakness']} 200% (Weak)" if enemy['weakness'] != 'None' else "Netral 100%"
    state_str = ", ".join(state_traits) if state_traits else "Resistensi standar (tanpa anomali status)"
    md.append(f"* **Resistensi Elemen:** {elem_str}")
    md.append(f"* **Resistensi Status:** {state_str}")
    pass_str = str(enemy['passive']).strip() if enemy['passive'] and str(enemy['passive']).strip() != 'None' else "Preserve SP (Stamina tersimpan antar battle)"
    md.append(f"* **Karakteristik / Passive:** {pass_str}")
    md.append("")

    # 5. Ekonomi & Rampasan (Combat Rewards)
    md.append("### 5. Ekonomi & Rampasan (Combat Rewards)")
    md.append("| Jenis Hadiah | Jumlah / Peluang | Keterangan |")
    md.append("| :--- | :--- | :--- |")
    md.append(f"| **Base EXP** | `{base_exp}` | Akumulasi Base Level (+3 Stat Point bebas) |")
    md.append(f"| **Class EXP** | `{class_exp}` | Akumulasi Class Level profesi aktif (Tier Cap & Learnings) |")
    md.append(f"| **Saka (Gold)** | `{enemy['gold']}` | Mata uang resmi penjelajahan |")
    
    if enemy['drop1'] and str(enemy['drop1']).strip():
        rate1 = int(round(float(enemy['drop1_rate'] or 0.1) * 100))
        md.append(f"| **Drop 1** | `{enemy['drop1']}` (`{rate1}%`) | Material alam / crafting |")
    if enemy['drop2'] and str(enemy['drop2']).strip():
        rate2 = int(round(float(enemy['drop2_rate'] or 0.05) * 100))
        md.append(f"| **Drop 2** | `{enemy['drop2']}` (`{rate2}%`) | Komponen sekunder |")
    if enemy['drop3'] and str(enemy['drop3']).strip():
        rate3 = int(round(float(enemy['drop3_rate'] or 0.01) * 100))
        md.append(f"| **Drop 3** | `{enemy['drop3']}` (`{rate3}%`) | Rampasan langka |")
    if enemy['boss_drop'] and str(enemy['boss_drop']).strip():
        rate_b = int(round(float(enemy['boss_drop_rate'] or 0.01) * 100))
        md.append(f"| **Boss / Unique Drop** | `{enemy['boss_drop']}` (`{rate_b}%`) | Rampasan unik / piala bos |")

    return "\n".join(md)

def run():
    enemies, skills, traits = load_database()
    print(f"Loaded {len(enemies)} enemies from database.")

    # Aliases
    aliases = {
        'orichalor': 'goldenscale',
        'argentfang': 'moonfang',
        'mithralis': 'silverwing',
        'grok tulang besi': 'grok tulang-besi',
        'nyai larasati': 'larasati',
        'kura kura sungai': 'kura-kura sungai'
    }

    # Find MD files
    md_files = glob.glob(os.path.join(BESTIARY_DIR, "**", "*.md"), recursive=True)
    md_map = {}
    for p in md_files:
        fname = os.path.basename(p)
        if fname.startswith('BESTIARY_') or fname.startswith('CREATURE_') or fname.startswith('WILDLIFE_') or '_audit' in p:
            continue
        cname = os.path.splitext(fname)[0].replace('_', ' ').lower()
        md_map[cname] = p

    # Map each enemy
    success_count = 0
    for enemy in enemies:
        ename = enemy['name'].lower().replace('-', ' ').replace('_', ' ')
        target_path = None
        for cname, p in md_map.items():
            mapped_c = aliases.get(cname, cname)
            if ename == mapped_c or ename == cname or ename.replace(' ', '') == mapped_c.replace(' ', ''):
                target_path = p
                break
        
        if not target_path:
            print(f"[WARN] No MD file found for {enemy['name']}")
            continue

        # Read MD
        with open(target_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Strip existing Game Data block if any
        if "# 📊 GAME DATA" in content:
            content = content.split("# 📊 GAME DATA")[0].rstrip()
            # Also strip trailing separator if any
            if content.endswith("---"):
                content = content[:-3].rstrip()

        # Generate new Game Data block
        gamedata_md = format_game_data_markdown(enemy, skills, traits)
        new_content = content.rstrip() + "\n" + gamedata_md + "\n"

        # Write back
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        success_count += 1
        print(f"[OK] Injected {enemy['name']} -> {os.path.basename(target_path)}")

    print(f"\nSuccessfully injected {success_count}/{len(enemies)} bestiary files!")

if __name__ == '__main__':
    run()

