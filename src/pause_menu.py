import pygame
from pathlib import Path

from .options import *


class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        assets_dir = Path(__file__).resolve().parent.parent / "assets"
        font_path = assets_dir / "dpcomic.ttf"

        self.title_font = pygame.font.Font(str(font_path), 96)
        self.button_font = pygame.font.Font(str(font_path), 48)

        self.button_rect = pygame.Rect(0, 0, 240, 90)
        self.button_rect.center = (WIDTH // 2, int(HEIGHT * 0.7))

    def run(self):
        running = True
        while running:
            self.clock.tick(FRAMERATE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.button_rect.collidepoint(event.pos):
                        return True
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        return True

            pygame.draw.rect(self.screen, BLACK, self.button_rect, border_radius=8)
            pygame.draw.rect(self.screen, WHITE, self.button_rect.inflate(-8, -8), border_radius=6)

            button_text = self.button_font.render("PLAY", True, BLACK)
            button_rect = button_text.get_rect(center=self.button_rect.center)
            self.screen.blit(button_text, button_rect)


            pygame.display.flip()

        return False