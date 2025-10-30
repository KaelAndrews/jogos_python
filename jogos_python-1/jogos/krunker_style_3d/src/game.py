# File: jogos_python/jogos/krunker_style_3d/src/game.py

import pygame
from pygame.locals import *
from engine import GameEngine
from player import Player
from assets_loader import load_assets
from classes.assaltantes import Assaltantes
from classes.policiais import Policiais

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Krunker Style 3D Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.engine = GameEngine()
        self.player = Player()
        self.assaltantes = Assaltantes()
        self.policiais = Policiais()
        load_assets()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def update(self):
        self.player.update()
        self.assaltantes.update()
        self.policiais.update()

    def render(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.engine.render(self.screen, self.player, self.assaltantes, self.policiais)
        pygame.display.flip()

    def quit(self):
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()