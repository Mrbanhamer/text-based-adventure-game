#  model for our text adventure.


class Location:
    """A place in the world with a name, description, and exits."""

    def __init__(self, name: str, description: str = "") -> None:
        self.name = name                # Visible name of the location
        self.description = description  # Short text shown to the player
        self.exits = {}                 # Dict: direction -> target location name (e.g., "north": "Armory")

    def add_exit(self, direction: str, target_name: str) -> None:
        # Connect this location to another location by direction
        self.exits[direction.lower()] = target_name

    def get_exit(self, direction: str):
        # Return the target location name for this direction, or None if missing
        return self.exits.get(direction.lower())

    def describe(self) -> str:
        # Return a simple human-readable description
        if self.exits:
            exits_text = ", ".join(sorted(self.exits.keys()))
        else:
            exits_text = "(no exits)"
        return f"{self.name}: {self.description} Exits: {exits_text}"

    def __repr__(self) -> str:
        # Developer-friendly view for debugging
        return f"Location(name={self.name!r}, exits={self.exits!r})"


class World:
    """Holds all locations and simple helpers to work with them."""

    def __init__(self) -> None:
        self.locations = {}  # Dict: location name -> Location object

    def add_location(self, loc: Location) -> None:
        # Store a Location by its name
        self.locations[loc.name] = loc

    def get(self, name: str):
        # Return a Location by name, or None if not found
        return self.locations.get(name)

    def connect(self, a_name: str, direction: str, b_name: str) -> None:
        # Create a one-way exit from A to B
        a = self.get(a_name)
        if a:
            a.add_exit(direction, b_name)

    def list_names(self) -> list[str]:
        # Return all location names (useful for debug/menus)
        return sorted(self.locations.keys())