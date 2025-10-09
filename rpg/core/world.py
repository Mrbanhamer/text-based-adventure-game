
class Room:
    """A very small room node with a name and one-way connections to other rooms."""

    def __init__(self, name: str):
        self.name = name              # visible room name (e.g., "Corridor")
        self.connections: list[Room] = []  # list of connected Room objects (one-way links)

    def add_connections(self, *rooms: "Room") -> None:
        """Link this room to all given target rooms (adds multiple at once)."""
        self.connections.extend(rooms)

    def get_connections(self) -> list[str]:
        """Return the names of all connected rooms (useful for printing/UI)."""
        return [r.name for r in self.connections]

    def __repr__(self) -> str:
        return f"Room(name={self.name!r}, connections={[r.name for r in self.connections]!r})"


#  Create rooms 
starting       = Room("Corridor")
enemy_room     = Room("Cemetery")
boss_room      = Room("Dragon's Lair")
npc_room1      = Room("Big armory")
npc_room2      = Room("Small armory")
prisoner_room  = Room("Prison")
lab_room       = Room("Laboratory")   # renamed variable to snake_case, same visible name

#  Connect rooms 
starting.add_connections(lab_room, npc_room1, prisoner_room)
enemy_room.add_connections(boss_room, prisoner_room)
boss_room.add_connections(enemy_room)
npc_room1.add_connections(starting, prisoner_room)
npc_room2.add_connections(prisoner_room)
prisoner_room.add_connections(starting, npc_room1, lab_room, npc_room2, enemy_room)
lab_room.add_connections(starting, npc_room1, prisoner_room)

#  to make importing/usage easy 

def find_room(name: str) -> Room | None:
    """Return a Room object by its visible name (case-sensitive)."""
    for r in ALL_ROOMS:
        if r.name == name:
            return r
    return None

def adjacency_map() -> dict[str, list[str]]:
    """Return a plain dict: {room_name: [connected_room_names, ...]}."""
    return {r.name: r.get_connections() for r in ALL_ROOMS}

# A flat list with every room object (handy for loops or exports)
ALL_ROOMS = [
    starting, enemy_room, boss_room,
    npc_room1, npc_room2, prisoner_room, lab_room
]

# Control what "from rpg.core.world import *" exports
__all__ = [
    "Room",
    "starting", "enemy_room", "boss_room",
    "npc_room1", "npc_room2", "prisoner_room", "lab_room",
    "ALL_ROOMS", "find_room", "adjacency_map",
]