
class Player:
    """Represents the human player in the game."""

    def __init__(self, name: str):
        self.name = name               # player's display name
        self.hp: int = 10              # hit points / health
        self.gold: int = 5             # starting gold
        
        self.items: list[str] = []

    def is_alive(self) -> bool:
        """Return True if the player still has health."""
        return self.hp > 0

    def add_gold(self, amount: int) -> None:
        """Increase (or decrease) the player's gold by 'amount' (amount can be negative)."""
        self.gold += amount

    def take_damage(self, amount: int) -> None:
        """Reduce health by 'amount', but never below 0."""
        if amount < 0:
            amount = 0
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        """Increase health by 'amount' (no max cap yet)."""
        if amount < 0:
            amount = 0
        self.hp += amount

    def add_item(self, item_name: str) -> None:
        """Put an item (by name) into the player's simple bag."""
        self.items.append(item_name)

    def has_item(self, item_name: str) -> bool:
        """Check if the player carries an item with this exact name."""
        return item_name in self.items