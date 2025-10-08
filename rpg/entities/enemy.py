import random

class Enemy:
    
    def __init__(self, name, hp, dmg_min, dmg_max):
        self.name = name
        self.hp = hp
        self.dmg_min = dmg_min
        self.dmg_max = dmg_max
        self._first_hit_done = False  # True after the enemy has been hit once

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        if amount < 0:
            amount = 0
        # If this is the first hit and it would kill us, leave 1 HP instead
        if not self._first_hit_done and amount >= self.hp:
            self.hp = 1
            self._first_hit_done = True
            return
        self.hp = max(0, self.hp - amount)
        self._first_hit_done = True

    def attack(self):
        return random.randint(self.dmg_min, self.dmg_max)

    def info(self):
        return f"{self.name} (HP: {self.hp}, dmg: {self.dmg_min}-{self.dmg_max})"
    
    