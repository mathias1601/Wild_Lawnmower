import pygame

from src.options import WIDTH, HEIGHT, FRAMERATE
from src.main_menu import MainMenu
from src.game import run


def fade_to_black(screen, duration_ms=400):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))

    elapsed = 0
    while elapsed < duration_ms:
        dt_ms = clock.tick(FRAMERATE)
        elapsed += dt_ms
        alpha = min(255, int(255 * (elapsed / duration_ms)))
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.flip()

def fade_from_black(screen, duration_ms=400):
    clock = pygame.time.Clock()
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))

    elapsed = 0
    while elapsed < duration_ms:
        dt_ms = clock.tick(FRAMERATE)
        elapsed += dt_ms
        alpha = max(0, 255 - int(255 * (elapsed / duration_ms)))
        overlay.set_alpha(alpha)
        screen.blit(overlay, (0, 0))
        pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        menu = MainMenu(screen)
        start_game = menu.run()

        if not start_game:
            break

        result = run(screen)  # game.py
        if result == "quit":
            break
        fade_to_black(screen)
    pygame.quit()


if __name__ == "__main__":
    main()