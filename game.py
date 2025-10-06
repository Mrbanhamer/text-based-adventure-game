# Program entry for the RPG game (CLI).
# Keep this file tiny; it only calls the core game runner.

from rpg.core.game import run_game  # Import the main function

if __name__ == "__main__":
    run_game()  # Start the game loop