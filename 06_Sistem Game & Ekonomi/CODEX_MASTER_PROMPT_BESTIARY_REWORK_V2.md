# Master Execution Prompt — Nusvanir Bestiary & World-Building Rework V2

You are working directly inside the Nusvanir repository opened in Visual Studio Code.

Repository:

`https://github.com/ultoid/nusvanir`

Your task is to audit, restructure, expand, and implement the Nusvanir Bestiary and its related world-building so that every creature has a coherent place in:

- Nusvanir canon and cosmology;
- regional ecology;
- taxonomy and faction relationships;
- RPG Maker MV combat;
- encounter progression;
- skills, states, and elements;
- drops, crafting, upgrades, and economy;
- quests and story;
- boss mechanics.

Do not stop at recommendations. Make safe, traceable repository changes according to the phased workflow below. However, do not invent missing canon or numerical balance data merely to make entries appear complete.

---

## 1. Non-negotiable rules

### 1.1 Read repository instructions first

Before editing anything:

1. Find and read every applicable `AGENTS.md` from the repository root down to the target directory.
2. Inspect the repository tree.
3. Read the current system documentation and the files referenced by this prompt.
4. Check Git status and preserve unrelated user changes.
5. Identify whether this workspace contains only the lore repository or also the active RPG Maker MV project/database.

Do not overwrite user changes. Do not use destructive Git operations. Do not change IDs or filenames referenced by the game without a repository-wide reference audit.

### 1.2 Mandatory stat authority

Before creating or changing any numerical stat, read and obey:

`06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md`

This document is the highest-level balance governance rule for Nusvanir.

If it does not exist:

- do not invent numerical stats;
- continue only with non-numerical audit, schema, lore, taxonomy, ecology, and documentation work;
- report the missing file as a blocker.

Any instruction in this prompt that appears to request stat generation is subordinate to `Pedoman_Pemberian_Stat.md`.

### 1.3 Never treat legacy numbers as final

Existing Bestiary values are `legacy candidates`. They may be retained temporarily for traceability, but must not be presented as calibrated or final unless they pass the current stat rules.

Examples include:

- Babi Hutan HP 150;
- Beruang Madu Raksasa HP 850;
- Moonfang HP 720000 / MP 450000;
- large HP values assigned to Thalantira creatures;
- old class or Tier labels attached to bosses.

Do not preserve these values merely because they already exist. Do not replace them with new guesses either.

### 1.4 Missing data is not permission to estimate

When required balance data is missing, use one of these statuses:

- `BLOCKED`: critical inputs are unavailable; do not provide numbers.
- `PROVISIONAL`: all assumptions are explicitly recorded; numbers are for experimental builds only.
- `CALIBRATED`: derived from the active database and passed reproducible simulation.
- `VALIDATED`: passed playtesting in the intended encounter context.

Do not use “final”, “balanced”, or `VALIDATED` without supporting evidence.

### 1.5 Canon before invention

Prefer established repository canon. When canon is incomplete:

1. identify the gap;
2. search all related files;
3. make the smallest coherent addition;
4. label proposals that need owner approval;
5. do not silently overwrite established lore.

Maintain Nusvanir’s identity: Indonesian/Nusantara influence, mythological high fantasy, dark fantasy, and RPG/MMORPG-style systems. Do not flatten it into generic Western fantasy.

---

## 2. Source-of-truth hierarchy

Resolve conflicts using this order:

1. Active RPG Maker MV runtime database and plugins.
2. Latest approved system documents.
3. Reproducible measurements, simulations, and playtest evidence.
4. Current canon/world-building documents.
5. Existing Bestiary entries as historical/legacy material.
6. Explicitly labeled design assumptions.

For combat balance, look for:

- `data/System.json`
- `data/Enemies.json`
- `data/Actors.json`
- `data/Classes.json`
- `data/Skills.json`
- `data/Weapons.json`
- `data/Armors.json`
- `data/States.json`
- plugin configuration and JavaScript files
- current spreadsheet/CSV databases
- formula documentation

For Nusvanir canon and systems, inspect at minimum:

- `00_Kosmologi & Sejarah/**`
- `01_Hukum Sihir/**`
- `02_World/**`
- `03_Region/**`
- `04_Ras/**`
- `05_Karakter & Tokoh Penting/**`
- `06_Sistem Game & Ekonomi/**`
- `07_Bestiary/**`
- `08_Story/**`
- root database/combined lore files

Treat generated aggregate files such as combined lore or application databases carefully. Determine whether they are sources or generated outputs before editing them.

---

## 3. Primary objective

Transform the Bestiary from a collection of short lore entries and inherited numbers into a coherent gameplay/world-building database integrating:

- identity and naming;
- origin and taxonomy;
- region, biome, habitat, and spawn conditions;
- ecology and behavior;
- civilization, culture, economy, and faction relationships;
- encounter type, combat role, and AI archetype;
- RPG Maker MV parameters;
- skills, passives, and states;
- elemental affinity and resistance;
- rewards and crafting uses;
- quest and story relevance;
- boss phases and special mechanics;
- balance status, sources, assumptions, and validation evidence.

The Bestiary must become usable by both writers and game implementers.

---

## 4. Phase 0 — repository and authority audit

Before major edits, produce an internal audit.

### 4.1 Identify the active sources

Determine:

1. Which files define current canon?
2. Which files define current class/Tier structure?
3. Which files define elemental interactions?
4. Which files define skills and damage formulas?
5. Which files define states and their behavior?
6. Which files define weapons, armor, relics, accessories, sockets, forge, and upgrades?
7. Which files define items, rarity, drops, crafting, and economy?
8. Which files define encounter progression, level bands, party size, and chapter order?
9. Which files define the active RPG Maker MV runtime database?
10. Which files are obsolete, duplicated, generated, or only historical?

### 4.2 Audit current Bestiary

Identify:

- every creature entry;
- Markdown/JSON pairs and whether they agree;
- missing pairs;
- duplicate creatures;
- inconsistent naming;
- mixed Indonesian/English terminology;
- obsolete class/Tier values;
- category/location/faction concepts mixed together;
- unexplained spawn locations;
- unsupported elements or weaknesses;
- unreferenced drops;
- creatures duplicated as both characters and Bestiary entries;
- bosses with no mechanics;
- numbers with no traceable basis.

### 4.3 Create the audit output

Create or update:

`07_Bestiary/BESTIARY_REWORK_AUDIT.md`

If a more appropriate existing documentation path is present, use it and explain the choice.

The audit must separate:

- confirmed facts;
- inconsistencies;
- missing information;
- safe automatic fixes;
- decisions requiring owner approval;
- numerical balance blockers.

Do not edit aggregate/generated files until their generation process is understood.

---

## 5. Phase 1 — Bestiary Standard V2

Create or update:

`07_Bestiary/BESTIARY_STANDARD_V2.md`

Define the canonical schema below. Adapt serialization to existing repository conventions, but do not discard fields without explaining why.

### 5.1 Identity

- ID
- Name
- Alternative Name
- Canonical Slug
- Species
- Creature Family
- Origin
- Faction
- Region
- Biome
- Sub Area

### 5.2 Classification

- Creature Type
- Encounter Type
- Threat Rank
- Rarity/Spawn Rarity
- Sentience Level
- Civilization Status

Creature Type must be separated from region, faction, and encounter type.

Candidate Creature Types include:

- Wildlife
- Magical Beast
- Spirit
- Elemental
- Jenggala
- Drahkthar
- Undead
- Construct
- Humanoid
- Dragon
- Divine Beast
- Voidborn
- Aberration

Do not adopt a candidate type unless it fits repository canon.

Encounter Type:

- Normal
- Elite
- Rare
- Mini Boss
- Boss
- Commander
- World Boss
- Story Boss

### 5.3 Gameplay identity

- Recommended Level or Progression Point
- Combat Role
- Attack Type
- Primary Element
- Secondary Element
- AI Archetype
- Intended Counterplay
- Troop Context
- Balance Status

Combat roles may include:

- Bruiser
- Tank
- Assassin
- Skirmisher
- Mage
- Support
- Controller
- Summoner
- Sniper
- Swarm

Role labels describe intended behavior; they do not authorize stat multipliers.

### 5.4 RPG Maker MV parameters

- MHP / HP
- MMP / MP
- ATK
- DEF
- MAT
- MDF
- AGI
- LUK

Every numerical block must also include:

- `stat_status`
- `balance_version`
- source dependencies
- party reference
- target encounter duration
- assumptions
- calculation summary
- simulation result
- playtest evidence
- unresolved blockers

If the required inputs are absent, leave numerical values null/TBD and use `BLOCKED`. Never fill fields merely to complete the schema.

### 5.5 Elemental affinity

Use the current 10-element system from:

`06_Sistem Game & Ekonomi/Mekanik_Efektivitas_Elemen.md`

Current documented elements:

- Api / Pyro
- Air / Hydro
- Tanah / Geo
- Udara / Aero
- Listrik / Electro
- Es / Cryo
- Besi / Ferro
- Suara / Sonic
- Cahaya / Holy
- Kegelapan / Dark

Do not create a new Void multiplier until the repository establishes Void as an element or defines separate rules.

Represent affinity/resistance in a way compatible with the engine. Do not double-count elemental strength in raw offensive/defensive parameters.

### 5.6 Status resistance

Use only states found in or explicitly planned by the current state database.

Possible examples such as Poison, Burn, Bleed, Freeze, Stun, Sleep, Blind, Silence, Curse, Fear, and Corruption are not automatically canon. Confirm each state first.

### 5.7 Skills and AI

For combat-capable creatures define:

- Basic Attack
- Active Skills
- Passive
- Special Mechanic
- AI conditions
- Action priority
- Target selection
- Resource use
- Enrage or desperation behavior when applicable

Keep behavior realistic for RPG Maker MV and installed plugins.

### 5.8 Spawn and ecology

- Region
- Biome
- Sub Area
- Time
- Weather
- Spawn Weight
- Pack Size
- Aggression
- Encounter Conditions
- Predator/Prey relationship
- Diet
- Migration or territory

Do not invent overly specific named locations unless supported by current world lore.

### 5.9 Rewards

- EXP
- Saka
- Common Drop
- Uncommon Drop
- Rare Drop
- Unique Drop
- Quest Drop
- Crafting/Forge/Alchemy/Summoning use

Before creating a new item, search the item database and all repository references. Avoid duplicates and respect the approved rarity system.

EXP and Saka require progression/economy calibration. If that calibration is missing, use `BLOCKED` or an explicitly documented provisional model.

### 5.10 World-building

- Description
- Lore
- Origin
- Ecology
- Behavior
- Diet
- Predators
- Prey
- Relationship with Civilization
- Cultural Significance
- Economic Value
- Known Uses
- Historical Notes
- Quest Relevance
- Story Relevance

Minor wildlife may be concise. Major creatures and bosses require deeper treatment.

---

## 6. Phase 2 — creature taxonomy

Create or update:

`07_Bestiary/CREATURE_TAXONOMY.md`

Separate:

- species;
- creature family/type;
- origin;
- faction;
- region;
- encounter type;
- threat rank.

Pay special attention to the canonical boundaries among:

- Wildlife;
- Magical Beasts;
- Spirits/Elementals;
- Jenggala;
- Drahkthar;
- Dhemit;
- Bhuta;
- Undead;
- Voidborn;
- Dragons/Nagarasven;
- Divine creatures/Arkahyan.

### 6.1 Jenggala

Do not automatically enforce the prior proposal that all Jenggala are corrupted creatures. Audit repository canon first.

If canon remains insufficient, write a clearly labeled proposal consistent with Nusvanir cosmology. Explain:

- origin;
- transformation mechanism;
- whether Jenggala reproduce;
- relationship to Mana, curses, darkness, and Raksamala;
- difference from wildlife, spirits, Drahkthar, and Voidborn;
- whether folklore-inspired creatures are species, corrupted forms, titles, or regional names.

### 6.2 Drahkthar

Clarify:

- whether Drahkthar is race, army, civilization, origin group, or umbrella term;
- hierarchy and relationship among Sangrahal, Bhuta, and Dhemit;
- relationship to Kala Laksana;
- difference from Jenggala, undead, and Voidborn;
- summoning and regeneration rules;
- relationship to Light/Holy purification.

Record unresolved canon decisions instead of silently inventing answers.

---

## 7. Phase 3 — numerical balance framework

Create or update:

`06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md`

This phase must obey `Pedoman_Pemberian_Stat.md`.

### 7.1 Required inputs

Before assigning numerical bands, locate and verify:

- party size;
- level cap and chapter/area level ranges;
- class parameter curves;
- equipment available per progression point;
- weapon ATK/MAT and armor DEF/MDF;
- skill damage/healing formulas;
- MP/TP costs and regeneration;
- critical, hit, evasion, guard, PDR, MDR, and variance;
- state application and resistance formulas;
- turn order and multi-action behavior;
- elemental multipliers;
- consumables, sockets, upgrades, buffs, and debuffs;
- target rounds/duration per encounter type;
- EXP/Saka economy targets.

### 7.2 If inputs are available

Build `LOW`, `EXPECTED`, and `HIGH` party profiles for each progression point.

Use reproducible calculations or scripts to derive:

- expected physical/magical damage;
- sustainable and burst damage per round;
- healing/shielding per round;
- enemy damage pressure;
- effective HP;
- action economy;
- elemental matchup outcomes;
- status/control impact;
- expected encounter duration;
- reward efficiency.

Define numerical stat bands only after these are measured.

### 7.3 If inputs are missing

Do not invent stat bands.

Instead, create the framework with:

- missing-input checklist;
- `BLOCKED` fields;
- source paths that must be added;
- formulas/workbook structure ready for later values;
- exact questions requiring owner decisions;
- legacy values preserved only in an audit appendix if useful.

Continue non-numerical Bestiary work while leaving stat values blocked.

### 7.4 Prohibited shortcuts

Do not use arbitrary rules such as:

- Elite = Normal ×2;
- Boss = Normal ×10;
- every later region increases all stats by a fixed percentage;
- Tier 5 automatically means a fixed HP or ATK value;
- larger creature automatically means proportionally larger stats;
- boss balance equals very high HP;
- matching another commercial game’s stat table.

Relative role profiles are allowed, but final numbers require calculation and validation.

---

## 8. Phase 4 — regional ecology

Audit and improve each major region where relevant:

- Mandala
- Astradipa
- Avalerion
- Cakrawala
- Tirta Amarta
- Nusa Sayendra
- Agnitra
- Raksamala
- Pegunungan Arkananta
- Laut Rangkaruna
- Thalantira

Connect creatures to:

- geography;
- climate;
- biome;
- flora/fauna;
- food chain;
- magical conditions;
- resources;
- settlements;
- civilization and race;
- government/faction;
- military;
- religion;
- economy and trade;
- technology and magic;
- dungeon and quest structure;
- conflict;
- danger level;
- travel routes.

Do not turn regional documents into repetitive checklists. Add only details that create meaningful causal connections.

Examples of desired consistency:

- Astradipa creatures must fit its forest ecology and Asrivana/Hanorok relationships.
- Agnitra creatures must reflect volcanic conditions and Nagarasven influence.
- Arkananta creatures/materials must connect to its mountains, caves, ores, and resident races.
- Raksamala creatures must reflect Drahkthar/demonic influence and fortress hierarchy.
- Rangkaruna creatures must fit marine traversal and trade threats.
- Thalantira creatures must feel abnormal without using unexplained stat inflation as their only distinction.

---

## 9. Phase 5 — drop, crafting, and economy integration

Build this chain:

`Creature → Drop → Material → Use → Equipment/Consumable/Upgrade/Quest → Economy`

For every meaningful drop:

1. search all item/material databases;
2. reuse existing canonical items where possible;
3. confirm rarity terminology;
4. identify at least one meaningful use;
5. check whether the drop duplicates another item’s function;
6. check regional economic implications;
7. check farming/exploit risks.

Possible uses include:

- crafting;
- forge;
- upgrade;
- alchemy;
- consumable;
- quest;
- trade;
- socket;
- enchantment;
- class progression;
- summoning.

Do not create filler drops. Do not create new items solely because a schema field is empty.

---

## 10. Phase 6 — occult and summoning integration

Audit all references to:

- Occultist;
- Cultist;
- Necromancer;
- Drahkthar;
- summoning;
- ritual materials;
- dark/curse states;
- related drops and items.

Determine:

- what each class can summon;
- what resource or material is required;
- whether the summoned entity is a creature, spirit, undead, or Drahkthar;
- how the summoning connects to lore;
- how it works within the active game implementation;
- how the player obtains and consumes the relevant materials.

Examples such as essence, crystals, bones, souls, sigils, and corrupted blood are only prompts for searching existing content. Do not create them blindly.

---

## 11. Phase 7 — creature rework order

Use this order after standards and audits are ready:

1. Wildlife / Alam Liar
2. Jenggala
3. Drahkthar/demonic creatures
4. Regional creatures
5. Elite/Rare creatures
6. Mini Bosses
7. Bosses
8. Commanders/Sentinels/Chiefs
9. World/Story Bosses
10. Thalantira creatures

For each category:

1. create a category inventory;
2. identify contradictions and duplicates;
3. resolve safe issues;
4. rework lore/ecology/gameplay identity;
5. integrate drops and relevance;
6. apply stat status;
7. only calculate numbers if all stat gates pass;
8. validate Markdown/JSON consistency;
9. update the changelog;
10. run repository-wide reference checks.

Do not proceed through hundreds of entries in one uncontrolled edit. Work in reviewable batches.

---

## 12. Phase 8 — boss rework

Audit:

- Agnitra dragon bosses;
- Arkananta chiefs;
- Nusa Sayendra sentinels;
- Raksamala commanders;
- Avalerion guardians;
- Rangkaruna bosses;
- Thalantira bosses;
- story/world bosses.

Verify old class/Tier assignments against the latest class system.

For every important boss define:

- identity and lore;
- progression/story context;
- combat role;
- intended party profile;
- recognizable combat identity;
- skills and passives;
- AI/action pattern;
- phase structure;
- threshold mechanics;
- summon/add mechanics;
- arena mechanics;
- break/stagger mechanic;
- enrage condition;
- elemental and status interactions;
- counterplay and telegraphing;
- rewards and unique drops;
- numerical stat status and evidence.

Calculate each phase and the entire encounter. Include multi-actions, counters, heal, shield, regeneration, invulnerability, adds, and hazards in action economy and effective HP.

Do not solve difficulty only by increasing HP or damage.

---

## 13. Data synchronization rules

Where both Markdown and JSON versions exist:

1. identify which is canonical;
2. inspect the application/build process;
3. update the canonical source first;
4. update or regenerate mirrors using the project’s established method;
5. verify both versions agree;
6. never hand-edit generated aggregates unless that is the documented workflow.

Preserve stable IDs. Before renaming or moving any file, search the whole repository for references.

If no source/generation convention exists, document a proposed convention before mass edits.

---

## 14. Git and change safety

- Work on the current user-approved branch. If currently on `main`, recommend a feature branch but do not switch if doing so would violate user intent or discard work.
- Check `git status` before and after each batch.
- Preserve unrelated changes.
- Never use `git reset --hard`, destructive checkout, or force push.
- Do not commit unless the user requested commits or repository instructions explicitly authorize them.
- If commits are authorized, use small logical commits by phase/category.
- Do not push unless explicitly requested.

Before modifying an ID or structure consumed by the game, perform a full reference search and note compatibility impact.

---

## 15. Required documentation

Create or update, adapting paths only when an equivalent already exists:

- `06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md` — mandatory rules, supplied by project owner.
- `06_Sistem Game & Ekonomi/MONSTER_BALANCE_FRAMEWORK.md`
- `07_Bestiary/BESTIARY_REWORK_AUDIT.md`
- `07_Bestiary/BESTIARY_STANDARD_V2.md`
- `07_Bestiary/CREATURE_TAXONOMY.md`
- `07_Bestiary/BESTIARY_REWORK_CHANGELOG.md`

Do not create duplicate documentation if equivalent files exist. Merge carefully and preserve useful content.

The changelog must track:

- date/batch;
- files changed;
- creatures changed;
- canon decisions;
- schema changes;
- legacy values retained or rejected;
- items reused;
- new items proposed/created;
- stat status changes;
- simulation/playtest evidence;
- unresolved blockers;
- owner decisions required.

---

## 16. Verification after every batch

Run checks appropriate to the repository:

- Markdown formatting;
- JSON parse/validation;
- duplicate IDs and names;
- broken internal references;
- Markdown/JSON parity;
- unknown elements;
- unknown states;
- unknown item/drop references;
- obsolete class/Tier labels;
- invalid rarity terms;
- orphan files;
- generated data consistency;
- Git diff review.

For numerical changes also verify:

- source dependencies recorded;
- assumptions recorded;
- `LOW`, `EXPECTED`, and `HIGH` profiles tested;
- physical and magical cases tested;
- elemental `0.5x`, `1x`, and `2x` cases tested when possible;
- critical/burst worst case tested;
- entire troop action economy tested;
- target rounds/pressure met;
- results reproducible;
- balance status accurate.

Do not label a batch complete when required checks fail.

---

## 17. Decision policy

### May proceed automatically

- repository inspection;
- reference searches;
- audit documentation;
- schema documentation;
- obvious typo/format repairs with no canon impact;
- safe Markdown/JSON parity fixes;
- adding traceability fields;
- marking unsupported stats as legacy or blocked;
- expanding descriptions using clearly established canon;
- creating simulation scaffolding without invented inputs.

### Must stop or request owner decision before applying

- changing foundational cosmology;
- redefining a race/species/faction in a canon-changing way;
- choosing among conflicting canon sources when authority cannot be established;
- defining final level cap, party size, or progression bands;
- choosing target encounter duration/pressure without project guidance;
- changing core damage/element/state formulas;
- deleting established creatures/items/lore;
- changing database IDs;
- introducing a new rarity tier;
- introducing Void as a standard combat element;
- assigning `VALIDATED` without playtest evidence.

When blocked, do not halt all useful work. Complete safe work, record the blocker, and present a concise decision list.

---

## 18. First execution instructions

Begin now in this exact order:

1. Read applicable `AGENTS.md` files.
2. Inspect Git status and repository structure.
3. Verify the existence and content of `06_Sistem Game & Ekonomi/Pedoman_Pemberian_Stat.md`.
4. Locate Bestiary, class, skill, state, item, equipment, element, forge, crafting, economy, region, race, story, and runtime database files.
5. Determine source-of-truth and generated-file relationships.
6. Create/update `BESTIARY_REWORK_AUDIT.md`.
7. Create/update `BESTIARY_STANDARD_V2.md`.
8. Create/update `CREATURE_TAXONOMY.md`.
9. Create/update `MONSTER_BALANCE_FRAMEWORK.md`:
   - populate it numerically only if all required inputs exist;
   - otherwise create a blocked framework and a precise missing-data report.
10. Begin the Wildlife / Alam Liar rework as the first controlled batch.
11. Update the changelog.
12. Run verification and review the diff.

For Wildlife:

- improve identity, ecology, behavior, habitat, civilization/economic relationship, gameplay role, spawn structure, and drops;
- reuse existing canon/items;
- preserve useful lore;
- mark existing unsupported numbers as legacy candidates;
- do not replace unsupported numbers with guesses;
- assign numerical values only if the stat gates are satisfied.

After Wildlife, do not automatically rewrite the entire remaining Bestiary in one pass. Report the completed batch, blockers, owner decisions, and the safest next batch. Continue automatically only when the next batch does not require unresolved canon or balance decisions.

---

## 19. Required completion report

At the end of each execution, report:

### Changes

- files created;
- files modified;
- creatures audited;
- creatures reworked;
- duplicate entries resolved;
- terminology normalized;
- items reused;
- items proposed/created;
- legacy numbers retained, removed, or marked blocked;
- stat statuses assigned or changed.

### Verification

- checks run;
- checks passed;
- checks failed;
- simulations run;
- playtest evidence available;
- Markdown/JSON parity status.

### Blockers

- missing runtime databases;
- missing formulas;
- missing progression/equipment baseline;
- canon conflicts;
- decisions requiring project-owner approval.

### Next action

Provide one recommended next batch with clear scope. Do not claim completion if the repository still has known unresolved issues within the requested batch.

---

## 20. Definition of success

The rework is successful when:

- every creature belongs to a coherent taxonomy;
- region and ecology explain why it exists and where it appears;
- lore and gameplay identity reinforce each other;
- drops connect to real uses and the economy;
- skills and AI provide a distinct combat role;
- bosses are defined by mechanics rather than HP inflation;
- numerical stats are traceable to actual formulas and party baselines;
- unsupported numbers are visibly blocked or provisional;
- Markdown, JSON, and game references remain consistent;
- changes are reviewable, reversible, and documented.

The priority is not to fill every field quickly. The priority is to build a Bestiary that is internally consistent, implementable, measurable, and trustworthy.
