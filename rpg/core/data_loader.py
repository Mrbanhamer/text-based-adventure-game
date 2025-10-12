
import json      # read/write JSON files
import os        # build file paths that work on all operating systems


def _project_root() -> str:
    """Return absolute path to the project root (two folders up from this file)."""
    # __file__ = this file's path; dirname gives folder; join("..","..") goes two levels up
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def get_default_world_path(filename: str = "world.json") -> str:
    """Absolute path to data/world.json (or another filename in /data)."""
    return os.path.join(_project_root(), "data", filename)


def get_default_items_path(filename: str = "items.json") -> str:
    """Absolute path to data/items.json (or another filename in /data)."""
    return os.path.join(_project_root(), "data", filename)


# --------------------------- WORLD ------------------------------------

def load_world_json(path: str | None = None) -> dict:
    """
    Read and return the JSON dict from data/world.json.
    Returns an empty dict {} if the file is missing or invalid (safe fallback).
    """
    world_path = path or get_default_world_path()
    try:
        with open(world_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def world_locations_map(world_data: dict) -> dict[str, dict]:
    """
    Convert raw world JSON into a lookup:
      { "RoomName": {"description": str, "exits": [neighbor names]} }

    Accepts both styles for 'exits':
      - dict: {"left": "Armory", "right": "Lab"}  -> we keep only the room names
      - list: ["Armory", "Lab"]
    """
    out: dict[str, dict] = {}
    for loc in world_data.get("locations", []):
        name = loc.get("name")
        if not name:
            continue
        raw_exits = loc.get("exits", [])
        if isinstance(raw_exits, dict):
            exits_list = list(raw_exits.values())   # take only destination names
        elif isinstance(raw_exits, list):
            exits_list = raw_exits
        else:
            exits_list = []
        out[name] = {
            "description": loc.get("description", ""),
            "exits": exits_list,
        }
    return out


# --------------------------- ITEMS ------------------------------------

def load_items_json(path: str | None = None) -> dict:
    """
    Read and return the JSON dict from data/items.json.

    Expected structure:
      {
        "items": [ {name, kind, value, description}, ... ],
        "rooms": { "RoomName": ["ItemName", ...], ... }
      }

    Returns {} if file is missing or invalid (safe fallback).
    """
    items_path = path or get_default_items_path()
    try:
        with open(items_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def room_items_map(items_data: dict) -> dict[str, list[str]]:
    """
    From items JSON, return a simple room -> [item names] mapping.
    Example: { "Laboratory": ["Health Potion"], "Big armory": ["Sword", "Shield"] }
    """
    return dict(items_data.get("rooms", {}))


def defined_items(items_data: dict) -> dict[str, dict]:
    """
    From items JSON, return itemName -> itemDefinition mapping.
    Example: { "Sword": {"name":"Sword","kind":"weapon",...}, ... }
    """
    out: dict[str, dict] = {}
    for item in items_data.get("items", []):
        name = item.get("name")
        if name:
            out[name] = item
    return out


# --------------------------- SAVE BACK --------------------------------

def save_items_json(items_data: dict, path: str | None = None) -> None:
    """
    Overwrite data/items.json with the given dict.
    Use after you modify items_data["rooms"] (e.g., remove a picked item).
    """
    items_path = path or get_default_items_path()
    with open(items_path, "w", encoding="utf-8") as f:
        json.dump(items_data, f, indent=2, ensure_ascii=False)


def pop_item_from_room(room_name: str, item_name: str, items_data: dict) -> bool:
    """
    Remove one item by name from items_data["rooms"][room_name], if present.
    Return True if removed, False if not found. (Call save_items_json(...) afterwards.)
    """
    rooms = items_data.setdefault("rooms", {})
    items = rooms.get(room_name, [])
    if item_name in items:
        items.remove(item_name)
        return True
    return False