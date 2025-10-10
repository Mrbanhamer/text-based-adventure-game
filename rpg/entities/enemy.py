import random  # used for damage rolls
from abc import ABC, abstractmethod  # to declare an abstract base class


class Enemy(ABC):
    """Abstract base for enemies (shared HP/damage-range + common logic)."""

    def __init__(self, name: str, hp: int, dmg_min: int, dmg_max: int):
        self.name = name          # enemy display name
        self.hp = hp              # hit points (health)
        self.dmg_min = dmg_min    # minimum damage per hit
        self.dmg_max = dmg_max    # maximum damage per hit
        self._first_hit_done = False  # prevents dying on the very first hit

    def is_alive(self) -> bool:
        """Return True if the enemy has more than 0 HP."""
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """
        Reduce HP by 'amount' (never below 0).

        First-hit protection: if the very first hit would kill the enemy,
        leave it at 1 HP instead. 
        """
        if amount < 0:
            amount = 0
        if not self._first_hit_done and amount >= self.hp:
            self.hp = 1
            self._first_hit_done = True
            return
        self.hp = max(0, self.hp - amount)
        self._first_hit_done = True

    @abstractmethod
    def attack(self) -> int:
        """
        Abstract: return the damage dealt by this enemy.
        Subclasses must implement this (e.g., random in a range).
        """
        raise NotImplementedError

    def info(self) -> str:
       
        return f"{self.name} (HP: {self.hp}, dmg: {self.dmg_min}-{self.dmg_max})"


class BasicEnemy(Enemy):
    """Concrete enemy that rolls damage uniformly in [dmg_min, dmg_max]."""

    def attack(self) -> int:
        # Use the simple random roll 
        return random.randint(self.dmg_min, self.dmg_max)


# ---

def create_skeleton() -> Enemy:
    #  returns a concrete subclass.
    return BasicEnemy("Skeleton", hp=10, dmg_min=1, dmg_max=3)


def create_dragon() -> Enemy:
    # Stronger boss enemy.
    return BasicEnemy("Dragon", hp=40, dmg_min=4, dmg_max=8)