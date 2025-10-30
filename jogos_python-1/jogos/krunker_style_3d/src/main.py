# File: jogos_python/jogos/krunker_style_3d/src/main.py

import pygame
from engine import GameEngine
from assets_loader import load_assets
from game import Game

def main():
    pygame.init()
    
    # Load game assets
    load_assets()

    # Initialize the game engine
    engine = GameEngine()

    # Create a new game instance
    game = Game(engine)

    # Start the main game loop
    while engine.running:
        engine.handle_events()
        game.update()
        engine.render(game)

    pygame.quit()

if __name__ == "__main__":
    main()