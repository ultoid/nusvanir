import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent / "07_Bestiary"
skip_names = {
    "BESTIARY_REWORK_AUDIT.md",
    "BESTIARY_REWORK_CHANGELOG.md",
    "BESTIARY_STANDARD_V2.md",
    "CREATURE_TAXONOMY.md",
}


def infer_category(path: Path):
    rel = str(path.relative_to(root))
    if "01_Alam_Liar" in rel:
        return "01 Alam Liar", "Wildlife"
    if "02_Jenggala" in rel:
        return "02 Jenggala", "Jenggala"
    if "03_Thalantira" in rel:
        return "03 Thalantira", "Voidborn / Aberration (provisional)"
    if "04_Guardians_of_Avalerion_Outpost" in rel:
        return "04 Guardians of Avalerion Outpost", "Guardian / Elite"
    if "05_Dragons_of_Agnitra_Nest" in rel:
        return "05 Dragons of Agnitra Nest", "Dragon / Apex Predator"
    if "06_Chiefs_of_Arkananta" in rel:
        return "06 Chiefs of Arkananta", "Authority / Chieftain"
    if "07_Sentinels_of_Nusa_Sayendra" in rel:
        return "07 Sentinels of Nusa Sayendra", "Sentinel / Commander"
    if "08_Commanders_of_Raksamala_Fortress" in rel:
        return "08 Commanders of Raksamala Fortress", "Commander / Infernal"
    if "09_Laut_Rangkaruna" in rel:
        return "09 Laut Rangkaruna", "Sea Beast / Abyssal"
    return "Bestiary", "Unclassified"


for p in sorted(root.rglob("*.md")):
    if p.name in skip_names:
        continue
    text = p.read_text(encoding="utf-8")
    if "**Status:**" in text:
        continue

    category, creature_type = infer_category(p)
    hp = re.search(r"\*\*HP:\*\*\s*(\d+)", text)
    mp = re.search(r"\*\*MP:\*\*\s*(\d+)", text)
    ele = re.search(r"\*\*Elemen:\*\*\s*(.+)", text)
    weak = re.search(r"\*\*Kelemahan:\*\*\s*(.+)", text)
    loc = re.search(r"\*\*Spawn Location:\*\*\s*(.+)", text)
    region = loc.group(1).strip() if loc else "TBD"
    hp_val = hp.group(1) if hp else "TBD"
    mp_val = mp.group(1) if mp else "TBD"
    ele_val = ele.group(1).strip() if ele else "TBD"
    weak_val = weak.group(1).strip() if weak else "TBD"

    block = (
        "\n**Status:** BLOCKED (legacy candidate; angka tetap untuk traceability, bukan final)\n"
        f"**Category:** {category}\n"
        f"**Creature Type:** {creature_type}\n"
        f"**Region:** {region}\n"
        "**Biome:** TBD\n"
        "**Encounter Type:** TBD\n"
        "**Combat Role:** TBD\n"
        "**Stat Status:** BLOCKED\n"
        f"**Legacy Values:** HP {hp_val} / MP {mp_val} / Element {ele_val} / Weakness {weak_val}\n\n"
    )

    if "### Deskripsi" in text:
        text = text.replace("### Deskripsi\n", block + "### Deskripsi\n", 1)
    else:
        text += "\n### Deskripsi\n" + block
    p.write_text(text, encoding="utf-8")

for p in sorted(root.rglob("*.json")):
    if p.name in skip_names:
        continue
    try:
        obj = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        continue
    if obj.get("stat_status") == "BLOCKED":
        continue

    category, creature_type = infer_category(p)
    obj["category"] = category
    obj["creature_type"] = creature_type
    obj["encounter_type"] = "TBD"
    obj["combat_role"] = "TBD"
    obj["stat_status"] = "BLOCKED"
    obj["balance_status"] = "BLOCKED"
    obj["legacy_values"] = {
        "hp": obj.get("hp"),
        "mp": obj.get("mp"),
        "element": obj.get("element"),
        "weakness": obj.get("weakness"),
    }
    obj["source_status"] = "legacy_candidate"
    obj["region"] = obj.get("location", "TBD")
    obj["biome"] = "TBD"
    obj["notes"] = "Angka numerik lama disimpan untuk traceability; status final ditahan sampai baseline progression dan formula skill tersedia."
    if "description" in obj and "ecology" not in obj:
        obj["ecology"] = "TBD"
    if "description" in obj and "behavior" not in obj:
        obj["behavior"] = "TBD"
    if "description" in obj and "relationship_with_civilization" not in obj:
        obj["relationship_with_civilization"] = "TBD"
    if "description" in obj and "drops" not in obj:
        obj["drops"] = "TBD"
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=4), encoding="utf-8")

print("Processed all Bestiary markdown and json files.")
