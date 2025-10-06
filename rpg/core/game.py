# main.py
from world import starting, enemy_room, boss_room, npc_room

current_room = starting

def run_game():
    global current_room
    print(f"You are in the {current_room.name}.")
    
    while True:
        print(f"Connected rooms: {', '.join(current_room.get_connections())}")
        next_room_name = input("Where do you want to go? ").strip()
        
        # Find the room object with that name in current room's connections
        found_room = None
        for room in current_room.connections:
            if room.name.lower() == next_room_name.lower():
                found_room = room
                break
        
        if found_room:
            current_room = found_room
            print(f"You move to the {current_room.name}.\n")
        else:
            print("You can't go there from here.\n")

# Start the game
if __name__ == "__main__":
    run_game()
