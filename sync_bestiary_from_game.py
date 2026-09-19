import json
import re
from pathlib import Path

root = Path(r"e:\Ananto\Emulatoid\Nusvanir")
enemy_db = root / "10_Game Project" / "Tales of The Dark Time" / "data" / "Enemies.json"
bestiary_root = root / "07_Bestiary"
skip_names = {
    "BESTIARY_REWORK_AUDIT.md",
    "BESTIARY_REWORK_CHANGELOG.md",
    "BESTIARY_STANDARD_V2.md",
    "CREATURE_TAXONOMY.md",
}

def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (value or "").lower())


def extract_note(note: str, tag: str):
    m = re.search(rf"<{re.escape(tag)}:\s*(.+?)>", note)
    if m:
        return m.group(1).strip()
    return "TBD"

with enemy_db.open("r", encoding="utf-8") as f:
    raw = json.load(f)

enemies = {}
for entry in raw:
    if not isinstance(entry, dict):
        continue
    name = (entry.get("name") or "").strip()
    if not name:
        continue
    enemies[normalize(name)] = entry

for md_path in sorted(bestiary_root.rglob("*.md")):
    if md_path.name in skip_names:
        continue
    key = normalize(md_path.stem)
    enemy = enemies.get(key)
    if not enemy:
        continue
    note = enemy.get("note", "")
    group = extract_note(note, "NUSV Bestiary Group")
    rank = extract_note(note, "NUSV Enemy Rank")
    tier = extract_note(note, "NUSV Tier")
    region = extract_note(note, "NUSV Region")
    element = extract_note(note, "NUSV Element")
    weakness = extract_note(note, "NUSV Weakness")
    attack_type = extract_note(note, "NUSV Attack Type")
    params = enemy.get("params") or [0] * 8
    if len(params) < 8:
        params = params + [0] * (8 - len(params))
    hp = int(params[0])
    mp = int(params[1])

    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"\*\*Elemen:\*\*\s*.+", f"**Elemen:** {element}", text, count=1)
    text = re.sub(r"\*\*Kelemahan:\*\*\s*.+", f"**Kelemahan:** {weakness}", text, count=1)
    text = re.sub(r"\*\*Tipe Serangan:\*\*\s*.+", f"**Tipe Serangan:** {attack_type}", text, count=1)
    text = re.sub(r"\*\*HP:\*\*\s*\d+", f"**HP:** {hp}", text, count=1)
    text = re.sub(r"\*\*MP:\*\*\s*\d+", f"**MP:** {mp}", text, count=1)
    text = re.sub(r"\*\*Spawn Location:\*\*\s*.+", f"**Spawn Location:** {region}", text, count=1)

    status_block = (
        "\n**Status:** VERIFIED (matched runtime data in game project)\n"
        f"**Category:** {group}\n"
        f"**Enemy Rank:** {rank}\n"
        f"**Tier:** {tier}\n"
        f"**Verified Source:** 10_Game Project/Tales of The Dark Time/data/Enemies.json\n"
        f"**Runtime Values:** HP {hp} / MP {mp} / Element {element} / Weakness {weakness} / Attack Type {attack_type}\n\n"
    )
    if "**Status:**" in text:
        text = re.sub(r"\*\*Status:\*\*.*?\n\n(?=### Deskripsi)", status_block, text, count=1, flags=re.S)
    else:
        text = text.replace("### Deskripsi\n", status_block + "### Deskripsi\n", 1)
    md_path.write_text(text, encoding="utf-8")

for json_path in sorted(bestiary_root.rglob("*.json")):
    if json_path.name in {"BESTIARY_REWORK_AUDIT.md", "BESTIARY_REWORK_CHANGELOG.md", "BESTIARY_STANDARD_V2.md", "CREATURE_TAXONOMY.md"}:
        continue
    # File checks not for docs, but only relevant JSONs with same names as enemies
    try:
        obj = json.loads(json_path.read_text(encoding="utf-8"))
    except Exception:
        continue
    key = normalize(obj.get("title") or obj.get("id") or json_path.stem)
    enemy = enemies.get(key)
    if not enemy:
        continue
    note = enemy.get("note", "")
    group = extract_note(note, "NUSV Bestiary Group")
    rank = extract_note(note, "NUSV Enemy Rank")
    tier = extract_note(note, "NUSV Tier")
    region = extract_note(note, "NUSV Region")
    element = extract_note(note, "NUSV Element")
    weakness = extract_note(note, "NUSV Weakness")
    attack_type = extract_note(note, "NUSV Attack Type")
    params = enemy.get("params") or [0] * 8
    if len(params) < 8:
        params = params + [0] * (8 - len(params))
    hp = int(params[0])
    mp = int(params[1])

    legacy = {
        "hp": obj.get("hp"),
        "mp": obj.get("mp"),
        "element": obj.get("element"),
        "weakness": obj.get("weakness"),
        "attack_type": obj.get("attack_type"),
        "location": obj.get("location"),
    }

    obj["category"] = group
    obj["rank"] = rank
    obj["tier"] = tier
    obj["element"] = element
    obj["weakness"] = weakness
    obj["attack_type"] = attack_type
    obj["hp"] = hp
    obj["mp"] = mp
    obj["location"] = region
    obj["stat_status"] = "VERIFIED"
    obj["balance_status"] = "VERIFIED"
    obj["source_status"] = "runtime_game_data"
    obj["verified_source"] = "10_Game Project/Tales of The Dark Time/data/Enemies.json"
    obj["legacy_values"] = legacy
    obj["runtime_values"] = {
        "hp": hp,
        "mp": mp,
        "element": element,
        "weakness": weakness,
        "attack_type": attack_type,
        "region": region,
    }
    json_path.write_text(json.dumps(obj, ensure_ascii=False, indent=4), encoding="utf-8")

print("Bestiary synced to game runtime data for matching enemy names.")
