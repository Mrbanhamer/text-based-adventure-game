# This file make the folder 'entities' a Python package.
# It also allow us to import the main classes directly from this package.

from .player import Player      #import Player class , The player's controllable character
from .npc import NPC            # import NPC class , Non-player character base class
from .inventory import Inventory   # import Inventory class, Container that holds items for an entity
from .items import Item      # import Item class, Base item type used by inventories


