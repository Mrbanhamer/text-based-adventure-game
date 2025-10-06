class Item:
    def __init__(self, name:str, item_type: str, value: int = 0, description: str = ""):
        self.name = name #ex name of item type, "Sword", "Shield", "Helm".
        self.item_type = item_type #type of item, "Weapon", "Armour".
        self.value = value #ex cost of item bought in currency "5 gold"
        self.description = description #Description of the item, tooltip.

    def info(self) -> str:
        return f"{self.name} [{self.item_type}] (value: {self.value})" #returns readable summary of the item
    
    def __repr__(self) -> str:
        return f"Item (name= {self.name!r}, type= {self.item_type!r}, value= {self.value!r}, description= {self.description!r})"