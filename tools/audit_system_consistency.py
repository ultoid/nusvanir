import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

findings = []

def audit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.splitlines()

    relpath = os.path.relpath(filepath, '.')

    # 1. Check TP mentions
    for idx, line in enumerate(lines, 1):
        # find standalone TP
        if re.search(r'\bTP\b', line):
            # allow sentences like "menggantikan sistem TP", "menggantikan TP menjadi Stamina Points", "TP Gain" in items table headers if explaining
            if re.search(r'(menggantikan|mengubah|replace|tradisional).*TP', line, re.IGNORECASE):
                continue
            if 'TP System: Digantikan' in line or 'Sistem SP (Stamina Points): Menggantikan TP' in line:
                continue
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'TP vs SP Inconsistency',
                'detail': line.strip()
            })

    # 2. Check for old letter rank parameters (MHP: A, MMP: B, etc.)
    for idx, line in enumerate(lines, 1):
        if re.search(r'MHP:\s*[A-S]\b', line):
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'Old Letter Rank Parameters',
                'detail': line.strip()
            })

    # 3. Check for outdated BLOCKED / Missing Data statements that contradict established rules
    for idx, line in enumerate(lines, 1):
        if 'BLOCKED' in line and ('Pedoman' in filepath or 'MONSTER_BALANCE' in filepath or 'CODEX_MASTER' in filepath):
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'Outdated Governance / BLOCKED Status',
                'detail': line.strip()
            })
        if 'belum menyediakan kurva parameter' in line or 'belum memuat database runtime' in line:
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'Outdated Missing Database Claim',
                'detail': line.strip()
            })

    # 4. Check for Action RPG or Real-Time remnants
    for idx, line in enumerate(lines, 1):
        if re.search(r'\b(action\s*rpg|real-?time|realtime)\b', line, re.IGNORECASE):
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'Action RPG / Real-time Remnant',
                'detail': line.strip()
            })

    # 5. Check for old Level Cap contradictions (e.g. Level 99 without Tier caps)
    for idx, line in enumerate(lines, 1):
        if re.search(r'\bmaks\s*99\b|\blevel\s*99\b', line, re.IGNORECASE) and 'MONSTER_BALANCE' in filepath:
            findings.append({
                'file': relpath,
                'line': idx,
                'category': 'Level 99 without Tier Cap',
                'detail': line.strip()
            })

# Scan 06_Sistem Game & Ekonomi
for root, dirs, files in os.walk('06_Sistem Game & Ekonomi'):
    for f in files:
        if f.endswith('.md'):
            audit_file(os.path.join(root, f))

# Scan 07_Bestiary
for root, dirs, files in os.walk('07_Bestiary'):
    for f in files:
        if f.endswith('.md') and not f.startswith('.'):
            audit_file(os.path.join(root, f))

print(f"Total audit findings: {len(findings)}")
by_cat = {}
for item in findings:
    c = item['category']
    if c not in by_cat: by_cat[c] = []
    by_cat[c].append(item)

for c, items in by_cat.items():
    print(f"\n=== CATEGORY: {c} ({len(items)} issues) ===")
    for it in items[:10]:
        print(f"  [{it['file']}:{it['line']}] {it['detail'][:100]}")
    if len(items) > 10:
        print(f"  ... and {len(items)-10} more")

