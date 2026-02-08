import pygame
from .options import *
from .assets import SNEILESKO
class Projectile:
    def __init__(self, x, y, vx, vy, garden):
        self.garden = garden
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.snailshoe =pygame.transform.smoothscale(SNEILESKO,
                                                     (TILE_SIZE, TILE_SIZE))

        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def update(self, dt):
        self.x += self.vx*dt
        self.y += self.vy*dt
        self.rect.topleft = (int(self.x), int(self.y))

    def is_offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH // TILE_SIZE or 
                self.rect.top < 0 or self.rect.bottom > HEIGHT // TILE_SIZE)
    
    def transform(self):
        return pygame.Rect(
            self.rect.left * TILE_SIZE,
            self.rect.top * TILE_SIZE,
            self.rect.width * TILE_SIZE,
            self.rect.height * TILE_SIZE
        )
    
    def draw(self, screen):
        screen.blit(self.snailshoe, self.transform())

    def collides_with(self, lawn_mower_rect):
        return self.rect.colliderect(lawn_mower_rect)