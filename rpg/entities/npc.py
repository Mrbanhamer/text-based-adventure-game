class NPC:
    """ Represents a non-player character in the game."""

    def __init__(self, name: str, friendly: bool = True):
        self.name = name  # The NPC's display name

        
        self.friendly = friendly       # Attitude toward the player, True = ally/neutral, False = hostile
        self.dialogue = ""           #Simple dialogue line (placeholder for now),  One-line message the NPC can say

    def set_dialogue(selg, text: str) -> None :
        
        self.dialogue= text          # Store a simple dialogue line for later use

    def speak(self) -> str :
        return self.dialogue      # Return what the NPC would say (empty string if nothing set)


    def is_hostile(self) -> bool:
        return not self.friendly      #  True if this NPC is not friendly


        




