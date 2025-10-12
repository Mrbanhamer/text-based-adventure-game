
from colorama import init, Fore     # external lib for simple terminal colors
init(autoreset=True)                # auto-reset colors after each print

from rpg.entities import create_skeleton, create_dragon  # enemy factories


def _player_damage(bag: list[str]) -> int:
    """
    Compute a player damage number from picked items (strings).
    Rules:
      base = 2
      +1 if "Sword"
      +1 if "Bow"
      +2 if "Battle Axe"
      +1 if "Dagger"
    """
    base = 2
    s = {n.lower() for n in bag}
    if "sword" in s:
        base += 1
    if "bow" in s:
        base += 1
    if "battle axe" in s:
        base += 2
    if "dagger" in s:
        base += 1
    return max(1, base)


def _enemy_for_room(room_name: str):
    """Return an enemy object based on the room name (or None if no enemy)."""
    name = room_name.lower()
    if name == "cemetery":
        return create_skeleton()
    if name == "dragon's lair":
        return create_dragon()
    return None


def start_combat_in_room(room_name: str, bag: list[str], player_hp: int = 10) -> str:
    """
    Very small loop combat:
      - If room is Dragon's Lair:
          * Win instantly if you have Armor + Battle Axe + Shield
          * Otherwise, refuse the fight
      - Else (e.g., Cemetery): player and enemy trade hits until one falls.

    Returns: "win", "lose", or "none" (if no fight happened).
    """
    room_lower = room_name.lower()

    # --- Special story rule: the Dragon is only beatable with full gear 
    if room_lower == "dragon's lair":
        need = {"armor", "battle axe", "shield"}
        have = {n.lower() for n in bag}
        if not need.issubset(have):
            print("You are not ready for the Dragon (need: Armor, Battle Axe, Shield).")
            return "none"
        # Fully equipped → auto victory 
        print("You are fully equipped to face the Dragon!")
        print("With your powerful gear, you slay the Dragon in one mighty blow!")
        print(Fore.GREEN + "Congratulations — you won the game! 🏆")
        return "win"

    # --- Normal combat flow for regular enemies (e.g., Skeleton)
    enemy = _enemy_for_room(room_name)
    if enemy is None:
        print("(combat) No enemy in this room.")
        return "none"

    print(f"A {enemy.name} appears! {enemy.info()}")
    php = player_hp  # player's temporary HP for this fight

    while True:
        # Player turn
        pdmg = _player_damage(bag)
        enemy.take_damage(pdmg)
        print(f"You hit the {enemy.name} for {pdmg}. {enemy.name} HP = {enemy.hp}")
        if not enemy.is_alive():
            print(Fore.GREEN + f"You defeated the {enemy.name}!")
            return "win"

        # Enemy turn
        edmg = enemy.attack()
        php = max(0, php - edmg)
        print(f"The {enemy.name} hits you for {edmg}. Your HP = {php}")
        if php <= 0:
            print(Fore.RED + "You died. Game over.")
            return "lose"