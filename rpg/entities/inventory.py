from .items import Item  # Base item class (has: name, kind, value, description)

class Inventory:
    """Very small inventory that stores Item objects."""

    def __init__(self) -> None:
        self.items: list[Item] = []  # internal storage (simple Python list)

    def add(self, item: Item) -> None:
        """Add one item to the inventory."""
        self.items.append(item)
        print(f"> Added {item.name} to inventory")

    def remove_by_name(self, name: str) -> bool:
        """
        Remove the *first* item whose name matches (case-insensitive).
        Returns True if removed, otherwise False.
        """
        target = name.lower()
        for i, it in enumerate(self.items):
            if it.name.lower() == target:
                del self.items[i]
                print(f"> Removed {name} from inventory.")
                return True
        # Only print this once *after* we tried all items
        print(f"> No item named '{name}' found.")
        return False

    def has(self, name: str) -> bool:
        """Return True if any item with this name exists (case-insensitive)."""
        target = name.lower()
        return any(it.name.lower() == target for it in self.items)

    def get_first(self, name: str) -> Item | None:
        """Return the first matching item, or None if not found."""
        target = name.lower()
        for it in self.items:
            if it.name.lower() == target:
                return it
        return None

    def list_names(self) -> list[str]:
        """Return a list with the names of all items."""
        return [it.name for it in self.items]

    def count(self) -> int:
        """Return how many items are stored."""
        return len(self.items)

    def show(self) -> None:
        """
        Print all items in a simple list.
        Uses Item.kind and Item.value to keep it consistent with your Item class.
        """
        if not self.items:
            print("> Inventory is empty.")
        else:
            print("\n--- INVENTORY ---")
            for it in self.items:
                # Fallbacks are here just in case an Item is missing a field
                kind = getattr(it, "kind", "item")
                value = getattr(it, "value", 0)
                print(f"- {it.name} [{kind}] (value: {value})")
            print("-----------------\n")

    def __repr__(self) -> str:
        return f"Inventory(items={self.items!r})"