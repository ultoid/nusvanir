import os
import json

db_file = r"e:\Nusvanir_Vault\Nusvanir_Wiki_App\database.js"

with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

json_str = content.replace("const nusvanirDB = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

db = json.loads(json_str)

print("Searching for Leviathan/Leviatan in content:")
for entry in db:
    text = entry['content'].lower()
    if "leviat" in text:
        print(f"Found in: {entry['filepath']}")
        
print("Searching for other overlapping names in content:")
