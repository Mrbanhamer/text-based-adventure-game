# Import Player class (represents the human player: name, hp, gold, items)
from rpg.entities import Player

# Import helpers to load the world (locations/exits) from data/world.json
from rpg.core.data_loader import load_world, get_default_world_path


def run_game() -> None:
    # --- Setup (title + player creation) ---
    # Print a simple title. flush=True makes sure it appears immediately in some terminals.
    print("=== Dungeon Escape (prototype) ===", flush=True)

    # Ask the user for their name. If empty, use "Hero".
    # .strip() removes extra spaces; .lower() is not needed here because names can keep case.
    name = input("Enter your name: ").strip() or "Hero"

    # Create the Player object with default stats (hp=10, gold=5, items=[])
    player = Player(name)

    # --- Load world data from JSON ---
    # Compute the absolute path to data/world.json so it works from anywhere in the project.
    world_path = get_default_world_path()

    # Read and build the World object (with Location objects inside) from the JSON file.
    world = load_world(world_path)

    # --- Choose a start location ---
    # We try to start in a location named "Corridor" (if it exists).
    # If not, we pick the first available location in the world (if any).
    current_name = "Corridor" if world.get("Corridor") else (world.list_names()[0] if world.list_names() else None)

    # If there are no locations at all, we cannot run the game. Exit politely.
    if current_name is None:
        print("No locations found in world data. Exiting.", flush=True)
        return

    # --- Small helper to show where we are ---
    # This inner function prints the current location name, description, and exits.
    def show_location() -> None:
        # Look up the Location object by its name.
        loc = world.get(current_name)

        # Safety check: if something went wrong and the location is missing, tell the player.
        if not loc:
            print("(Unknown place)", flush=True)
            return

        # Show a human-friendly description: "Name: Description. Exits: left, right"
        print(loc.describe(), flush=True)

    # Greet the player and hint that 'help' shows the commands.
    print(f"Welcome, {player.name}! Type 'help' for commands.", flush=True)

    # Immediately show where the player is (name/description/exits).
    show_location()

    # --- Main command loop ---
    # Keep asking for commands until the player types quit/exit/q.
    while True:
        # Read one command line from the user.
        # .strip() removes spaces; .lower() makes command matching easier.
        cmd = input("> ").strip().lower()

        # --- Quit command ---
        # If the user wants to exit, say goodbye and break the loop.
        if cmd in ("quit", "exit", "q"):
            print("Goodbye!", flush=True)
            break

        # --- Help command ---
        # Show a short list of available commands (kept minimal for beginners).
        elif cmd == "help":
            print(
                "Commands: help, status, look, where, exits, "
                "go <direction>, take <item>, damage <n>, heal <n>, quit",
                flush=True
            )

        # --- Status command ---
        # Print player's name, HP, gold, and a comma-separated list of carried item names.
        elif cmd == "status":
            items = ", ".join(player.items) if player.items else "(no items)"
            print(f"Name: {player.name} | HP: {player.hp} | Gold: {player.gold} | Items: {items}", flush=True)

        # --- Look command ---
        # Reprint the current location description (useful after moving).
        elif cmd == "look":
            show_location()

        # --- Where/Exits command ---
        # Show only the available exits (directions) from the current location.
        elif cmd in ("where", "exits"):
            loc = world.get(current_name)
            if loc and loc.exits:
                # Sort exits for stable order (e.g., "left, right").
                print("Exits:", ", ".join(sorted(loc.exits.keys())), flush=True)
            else:
                print("No exits here.", flush=True)

        # --- Go command ---
        # Move to another location by direction: e.g., "go left"
        elif cmd.startswith("go "):
            # Extract everything after the first space: that's the direction text.
            direction = cmd.split(" ", 1)[1].strip().lower()

            # Get the current Location object.
            loc = world.get(current_name)

            # Safety check: if current location vanished (should not happen), warn and continue.
            if not loc:
                print("You are nowhere. (Data error)", flush=True)
                continue

            # Look up the target location name for this direction (or None if invalid).
            target_name = loc.get_exit(direction)

            # If the exit exists and the target location is valid, move and show the new place.
            if target_name and world.get(target_name):
                current_name = target_name
                show_location()
            else:
                # Otherwise inform the player that this direction is not available from here.
                print(f"You can't go '{direction}' from here.", flush=True)

        # --- Take command ---
        # Add a plain item name into the player's simple bag (placeholder system for now).
        elif cmd.startswith("take "):
            # Extract the item name text after "take ".
            item_name = cmd.split(" ", 1)[1].strip()

            # Only add if the user actually typed a name.
            if item_name:
                player.add_item(item_name)
                print(f"Added item: {item_name}", flush=True)
            else:
                print("Usage: take <item>", flush=True)

        # --- Damage command ---
        # Reduce the player's HP by an integer amount: e.g., "damage 3"
        elif cmd.startswith("damage "):
            try:
                # Parse the number after "damage ".
                amount = int(cmd.split(" ", 1)[1].strip())
            except ValueError:
                # If not a valid integer, show correct usage and continue the loop.
                print("Usage: damage <number>", flush=True)
                continue

            # Apply damage (the Player class prevents HP from going below 0).
            player.take_damage(amount)
            print(f"HP is now {player.hp}", flush=True)

            # If HP reached 0, end the game.
            if not player.is_alive():
                print("You died. Game over.", flush=True)
                break

        # --- Heal command ---
        # Increase the player's HP by an integer amount: e.g., "heal 2"
        elif cmd.startswith("heal "):
            try:
                # Parse the number after "heal ".
                amount = int(cmd.split(" ", 1)[1].strip())
            except ValueError:
                print("Usage: heal <number>", flush=True)
                continue

            # Apply healing (we do not cap maximum HP yet, to keep things simple).
            player.heal(amount)
            print(f"HP is now {player.hp}", flush=True)

        # --- Unknown command fallback ---
        # If the user typed something we do not recognize, suggest using help.
        else:
            print("Unknown command. Type 'help'.", flush=True)