import os
import sys
import re
import openpyxl

# Force UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

EXCEL_PATH = 'Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx'
OUTPUT_DIR = '06_Sistem Game & Ekonomi/Items'
os.makedirs(OUTPUT_DIR, exist_ok=True)

wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)

# -------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------
def format_saka(tamra_val):
    if tamra_val is None or tamra_val == 0:
        return '0 Saka (Tidak Dijual / Bebas)'
    val = int(tamra_val)
    kencana = val // 10000
    rem = val % 10000
    rajata = rem // 100
    tamra = rem % 100
    
    parts = []
    if kencana > 0:
        parts.append(f'{kencana} Kencana')
    if rajata > 0:
        parts.append(f'{rajata} Rajata')
    if tamra > 0:
        parts.append(f'{tamra} Tamra')
    
    formatted = ' '.join(parts) if parts else '0 Tamra'
    return f'{formatted} ({val:,} Tamra)'

def format_saka_short(tamra_val):
    if tamra_val is None or tamra_val == 0:
        return '0 Saka'
    val = int(tamra_val)
    kencana = val // 10000
    rem = val % 10000
    rajata = rem // 100
    tamra = rem % 100
    
    parts = []
    if kencana > 0:
        parts.append(f'{kencana}K')
    if rajata > 0:
        parts.append(f'{rajata}R')
    if tamra > 0:
        parts.append(f'{tamra}T')
    
    return ' '.join(parts) if parts else '0T'

def rarity_badge(r):
    badges = {
        'Common': '⚪ Common',
        'Uncommon': '🟢 Uncommon',
        'Rare': '🔵 Rare',
        'Epic': '🟣 Epic',
        'Legendary': '🟡 Legendary',
        'Mythic': '🔴 Mythic'
    }
    return badges.get(r, f'⚪ {r}')

# -------------------------------------------------------------
# 1. PARSE WEAPON & ARMOR RECIPES
# -------------------------------------------------------------
material_recipes = {}

def parse_recipe(recipe_str, item_name, item_type):
    if not recipe_str or recipe_str in ['NOT CRAFTABLE', 'None', '-']:
        return
    parts = str(recipe_str).split('+')
    for p in parts:
        p = p.strip()
        m = re.match(r'^(.*?)\s*[×x*]\s*(\d+)$', p)
        if m:
            mat = m.group(1).strip()
            qty = int(m.group(2))
        else:
            mat = p
            qty = 1
        if mat not in material_recipes:
            material_recipes[mat] = []
        material_recipes[mat].append(f'{item_name} ({item_type}, butuh {qty}x)')

w_sheet = wb['NUSV-WEAPON']
for row in w_sheet.iter_rows(min_row=2, values_only=True):
    name = row[1]
    recipe = row[6]
    w_type = row[2]
    parse_recipe(recipe, name, f'Senjata {w_type}')

a_sheet = wb['NUSV-ARMOR']
for row in a_sheet.iter_rows(min_row=2, values_only=True):
    name = row[1]
    recipe = row[8]
    a_slot = row[2]
    parse_recipe(recipe, name, f'Armor {a_slot}')

# -------------------------------------------------------------
# 2. PARSE ENEMY DROPS
# -------------------------------------------------------------
enemy_drops = {}
e_sheet = wb['NUSV-ENEMIES']
for row in e_sheet.iter_rows(min_row=2, values_only=True):
    if not any(row): continue
    enemy_name = row[1]
    region = row[8]
    for drop_col, rate_col in [(37, 38), (39, 40), (41, 42), (43, 44)]:
        drop_item = row[drop_col]
        drop_rate = row[rate_col]
        if drop_item and str(drop_item).strip() not in ['None', '', '-']:
            drop_item = str(drop_item).strip()
            if drop_item not in enemy_drops:
                enemy_drops[drop_item] = []
            rate_str = f'{int(float(drop_rate)*100)}%' if drop_rate is not None and isinstance(drop_rate, (int, float)) else str(drop_rate)
            enemy_drops[drop_item].append((enemy_name, region, rate_str))

# -------------------------------------------------------------
# 3. LOAD ALL ITEMS
# -------------------------------------------------------------
items_sheet = wb['NUSV-ITEMS']
items_by_cat = {
    'Consumable': [],
    'Material': [],
    'Forge': [],
    'Valuable': [],
    'Key Item': []
}

for row in items_sheet.iter_rows(min_row=3, values_only=True):
    if not any(row): continue
    it = {
        'name': str(row[0]).strip() if row[0] else '',
        'category': str(row[1]).strip() if row[1] else '',
        'subcategory': str(row[2]).strip() if row[2] else '',
        'rarity': str(row[3]).strip() if row[3] else 'Common',
        'desc': str(row[4]).strip() if row[4] else '',
        'price': float(row[5]) if row[5] is not None else 0.0,
        'sell_price': float(row[6]) if row[6] is not None else 0.0,
        'source': str(row[7]).strip() if row[7] else '',
        'region': str(row[8]).strip() if row[8] else '',
        'item_type': str(row[9]).strip() if row[9] else 'Regular Item',
        'consumable': str(row[10]).strip() if row[10] else 'No',
        'scope': str(row[11]).strip() if row[11] else 'None',
        'occasion': str(row[12]).strip() if row[12] else 'Never',
        'speed': row[13],
        'success': row[14],
        'repeat': row[15],
        'tp_gain': row[16],
        'hit_type': str(row[17]).strip() if row[17] else 'None',
        'damage_type': str(row[18]).strip() if row[18] else 'None',
        'element': str(row[19]).strip() if row[19] else 'None',
        'formula': str(row[20]).strip() if row[20] else 'None',
        'variance': row[21],
        'critical': row[22],
        'effects': str(row[23]).strip() if row[23] else 'None',
        'notetag': str(row[24]).strip() if row[24] else 'None',
        'remarks': str(row[25]).strip() if row[25] else ''
    }
    if it['category'] in items_by_cat:
        items_by_cat[it['category']].append(it)

# -------------------------------------------------------------
# BUILD 01_CONSUMABLES.MD
# -------------------------------------------------------------
def build_consumables():
    items = items_by_cat['Consumable']
    
    subcat_map = {
        'Recovery - HP': '1. Ramuan Pemulih HP (Health Recovery)',
        'Recovery - MP': '2. Ramuan Pemulih MP (Mana Recovery)',
        'Recovery - HP+MP': '3. Ramuan Pemulih Campuran (Elixir HP + MP)',
        'Recovery - SP': '4. Ramuan Pemulih SP (Stamina Points Recovery)',
        'Revival': '5. Ramuan Kebangkitan (Revival & Anti-Death)',
        'Status Cure': '6. Obat & Penawar Status Ailment',
        'Battle Buff': '7. Tonik Penguat Tempur (Battle Stat Tonics)',
        'Magic Scroll': '8. Gulungan Sihir Tempur (Combat Magic Scrolls)'
    }
    
    subcat_tactics = {
        'Recovery - HP': 'Memulihkan Hit Points secara instan dalam pertarungan turn-based atau saat eksplorasi menu.',
        'Recovery - MP': 'Memulihkan Mana Points untuk menjaga ketersediaan spellcaster (Mage, Cleric, Cultist).',
        'Recovery - HP+MP': 'Pemulihan ganda darurat tingkat tinggi untuk skenario boss battle yang intens.',
        'Recovery - SP': 'Memulihkan Stamina Points (SP) karakter fisik untuk mengeksekusi skill jurus dan kombo fisik tanpa henti.',
        'Revival': 'Membangkitkan sekutu dari status Death/Knockout dalam giliran tempur.',
        'Status Cure': 'Menghilangkan status abnormal spesifik (Bleed, Burn, Poison, Chill, Paralyze, Confusion, Silence, Blind, Curse).',
        'Battle Buff': 'Memberikan peningkatan atribut sementara (+25% / 1 Stage Buff) selama pertempuran (3-5 Turn).',
        'Magic Scroll': 'Memicu mantra sihir elemental langsung ke target musuh tanpa menghabiskan MP pengguna (skala MAT caster).'
    }

    md = []
    md.append('# 🧪 Database Item: Consumables (Barang Konsumsi)')
    md.append('\nDokumen ini mencakup seluruh **Item Konsumsi (Consumables)** dalam dunia Nusvanir yang dapat digunakan oleh karakter selama pertempuran (*Turn-Based Combat*) maupun di luar pertempuran (*Field/Menu*).')
    md.append('\n> [!NOTE]\n> **Aturan Mekanik Pertempuran Turn-Based Nusvanir:**\n> - Menggunakan item dalam pertempuran mengonsumsi **1 Tindakan Giliran (Action Turn)** karakter.\n> - Item pemulihan SP (*Focus Drop / Essence / Elixir*) sangat krusial bagi kelas fisik (*Fighter, Warrior, Rogue, Martial Artist*) karena sistem turn-based mempertahankan SP (*Preserve SP*) antar pertempuran.')
    md.append('\n---\n')

    grouped = {}
    for it in items:
        sub = it['subcategory']
        if sub not in grouped: grouped[sub] = []
        grouped[sub].append(it)

    for subcat_key, section_title in subcat_map.items():
        if subcat_key not in grouped: continue
        sub_items = grouped[subcat_key]
        md.append(f'## {section_title}\n')
        md.append(f'{subcat_tactics.get(subcat_key, "")}\n')
        
        md.append('| Nama Item | Rarity | Target / Scope | Penggunaan | Harga Beli | Harga Jual | Efek Utama |')
        md.append('|---|---|---|---|---|---|---|')
        for it in sub_items:
            md.append(f"| **{it['name']}** | {rarity_badge(it['rarity'])} | {it['scope']} | {it['occasion']} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | {it['effects']} |")
        md.append('\n')

        for it in sub_items:
            md.append(f"### 🔹 {it['name']}")
            md.append(f"- **Kategori / Subkategori:** Consumable / `{it['subcategory']}`")
            md.append(f"- **Tingkat Kelangkaan (Rarity):** {rarity_badge(it['rarity'])}")
            md.append(f"- **Harga Beli Pasar:** {format_saka(it['price'])}")
            md.append(f"- **Harga Jual Standar (40%):** {format_saka(it['sell_price'])}")
            md.append(f"- **Target Penggunaan (Scope):** `{it['scope']}`")
            md.append(f"- **Waktu Penggunaan (Occasion):** `{it['occasion']}`")
            md.append(f"- **Deskripsi Lore:** *\"{it['desc']}\"*")
            md.append(f"- **Efek Mekanik Game:** **{it['effects']}**")
            if it['formula'] and it['formula'] != 'None':
                md.append(f"- **Formula Efek / Damage:** `{it['formula']}`")
            if it['element'] and it['element'] != 'None':
                md.append(f"- **Elemen Kerusakan:** `{it['element']}`")
            md.append(f"- **Sumber Perolehan:** {it['source']} ({it['region']})")
            if it['remarks']:
                md.append(f"- **Catatan Implementasi:** {it['remarks']}")
            md.append('\n')

    out_path = os.path.join(OUTPUT_DIR, '01_Consumables.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path} ({len(items)} items)")

# -------------------------------------------------------------
# BUILD 02_MATERIALS.MD
# -------------------------------------------------------------
def build_materials():
    items = items_by_cat['Material']
    
    # Define cohesive thematic groups for all 44 material subcategories
    groups = [
        {
            'title': '1. Logam & Bijih Tambang (Ores & Metals)',
            'desc': 'Mineral logam murni yang ditambang dari perut bumi Nusvanir untuk penempaan senjata tajam dan baju zirah berat.',
            'subcats': ['Ore']
        },
        {
            'title': '2. Kayu & Ranting Keramat (Woods & Timber)',
            'desc': 'Kayu pilihan dari hutan-hutan purba Nusvanir (Mandala, Astradipa, Asrivana) untuk tangkai busur, tongkat sihir, dan perisai.',
            'subcats': ['Wood']
        },
        {
            'title': '3. Batuan & Mineral Geologis (Stones & Geological Minerals)',
            'desc': 'Batuan keras dan mineral alam yang memiliki resonansi elemen alami untuk fondasi perisai, helm batu, dan jimat.',
            'subcats': ['Stone']
        },
        {
            'title': '4. Tumbuhan Herbal & Flora Alkimia (Herbs & Flora)',
            'desc': 'Tanaman berkhasiat medis dan magis yang dikumpulkan oleh petualang untuk diracik menjadi ramuan penyembuh dan penawar racun.',
            'subcats': ['Herb']
        },
        {
            'title': '5. Serat Alami & Benang Tenun (Fibers & Threads)',
            'desc': 'Serat nabati dan benang sutra mistis untuk menjahit jubah sihir para penyihir dan lapisan dalam zirah pelindung.',
            'subcats': ['Fiber']
        },
        {
            'title': '6. Kulit, Bulu & Mantel Binatang (Hides, Pelts, Furs & Feathers)',
            'desc': 'Kulit dan bulu hasil buruan binatang buas untuk penyamakan baju zirah kulit, rompi pengelana, dan sarung tangan.',
            'subcats': ['Hide', 'Fur', 'Feather']
        },
        {
            'title': '7. Tulang, Taring & Tanduk Fauna (Bones, Fangs & Horns)',
            'desc': 'Bagian tubuh keras dari predator buas untuk mata anak panah, belati bertaring, gelang penguat, dan helm bertanduk.',
            'subcats': ['Bone', 'Fang', 'Horn']
        },
        {
            'title': '8. Sisik, Cangkang & Karapas Fauna (Scales, Shells & Carapaces)',
            'desc': 'Lapisan pelindung alami dari reptil, amfibi, dan serangga raksasa untuk pelat zirah keras dan perisai anti-sihir.',
            'subcats': ['Scale', 'Shell', 'Carapace', 'Metallic Carapace']
        },
        {
            'title': '9. Daging, Cairan & Bahan Kuliner Monster (Monster Flesh, Fluids & Cooking)',
            'desc': 'Bahan organik basah dari makhluk hidup untuk kebutuhan logistik perkemahan, racun pelumas senjata, atau ramuan alkimia pekat.',
            'subcats': ['Monster Flesh', 'Monster Fluid', 'Cooking']
        },
        {
            'title': '10. Bagian Anatomi Monster Khusus (Specific Monster Parts, Fauna & Corals)',
            'desc': 'Organ unik dari monster-monster terestrial dan lautan yang memiliki sifat khusus untuk senjata finesse dan aksesoris langka.',
            'subcats': ['Monster Parts', 'Fauna', 'Coral']
        },
        {
            'title': '11. Kristal Alami & Serpihan Elemen Dasar (Natural Crystals & Elemental Scrap)',
            'desc': 'Kristal mentah yang mengkristal di gua-gua atau runtuhan kuno, menjadi bahan dasar pembuatan rune sihir dasar.',
            'subcats': ['Crystal', 'Elemental Remnant', 'Metal Scrap']
        },
        {
            'title': '12. Esensi Arwah, Jiwa & Okultis (Spirit, Occult, Bhuta & Soul Remnants)',
            'desc': 'Residu metafisika dari roh gentayangan, prajurit Bhuta, dan kultis gelap untuk pembuatan jubah berhantu dan katalis ritual.',
            'subcats': ['Spirit Remnant', 'Spirit Core', 'Occult Material', 'Bhuta Remnant', 'Soul Material', 'Summoning Catalyst']
        },
        {
            'title': '13. Inti Monster & Sisa Bos Regional (Monster & Boss Cores, Chief Materials)',
            'desc': 'Inti kristal energi monster kuat dan peninggalan para Chief Arkananta atau penguasa laut untuk perlengkapan Tier Tinggi.',
            'subcats': ['Monster Core', 'Boss Core', 'Boss Material', 'Chief Material']
        },
        {
            'title': '14. Bagian Tubuh Drakthar & Konstruk Sentinel (Drakthar & Ancient Constructs)',
            'desc': 'Material dari ras Drakthar bawah tanah dan mekanisme automatik reruntuhan kuno untuk perlengkapan perang mekanis.',
            'subcats': ['Drakthar Body Part', 'Drakthar Core', 'Construct Core', 'Artificial Body', 'Artificial Core']
        },
        {
            'title': '15. Material Sakral Bangsa Garuda (Garuda Sacred Relics)',
            'desc': 'Bulu suci dan cakar sakral dari Sentinel Nusa Sayendra yang didapatkan dari ujian kehormatan, bukan mutilasi.',
            'subcats': ['Garuda Material']
        },
        {
            'title': '16. Material Naga Purba Nusvanir (Dragon Materials)',
            'desc': 'Bahan legendaris yang berasal dari naga kuno benua Nusvanir, memiliki ketahanan panas luar biasa dan kekuatan magis tak tertandingi.',
            'subcats': ['Dragon Material']
        },
        {
            'title': '17. Material Para Panglima Iblis Raksamala (Demon Commander Materials)',
            'desc': 'Inti dan sisik terkutuk dari 7 Jenderal Iblis Raksamala (Asmodea, Beelzebub, Belphegor, Leviathanus, Luciferus, Mamon, Vraka).',
            'subcats': ['Commander Material']
        },
        {
            'title': '18. Material Entitas Void & Dimensi Astral (Void & Astral Materials)',
            'desc': 'Materi anomali antariksa dan kehampaan mutlak yang menembus batas realitas, digunakan untuk menempa persenjataan Mythic.',
            'subcats': ['Void Material', 'Astral Material']
        }
    ]

    md = []
    md.append('# ⚒️ Database Item: Materials (Bahan Baku & Crafting)')
    md.append('\nDokumen ini merangkum seluruh **206 Material Crafting** di dunia Nusvanir yang digunakan oleh pandai besi (*Blacksmith*), ahli alkimia (*Alchemist*), dan penenun (*Tailor*) untuk menciptakan senjata, armor, jimat, dan perlengkapan petualang.')
    md.append('\n> [!NOTE]\n> **Standarisasi Tingkat Material (Material Tier):**\n> - **T1 (Tier 1):** Common (Harga Beli: 25 Tamra | Jual: 13 Tamra)\n> - **T2 (Tier 2):** Uncommon (Harga Beli: 80 Tamra | Jual: 40 Tamra)\n> - **T3 (Tier 3):** Rare Regional (Harga Beli: 250 Tamra | Jual: 125 Tamra)\n> - **T4 (Tier 4):** Advanced Rare (Harga Beli: 700 Tamra | Jual: 350 Tamra)\n> - **T5 (Tier 5):** Epic (Harga Beli: 1,800 Tamra | Jual: 900 Tamra)\n> - **T6 (Tier 6):** High Epic / Boss (Harga Beli: 5,000 Tamra | Jual: 2,500 Tamra)\n> - **T7 (Tier 7):** Legendary (Harga Beli: 15,000 Tamra | Jual: 7,500 Tamra)\n> - **T8 (Tier 8):** Late-Game Legendary (Harga Beli: 50,000 Tamra | Jual: 25,000 Tamra)\n> - **T9 (Tier 9):** Mythic / Endgame (Harga Beli: 150,000 Tamra | Jual: 75,000 Tamra)')
    md.append('\n---\n')

    # Quick item lookup by name
    items_dict = {it['name']: it for it in items}
    processed_names = set()

    for grp in groups:
        md.append(f"## {grp['title']}\n")
        md.append(f"{grp['desc']}\n")
        
        # Collect items in this group
        grp_items = [it for it in items if it['subcategory'] in grp['subcats']]
        
        # Summary table
        md.append('| Nama Material | Subkategori | Rarity | Tier / Desain | Beli | Jual | Sumber Drop / Gathering |')
        md.append('|---|---|---|---|---|---|---|')
        for it in grp_items:
            processed_names.add(it['name'])
            tier_str = it['remarks'] if it['remarks'] else '-'
            md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {tier_str} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | {it['source']} |")
        md.append('\n')

        # Detailed item cards
        for it in grp_items:
            md.append(f"### 🔸 {it['name']}")
            md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
            if it['remarks']:
                md.append(f"- **Klasifikasi Desain:** `{it['remarks']}`")
            md.append(f"- **Nilai Ekonomi:** Beli: {format_saka(it['price'])} | Jual: {format_saka(it['sell_price'])}")
            md.append(f"- **Wilayah Asal (Region):** {it['region']}")
            md.append(f"- **Sumber Perolehan:** {it['source']}")
            
            # Enemy drops reverse lookup
            drops = enemy_drops.get(it['name'], [])
            if drops:
                drop_strs = [f"**{d[0]}** ({d[1]}, Peluang: {d[2]})" for d in drops]
                md.append(f"- **Monster Penjatuh (Bestiary Drops):** {'; '.join(drop_strs)}")
            
            md.append(f"- **Deskripsi Lore:** *\"{it['desc']}\"*")
            
            # Recipe usage reverse lookup
            recipes = material_recipes.get(it['name'], [])
            if recipes:
                md.append(f"- **Kegunaan & Resep Penempaan (Crafting Uses):**")
                for r in recipes:
                    md.append(f"  * Digunakan untuk menempa **{r}**")
            else:
                md.append(f"- **Kegunaan Utama:** Bahan baku crafting peralatan, peracikan ramuan alkimia, atau komoditas perdagangan.")
            
            md.append('\n')

    # Check any unprocessed items
    unproc = [it for it in items if it['name'] not in processed_names]
    if unproc:
        print(f"Warning: {len(unproc)} unprocessed materials! Names: {[u['name'] for u in unproc]}")

    out_path = os.path.join(OUTPUT_DIR, '02_Materials.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path} ({len(items)} items)")

# -------------------------------------------------------------
# BUILD 03_FORGE_&_ENHANCEMENT.MD
# -------------------------------------------------------------
def build_forge():
    items = items_by_cat['Forge']
    
    md = []
    md.append('# 🔨 Database Item: Forge, Socket & Enhancement')
    md.append('\nDokumen ini mencakup seluruh **106 Item Penempaan, Kristal Soket, dan Batu Peningkatan (Enhance Stones)** dalam sistem permainan RPG Turn-Based Nusvanir.')
    md.append('\n> [!NOTE]\n> **Mekanik Penempaan & Soket di Nusvanir:**\n> 1. **Peningkatan Rarity (Upgrade Core):** Menaikkan mutu peralatan dari Common hingga Mythic.\n> 2. **Pembukaan Soket (Socket Core):** Membuka slot soket 1 hingga 4 pada senjata dan baju zirah.\n> 3. **Pemasangan Kristal Stat (Stat Crystal):** Memasang kristal ke dalam soket untuk memberikan bonus persentase atribut Turn-Based secara permanen.\n> 4. **Peningkatan Refine (Enhance Stone):** Menaikkan level +1 hingga +20 pada senjata/armor.')
    md.append('\n---\n')

    # 1. Stat Crystals (72 items)
    stat_crystals = [it for it in items if it['subcategory'] == 'Stat Crystal']
    md.append('## 1. Kristal Soket Stat Turunan (Stat Crystals - 72 Item)\n')
    md.append('Kristal soket yang dapat dipasang ke dalam slot soket peralatan yang telah dibuka. Setiap kristal memberikan peningkatan persentase terhadap 18 Atribut Dasar dan Turunan Turn-Based Nusvanir:\n')
    
    # Group crystals by root name (e.g. Vital Crystal, Mana Crystal, etc.)
    crystal_roots = {}
    for it in stat_crystals:
        # e.g. "Vital Crystal 1" -> root "Vital Crystal", tier "1"
        m = re.match(r'^(.*?)\s*(\d+)$', it['name'])
        if m:
            root = m.group(1).strip()
            tier = int(m.group(2))
        else:
            root = it['name']
            tier = 1
        if root not in crystal_roots:
            crystal_roots[root] = {}
        crystal_roots[root][tier] = it

    md.append('| Nama Kristal | Atribut yang Ditingkatkan | Tier 1 (Common) | Tier 2 (Uncommon) | Tier 3 (Rare) | Tier 4 (Epic) |')
    md.append('|---|---|---|---|---|---|')
    for root, tiers in crystal_roots.items():
        t1 = tiers.get(1, {})
        t2 = tiers.get(2, {})
        t3 = tiers.get(3, {})
        t4 = tiers.get(4, {})
        stat_target = t1.get('effects', '-')
        # Clean stat target string
        stat_name = re.sub(r'[\+\d\%]', '', stat_target).strip()
        md.append(f"| **{root}** | **{stat_name}** | {t1.get('effects', '-')} | {t2.get('effects', '-')} | {t3.get('effects', '-')} | {t4.get('effects', '-')} |")
    md.append('\n')

    md.append('### Rincian Lengkap Kristal Soket per Atribut\n')
    for root, tiers in crystal_roots.items():
        t1 = tiers.get(1, {})
        md.append(f"#### 💎 {root} (Tier 1 ~ 4)")
        md.append(f"- **Target Modifikasi Atribut:** `{t1.get('effects', '-')}`")
        md.append(f"- **Deskripsi Umum:** *\"{t1.get('desc', '').replace('by 3%', 'secara proporsional').replace('by 2%', 'secara proporsional').replace('by 1%', 'secara proporsional')}\"*")
        md.append(f"- **Daftar Tingkatan & Nilai Bonus:**")
        for tier_num in [1, 2, 3, 4]:
            t_item = tiers.get(tier_num)
            if t_item:
                md.append(f"  * **{t_item['name']}** ({rarity_badge(t_item['rarity'])}) — Efek: **{t_item['effects']}** | Beli: {format_saka(t_item['price'])} | Jual: {format_saka(t_item['sell_price'])}")
        md.append('\n')

    # 2. Elemental & Special Crystals (10 items)
    elem_crystals = [it for it in items if it['subcategory'] in ['Elemental Crystal', 'Occult Crystal', 'Special Crystal']]
    md.append('## 2. Kristal Elemen & Kosmis (Elemental & Cosmic Crystals - 10 Item)\n')
    md.append('Kristal magis yang terbentuk dari inti anomali elemental murni atau zat antariksa, digunakan untuk membuka soket sihir khusus, menempa rune, atau memberikan afinitas elemen pada senjata.\n')
    
    md.append('| Nama Kristal | Subkategori | Rarity | Harga Beli | Harga Jual | Sumber Perolehan | Efek & Fungsi Utama |')
    md.append('|---|---|---|---|---|---|---|')
    for it in elem_crystals:
        md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | {it['source']} | {it['desc']} |")
    md.append('\n')

    for it in elem_crystals:
        md.append(f"### 🔮 {it['name']}")
        md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
        md.append(f"- **Nilai Ekonomi:** Beli: {format_saka(it['price'])} | Jual: {format_saka(it['sell_price'])}")
        md.append(f"- **Wilayah Asal:** {it['region']} | **Sumber:** {it['source']}")
        md.append(f"- **Deskripsi Lore:** *\"{it['desc']}\"*")
        recipes = material_recipes.get(it['name'], [])
        if recipes:
            md.append(f"- **Resep Penempaan yang Membutuhkan:**")
            for r in recipes:
                md.append(f"  * **{r}**")
        else:
            md.append(f"- **Kegunaan Penempaan:** Bahan penempaan senjata elemen tingkat tinggi, afinitas serangan, dan socketing sihir legendaris.")
        md.append('\n')

    # 3. Enhance Stones (9 items)
    enhance_items = [it for it in items if it['subcategory'] in ['Enhance Stone', 'Enhance Special']]
    md.append('## 3. Batu Peningkatan Tempa (Enhance Stones - 9 Item)\n')
    md.append('Katalis penempaan yang digunakan oleh pandai besi untuk menaikkan tingkat penguatan (+1 s.d. +20) pada senjata dan baju zirah.\n')
    
    md.append('| Nama Item | Subkategori | Rarity | Harga Beli | Harga Jual | Batas Penguatan / Efek Perlindungan |')
    md.append('|---|---|---|---|---|---|')
    for it in enhance_items:
        md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | **{it['effects']}** |")
    md.append('\n')

    for it in enhance_items:
        md.append(f"### 🛡️ {it['name']}")
        md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
        md.append(f"- **Nilai Ekonomi:** Beli: {format_saka(it['price'])} | Jual: {format_saka(it['sell_price'])}")
        md.append(f"- **Efek Mekanik Penempaan:** **{it['effects']}**")
        md.append(f"- **Deskripsi:** *\"{it['desc']}\"*")
        md.append(f"- **Sumber Perolehan:** {it['source']} ({it['region']})")
        md.append('\n')

    # 4. Socket Cores (6 items)
    socket_items = [it for it in items if it['subcategory'] in ['Socket Core', 'Socket Special']]
    md.append('## 4. Inti Pembuka Soket (Socket Cores - 6 Item)\n')
    md.append('Alat penempa khusus untuk melubangi slot soket kristal pada senjata dan zirah yang memenuhi syarat.\n')
    
    md.append('| Nama Item | Subkategori | Rarity | Harga Beli | Harga Jual | Efek Pembukaan Soket |')
    md.append('|---|---|---|---|---|---|')
    for it in socket_items:
        md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | **{it['effects']}** |")
    md.append('\n')

    for it in socket_items:
        md.append(f"### ⚙️ {it['name']}")
        md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
        md.append(f"- **Nilai Ekonomi:** Beli: {format_saka(it['price'])} | Jual: {format_saka(it['sell_price'])}")
        md.append(f"- **Efek Mekanik:** **{it['effects']}**")
        md.append(f"- **Deskripsi:** *\"{it['desc']}\"*")
        md.append(f"- **Sumber Perolehan:** {it['source']} ({it['region']})")
        md.append('\n')

    # 5. Upgrade Cores (9 items)
    upgrade_items = [it for it in items if it['subcategory'] in ['Upgrade Core', 'Upgrade Special']]
    md.append('## 5. Inti Peningkatan Mutu (Upgrade Cores - 9 Item)\n')
    md.append('Inti energi penempaan untuk mentransmutasi mutu (*Rarity Tier*) perlengkapan menjadi satu tingkat lebih tinggi secara permanen.\n')
    
    md.append('| Nama Item | Subkategori | Rarity | Harga Beli | Harga Jual | Efek Transmutasi Mutu |')
    md.append('|---|---|---|---|---|---|')
    for it in upgrade_items:
        md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {format_saka_short(it['price'])} | {format_saka_short(it['sell_price'])} | **{it['effects']}** |")
    md.append('\n')

    for it in upgrade_items:
        md.append(f"### ⭐ {it['name']}")
        md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
        md.append(f"- **Nilai Ekonomi:** Beli: {format_saka(it['price'])} | Jual: {format_saka(it['sell_price'])}")
        md.append(f"- **Efek Mekanik:** **{it['effects']}**")
        md.append(f"- **Deskripsi:** *\"{it['desc']}\"*")
        md.append(f"- **Sumber Perolehan:** {it['source']} ({it['region']})")
        md.append('\n')

    out_path = os.path.join(OUTPUT_DIR, '03_Forge_&_Enhancement.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path} ({len(items)} items)")

# -------------------------------------------------------------
# BUILD 04_VALUABLES.MD
# -------------------------------------------------------------
def build_valuables():
    items = items_by_cat['Valuable']
    
    md = []
    md.append('# 💰 Database Item: Valuables (Barang Berharga, Trophy & Curio)')
    md.append('\nDokumen ini mencakup seluruh **36 Item Berharga (Valuables)** di dunia Nusvanir yang memiliki nilai jual tinggi, menjadi bukti perburuan monster buronan (*Bounty Hunt*), atau tanda jasa kehormatan faksi.')
    md.append('\n> [!NOTE]\n> **Aturan Ekonomi Barang Berharga (Valuables):**\n> - **Bebas Pajak:** Barang berharga tidak dikenakan penalti potongan harga konsumsi (rasio jual murni 50% atau bernilai tinggi di Pasar Putih & Gilda Arthapasa).\n> - **Bukti Perburuan (Bounty Proof):** Dapat disetorkan ke resepsionis Gilda Arthapasa di Lingkar Bumi untuk mendapatkan poin reputasi petualang dan kenaikan *Rank Gilda* (Bronze -> Silver -> Gold -> Platinum -> Apex).\n> - **Barter Eksklusif:** Suku pedalaman Arkananta dan Saudagar Khoja di Pasar Gelap Cakrawala menerima trophy tertentu sebagai alat tukar barang pusaka.')
    md.append('\n---\n')

    # Group by thematic types
    groups = [
        {
            'title': '1. Trophy Perburuan Fauna & Monster Terestrial (Monster Trophies)',
            'subcats': ['Monster Trophy', 'Natural Curio']
        },
        {
            'title': '2. Trophy Pemimpin Suku Arkananta (Chief Trophies)',
            'subcats': ['Chief Trophy']
        },
        {
            'title': '3. Lambang Ksatria Kerajaan Avalerion (Avalerion Insignias & Curios)',
            'subcats': ['Avalerion Insignia', 'Avalerion Curio']
        },
        {
            'title': '4. Trophy Entitas Supranatural & Makhluk Terkutuk (Spirit, Occult & Drakthar)',
            'subcats': ['Spirit Trophy', 'Occult Trophy', 'Drakthar Trophy', 'Bhuta Remnant']
        },
        {
            'title': '5. Trophy Entitas Void & Dimensi Astral (Void & Astral Trophies)',
            'subcats': ['Void Trophy', 'Astral Trophy']
        }
    ]

    for grp in groups:
        md.append(f"## {grp['title']}\n")
        grp_items = [it for it in items if it['subcategory'] in grp['subcats']]
        
        md.append('| Nama Item | Subkategori | Rarity | Nilai Jual (Saka) | Sumber Monster / Wilayah | Deskripsi Singkat |')
        md.append('|---|---|---|---|---|---|')
        for it in grp_items:
            md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | **{format_saka_short(it['sell_price'])}** | {it['source']} ({it['region']}) | {it['desc']} |")
        md.append('\n')

        for it in grp_items:
            md.append(f"### 🏆 {it['name']}")
            md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
            md.append(f"- **Nilai Jual Pasar:** **{format_saka(it['sell_price'])}** (Harga Beli: {format_saka(it['price'])})")
            md.append(f"- **Sumber Perolehan:** Monster **{it['source']}**")
            md.append(f"- **Wilayah Asal:** {it['region']}")
            md.append(f"- **Deskripsi Lore:** *\"{it['desc']}\"*")
            md.append(f"- **Kegunaan Khusus:** Bukti perburuan resmi Gilda Arthapasa untuk menyelesaikan quest buronan, barter komoditas berharga di Arkananta/Cakrawala, dan sumber pemasukan Saka utama petualang.")
            md.append('\n')

    out_path = os.path.join(OUTPUT_DIR, '04_Valuables.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path} ({len(items)} items)")

# -------------------------------------------------------------
# BUILD 05_KEY_ITEMS.MD
# -------------------------------------------------------------
def build_key_items():
    items = items_by_cat['Key Item']
    
    md = []
    md.append('# 🗝️ Database Item: Key Items (Barang Kunci, Segel & Perjanjian)')
    md.append('\nDokumen ini mencakup seluruh **21 Barang Kunci (Key Items)** dalam dunia Nusvanir yang terkait erat dengan alur narasi ekspedisi, gerbang wilayah sakral, dan ritual kontrak pemanggilan iblis untuk profesi khusus.')
    md.append('\n> [!NOTE]\n> **Aturan Mekanik Barang Kunci (Key Items):**\n> - **Permanen:** Key Item tidak dapat dijual, dibuang, atau dihancurkan oleh pemain.\n> - **Syarat Kontrak Necromancer:** Perjanjian Iblis (*Demon Covenants*) adalah item kunci wajib yang memungkinkan Class **Necromancer** (Tier 3 Jalur Sihir) mengakses kemampuan pasif dan pemanggilan entitas Demon Commander dalam pertarungan Turn-Based.\n> - **Akses Gerbang Sakral:** Lambang Sentinel dan Segel Iblis membuka rute ke area Endgame di Benteng Raksamala dan Puncak Nusa Sayendra.')
    md.append('\n---\n')

    groups = [
        {
            'title': '1. Jimat & Katalis Pemanggilan Mistis (Summoning Catalysts)',
            'subcats': ['Summoning Catalyst']
        },
        {
            'title': '2. Lambang Kehormatan Para Sentinel Nusa Sayendra (Sentinel Trophies)',
            'subcats': ['Sentinel Trophy']
        },
        {
            'title': '3. Segel Otoritas Panglima Iblis Raksamala (Commander Sigils & Trophy)',
            'subcats': ['Commander Sigil', 'Commander Trophy']
        },
        {
            'title': '4. Dokumen Kontrak Perjanjian Iblis (Demon Covenants - Necromancer Contract)',
            'subcats': ['Demon Covenant']
        },
        {
            'title': '5. Kontrak Hitam Tertinggi Raja Iblis Sangrahal (Demon Lord Covenant)',
            'subcats': ['Demon Lord Covenant']
        }
    ]

    for grp in groups:
        md.append(f"## {grp['title']}\n")
        grp_items = [it for it in items if it['subcategory'] in grp['subcats']]
        
        md.append('| Nama Key Item | Subkategori | Rarity | Sumber Perolehan | Wilayah | Kegunaan Kunci |')
        md.append('|---|---|---|---|---|---|')
        for it in grp_items:
            md.append(f"| **{it['name']}** | `{it['subcategory']}` | {rarity_badge(it['rarity'])} | {it['source']} | {it['region']} | {it['desc']} |")
        md.append('\n')

        for it in grp_items:
            md.append(f"### 🗝️ {it['name']}")
            md.append(f"- **Subkategori:** `{it['subcategory']}` | **Kelangkaan:** {rarity_badge(it['rarity'])}")
            md.append(f"- **Status Kepemilikan:** Barang Kunci Tidak Dijual (`0 Saka`)")
            md.append(f"- **Sumber Perolehan:** {it['source']}")
            md.append(f"- **Wilayah Terkait:** {it['region']}")
            md.append(f"- **Deskripsi Lore:** *\"{it['desc']}\"*")
            
            # Deep gameplay utility explanation
            if it['subcategory'] == 'Demon Covenant':
                cmd_name = it['name'].replace('Covenant of ', '')
                md.append(f"- **Kegunaan Mekanik Game:** Syarat mutlak bagi karakter kelas **Necromancer** untuk mengikat kontrak pasif dengan Panglima Iblis **{cmd_name}**. Membuka skill pemanggilan arwah/avatar {cmd_name} di daftar *Learnings* class.")
            elif it['subcategory'] == 'Demon Lord Covenant':
                md.append(f"- **Kegunaan Mekanik Game:** Item kunci tingkat Endgame tertinggi. Membuka pintu ke tahta Raja Iblis Sangrahal dan memungkinkan Necromancer mengakses sihir pemanggilan puncak *Dark Lord Descent*.")
            elif it['subcategory'] == 'Commander Sigil':
                md.append(f"- **Kegunaan Mekanik Game:** Bukti penaklukan Demon Commander di Benteng Raksamala. Digunakan sebagai bahan ritual okultis untuk menyusun *Demon Covenant* yang bersangkutan.")
            elif it['subcategory'] == 'Sentinel Trophy':
                md.append(f"- **Kegunaan Mekanik Game:** Bukti pengakuan kehormatan dari para Sentinel Nusa Sayendra. Membuka akses ke Puncak Mahameru dan tempat suci bangsa Garuda.")
            elif it['subcategory'] == 'Summoning Catalyst':
                md.append(f"- **Kegunaan Mekanik Game:** Menstabilkan ritual pemanggilan roh alam liar Jenggala tanpa risiko kehilangan kendali mana.")
            
            md.append('\n')

    out_path = os.path.join(OUTPUT_DIR, '05_Key_Items.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path} ({len(items)} items)")

# -------------------------------------------------------------
# BUILD README.MD
# -------------------------------------------------------------
def build_readme():
    total_items = sum(len(lst) for lst in items_by_cat.values())
    
    md = []
    md.append('# 📦 Database Master Item & Inventaris Nusvanir')
    md.append('\nSelamat datang di repositori database resmi item, barang konsumsi, bahan baku penempaan, barang berharga, dan barang kunci untuk proyek **Nusvanir RPG (Turn-Based System)**.')
    md.append(f'\nTotal seluruh item yang terdaftar dan terintegrasi dalam database adalah **{total_items} Item**, yang bersumber langsung dari `Database/NUSV - Database [CLASS, SKILL, STATE, TYPE].xlsx`.')
    md.append('\n---\n')

    md.append('## 🗂️ Struktur Direktori Database Items\n')
    md.append('| File Dokumen | Kategori Item | Jumlah Item | Ruang Lingkup & Fungsi Utama |')
    md.append('|---|---|---|---|')
    md.append('| [01_Consumables.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/01_Consumables.md) | **Consumable** | 29 Item | Ramuan HP/MP/SP, Revive, Obat Status, Tonik Buff Tempur, dan Gulungan Sihir. |')
    md.append('| [02_Materials.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/02_Materials.md) | **Material** | 206 Item | Bijih tambang, kayu hutan, batuan, herbal, kulit, tulang, sisa arwah, hingga material naga purba. |')
    md.append('| [03_Forge_&_Enhancement.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) | **Forge** | 106 Item | Kristal soket stat (18 stat turn-based x 4 tier), kristal elemen, Enhance Stone, Socket Core, Upgrade Core. |')
    md.append('| [04_Valuables.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/04_Valuables.md) | **Valuable** | 36 Item | Trophy perburuan monster, emblem Chief Arkananta, lambang ksatria Avalerion, fosil langka. |')
    md.append('| [05_Key_Items.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/05_Key_Items.md) | **Key Item** | 21 Item | Jimat pemanggilan, segel komandan iblis, dan Demon Covenants untuk kontrak kelas Necromancer. |')
    md.append('\n---\n')

    md.append('## 🪙 Standarisasi Mata Uang & Valuasi Ekonomi (Saka)\n')
    md.append('Seluruh nilai item dalam game mengacu pada mata uang koin mineral resmi Nusvanir:\n')
    md.append('1. **Saka Tamra (Tembaga):** Koin dasar (1 Tamra). Dipakai untuk transaksi mikro dan kebutuhan dasar rakyat jelata.\n')
    md.append('2. **Saka Rajata (Perak):** Koin menengah (**1 Saka Rajata = 100 Saka Tamra**). Mata uang standar petualang dan perdagangan umum.\n')
    md.append('3. **Saka Kencana (Emas):** Koin tertinggi (**1 Saka Kencana = 100 Saka Rajata = 10,000 Saka Tamra**). Digunakan untuk senjata pusaka, material epik, dan transaksi makro bangsawan.\n')
    md.append('\n> [!TIP]\n> **Aturan Penjualan Kembali (Sell Ratio):**\n> - **Barang Biasa & Material:** Dijual seharga **50% (0.5x)** dari harga beli pasar.\n> - **Item Konsumsi (Consumables):** Dijual seharga **40% (0.4x)** dari harga beli pasar guna mencegah arbitrase toko (*flipping*).\n> - **Barang Kunci (Key Items):** Tidak memiliki harga jual (*Unsellable*).\n')
    md.append('\n---\n')

    md.append('## ⚔️ Integrasi Mekanik Turn-Based RPG\n')
    md.append('Setiap kategori item memiliki dampak langsung terhadap gameplay pertempuran berbasis giliran (*Turn-Based Combat*):\n')
    md.append('- **Sistem Stamina Points (SP):** Menggantikan sistem TP lama. Karakter fisik memerlukan SP untuk skill jurus. Penggunaan item seperti *Focus Drop* dan pemasangan *Focus Crystal* menjaga sustain SP karakter selama pertempuran panjang.\n')
    md.append('- **Konsumsi 1 Action Turn:** Penggunaan item pemulihan atau buff selama battle mengonsumsi giliran aksi karakter, menuntut perhitungan taktis antara menyerang, bertahan, atau memulihkan sekutu.\n')
    md.append('- **18 Kristal Soket Presisi:** Seluruh kristal soket pada [03_Forge_&_Enhancement.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/03_Forge_&_Enhancement.md) secara akurat memodifikasi 18 Parameter RPG Nusvanir: `Max HP`, `Max MP`, `ATK`, `DEF`, `MAT`, `MDF`, `Action Speed (AGI)`, `LUK`, `Hit Rate (HIT)`, `Evasion (EVA)`, `Magic Evasion (MEV)`, `Critical Rate (CRI)`, `Critical Evasion (CEV)`, `Magic Reflection (MRF)`, `Counter Attack (CNT)`, `HP Regen (HRG)`, `MP Regen (MRG)`, dan `SP Regen (TRG)`.\n')
    md.append('- **Sinergi Kontrak Necromancer:** Kontrak iblis pada [05_Key_Items.md](file:///e:/Ananto/Emulatoid/Nusvanir/06_Sistem%20Game%20&%20Ekonomi/Items/05_Key_Items.md) mengaktifkan cabang skill pemanggilan arwah bagi class Necromancer sesuai alur Dual Level System.\n')

    out_path = os.path.join(OUTPUT_DIR, 'README.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))
    print(f"Created {out_path}")

# Run all builders
build_materials()
build_forge()
build_valuables()
build_key_items()
build_readme()
print("All items database files successfully generated!")

