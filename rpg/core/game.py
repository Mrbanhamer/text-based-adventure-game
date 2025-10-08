# main.py
import json
from .world import starting, enemy_room, boss_room, npc_room1, npc_room2, Lab_room, prisoner_room

def run_game():
    global current_room
    current_room = starting
    while True:
        if current_room == npc_room1 or npc_room2:
            print("type <trade> to trade")
        print("type <move> to move to a different room")
        command = input("decide action: ")
        if command == "move":
            while True:
                print(f"\nYou are in the {current_room.name}.")
                print(f"\nConnected rooms: {', '.join(current_room.get_connections())}")
                next_room_name = input("\nWhere do you want to go? ").strip()
                
                # Find the room object with that name in current room's connections
                found_room = None
                for room in current_room.connections:
                    if room.name.lower() == next_room_name.lower():
                        found_room = room
                        break
                
                if found_room:
                    current_room = found_room
                    print(f"You move to the {current_room.name}.\n")
                    break
                else:
                    print("You can't go there from here.\n")
        elif command == "trade" and current_room == npc_room1 or npc_room2:
            #trade():
            pass


# Start the game
if __name__ == "__main__":
    run_game()
