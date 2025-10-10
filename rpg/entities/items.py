# Minimal Item class used by inventories and trading.

class Item:
    """Represents a generic item (weapon, armor, potion, key, etc.)."""

    def __init__(self, name: str, kind: str, value: int = 0, description: str = ""):
        self.name = name          # visible name, e.g. "Sword", "Shield"
        self.kind = kind          # item category, e.g. "weapon", "armor", "consumable", "key"
        self.value = value        # gold value (used for trading or display)
        self.description = description  # short text about the item

    def info(self) -> str:
        # Human-readable summary used in simple UIs or logs
        return f"{self.name} [{self.kind}] (value: {self.value})"

    def __repr__(self) -> str:
        
        return (
            f"Item(name={self.name!r}, kind={self.kind!r}, "
            f"value={self.value!r}, description={self.description!r})"
        )