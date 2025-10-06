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
npc_room1 = room("Big armory")
npc_room2 = room("Small armory")
prisoner_room = room("Prison")
Lab_room = room("Laboratory")

starting.add_connections(Lab_room, npc_room1, prisoner_room)
enemy_room.add_connections(boss_room, prisoner_room)
boss_room.add_connections(enemy_room)
npc_room1.add_connections(starting, prisoner_room)
npc_room2.add_connections(prisoner_room)
prisoner_room.add_connections(starting, npc_room1, Lab_room, npc_room2, enemy_room)
Lab_room.add_connections(starting, npc_room1, prisoner_room)
