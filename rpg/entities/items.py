# A minimal Item class for our game.


class Item:
    """ Represents a generic item (weapon, armor_ potion, etc.). """

    def __init__(self, name: str, kind: str, value: int=0, description: str = "" ):
        self.name = name  # Visible name of the item (e.g., "Sword", "Shield")
         
        self.kind = kind     # Category/type of the item (e.g., "weapon", "armor", "potion", "key")

        self.value = value  # Gold value of the item (used for trading later)

        self.description = description      # Short text about the item (optional, for tooltips or logs)

    def info(self) -> str:

        return f"{self.name} [{self.kind}] (value: {self.value})"      # Return a human-readable summary of the item

    def __repr__(self) -> str:

        return f"Item (name= {self.name!r}, kind= {self.kind!r}, value= {self.value}, description={self.description!r})"

        