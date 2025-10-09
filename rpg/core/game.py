import json  
from rpg.systems.combat import start_combat_in_room
from .world import (
    starting, enemy_room, boss_room,
    npc_room1, npc_room2, lab_room, prisoner_room
)

# Movement helper (should return the next room object)
from rpg.systems.movement import movement_place

# Import JSON helpers for items
from .data_loader import (
    load_items_json, room_items_map,
    pop_item_from_room, save_items_json
)
from colorama import init, Fore, Style  # external lib for  colors
init(autoreset=True)

#  which rooms allow picking items (adjust as you like)
PICKUP_ROOMS = (npc_room1, npc_room2, lab_room)

#  (list of item names) until a full Player/Inventory is plugged in
bag: list[str] = []


def run_game() -> None:
    print(Fore.CYAN +"=== Dungeon Escape ===", flush=True)
    """
     main loop:
      - Shows context actions depending on the current room
      - Reads a  command and executes a tiny placeholder
      - Movement is delegated to movement_place(current_room)
      -  'pickup' using items.json via data_loader
    """
    global current_room  
    current_room = starting  # begin in the Corridor

    # Load items JSON once and keep a small in-memory map (room -> [items...])
    items_data = load_items_json()
    room_to_items = room_items_map(items_data)

    while True:
        #  Contextual hints (what you can do here) 
        if current_room in (npc_room1, npc_room2):
            print("type <trade> to trade")
            print("type <talk> to talk to the merchant") 

        print("type <move> to move to a different room")
        print("type <inventory> to open the inventory")

        # Rooms where you can pick up items (placeholder)
        if current_room in PICKUP_ROOMS:
            print("type <pickup> to pick up an item")

        # Enemies live in these rooms; offer the fight command
        if current_room in (enemy_room, boss_room):
            print("type <fight> to fight")

        #  Read a command 
        command = input("decide action: ").strip().lower()

        # --- Movement 
        if command == "move":
            next_room = movement_place(current_room)
            if next_room is not None:
                current_room = next_room
            else:
                print("You stay where you are.")

        # --- Trading (only in NPC rooms) 
        elif command == "trade" and current_room in (npc_room1, npc_room2):
            print("(trade) You talk to the merchant... (placeholder)")

        # --- Inventory screen 
        elif command == "inventory":
            if bag:
                print("\n--- INVENTORY ---")
                for n in bag:
                    print(f"- {n}")
                print("-----------------\n")
            else:
                print("(inventory) Your bag is currently empty.")

        # --- Fighting 
        elif command == "fight":
            # Only allow in enemy rooms
            if current_room not in (enemy_room, boss_room):
                print("There is no enemy here.")
            else:
                # Optional: require gear before Dragon (story rule)
                if current_room is boss_room:
                    need = {"Armor", "Battle Axe", "Shield"}
                    if not need.issubset({n for n in bag}):
                        print("You are not ready for the Dragon (need: Armor, Battle Axe, Shield).")
                    else:
                        start_combat_in_room(current_room.name, bag, player_hp=10)
                else:
                    start_combat_in_room(current_room.name, bag, player_hp=10)

        # --- Pick up item (only in pickup rooms) 
        elif command == "pickup" and current_room in PICKUP_ROOMS:
            room_name = current_room.name
            items_here = room_to_items.get(room_name, [])

            if not items_here:
                print("(pickup) There is nothing to pick up here.")
            else:
                item_name = items_here[0]     # take the first item 
                bag.append(item_name)         # add to temporary bag
                print(f"(pickup) You picked up: {item_name}")

                removed = pop_item_from_room(room_name, item_name, items_data)
                if removed:
                    save_items_json(items_data)
                    room_to_items = room_items_map(items_data)
        elif command == "talk":
            if current_room in (npc_room1, npc_room2):
                print(Fore.CYAN + "Merchant: 'Greetings, traveler. Looking for gear?'")
            else:
                print("No one to talk to here")

        # --- Exit the loop 
        elif command in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        # --- Unknown command 
        else:
            print("Unknown command. Try: move, trade, inventory, fight, pickup, quit")