from rpg.entities import Enemy  # type hints only (we also accept any object with .hp/.attack/.take_damage)
# We will compute damage using only player.items (a list of strings)


def _player_damage(player) -> int:
    """
    Compute a very simple player damage number based on items (strings) in player.items.

    Rules (easy to tweak):
      - Base damage = 2
      - +1 if player has "Sword"
      - +1 if player has "Bow"
      - +2 if player has "Battle Axe"
      - +1 if player has "Dagger"

    We do NOT stack weapon types realistically; we just add bonuses if the string is present.
    This keeps it simple for beginners.
    """
    base = 2
    items = set(player.items)  # set for quick "in" checks

    if "Sword" in items:
        base += 1
    if "Bow" in items:
        base += 1
    if "Battle Axe" in items:
        base += 2
    if "Dagger" in items:
        base += 1

    # never return less than 1 damage
    return max(1, base)


def _enemy_damage(enemy: Enemy, player) -> int:
    """
    Enemy rolls damage using enemy.attack().
    We then reduce incoming damage if the player has defensive items:

      - "Shield" reduces damage by 1
      - "Armor"  reduces damage by 1

    Damage never goes below 0.
    """
    dmg = enemy.attack()
    items = set(player.items)

    if "Shield" in items:
        dmg -= 1
    if "Armor" in items:
        dmg -= 1

    return max(0, dmg)


def start_combat(player, enemy: Enemy) -> str:
    """
    Run a tiny turn-based combat:
      1) Player hits first
      2) If enemy still alive, enemy hits
      3) Repeat until someone reaches 0 HP

    Prints simple log lines and returns:
      - "win"  if enemy dies
      - "lose" if player dies
    """
    print(f"A {enemy.name} appears! ({enemy.info()})", flush=True)

    while True:
        # --- Player's turn ---
        pdmg = _player_damage(player)
        enemy.take_damage(pdmg)
        print(f"You hit the {enemy.name} for {pdmg}. {enemy.name} HP = {enemy.hp}", flush=True)

        if not enemy.is_alive():
            print(f"You defeated the {enemy.name}!", flush=True)
            return "win"

        # --- Enemy's turn ---
        edmg = _enemy_damage(enemy, player)
        if edmg > 0:
            player.take_damage(edmg)
            print(f"The {enemy.name} hits you for {edmg}. Your HP = {player.hp}", flush=True)
        else:
            print(f"The {enemy.name} fails to hurt you.", flush=True)

        if not player.is_alive():
            print("You died. Game over.", flush=True)
            return "lose