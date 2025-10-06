from .items import Item

class Inventory: #Container that hold items
    
    def __init__(self) -> None:
        self.items = []

    def add(self, item: Item) -> None: #Add a item to the inventory
        self.items.append(item)
        print(f"> added {item.name} to inventory")

    def remove_by_name(self, name: str) -> bool:
        for i, it in enumerate(self.items):
            if it.name.lower() ==  name.lower():
                del self.items[i]
                print(f"> Removed {name} from inventory.")
                return True
            print(f"> No item named '{name}' found.")
            return False
        
    def has(self, name: str) -> bool: #Checks if item exists
        return any(it.name.lower() == name.lower() for it in self.items)

    def get_first(self, name: str): #Returns the first matching item if found, otherwise return None.
        for it in self.items:
            if it.name.lower() == name.lower():
                return it
        return None
    
    def list_names(self) -> list[str]: #Returns a list of item names.
        return [it.name for it in self.items]
    
    def count(self) -> int: #Returns a total amount of items.
        return len(self.items)
    
    def show(self) -> None: #Print all items
        if not self.items:
            print(f"> Inventory is empty.")
        else:
            print("\n--- INVENTORY ---")
            for it in self.items:
                print(f"- {it.name} [{it.item_type}] (value: {it.value})")
            print("-----------------\n")
    
    def __repr__(self) -> str:
        return f"Inventory(items={self.items!r})"
    