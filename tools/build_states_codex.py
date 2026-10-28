import os
import sys
import re
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

EXCEL_PATH = 'Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx'
OUTPUT_FILE = '06_Sistem Game & Ekonomi/Kamus_State_&_Status_Efek.md'

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

print("Reading MV STATES sheet...")
raw_states = read_excel_sheet('MV STATES')
headers = raw_states[0]
state_rows = [dict(zip(headers, r)) for r in raw_states[1:] if len(r) > 1 and r[0].strip()]

# Filter canonical and skill effects
canonical = []
skill_effects = []

for s in state_rows:
    sid_raw = s.get('State ID', '')
    try:
        sid = int(float(sid_raw))
        if sid <= 226:
            canonical.append((sid, s))
        else:
            skill_effects.append((sid, s))
    except ValueError:
        pass

canonical.sort(key=lambda x: x[0])
skill_effects.sort(key=lambda x: x[0])

print(f"Loaded {len(canonical)} canonical states and {len(skill_effects)} skill effect states.")

md = []
md.append("---")
md.append("title: Kamus_State_&_Status_Efek")
md.append("tags:")
md.append("  - Sistem_Game_Ekonomi")
md.append("  - Combat_Engine")
md.append("  - States_Database")
md.append("  - Status_Effects")
md.append("  - Turn_Based_RPG")
md.append("---\n")
md.append("# 📜 Kamus Status Efek & State Tempur Nusvanir (ID 201 – 477)\n")
md.append("Dokumen ini adalah **kodifikasi resmi seluruh State, Status Efek, Buff, Debuff, Crowd Control (CC), dan Pasif** dalam game RPG *Turn-Based* Nusvanir.")
md.append("Seluruh entri dikonfigurasi secara presisi sesuai dengan parameter engine pada spreadsheet **`MV STATES`** dan terintegrasi dengan plugin **`YEP_BuffsStatesCore`** serta **`YEP_AutoPassiveStates`**.\n")
md.append("---\n")
md.append("## 🧭 1. Arsitektur & Aturan Sistem State Nusvanir\n")
md.append("### A. Pembagian 3 Kategori Besar State")
md.append("1. **Status Effect & Canonical States (ID 201 – 226):** Status penyakit umum, DoT (*Damage over Time*), Hard CC, debuff kerentanan, dan penanda afinitas yang dapat diterapkan oleh berbagai mantra, item, maupun serangan monster.")
md.append("2. **Skill Effect States (ID 301 – 477):** Efek temporer unik yang dipicu oleh skill spesifik kelas (*War Cry, Solid Stance, Iron Fortress, Barrier, Transformation*).")
md.append("3. **Passive States (Auto-Passive System):** Keahlian pasif permanen berdasarkan Ras, Class Mastery, atau Peralatan yang aktif otomatis tanpa hitungan durasi turn.\n")
md.append("### B. Parameter Mekanik Kunci")
md.append("* **Priority (Prioritas Tampilan 50–95):** Menentukan urutan ikon yang ditampilkan di atas kepala unit. State dengan nilai prioritas tertinggi (misal: Petrify 95, Stun 90) akan menimpa tampilan status berprioritas rendah (Slow 50).")
md.append("* **Restriction (Pembatasan Gerak):**")
md.append("  * `None`: Unit bebas bertindak normal.")
md.append("  * `Cannot Move`: Unit kehilangan giliran total (Stun, Freeze, Paralyze, Petrify).")
md.append("  * `Attack Anyone`: Unit kalap dan menyerang target acak tanpa membedakan kawan atau lawan (Confusion).")
md.append("* **Auto-Removal Timing:** Pengurangan durasi terjadi pada fase **Turn End** giliran unit.")
md.append("* **Remove by Damage:** Beberapa state mental (seperti *Sleep* atau *Confusion*) memiliki peluang terlepas seketika apabila target menerima kerusakan fisik.")
md.append("* **Boss Rule & Immunity:** Musuh berpangkat Boss memiliki imunitas bawaan (*State Rate = 0%*) terhadap *Instant Death* dan pengurangan durasi maksimal 1 turn untuk Hard CC.\n")
md.append("---\n")

# -------------------------------------------------------------
# 2. CANONICAL STATES (ID 201 - 226)
# -------------------------------------------------------------
md.append("## ☣️ 2. Status Efek Kanonikal (Canonical States: ID 201 – 226)\n")
md.append("| ID | Nama State | Kategori | Prioritas | Pembatasan (Restriction) | Durasi (Turn) | Lepas Saat Dipukul | Pengaruh & Traits Mekanis |")
md.append("|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---|")

for sid, s in canonical:
    name = s.get('State Name', '')
    cat = s.get('Category', '')
    prio = int(float(s.get('Priority', 0))) if s.get('Priority', '') else 0
    restr = s.get('Restriction', 'None')
    t_min = int(float(s.get('Min Turns', 0))) if s.get('Min Turns', '') else 0
    t_max = int(float(s.get('Max Turns', 0))) if s.get('Max Turns', '') else 0
    t_str = f"{t_min} T" if t_min == t_max else f"{t_min}-{t_max} T"
    dmg_rem = s.get('Remove by Damage', 'No')
    traits = s.get('Traits / Mechanical Setup', '-')
    md.append(f"| **{sid}** | **{name}** | `{cat}` | `{prio}` | `{restr}` | `{t_str}` | `{dmg_rem}` | {traits} |")

md.append("\n### Rincian Mendalam 26 Status Efek Kanonikal\n")

for sid, s in canonical:
    name = s.get('State Name', '')
    cat = s.get('Category', '')
    prio = int(float(s.get('Priority', 0))) if s.get('Priority', '') else 0
    restr = s.get('Restriction', 'None')
    t_min = int(float(s.get('Min Turns', 0))) if s.get('Min Turns', '') else 0
    t_max = int(float(s.get('Max Turns', 0))) if s.get('Max Turns', '') else 0
    rem_end = s.get('Remove at Battle End', 'Yes')
    rem_dmg = s.get('Remove by Damage', 'No')
    pct_dmg = s.get('Damage Removal %', '0')
    traits = s.get('Traits / Mechanical Setup', '-')
    boss = s.get('Boss Rule / Resistance', 'Normal')
    impl = s.get('Implementation', 'Native MV')
    notes = s.get('Notes', '-')

    md.append(f"#### 🔹 [{sid}] {name}")
    md.append(f"- **Kategori & Prioritas:** `{cat}` | Prioritas Tampilan: `{prio}`")
    md.append(f"- **Pembatasan Aksi (*Restriction*):** `{restr}`")
    md.append(f"- **Durasi Giliran:** `{t_min} – {t_max} Giliran (Turn End decay)`")
    md.append(f"- **Pelepasan Pertempuran:** Dihapus saat battle usai: `{rem_end}` | Lepas jika terkena damage: `{rem_dmg}` ({pct_dmg}%)")
    md.append(f"- **Mekanik & Pengaruh Parameter:** {traits}")
    if boss != 'Normal' and boss != '-':
        md.append(f"- **Aturan Boss:** ⚠️ **{boss}**")
    if notes != '-':
        md.append(f"- **Catatan Desain & Lore:** *\"{notes}\"*")
    md.append("\n")

# -------------------------------------------------------------
# 3. SKILL EFFECT STATES (ID 301 - 477)
# -------------------------------------------------------------
md.append("---\n")
md.append("## ⚡ 3. Status Efek Skill Khusus & Pasif Kelas (ID 301 – 477)\n")
md.append("Status efek berikut dipicu secara eksklusif oleh pohon skill profesi petualang atau auto-passive trait:\n")

# Group skill effects by class family if possible
md.append("| ID | Nama State Efek Skill | Kategori | Prioritas | Pembatasan | Durasi | Efek Modifikasi Parameter & Mekanik |")
md.append("|:---:|:---|:---:|:---:|:---:|:---:|:---|")

for sid, s in skill_effects:
    name = s.get('State Name', '')
    cat = s.get('Category', '')
    prio = int(float(s.get('Priority', 0))) if s.get('Priority', '') else 0
    restr = s.get('Restriction', 'None')
    t_min = int(float(s.get('Min Turns', 0))) if s.get('Min Turns', '') else 0
    t_max = int(float(s.get('Max Turns', 0))) if s.get('Max Turns', '') else 0
    t_str = "Permanen" if t_min == 0 and t_max == 0 else (f"{t_min} T" if t_min == t_max else f"{t_min}-{t_max} T")
    traits = s.get('Traits / Mechanical Setup', '-')
    md.append(f"| **{sid}** | **{name}** | `{cat}` | `{prio}` | `{restr}` | `{t_str}` | {traits} |")

md.append("\n### Rincian Roster Efek Skill Per Kategori Kelas\n")

for sid, s in skill_effects:
    name = s.get('State Name', '')
    cat = s.get('Category', '')
    prio = int(float(s.get('Priority', 0))) if s.get('Priority', '') else 0
    restr = s.get('Restriction', 'None')
    t_min = int(float(s.get('Min Turns', 0))) if s.get('Min Turns', '') else 0
    t_max = int(float(s.get('Max Turns', 0))) if s.get('Max Turns', '') else 0
    dur = "Permanen (Auto-Passive)" if t_min == 0 and t_max == 0 else f"{t_min} – {t_max} Giliran"
    traits = s.get('Traits / Mechanical Setup', '-')
    notes = s.get('Notes', '-')
    impl = s.get('Implementation', 'Native MV')

    md.append(f"#### 🔸 [{sid}] {name}")
    md.append(f"- **Kategori & Durasi:** `{cat}` | `{dur}` | Prioritas: `{prio}`")
    md.append(f"- **Efek Mekanik & Modifikator Stat:** {traits}")
    if notes != '-':
        md.append(f"- **Catatan Implementasi:** {notes} *(Engine: {impl})*")
    md.append("\n")

# Write output file
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("\n".join(md))

print(f"Kamus_State_&_Status_Efek.md generated successfully at {OUTPUT_FILE} ({len(md)} lines).")
