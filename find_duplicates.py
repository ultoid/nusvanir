import os
import json
import re
from collections import defaultdict

db_file = r"e:\Nusvanir_Vault\Nusvanir_Wiki_App\database.js"

with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract JSON from JS file
json_str = content.replace("const nusvanirDB = ", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

db = json.loads(json_str)

titles = defaultdict(list)
words_map = defaultdict(list)

stop_words = {"di", "dari", "yang", "dan", "sang", "penjaga", "raksasa", "kematian", "laut", "hutan", "nusa", "kota", "desa", "pulau", "raja", "ratu", "ksatria"}

for entry in db:
    title = entry['title'].lower().strip()
    path = entry['filepath']
    
    # Check exact title match
    titles[title].append(path)
    
    # Check word level match for finding overlapping base names (like Hydra vs Hydra Jurang)
    words = re.findall(r'\b\w+\b', title)
    for w in words:
        if w not in stop_words and len(w) > 3:
            words_map[w].append((title, path))

print("=== EXACT OR VERY SIMILAR TITLES ===")
for t, paths in titles.items():
    if len(paths) > 1:
        print(f"Title: '{t}' found in:")
        for p in paths:
            print(f"  - {p}")
            
print("\n=== POTENTIAL NAME COLLISIONS (Shared Words) ===")
# Find words that appear in multiple DIFFERENT titles
for w, items in words_map.items():
    unique_titles = list(set([i[0] for i in items]))
    if len(unique_titles) > 1 and len(unique_titles) <= 5: # Limit to avoid common words
        print(f"\nWord: '{w}' appears in:")
        for t, p in items:
            print(f"  - [{t}] : {p}")
