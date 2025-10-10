import random  # used for enemy.attack() damage rolls


class Enemy:
    """A very small enemy object with HP and a simple damage range."""

    def __init__(self, name: str, hp: int, dmg_min: int, dmg_max: int):
        self.name = name          # enemy display name
        self.hp = hp              # hit points (health)
        self.dmg_min = dmg_min    # minimum damage per hit
        self.dmg_max = dmg_max    # maximum damage per hit
        self._first_hit_done = False  # prevents dying on the very first hit

    def is_alive(self) -> bool:
        # Returns True if the enemy has more than 0 HP
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        # Decrease HP by 'amount', but never below 0
        if amount < 0:
            amount = 0
        # First-hit protection: if first hit would kill, leave 1 HP instead
        if not self._first_hit_done and amount >= self.hp:
            self.hp = 1
            self._first_hit_done = True
            return
        self.hp = max(0, self.hp - amount)
        self._first_hit_done = True

    def attack(self) -> int:
        # Return a random damage value between dmg_min and dmg_max (inclusive)
        return random.randint(self.dmg_min, self.dmg_max)

    def info(self) -> str:
        # Simple text about this enemy (used in logs/prints)
        return f"{self.name} (HP: {self.hp}, dmg: {self.dmg_min}-{self.dmg_max})"


#  enemies for our story 

def create_skeleton() -> Enemy:
    # Weak enemy for early game; enough HP to avoid easy one-shots
    return Enemy("Skeleton", hp=10, dmg_min=1, dmg_max=3)


def create_dragon() -> Enemy:
    # Strong final boss
    return Enemy("Dragon", hp=40, dmg_min=4, dmg_max=8)