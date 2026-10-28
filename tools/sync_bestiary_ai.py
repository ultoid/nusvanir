import os
import sys
import glob
import re
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

EXCEL_PATH = 'Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx'
BESTIARY_DIR = '07_Bestiary'

ELEMENT_MAP = {
    'Neutral': '01 Neutral',
    'Fire': '02 Fire',
    'Water': '03 Water',
    'Earth': '04 Earth',
    'Wind': '05 Air',
    'Air': '05 Air',
    'Lightning': '06 Electric',
    'Electric': '06 Electric',
    'Ice': '07 Ice',
    'Metal': '08 Steel',
    'Steel': '08 Steel',
    'Sonic': '09 Sound',
    'Sound': '09 Sound',
    'Holy': '10 Holy',
    'Light': '10 Holy',
    'Dark': '11 Dark',
}

def clean_element(elem_str):
    parts = [p.strip() for p in elem_str.split('/')]
    out = []
    for p in parts:
        out.append(ELEMENT_MAP.get(p, p))
    return '/'.join(out)

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

print("Reading NUSV-ENEMIES sheet...")
raw_enemies = read_excel_sheet('NUSV-ENEMIES')
headers = raw_enemies[0]
e_rows = [dict(zip(headers, r)) for r in raw_enemies[1:] if len(r) > 1 and r[0].strip()]

id_map = {}
for e in e_rows:
    try:
        eid = int(float(e['ID']))
        id_map[eid] = e
    except ValueError:
        pass

# Find all monster markdown files
all_files = glob.glob(os.path.join(BESTIARY_DIR, '*/*.md'))
monster_files = [f for f in all_files if not any(x in f for x in ['_audit', 'README', 'STANDARD', 'INVENTORY', 'REFERENCES'])]

print(f"Loaded {len(e_rows)} enemies from Excel. Found {len(monster_files)} monster files.")

def build_ai_block(e):
    rank = e.get('Enemy Rank', 'Normal').strip()
    s1 = e.get('Skill 1', 'Basic Attack').strip()
    s2 = e.get('Skill 2', '').strip()
    s3 = e.get('Skill 3', '').strip()

    if rank in ['Commander', 'Boss', 'Lord']:
        tier = 'Tier 3: Mastermind AI (Pengendali Arena Multifase)'
        actions = '2 Aksi per Giliran' if rank != 'Lord' else '3 Aksi per Giliran'
        act_tag = '<Action Times: 2>' if rank != 'Lord' else '<Action Times: 3>'
        targeting = 'Cerdas & adaptif; mengeksekusi target ber-HP rendah, membalas provokasi Taunt dengan serangan masif/AoE, dan mengeksekusi fase serangan terencana.'
        notetags = [act_tag, '<AI Priority>']
        if s3:
            notetags.append(f'HP% <= 30%: {s3}, All Foes')
        if s2:
            notetags.append(f'Turn % 3 == 0: {s2}, Highest ATK')
        if s3 and s3 != s2:
            notetags.append(f'HP% <= 50%: {s3}, Lowest HP%')
        notetags.append(f'Always: {s1}, Lowest DEF')
        notetags.append('</AI Priority>')
    elif rank in ['Elite', 'Mini Boss']:
        tier = 'Tier 2: Tactical AI (Taktis Pasukan Elit)'
        actions = '1 Aksi per Giliran (Peluang 2 Aksi saat HP <= 30%)'
        targeting = 'Membaca status party pemain; memprioritaskan target ber-HP rendah (eksekusi), membalas Taunt dengan serangan berelemen atau AoE.'
        notetags = ['<AI Priority>']
        if s3:
            notetags.append(f'HP% <= 25%: {s3}, Lowest HP%')
        if s2:
            notetags.append(f'State === Taunt: {s2}, Random')
            notetags.append(f'Turn % 2 == 0: {s2}, Random')
        notetags.append(f'Always: {s1}, Highest TGR')
        notetags.append('</AI Priority>')
    else:
        tier = 'Tier 1: Instinct-Driven AI (Naluri Alami)'
        actions = '1 Aksi per Giliran'
        targeting = 'Naluri satwa liar/prajurit biasa; menyerang target dengan bobot Target Rate (TGR) tertinggi (fokus pada Tanker yang memprovokasi).'
        notetags = ['<AI Priority>']
        if s3:
            notetags.append(f'HP% <= 40%: {s3}, Lowest HP%')
        if s2:
            notetags.append(f'Turn 2+: {s2}, Random')
        notetags.append(f'Always: {s1}, Highest TGR')
        notetags.append('</AI Priority>')

    res = []
    res.append("#### B. Konfigurasi AI Taktis (YEP_BattleAICore)")
    res.append(f"* **AI Behavioral Tier:** `{tier}`")
    res.append(f"* **Jumlah Aksi per Giliran:** `{actions}`")
    res.append(f"* **Logika Penargetan:** {targeting}")
    res.append("* **Notetag Engine (Salin ke Database RPG Maker MV):**")
    res.append("```text")
    res.append("\n".join(notetags))
    res.append("```")
    return "\n".join(res)

updated_count = 0
for fpath in monster_files:
    with open(fpath, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Extract Database ID
    m_id = re.search(r'\|\s*\*\*Database ID\*\*\s*\|\s*`?([\d\.]+)', content)
    if not m_id:
        print(f"Warning: No Database ID in {fpath}")
        continue
    
    eid = int(float(m_id.group(1)))
    e = id_map.get(eid)
    if not e:
        print(f"Warning: ID {eid} not found in Excel ({fpath})")
        continue

    # 1. Update Section 3. Skill & Pola Aksi Giliran
    def rep_formula(m):
        f = m.group(1).strip()
        if f.startswith('Math.max(1,'):
            return f"`{f}`"
        elif f.startswith('Math.max(0,'):
            return f"`{f.replace('Math.max(0,', 'Math.max(1,')}`"
        elif 'a.atk' in f or 'a.mat' in f:
            return f"`Math.max(1, {f})`"
        return f"`{f}`"

    def rep_table_row(m):
        pre, elem, post = m.group(1), m.group(2), m.group(3)
        clean_el = clean_element(elem)
        return f"{pre}`{clean_el}`{post}"

    content = re.sub(r"(\|\s*\*\*[^*]+\*\*\s*\|\s*)`([^`]+)`(\s*/\s*[^|]+\|)", rep_table_row, content)
    content = re.sub(r"`(a\.atk[^`]+|a\.mat[^`]+|Math\.max\([^`]+)`", rep_formula, content)

    # 2. Add or Replace Konfigurasi AI Taktis
    ai_block = build_ai_block(e)
    
    if "#### B. Konfigurasi AI Taktis" in content:
        content = re.sub(r"#### B\. Konfigurasi AI Taktis[\s\S]*?(?=### 4\.|\Z)", ai_block + "\n\n", content)
    elif "### 3. Skill & Pola Aksi Giliran (AI Actions)" in content:
        parts = content.split("### 4. Traits & Resistensi Khusus")
        if len(parts) == 2:
            sec3 = parts[0]
            if "#### A. Daftar Skill & Syarat Pemicu" not in sec3:
                sec3 = sec3.replace("### 3. Skill & Pola Aksi Giliran (AI Actions)\n*Acuan resmi", "### 3. Skill & Pola Aksi Giliran (AI Actions)\n\n#### A. Daftar Skill & Syarat Pemicu\n*Acuan resmi")
            content = sec3.rstrip() + "\n\n" + ai_block + "\n\n### 4. Traits & Resistensi Khusus" + parts[1]

    with open(fpath, 'w', encoding='utf-8') as fp:
        fp.write(content)
    
    updated_count += 1

print(f"Successfully calibrated all {updated_count} / {len(monster_files)} monster files!")
