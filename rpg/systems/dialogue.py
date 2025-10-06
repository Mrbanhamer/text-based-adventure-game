
from rpg.entities import NPC, Player  # Use our simple NPC and Player classes


def start_dialogue(npc: NPC, player: Player) -> None:
    """
    Run a very small text-based dialogue loop with one NPC.

    Commands inside the loop:
      - say           -> the NPC speaks its current dialogue line
      - set <text>    -> change the NPC's dialogue line (useful for testing)
      - bye / q / exit-> end the conversation

    This function is intentionally small so we can extend it later
    (e.g., trade, quests) without confusing beginners.
    """
    # Greeting line to show who you are talking to
    print(f"You approach {npc.name}.", flush=True)

    # If the NPC has no dialogue yet, hint how to add one
    if not npc.speak():
        print("(This NPC has no dialogue yet. Type: set Hello there!)", flush=True)

    # Dialogue input loop
    while True:
        cmd = input("(talk)> ").strip().lower()  # read a small command

        # End the conversation
        if cmd in ("bye", "q", "exit"):
            print("You end the conversation.", flush=True)
            break

        # Make the NPC speak its current line (may be empty)
        elif cmd == "say":
            line = npc.speak()
            if line:
                print(f"{npc.name}: {line}", flush=True)
            else:
                print(f"{npc.name} is silent.", flush=True)

        # Change the NPC's dialogue line (useful for quick tests)
        elif cmd.startswith("set "):
            text = cmd.split(" ", 1)[1]  # grab everything after 'set '
            npc.set_dialogue(text)
            print("Dialogue updated.", flush=True)

        # Help / fallback
        else:
            print("Commands: say, set <text>, bye", flush=True)