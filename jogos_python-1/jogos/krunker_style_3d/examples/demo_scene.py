import pygame
from src.engine import GameEngine
from src.assets_loader import load_assets
from src.classes.assaltantes import Assaltantes
from src.classes.policiais import Policiais

def demo_scene():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Demo Scene - Krunker Style 3D")

    # Load assets
    load_assets()

    # Initialize game engine
    engine = GameEngine(screen)

    # Create characters
    assaltante = Assaltantes(gender='male')
    policial = Policiais(gender='female')

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((135, 206, 235))  # Sky blue background

        # Render characters
        assaltante.render()
        policial.render()

        # Update display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    demo_scene()