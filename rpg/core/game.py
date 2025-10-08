import json
from .world import starting, enemy_room, boss_room, npc_room1, npc_room2, Lab_room, prisoner_room
from rpg.systems.movement import movement_place

def run_game():
    global current_room
    current_room = starting
    while True:
        if current_room in (npc_room1, npc_room2):
            print("type <trade> to trade")
        print("type <move> to move to a different room")
        print("type <inventory> to open the inventory")
        # skriv in rummen du ska kunna plocka up items från
        if current_room in ():
            print("pickup item")
        command = input("decide action: ")
        if command.lower() == "move":
            current_room = movement_place(current_room)
        elif command.lower() == "trade" and current_room in (npc_room1, npc_room2):
            #trade():
            pass
        elif command.lower() == "inventory":
            pass
        elif command.lower() == "fight" and current_room in (enemy_room, boss_room):
            pass
        elif command.lower() == "pickup" and current_room in ():
            pass


# Start the game
if __name__ == "__main__":
    run_game()