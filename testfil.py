import Item
import Inventory
from items import Item
from inventory import Inventory

inv = Inventory()
inv.add(Item("Sword", "weapon", 10))
inv.add(Item("Shield", "armor", 5))
inv.add(Item("Potion", "potion", 2))

inv.show()

inv.remove_by_name("Potion")
inv.show()

print("Has sword?", inv.has("sword"))
print("Count:", inv.count())