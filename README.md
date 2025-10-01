# text based adventure game
A game where you go on a adventure using text instead of a visual screen

Updated readme file

 Struktur:

 rpg-game/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ game.py # Programstart (CLI)
├─ rpg/
│ ├─ __init__.py
│ ├─ core/
│ │ ├─ __init__.py
│ │ ├─ game.py # Game-loop & tillstånd
│ │ ├─ world.py # World, Location
│ │ └─ data_loader.py # Laddar JSON-data
│ ├─ entities/
│ │ ├─ __init__.py
│ │ ├─ player.py # Player-klass (HP, gold, inventory)
│ │ ├─ npc.py # NPC-klass (dialog, trade)
│ │ ├─ inventory.py # Inventory-klass
│ │ └─ items.py # Item, Weapon, Consumable
│ ├─ systems/
│ │ ├─ __init__.py
│ │ ├─ combat.py # fight
│ │ ├─ dialogue.py # talk to npc
│ │ ├─ movement.py # walk to destination
│ │ ├─ loot.py # pick up items
│ │ └─ trading.py # trade with npc (prio)
│ └─ utils/
│ ├─ __init__.py
│ ├─ io.py # Rich console-UI
│ ├─ save_load.py # spara/ladda (json)
│ └─ time_utils.py # datetime-hjälp
├─ data/
│ ├─ items.json
│ ├─ npcs.json
│ └─ world.json
└─ tests/
├─ __init__.py
└─ test_combat.py
