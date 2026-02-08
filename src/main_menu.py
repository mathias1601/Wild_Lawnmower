import pygame
from pathlib import Path

from .options import *


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        assets_dir = Path(__file__).resolve().parent.parent / "assets"
        background_path = assets_dir / "main_menu.png"

        self.background = pygame.image.load(str(background_path)).convert()
        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

    def run(self):

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        running = True
        while running:
            self.clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return True
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        return True

        return False