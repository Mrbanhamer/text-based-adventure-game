import json
import random

# -----------------------------
# Läsa JSON-filen
# -----------------------------
with open("world.json", "r") as file:
    world = json.load(file)

# -----------------------------
# Spelarstatus
# -----------------------------
inventory = []
gold = 5
hp = 10
current_node = "start"

# -----------------------------
# Huvudloop för spelet
# -----------------------------
while True:
    node = world[current_node]

    # Visa nodens text
    print("\n" + node["text"] + "\n")

    # Slumpmässiga händelser
    if current_node == "steal_result":
        if random.random() < 0.5:
            current_node = "steal_success"
        else:
            current_node = "steal_fail"
        continue

    if current_node == "battle_result":
        if "Armor" in inventory and "Axe" in inventory:
            current_node = "battle_victory"
        elif "Sword" in inventory and random.random() < 1/3:
            current_node = "battle_victory"
        elif "Bow" in inventory and random.random() < 0.5:
            current_node = "battle_victory"
        else:
            current_node = "skeleton_defeat"
        continue

    if current_node == "dragon_result":
        if all(item in inventory for item in ["Armor", "Axe", "Shield"]):
            current_node = "dragon_victory"
        else:
            current_node = "dragon_defeat"
        continue

    # Visa val
    choices = node.get("choices", [])
    if not choices:
        print("\nGAME OVER")
        print(f"HP: {hp}, Gold: {gold}, Inventory: {inventory}")
        break

    for i, choice in enumerate(choices):
        print(f"{i+1}. {choice['text']}")

    # Få spelarens val
    try:
        selection = int(input("\nChoose an option: ")) - 1
        if selection < 0 or selection >= len(choices):
            print("Invalid choice. Try again.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue

    choice_data = choices[selection]

    # Hantera guld
    if "cost" in choice_data:
        if gold >= choice_data["cost"]:
            gold -= choice_data["cost"]
            print(f"You paid {choice_data['cost']} gold.")
        else:
            print("Not enough gold!")
            continue

    # Lägg till item
    if "add_item" in choice_data:
        inventory.append(choice_data["add_item"])
        print(f"You obtained: {choice_data['add_item']}")

    if "add_items" in choice_data:
        for item in choice_data["add_items"]:
            inventory.append(item)
            print(f"You obtained: {item}")

    # Ändra HP
    if "hp_change" in node:
        hp += node["hp_change"]
        print(f"Your HP changed by {node['hp_change']}")

    # Gå till nästa nod
    current_node = choice_data["next"]