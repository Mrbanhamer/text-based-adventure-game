from rpg.core.world import starting, enemy_room, boss_room, npc_room1, npc_room2, Lab_room, prisoner_room

def movement_place(current_room):
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
            return current_room
        else:
            print("You can't go there from here.\n")