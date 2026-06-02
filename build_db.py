import os
import json

vault_dir = r"e:\Ananto\Emulatoid\Nusvanir"
wiki_dir = os.path.join(vault_dir, "Nusvanir_Wiki_App")
out_js = os.path.join(wiki_dir, "database.js")

db = []

for root, dirs, files in os.walk(vault_dir):
    if "Nusvanir_Wiki_App" in root or ".gemini" in root or ".system_generated" in root:
        continue
    for file in files:
        if file.endswith(".md") and file != "Nusvanir_Database.json":
            md_path = os.path.join(root, file)
            json_path = md_path[:-3] + ".json"
            
            with open(md_path, 'r', encoding='utf-8', errors='ignore') as f:
                md_content = f.read()
                
            rel_path = md_path[len(vault_dir)+1:]
            folder_path = os.path.dirname(rel_path).replace("\\", "/")
            if folder_path == "":
                folder_path = "Lainnya"
                
            entry = {
                "id": file[:-3],
                "filename": file,
                "filepath": rel_path.replace("\\", "/"),
                "folderPath": folder_path,
                "title": file[:-3].replace("_", " "),
                "content": md_content
            }
                
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8', errors='ignore') as jf:
                        json_data = json.load(jf)
                        entry.update(json_data)
                except Exception as e:
                    pass
                    
            db.append(entry)

with open(out_js, 'w', encoding='utf-8') as outf:
    outf.write("const nusvanirDB = " + json.dumps(db, ensure_ascii=False) + ";")
