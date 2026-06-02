import os

vault = r"e:\Ananto\Emulatoid\Nusvanir"

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
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
