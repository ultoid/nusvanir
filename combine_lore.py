import os

directories = [
    "00_Kosmologi & Sejarah",
    "01_Hukum Sihir",
    "02_World",
    "03_Region",
    "04_Ras",
    "05_Karakter & Tokoh Penting",
    "06_Sistem Game & Ekonomi",
    "07_Bestiary",
    "08_Story"
]

output_file = "all_lore_combined.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for d in directories:
        if not os.path.exists(d):
            print(f"Directory not found: {d}")
            continue
        
        for root, _, files in os.walk(d):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    out.write(f"\n\n{'='*50}\n")
                    out.write(f"FILE: {filepath}\n")
                    out.write(f"{'='*50}\n\n")
                    with open(filepath, "r", encoding="utf-8") as f:
                        out.write(f.read())

print("Done combining lore.")
