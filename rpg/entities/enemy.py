import random  # for simple damage rolls


class Enemy:
    """A very small enemy object."""

    def __init__(self, name, hp, dmg_min, dmg_max):
        
        self.name = name        # enemy name 
        self.hp = hp            # hit points (health)
        self.dmg_min = dmg_min  # lowest damage per hit
        self.dmg_max = dmg_max  # highest damage per hit

    def is_alive(self):
        # Returns True if the enemy has more than 0 HP
        return self.hp > 0

    def take_damage(self, amount):
        # Decrease HP by 'amount', but never below 0
        if amount < 0:
            amount = 0
        self.hp = max(0, self.hp - amount)

    def attack(self):
        # Return a random damage value between dmg_min and dmg_max
        return random.randint(self.dmg_min, self.dmg_max)

    def info(self):
        # A simple text about this enemy
        return f"{self.name} (HP: {self.hp}, dmg: {self.dmg_min}-{self.dmg_max})"


# Ready-made enemies for our story (use these helpers to create them)
def create_skeleton():
    # Weak enemy for early game
    return Enemy("Skeleton", 6, 1, 3)


def create_dragon():
    # Strong final boss
    return Enemy("Dragon", 30, 4, 8)