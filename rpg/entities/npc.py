class NPC:
    

    def __init__(self, name: str, dialog: str = ""):
        self.name = name          # NPC display name
        self.dialog = dialog      # what they say when you talk to them

    def talk(self) -> None:
        """Print one line of dialog (or a default message)."""
        if self.dialog:
            print(self.dialog)
        else:
            print(f"{self.name} has nothing to say right now.")

    def __repr__(self) -> str:
        return f"NPC(name={self.name!r})"
    

