
from rpg.entities import create_skeleton, create_dragon  # enemy factories
from colorama import init, Fore
init(autoreset=True)


def _player_damage(bag: list[str]) -> int:
    """
    Compute a tiny player damage number from picked items (strings).
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
    """Return an enemy object based on the room name."""
    name = room_name.lower()
    if name == "cemetery":
        return create_skeleton()
    if name == "dragon's lair":
        return create_dragon()
    return None


def start_combat_in_room(room_name: str, bag: list[str], player_hp: int = 10) -> str:
    """
    Very small loop:
      - player hits first using _player_damage(bag)
      - enemy hits using enemy.attack()
    Returns "win" or "lose".
    """
    enemy = _enemy_for_room(room_name)
    if enemy is None:
        print("(combat) No enemy in this room.")
        return "none"

    print(f"A {enemy.name} appears! {enemy.info()}")

    # Simple player state (just HP number for now)
    php = player_hp

    while True:
        # Player turn
        pdmg = _player_damage(bag)
        enemy.take_damage(pdmg)
        print(f"You hit the {enemy.name} for {pdmg}. {enemy.name} HP = {enemy.hp}")
        if not enemy.is_alive():
            print(Fore.GREEN +f"You defeated the {enemy.name}!")
            return "win"

        # Enemy turn
        edmg = enemy.attack()
        php = max(0, php - edmg)
        print(f"The {enemy.name} hits you for {edmg}. Your HP = {php}")
        if php <= 0:
            print(Fore.RED +"You died. Game over.")
            return "lose"