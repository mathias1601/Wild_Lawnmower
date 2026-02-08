import pygame
from .options import *
from .Garden import Garden
from assets.sneileskooo import sneilesko_u_bg
class Projectile:
    def __init__(self, x, y, vx, vy, garden):
        self.garden = garden
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.snailshoe = s = pygame.transform.smoothscale(pygame.image.load("sneilesko_u_bg.png").convert_alpha()) 
        self.rect = pygame.Rect(self.x, self.y, 1, 1)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (int(self.x), int(self.y))

    def is_offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH // TILE_SIZE or 
                self.rect.top < 0 or self.rect.bottom > HEIGHT // TILE_SIZE)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.snailshoe, self.garden.transform(self.rect))

    def collides_with(self, lawn_mower_rect):
        return self.rect.colliderect(lawn_mower_rect)