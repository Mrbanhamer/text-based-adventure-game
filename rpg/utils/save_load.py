# Simple save/load helpers for the game.
# No new files inside repo: we use the OS temp directory for save files.

import json          # For reading/writing JSON files
import os            # For building file paths that work on all systems
import tempfile      # To get the OS temporary directory (outside your repo)


def get_default_save_path(filename: str = "rpg_save.json") -> str:
    """
    Return an absolute path to a save file in the OS temp directory.
    Example (Windows): C:\\Users\\<you>\\AppData\\Local\\Temp\\rpg_save.json

    We do this to avoid creating any new files inside your repository structure.
    """
    temp_dir = tempfile.gettempdir()        # e.g., C:\Users\you\AppData\Local\Temp
    return os.path.join(temp_dir, filename) # join temp path with filename


def save_game(state: dict, path: str | None = None) -> None:
    """
    Save the given state dictionary to a JSON file.

    Parameters:
        state: a plain dict with serializable values (strings, ints, lists, dicts)
        path: optional custom path; if None, use the OS temp directory
    """
    save_path = path or get_default_save_path()     # choose where to save (temp by default)

    # Write JSON with pretty indentation; ensure_ascii=False keeps å/ä/ö readable
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def load_game(path: str | None = None) -> dict:
    """
    Load and return a state dictionary from a JSON file.

    Parameters:
        path: optional custom path; if None, read from the OS temp directory

    Returns:
        A dict with the loaded game state. If the file does not exist or is invalid,
        return an empty dict {} as a safe fallback.
    """
    load_path = path or get_default_save_path()     # choose where to load from (temp by default)

    if not os.path.exists(load_path):               # if no save file yet, return empty state
        return {}

    try:
        with open(load_path, "r", encoding="utf-8") as f:
            return json.load(f)                     # parse JSON into a Python dict
    except Exception:
        return {}                                   # on any error (e.g., corrupted file), return empty