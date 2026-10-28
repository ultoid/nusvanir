import os
import glob
import re

WEAPON_MAP = {
    "Long Sword": "01 Long Sword",
    "Sword": "02 Sword",
    "Gloves": "03 Gloves",
    "Glove": "03 Gloves",
    "Claw": "03 Gloves",
    "Spear": "04 Spear",
    "Axe": "05 Axe",
    "Greataxe": "05 Axe",
    "Greatsword": "01 Long Sword",
    "Staff": "06 Staff",
    "Rune": "07 Rune",
    "Long Bow": "08 Long Bow",
    "Bow": "08 Long Bow",
    "Crossbow": "09 Crossbow",
    "Dagger": "10 Dagger",
}

ARMOR_MAP = {
    "Basic Clothes": "01 Basic Clothes",
    "Basic Armor": "01 Basic Clothes",
    "Magic Robe": "02 Magic Robe",
    "Robe": "02 Magic Robe",
    "Light Armor": "03 Light Armor",
    "Heavy Armor": "04 Heavy Armor",
    "Light Shield": "05 Light Shield",
    "Small Shield": "05 Light Shield",
    "Heavy Shield": "06 Heavy Shield",
    "Large Shield": "06 Heavy Shield",
}

ELEMENT_MAP = {
    "None / Neutral": "01 Neutral",
    "Normal Attack": "01 Neutral",
    "Fire": "02 Fire",
    "Water": "03 Water",
    "Earth": "04 Earth",
    "Wind": "05 Air",
    "Air": "05 Air",
    "Lightning": "06 Electric",
    "Electric": "06 Electric",
    "Ice": "07 Ice",
    "Metal": "08 Steel",
    "Steel": "08 Steel",
    "Sonic": "09 Sound",
    "Sound": "09 Sound",
    "Holy": "10 Holy",
    "Dark": "11 Dark",
    "Dragon": "01 Neutral",
}

def clean_items(text, mapping):
    # Strip any existing leading numbers
    parts = [p.strip() for p in text.split(",")]
    out = []
    seen = set()
    for p in parts:
        # strip markdown formatting
        p_clean = re.sub(r"^\d{2}\s+", "", p).strip()
        # Find match
        matched = False
        # Sort keys by descending length
        for k in sorted(mapping.keys(), key=lambda x: -len(x)):
            if k.lower() in p_clean.lower():
                val = mapping[k]
                if val not in seen:
                    seen.add(val)
                    out.append(val)
                matched = True
                break
        if not matched and p_clean:
            if p_clean not in seen:
                seen.add(p_clean)
                out.append(p_clean)
    return ", ".join(out)

def update_class_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    is_fisik = "01_Jalur_Fisik" in file_path
    is_sihir = "02_Jalur_Sihir" in file_path
    is_lincah = "03_Jalur_Lincah" in file_path
    fname = os.path.basename(file_path)

    # 1. Update Weapons line
    def rep_weapon(m):
        prefix = m.group(1)
        items = m.group(2)
        return f"{prefix} {clean_items(items, WEAPON_MAP)}"

    content = re.sub(r"(\*\s*\*\*Senjata yang Dapat Digunakan(?:\s*\(Weapon Types\))?:\*\*)(.*)", rep_weapon, content)

    # 2. Update Armors line
    def rep_armor(m):
        prefix = m.group(1)
        items = m.group(2)
        return f"{prefix} {clean_items(items, ARMOR_MAP)}"

    content = re.sub(r"(\*\s*\*\*Zirah & Pelindung(?:\s*\(Armor Types\))?:\*\*)(.*)", rep_armor, content)

    # 3. Update Table Rows
    lines = content.split("\n")
    new_lines = []
    active_types = set()

    for line in lines:
        # Check table row
        # Example: | **1.0** | **Heavy Slash** | `Physical` / `Normal Attack` | ...
        m_row = re.match(r"^(\s*\|\s*\*\*[\d\.]+\*\*\s*\|\s*\*\*[^*]+\*\*\s*\|\s*)`([^`]+)`\s*/\s*`([^`]+)`(.*)$", line)
        if m_row:
            pre, stype, selem, post = m_row.group(1), m_row.group(2).strip(), m_row.group(3).strip(), m_row.group(4)
            skill_name_m = re.search(r"\*\*([^*]+)\*\*", pre)
            skill_name = skill_name_m.group(1).strip() if skill_name_m else ""

            # Map stype
            new_type = stype
            if stype == "Physical":
                new_type = "03 Skill"
            elif stype == "Support":
                if skill_name in ["Call of Nature: Falcon"]:
                    new_type = "04 Summon"
                elif skill_name in ["Bulwark of Light", "Sanctuary of Light", "Divine Citadel"]:
                    new_type = "01 White Magic"
                elif is_fisik or is_lincah:
                    new_type = "03 Skill"
                elif is_sihir:
                    if any(c in fname for c in ["Acolyte", "Cleric", "Priest"]):
                        new_type = "01 White Magic"
                    else:
                        new_type = "02 Black Magic"
            elif stype == "Dark Magic":
                new_type = "02 Black Magic"
            elif stype == "Transformation":
                if "Dragoon" in fname:
                    new_type = "03 Skill"
                else:
                    new_type = "05 Ultimate"
            elif stype == "Summon":
                new_type = "04 Summon"
            elif stype == "Ultimate" or stype == "05 Ultimate":
                new_type = "05 Ultimate"
            elif stype == "White Magic" or stype == "01 White Magic":
                new_type = "01 White Magic"
            elif stype == "Black Magic" or stype == "02 Black Magic":
                new_type = "02 Black Magic"
            elif stype == "Skill" or stype == "03 Skill":
                new_type = "03 Skill"
            elif stype == "Passive":
                new_type = "Passive"

            if new_type in ["01 White Magic", "02 Black Magic", "03 Skill", "04 Summon", "05 Ultimate"]:
                active_types.add(new_type)

            # Map element
            new_elem = ELEMENT_MAP.get(selem, "01 Neutral")
            
            # Map Math.max(0, to Math.max(1,
            post = post.replace("Math.max(0,", "Math.max(1,")
            post = post.replace("b.def * 0.5 (Crit: Yes)", "b.def * 0.75 (Crit: Yes)")

            new_line = f"{pre}`{new_type}` / `{new_elem}`{post}"
            new_lines.append(new_line)
        else:
            # Also check Math.max(0 in other lines
            line = line.replace("Math.max(0,", "Math.max(1,")
            new_lines.append(line)

    # 4. Update Tipe Skill yang Dibuka line
    sorted_types = sorted(list(active_types))
    types_str = ", ".join(sorted_types) if sorted_types else "03 Skill, 05 Ultimate"
    
    final_lines = []
    for line in new_lines:
        if "Tipe Skill yang Dibuka" in line:
            final_lines.append(f"* **Tipe Skill yang Dibuka (Skill Types):** `{types_str}` *(Skill pasif aktif otomatis via YEP_AutoPassiveStates)*")
        else:
            final_lines.append(line)

    new_content = "\n".join(final_lines)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Tool update_classes_types.py ready.")
