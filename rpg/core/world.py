# The basic room function, acts as a template for all the other rooms
class room:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connections(self, *rooms):
        self.connections.extend(rooms)

    def get_connections(self):
        return [room.name for room in self.connections]

starting = room("Corridor")
enemy_room = room("Cemetery")
boss_room = room("Dragon's Lair")
npc_room1 = room(" Room")
# npc_room2 = room("Armory")

starting.add_connections(enemy_room, npc_room1)
enemy_room.add_connections(starting, boss_room, npc_room1)
boss_room.add_connections(enemy_room)
npc_room1.add_connections(starting, enemy_room)
