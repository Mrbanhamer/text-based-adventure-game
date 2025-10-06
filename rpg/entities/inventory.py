# A minimal Inventory class for our game.
# It stores Item objects and offers  operations.

from .items import Item  # Item type used by the inventory

class Inventory:
    """Simple container that holds Item objects."""

    def __init__(self) -> None:
       
        self.items = []   # Internal storage for items (a plain Python list)

    def add(self, item: Item) -> None:
        
        self.items.append(item) # Put one Item into the inventory

    def remove_by_name(self, name: str) -> bool:
       
        for i, it in enumerate(self.items):  # Remove the first Item whose name matches; return True if removed
            if it.name == name:
                del self.items[i]
                return True
        return False

    def has(self, name: str) -> bool:
       
        return any(it.name == name for it in self.items)  # Check if any Item with this name exists

    def get_first(self, name: str):
       
        for it in self.items:  # Return the first matching Item or None if not found
            if it.name == name:
                return it
        return None

    def list_names(self) -> list[str]:
       
        return [it.name for it in self.items]  # Return a list of item names 

    def count(self) -> int:
        
        return len(self.items) # Return how many items are stored

    def __repr__(self) -> str:
        
        return f"Inventory(items={self.items!r})"  # Developer-friendly view for debugging





