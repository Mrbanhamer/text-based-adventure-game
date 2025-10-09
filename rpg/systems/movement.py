
from rpg.core.world import (
    starting, enemy_room, boss_room,
    npc_room1, npc_room2, lab_room, prisoner_room
)



def movement_place(current_room):
    """
    Ask the player for the name of a connected room and move there.

    Input:  current_room (a Room object)
    Output: the chosen Room object (or the same room if staying/cancel)

    Rules:
      - We print where you are and list connected room names.
      - The player must type the *full* room name exactly as shown
        (case-insensitive match is allowed).
      - Empty input / 'stay' / 'cancel' keeps you in the same room.
    """
    while True:
        # Show current location
        print(f"\nYou are in the {current_room.name}.", flush=True)

        # List connections by their visible names
        names = current_room.get_connections()
        if names:
            print(f"Connected rooms: {', '.join(names)}", flush=True)
        else:
            # Dead end: no exits from here
            print("There are no exits from here.", flush=True)
            return current_room

        # Ask for a destination by *room name*
        next_room_name = input("Where do you want to go? ").strip()

        # Allow a simple cancel/stay option
        if next_room_name.lower() in ("", "stay", "cancel"):
            print("You stay where you are.", flush=True)
            return current_room

        # Try to find a connection with that name (case-insensitive)
        found_room = None
        for r in current_room.connections:
            if r.name.lower() == next_room_name.lower():
                found_room = r
                break

        if found_room:
            print(f"You move to the {found_room.name}.\n", flush=True)
            return found_room
        else:
            print("You can't go there from here. Type an exact connected room name.", flush=True)
            