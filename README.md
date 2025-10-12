# Ett enkelt textbaserat äventyrsspel byggt för att träna grunder: klasser, moduler, JSON-data, ett externt bibliotek och Git/GitHub-flöde.

-----------------------------------------------------

Struktur:

text-based-adventure-game/
├─ run.py                     # startar spelet
├─ requirements.txt           # colorama
├─ README.md
├─ rpg/
│  ├─ __init__.py
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ game.py             # huvud-loopen (move, pickup, inventory, fight, talk)
│  │  ├─ world.py            # Room-grafen (Corridor, Cemetery, etc.)
│  │  └─ data_loader.py      # laddar items.json/world.json och enkla helpers
│  ├─ systems/
│  │  ├─ __init__.py
│  │  ├─ movement.py         #  room→room förflyttning
│  │  └─ combat.py           #  strid + colorama-färg
│  └─ entities/
│     ├─ __init__.py         # exporterar Enemy + factories (create_skeleton/dragon) m.m.
│     ├─ items.py            # Item 
│     ├─ inventory.py        # Inventory 
│     ├─ enemy.py            # Enemy + create_skeleton/create_dragon
│     ├─ npc.py              # minimal NPC (talk)
│     └─ player.py           # Player 
├─ data/
│  ├─ items.json             # föremål + vilka rum som har loot
│  └─ world.json             # namn + beskrivning + connections
└─ .gitignore                #  Python-cache m.m.

----------------------------------------------------------------------------------------------------
Flowchart:

<img width="565" height="525" alt="flowchart" src="https://github.com/user-attachments/assets/4dcf06d2-692a-4cd9-b3bd-2a884573d27a" />


--------------------------------------------------------------------------------------

Game Story:

You wake up on a cold stone floor in a dark corridor, with no memory of how you got there. In your pocket, you find five gold coins — your only possession in this strange place. Ahead of you, the corridor splits, and your adventure begins.

To the left lies the armory, where a merchant offers you weapons. You may buy a sword, a bow — or try to steal a shield. Every choice you make shapes your destiny.
Further ahead, you discover the wizard’s laboratory, where a glowing health potion rests on the table. Will you give it to the wounded prisoner you meet later, or leave him to die?

If you choose compassion, the prisoner rewards you with a key to the second armory, where you find a battle axe and body armor.
But danger awaits — a skeleton blocks your path, its eyes glowing with eerie light. Only the well-prepared can defeat it and continue deeper into the dungeon.

Beyond the darkness lies your final trial: the Dragon.
Only those who carry armor, a battle axe, and a shield can survive its flames and escape into the moonlight — victorious at last.


--------------------------------------------------------------------------------------------
## Funktioner

- **Gå mellan rum:** Corridor, Laboratory, Big/Small Armory, Prison, Cemetery, Dragon’s Lair.
- **Plocka upp föremål:** Sword, Shield, Bow, Health Potion (från `data/items.json`).
- **Inventering:** se vad du bär just nu (enkel lista).
- **Strid:** Skeleton i Cemetery, och gating inför Dragon (kräver Armor + Battle Axe + Shield).
- **NPC-dialog:** enkel `talk` i armory-rum.
- **Extern modul:** [Colorama](https://pypi.org/project/colorama/) för enkel färg i konsolen.
- **JSON-data:** värld och items laddas från `data/world.json` och `data/items.json`.


--------------------------------------------------------------------------------------------

## Kommandon i spelet

- `move` → välj ett angränsande rum (skriv rumsnamnet)
- `pickup` → plocka upp första item i rummet (om något finns)
- `inventory` → visa det du bär (namnlista)
- `fight` → strid i Cemetery/Dragon’s Lair
- `talk` → prata med merchant i armory-rum
- `quit`/`exit`/`q` → avsluta


> I Dragon’s Lair måste du ha **Armor + Battle Axe + Shield** för att få slåss.

-----------------------------------------------------------------------------------------

## Installation

Kräver Python 3.10+.

```bash
# klona repo och gå till projektroten
git clone <repo-url>
cd text-based-adventure-game

# skapa/aktivera isolerad miljö
python -m venv .venv
# Git Bash:
source .venv/Scripts/activate


# installera beroenden
python -m pip install -r requirements.txt


Kör spelet:
# Git Bash på Windows:
winpty python -u run.py

# PowerShell/CMD:
python -u run.py

-----------------------------------------------

Gruppmedlemmar och arbetsfördelning

Projektet genomfördes som ett grupparbete med fyra deltagare. Arbetet organiserades via GitHub där varje medlem ansvarade för sin egen branch enligt följande:

feature-entities – Mahtab

feature-systems – Leonard

feature-core – Michael

feature-utils – Even

-----------------------------------------------

Mahtab:

Ansvarade för GitHub-strukturen, skapandet av branches och projektets mappstruktur.
Arbetade huvudsakligen med filerna player, enemy, game, combat och data_loader, samt hanterade felsökning och körning av projektet.

Leonard:

Skapade GitHub-repositoriet och ansvarade för den initiala planeringen av projektet.
Bidrog till att fördela uppgifter inom gruppen och arbetade med filerna game, movement, npc och __init__.

Michael:

Utvecklade projektets flödesschema och deltog i planeringen av spelets övergripande struktur.
Arbetade med filerna item och inventory, samt bidrog till problemlösning under utvecklingsprocessen.

Even:

Ansvarade för spelberättelsen och förtydligade händelseförloppet i spelet.
Arbetade med JSON-filerna och data_loader, samt deltog i planeringen och anpassningen av spelets innehåll.

---Samtliga gruppmedlemmar deltog i arbetet med README-filen och samarbetade aktivt med felsökning och stöd i GitHub-miljön under hela projektets gång.

-------------------------------------------------------------------

Vårt spel är byggt som en MVP (“Minimum Viable Product”) – en enkel, körbar version som visar våra viktigaste idéer: rörelse mellan rum, strid, och hantering av föremål. Det fungerar som en grund som vi kan bygga vidare på i framtiden.

---------------------------------------------------------------------




