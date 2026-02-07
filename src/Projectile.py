import pygame
from .options import *
from .Garden import Garden
class Projectile:
    def __init__(self, x, y, vx, vy, garden):
        self.garden = garden
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (int(self.x), int(self.y))

    def is_offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH // TILE_SIZE or 
                self.rect.top < 0 or self.rect.bottom > HEIGHT // TILE_SIZE)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.garden.transform(self.rect))

    def collides_with(self, lawn_mower_rect):
        return self.rect.colliderect(lawn_mower_rect)