import os
import sys
from src.main import Game

def run_local():
    # Set up the game environment
    os.environ['PYTHONASYNCIODEBUG'] = '1'  # Enable asyncio debug mode for better error messages

    # Initialize the game
    game = Game()

    try:
        # Start the game loop
        game.run()
    except Exception as e:
        print(f"An error occurred while running the game: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_local()