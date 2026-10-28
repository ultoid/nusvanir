import os
import sys
import re
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

EXCEL_PATH = 'Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx'
OUTPUT_DIR = '06_Sistem Game & Ekonomi/Equipment'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------
def format_saka(tamra_val):
    if tamra_val is None or tamra_val == '' or tamra_val == 0 or tamra_val == '0.0':
        return '0 Saka (Tidak Dijual / Bebas)'
    try:
        val = int(float(tamra_val))
    except ValueError:
        return str(tamra_val)
    if val == 0:
        return '0 Saka (Tidak Dijual / Bebas)'
    kencana = val // 10000
    rem = val % 10000
    rajata = rem // 100
    tamra = rem % 100
    
    parts = []
    if kencana > 0:
        parts.append(f'{kencana} Kencana')
    if rajata > 0:
        parts.append(f'{rajata} Rajata')
    if tamra > 0:
        parts.append(f'{tamra} Tamra')
    
    formatted = ' '.join(parts) if parts else '0 Tamra'
    return f'{formatted} ({val:,} Tamra)'

def format_saka_short(tamra_val):
    if tamra_val is None or tamra_val == '' or tamra_val == 0 or tamra_val == '0.0':
        return '0T'
    try:
        val = int(float(tamra_val))
    except ValueError:
        return str(tamra_val)
    if val == 0:
        return '0T'
    kencana = val // 10000
    rem = val % 10000
    rajata = rem // 100
    tamra = rem % 100
    
    parts = []
    if kencana > 0:
        parts.append(f'{kencana}K')
    if rajata > 0:
        parts.append(f'{rajata}R')
    if tamra > 0:
        parts.append(f'{tamra}T')
    
    return ' '.join(parts) if parts else '0T'

def rarity_badge(r):
    badges = {
        'Common': '⚪ Common',
        'Uncommon': '🟢 Uncommon',
        'Rare': '🔵 Rare',
        'Epic': '🟣 Epic',
        'Legendary': '🟡 Legendary',
        'Mythic': '🔴 Mythic'
    }
    return badges.get(r, f'⚪ {r}')

def read_excel_sheet(sheet_name):
    with zipfile.ZipFile(EXCEL_PATH) as z:
        shared_strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            with z.open('xl/sharedStrings.xml') as f:
                tree = ET.parse(f)
                for si in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                    text_parts = [node.text for node in si.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t') if node.text]
                    shared_strings.append(''.join(text_parts))

        sheet_rel = {}
        with z.open('xl/workbook.xml') as f:
            tree = ET.parse(f)
            for s in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheets/{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet'):
                sheet_rel[s.attrib['name']] = s.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
        rel_map = {}
        with z.open('xl/_rels/workbook.xml.rels') as f:
            tree = ET.parse(f)
            for r in tree.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                rel_map[r.attrib['Id']] = r.attrib['Target']

        target_file = 'xl/' + rel_map[sheet_rel[sheet_name]]
        with z.open(target_file) as f:
            tree = ET.parse(f)
            rows = []
            for row in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheetData/{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
                r_data = []
                for c in row.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                    val = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                    t = c.attrib.get('t')
                    if val is not None and val.text:
                        v = val.text
                        if t == 's':
                            v = shared_strings[int(v)] if int(v) < len(shared_strings) else v
                        r_data.append(v)
                    else:
                        r_data.append('')
                if any(r_data):
                    rows.append(r_data)
            return rows

print("Reading Excel sheets...")
weapons_raw = read_excel_sheet('NUSV-WEAPON')
armors_raw = read_excel_sheet('NUSV-ARMOR')

# Map headers
w_headers = weapons_raw[0]
w_rows = [dict(zip(w_headers, r)) for r in weapons_raw[1:] if len(r) > 1 and r[0].strip()]

a_headers = armors_raw[0]
a_rows = [dict(zip(a_headers, r)) for r in armors_raw[1:] if len(r) > 1 and r[0].strip()]

print(f"Loaded {len(w_rows)} weapons and {len(a_rows)} armors.")

# Helper to format stat list
def format_stat_list(item, stat_keys):
    stats = []
    for k in stat_keys:
        val = item.get(k, '')
        try:
            fval = float(val)
            if fval != 0:
                ival = int(fval) if fval == int(fval) else fval
                stats.append(f"{k} +{ival}" if ival > 0 else f"{k} {ival}")
        except ValueError:
            if val and val != '0' and val != '0.0':
                stats.append(f"{k}: {val}")
    return ", ".join(stats) if stats else "-"

# -------------------------------------------------------------
# BUILD 01_WEAPONS.MD
# -------------------------------------------------------------
W_ORDER = [
    ("01 Long Sword", "Long Sword", "Pedang dua tangan berbilah panjang dengan daya tebas tinggi, fokus pada STR."),
    ("02 Sword", "Sword", "Pedang satu tangan seimbang, standar prajurit dan ksatria pelindung."),
    ("03 Gloves", "Gloves", "Sarung tinju dan cakar tempur untuk praktisi bela diri tangan kosong."),
    ("04 Spear", "Spear", "Tombak panjang dengan jangkauan tusukan penetrasi zirah yang luas."),
    ("05 Axe", "Axe", "Kapak perang berdaya rusak masif dengan potensi critical burst tinggi."),
    ("06 Staff", "Staff", "Tongkat sihir alami yang menyalurkan energi Mana dan memperkuat MAT."),
    ("07 Rune", "Rune", "Batu rune dan fokus mistis untuk manipulasi mantra kutukan dan okultisme."),
    ("08 Long Bow", "Long Bow", "Busur panah jarak jauh dengan presisi akurat berbasis stat DEX."),
    ("09 Crossbow", "Crossbow", "Busur silang mekanis dengan daya tembus baut berkecepatan tinggi."),
    ("10 Dagger", "Dagger", "Belati lincah dengan kecepatan tebas dan bonus critical rate tinggi.")
]

w_md = []
w_md.append("---")
w_md.append("title: Weapons_Database")
w_md.append("tags:")
w_md.append("  - Sistem_Game_Ekonomi")
w_md.append("  - Equipment")
w_md.append("  - Weapon_Database")
w_md.append("  - Turn_Based_RPG")
w_md.append("---\n")
w_md.append("# ⚔️ Database Perlengkapan: Weapons (Senjata Petualang)\n")
w_md.append("Dokumen ini memuat seluruh **66 Senjata Resmi** di dunia Nusvanir yang telah terkalibrasi ke dalam sistem **Turn-Based RPG**, mengacu pada [STANDAR_DATABASE_TYPES_RPG_MAKER.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md).\n")
w_md.append("> [!NOTE]")
w_md.append("> **Karakteristik Senjata Nusvanir:**")
w_md.append("> - **10 Tipe Senjata Resmi:** Terbagi ke dalam senjata Melee (STR), Finesse/Ranged (DEX), Brawler (STR/AGI), dan Magic Focus (INT).")
w_md.append("> - **Sistem Hand / Slot:** `1H Primary` dapat dipadukan dengan tameng/off-hand di slot Secondary Weapon; `2H Primary` menyegel slot secondary demi output kerusakan maksimal.")
w_md.append("> - **6 Tingkat Rarity:** ⚪ Common (Tier 1), 🟢 Uncommon (Tier 2), 🔵 Rare (Tier 3), 🟣 Epic (Tier 4), 🟡 Legendary (Tier 5), 🔴 Mythic (Apex Artifact).")
w_md.append("> - **Sistem Valuasi:** Nilai beli dan jual dinyatakan dalam koin mineral resmi **Saka (Tamra, Rajata, Kencana)**.\n")
w_md.append("---\n")

for type_code, type_raw, type_desc in W_ORDER:
    items_in_type = [w for w in w_rows if w.get('Weapon Type', '').strip() == type_raw]
    w_md.append(f"## 🗡️ {type_code}\n")
    w_md.append(f"*{type_desc}*\n")
    w_md.append("| ID | Nama Senjata | Rarity | Slot | ATK | MAT | Stat Tambahan | Harga Beli | Harga Jual | Resep / Perolehan |")
    w_md.append("|:---:|:---|:---:|:---:|:---:|:---:|:---|:---|:---|:---|")
    
    for item in items_in_type:
        iid = int(float(item['ID']))
        name = item['Name']
        rarity = rarity_badge(item.get('Rarity', 'Common'))
        slot = item.get('Hand / Slot', '1H Primary')
        atk = int(float(item.get('ATK', 0))) if item.get('ATK', '') else 0
        mat = int(float(item.get('MAT', 0))) if item.get('MAT', '') else 0
        other_stats = format_stat_list(item, ['MHP', 'MMP', 'DEF', 'MDF', 'AGI', 'LUK'])
        b_price = format_saka_short(item.get('Market Price (Tamra)', '0'))
        s_price = format_saka_short(item.get('Sell Price (Tamra)', '0'))
        recipe = item.get('Craft Recipe', '') or item.get('Acquisition', '-')
        w_md.append(f"| **{iid:02d}** | **{name}** | {rarity} | {slot} | `+{atk}` | `+{mat}` | {other_stats} | {b_price} | {s_price} | {recipe} |")
    w_md.append("\n")

    # Detailed breakdown per weapon
    for item in items_in_type:
        iid = int(float(item['ID']))
        name = item['Name']
        rarity = rarity_badge(item.get('Rarity', 'Common'))
        slot = item.get('Hand / Slot', '1H Primary')
        recipe = item.get('Craft Recipe', '') or '-'
        acq = item.get('Acquisition', '-')
        traits = item.get('Type Traits', '-')
        spec1 = item.get('Special Effect 1', '')
        spec2 = item.get('Special Effect 2', '')
        sig = item.get('Signature Effect', '')
        lore = item.get('Lore Basis', '') or item.get('Notes', '')
        region = item.get('Lore Region / Culture', '-')
        
        all_stats = format_stat_list(item, ['ATK', 'MAT', 'MHP', 'MMP', 'DEF', 'MDF', 'AGI', 'LUK'])

        w_md.append(f"### 🔹 [{iid:02d}] {name}")
        w_md.append(f"- **Tipe Senjata & Slot:** `{type_code}` | `{slot}`")
        w_md.append(f"- **Tingkat Kelangkaan (Rarity):** {rarity}")
        w_md.append(f"- **Parameter Stat Tempur:** {all_stats}")
        w_md.append(f"- **Harga Pasar (Beli):** {format_saka(item.get('Market Price (Tamra)', '0'))}")
        w_md.append(f"- **Harga Jual Standar:** {format_saka(item.get('Sell Price (Tamra)', '0'))}")
        w_md.append(f"- **Resep Pembuatan (Craft Recipe):** `{recipe}`")
        w_md.append(f"- **Metode Perolehan:** {acq}")
        if traits and traits != '-':
            w_md.append(f"- **Weapon Traits:** {traits}")
        if spec1:
            w_md.append(f"- **Efek Khusus 1:** {spec1}")
        if spec2:
            w_md.append(f"- **Efek Khusus 2:** {spec2}")
        if sig:
            w_md.append(f"- **Signature Effect:** ✨ **{sig}**")
        if region and region != '-':
            w_md.append(f"- **Asal Wilayah / Budaya:** {region}")
        if lore:
            w_md.append(f"- **Latar Belakang Lore:** *\"{lore}\"*")
        w_md.append("\n")

with open(os.path.join(OUTPUT_DIR, '01_Weapons.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(w_md))

print("01_Weapons.md generated successfully.")

# -------------------------------------------------------------
# BUILD 02_ARMORS.MD
# -------------------------------------------------------------
A_SLOT_ORDER = [
    ("Armor", "🛡️ 1. Pelindung Tubuh (Body Armor)", "Zirah utama penentu pertahanan fisik dan magis tubuh. Terbagi menjadi Basic Clothes, Magic Robe, Light Armor, dan Heavy Armor."),
    ("Secondary Weapon", "🛡️ 2. Pelindung Tangan / Tameng (Shields)", "Tameng ringan (Light Shield) dan tameng berat (Heavy Shield) penambah mitigasi Guard (GRD) dan penangkis serangan."),
    ("Helm", "🪖 3. Pelindung Kepala (Helms & Headwear)", "Pelindung kepala penambah presisi, resistensi status mental/kebutaan, dan perlindungan vital."),
    ("Boots", "👢 4. Pelindung Kaki (Boots & Footwear)", "Alas kaki penunjang mobilitas, Action Speed (AGI), Evasion, serta pengurangan bahaya medan perang."),
    ("Accessory", "💍 5. Aksesoris (Rings, Amulets, & Charms)", "Perhiasan berdaya magis yang melipatgandakan parameter sekunder (X-Param & S-Param) dan resistensi status."),
    ("Relic", "🔮 6. Relik Pusaka Purba (Relics & Artifacts)", "Artefak purba berkekuatan mistis yang memberikan efek pasif pengubah mekanik tempur.")
]

a_md = []
a_md.append("---")
a_md.append("title: Armors_Database")
a_md.append("tags:")
a_md.append("  - Sistem_Game_Ekonomi")
a_md.append("  - Equipment")
a_md.append("  - Armor_Database")
a_md.append("  - Turn_Based_RPG")
a_md.append("---\n")
a_md.append("# 🛡️ Database Perlengkapan: Armors & Protective Gear (Zirah & Pelindung)\n")
a_md.append("Dokumen ini memuat seluruh **123 Perlengkapan Zirah & Pelindung** di dunia Nusvanir yang mencakup Body Armor, Shields, Helms, Boots, Accessories, dan Relics sesuai [STANDAR_DATABASE_TYPES_RPG_MAKER.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md).\n")
a_md.append("> [!NOTE]")
a_md.append("> **Aturan Sistem Zirah & Set Bonus Nusvanir:**")
a_md.append("> - **6 Tipe Zirah Resmi:** `01 Basic Clothes`, `02 Magic Robe`, `03 Light Armor`, `04 Heavy Armor`, `05 Light Shield`, `06 Heavy Shield`.")
a_md.append("> - **6 Slot Perlengkapan:** `Primary Weapon`, `Secondary Weapon`, `Helm`, `Armor`, `Boots`, `Accessory`, `Relic`.")
a_md.append("> - **Sistem Set Bonus:** Memasang 2, 3, 4, hingga 5 bagian dari set zirah yang sama (misal: *Mandala Guard Set, Raksawana Scout Set, Silkweaver Set*) membuka efek sinergi pasif kuat.")
a_md.append("> - **Mitigasi Guard:** Tameng secara drastis meningkatkan efisiensi parameter Guard Efficiency ($GRD$) saat karakter memilih aksi bertahan.\n")
a_md.append("---\n")

for slot_key, slot_title, slot_desc in A_SLOT_ORDER:
    items_in_slot = [a for a in a_rows if a.get('Equip Slot', '').strip() == slot_key]
    a_md.append(f"## {slot_title}\n")
    a_md.append(f"*{slot_desc}*\n")
    a_md.append("| ID | Nama Perlengkapan | Tipe Zirah | Rarity | Set | DEF | MDF | MHP/Stat Lain | Harga Beli | Harga Jual | Resep / Drop |")
    a_md.append("|:---:|:---|:---:|:---:|:---|:---:|:---:|:---|:---|:---|:---|")

    for item in items_in_slot:
        iid = int(float(item['ID']))
        name = item['Name']
        atype = item.get('Armor Type', slot_key)
        if atype == 'Basic Armor':
            atype = '01 Basic Clothes'
        rarity = rarity_badge(item.get('Rarity', 'Common'))
        set_name = item.get('Set Name', '') or '-'
        def_val = int(float(item.get('DEF', 0))) if item.get('DEF', '') else 0
        mdf_val = int(float(item.get('MDF', 0))) if item.get('MDF', '') else 0
        other_stats = format_stat_list(item, ['MHP', 'MMP', 'ATK', 'MAT', 'AGI', 'LUK'])
        b_price = format_saka_short(item.get('Market Price (Tamra)', '0'))
        s_price = format_saka_short(item.get('Sell Price (Tamra)', '0'))
        source = item.get('Craft Recipe', '') or item.get('Drop Source', '') or item.get('Acquisition', '-')
        a_md.append(f"| **{iid:02d}** | **{name}** | `{atype}` | {rarity} | {set_name} | `+{def_val}` | `+{mdf_val}` | {other_stats} | {b_price} | {s_price} | {source} |")
    a_md.append("\n")

    # Detailed items in slot
    for item in items_in_slot:
        iid = int(float(item['ID']))
        name = item['Name']
        atype = item.get('Armor Type', slot_key)
        if atype == 'Basic Armor':
            atype = '01 Basic Clothes'
        rarity = rarity_badge(item.get('Rarity', 'Common'))
        set_name = item.get('Set Name', '') or '-'
        recipe = item.get('Craft Recipe', '') or '-'
        drop = item.get('Drop Source', '') or '-'
        acq = item.get('Acquisition', '-')
        traits = item.get('Native MV Traits', '-')
        spec1 = item.get('Special Effect 1', '')
        spec2 = item.get('Special Effect 2', '')
        sig = item.get('Signature Effect', '')
        set2 = item.get('2 Set Bonus', '')
        set3 = item.get('3 Set Bonus', '')
        set4 = item.get('4 Set Bonus', '')
        set5 = item.get('5 Set Bonus', '')
        lore = item.get('Notes', '')
        region = item.get('Lore Region / Culture', '-')

        all_stats = format_stat_list(item, ['DEF', 'MDF', 'MHP', 'MMP', 'ATK', 'MAT', 'AGI', 'LUK'])

        a_md.append(f"### 🛡️ [{iid:02d}] {name}")
        a_md.append(f"- **Slot Perlengkapan & Tipe:** `{slot_key}` | `{atype}`")
        a_md.append(f"- **Tingkat Kelangkaan (Rarity):** {rarity}")
        if set_name != '-':
            a_md.append(f"- **Bagian dari Set:** ⚜️ **{set_name}**")
        a_md.append(f"- **Parameter Stat Pertahanan:** {all_stats}")
        a_md.append(f"- **Harga Pasar (Beli):** {format_saka(item.get('Market Price (Tamra)', '0'))}")
        a_md.append(f"- **Harga Jual Standar:** {format_saka(item.get('Sell Price (Tamra)', '0'))}")
        if recipe != '-':
            a_md.append(f"- **Resep Pembuatan (Craft Recipe):** `{recipe}`")
        if drop != '-':
            a_md.append(f"- **Monster Drop Source:** `{drop}`")
        a_md.append(f"- **Metode Perolehan:** {acq}")
        if traits and traits != '-':
            a_md.append(f"- **Traits Bawaan:** {traits}")
        if spec1:
            a_md.append(f"- **Efek Khusus 1:** {spec1}")
        if spec2:
            a_md.append(f"- **Efek Khusus 2:** {spec2}")
        if sig:
            a_md.append(f"- **Signature Effect:** ✨ **{sig}**")
        
        # Set bonuses
        if set2 or set3 or set4 or set5:
            a_md.append("- **Efek Sinergi Set:**")
            if set2:
                a_md.append(f"  * **[2 Set]:** {set2}")
            if set3:
                a_md.append(f"  * **[3 Set]:** {set3}")
            if set4:
                a_md.append(f"  * **[4 Set]:** {set4}")
            if set5:
                a_md.append(f"  * **[5 Set]:** {set5}")
        
        if region and region != '-':
            a_md.append(f"- **Asal Wilayah / Budaya:** {region}")
        if lore:
            a_md.append(f"- **Catatan / Lore:** *\"{lore}\"*")
        a_md.append("\n")

with open(os.path.join(OUTPUT_DIR, '02_Armors.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(a_md))

print("02_Armors.md generated successfully.")

# -------------------------------------------------------------
# BUILD README.MD
# -------------------------------------------------------------
r_md = []
r_md.append("# 🛡️ Database Induk Perlengkapan Petualang Nusvanir\n")
r_md.append("Katalog resmi seluruh perlengkapan senjata, zirah pelindung, tameng, aksesoris, dan relik purba untuk game RPG *Turn-Based* Nusvanir.\n")
r_md.append("Seluruh data pada direktori ini dihasilkan langsung dari spreadsheet master **`Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx`** dan diselaraskan dengan spesifikasi **[STANDAR_DATABASE_TYPES_RPG_MAKER.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/STANDAR_DATABASE_TYPES_RPG_MAKER.md)**.\n")
r_md.append("---\n")
r_md.append("## 📑 Struktur Berkas Perlengkapan\n")
r_md.append("| Berkas Dokumen | Kategori Perlengkapan | Jumlah Entri | Ruang Lingkup & Cakupan Utama |")
r_md.append("|---|---|:---:|---|")
r_md.append(f"| [01_Weapons.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/01_Weapons.md) | **Weapons (Senjata)** | **{len(w_rows)} Senjata** | 10 Tipe Senjata resmi (Long Sword, Sword, Gloves, Spear, Axe, Staff, Rune, Bow, Crossbow, Dagger) dari Tier Common hingga Mythic. |")
r_md.append(f"| [02_Armors.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Equipment/02_Armors.md) | **Armors & Gear (Zirah)** | **{len(a_rows)} Perlengkapan** | Pelindung Tubuh (Armor), Tameng (Shields), Pelindung Kepala (Helm), Sepatu (Boots), Aksesoris, dan Relik Pusaka Purba dengan sistem Set Bonus. |\n")
r_md.append("---\n")
r_md.append("## ⚙️ Integrasi Sistem Tempur Turn-Based\n")
r_md.append("1. **7 Slot Perlengkapan (`YEP_EquipCore`):**")
r_md.append("   - `01 Primary Weapon`: Senjata utama tangan kanan (atau senjata 2 tangan).")
r_md.append("   - `02 Secondary Weapon`: Tameng (Light/Heavy Shield), fokus magis, atau senjata kedua (*Dual Wield*).")
r_md.append("   - `03 Helm`: Pelindung kepala.")
r_md.append("   - `04 Armor`: Zirah tubuh (Basic Clothes, Magic Robe, Light Armor, Heavy Armor).")
r_md.append("   - `05 Boots`: Sepatu penambah Action Speed (AGI) dan Evasion.")
r_md.append("   - `06 Accessory`: Cincin, jimat, dan kalung stat sekunder.")
r_md.append("   - `07 Relic`: Pusaka sakral penambah efek pasif unik tempur.\n")
r_md.append("2. **Sinergi Soket Kristal & Tempa:**")
r_md.append("   - Seluruh senjata dan zirah dapat dipasangi kristal soket stat dari [03_Forge_&_Enhancement.md](file:///mnt/DC9EA2C29EA29494/Nusvanir_Vault/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) untuk meningkatkan 18 Parameter RPG secara presisi.")
r_md.append("3. **Sistem Sinergi Set Bonus:**")
r_md.append("   - Memasang perlengkapan dari seri yang sama (misal: *Mandala Guard, Deerhide, Ironwood, Sunken, Astral, Dragon Hunter*) mengaktifkan buff kumulatif 2-Set, 3-Set, 4-Set, hingga 5-Set.\n")

with open(os.path.join(OUTPUT_DIR, 'README.md'), 'w', encoding='utf-8') as f:
    f.write("\n".join(r_md))

print("README.md generated successfully.")
