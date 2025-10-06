# A Player class for our text adventure.

class Player:
    """Represents the human player in the game."""

    def __init__(self, name: str):
        self.name= name

        self.hp = 10    # Hit points / health
        self.gold = 5    # Starting gold
        

          # Simple item storage for now (list of item names).
        # We will replace this with a proper Inventory later.
        self.items = []
    

    def is_alive(self) -> bool :
        """ Return True if the player still has healf."""
        return self.hp > 0

    def add_gold(self, amount: int) -> None:
        """Increase or decrease the player's gold by 'amount."""

        self.gold += amount

    def take_damage (self, amount: int) -> None :
        """ Reduce health but never below zero."""
        self.hp = max (0, self.hp - amount)
 
    def heal (self, amount: int ) -> None:
        """ Increase health by 'amount' (no max cap yet). """
        self.hp += amount

    def add_item (self,item_name: str) -> None:
        """ put an item (by name) into the player's simple bag."""
        self.item.append (item_name)


    def has_item( self, item_name :str) -> bool :
        """ check if the player carries an item with this name."""
        return item_name in self.items

        



