import os
import subprocess

vault = r"e:\Ananto\Emulatoid\Nusvanir"

# 1. First rename files and directories using git mv
items = [
    r"02_World\Pulau_Kegelapan_Raksamala.json",
    r"02_World\Raksamala.md",
    r"03_Region\10_Raksamala",
    r"05_Karakter & Tokoh Penting\09_Raksamala",
    r"07_Bestiary\08_Commanders_of_Raksamala_Fortress",
    r"08_Story\02_Prologue\12_Kisah_Cinta_dan_Kutukan_Raksamala.md"
]

for item in items:
    src = os.path.join(vault, item)
    dst = os.path.join(vault, item.replace("Raksamala", "Raksmala"))
    if os.path.exists(src):
        print(f"Renaming {src} to {dst}")
        subprocess.run(["git", "mv", src, dst], cwd=vault)

# 2. Update contents of all markdown and json files
for root, dirs, files in os.walk(vault):
    if ".git" in root or ".obsidian" in root or "Nusvanir_Wiki_App" in root:
        continue
    for file in files:
        if file.endswith(".md") or file.endswith(".json"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            new_content = content.replace("Raksamala", "Raksmala")
            new_content = new_content.replace("raksamala", "raksmala")
            
            # Change Saka Kencana to Saka Rajata only in 08_Story
            if "08_Story" in root:
                new_content = new_content.replace("Saka Kencana", "Saka Rajata")
                
            if new_content != content:
                print(f"Updating content of {path}")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
