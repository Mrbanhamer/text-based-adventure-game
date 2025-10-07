# Loads world data from JSON and builds a World object.


import json
import os

from .world import World, Location  # Use our simple world classes


def get_default_world_path() -> str:
    """
    Return the absolute path to data/world.json
    (works no matter where you run the program from).
    """
    # __file__ is rpg/core/data_loader.py -> go up two folders to project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    return os.path.join(project_root, "data", "world.json")


def load_world(json_path: str) -> World:
    """
    Read a JSON file and build a World with Location objects.
    Expected JSON structure:

    {
      "locations": [
        {
          "name": "Corridor",
          "description": "A dark, cold stone corridor.",
          "exits": { "left": "Armory", "right": "Wizard Lab" }
        },
        { "name": "Armory", "description": "Dusty racks and a locked chest." },
        { "name": "Wizard Lab", "description": "Bottles and strange notes." }
      ]
    }
    """
    # 1) Read JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 2) Create an empty world
    world = World()

    # 3) First pass: create all locations (without exits)
    for loc_data in data.get("locations", []):
        name = loc_data["name"]                       # required field
        description = loc_data.get("description", "") # optional field
        world.add_location(Location(name, description))

    # 4) Second pass: connect exits (now that all locations exist)
    for loc_data in data.get("locations", []):
        name = loc_data["name"]
        exits = loc_data.get("exits", {})             # optional dict: direction -> target name
        for direction, target_name in exits.items():
            # Only connect if both ends exist
            if world.get(name) and world.get(target_name):
                world.connect(name, direction, target_name)

    return world