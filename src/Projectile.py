import pygame
from .options import *
from .assets import SNEILESKO
class Projectile:
    def __init__(self, x, y, direction, garden):
        self.garden = garden
        self.x = x
        self.y = y
        self.direction = direction.normalize() if direction.length() > 0 else pygame.Vector2(0, 0)
        self.speed = BULLET_SPEED
        self.snailshoe =pygame.transform.smoothscale(SNEILESKO,
                                                     (TILE_SIZE, TILE_SIZE))

        self.rect = pygame.Rect(self.x, self.y, self.snailshoe.get_width(), self.snailshoe.get_height())

    def update(self, dt):
        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt
        self.rect.topleft = (int(self.x), int(self.y))

    def is_offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH or 
                self.rect.top < 0 or self.rect.bottom > HEIGHT)
    
    def draw(self, screen):
        screen.blit(self.snailshoe, self.rect)

    def collides_with(self, lawn_mower_rect):
        return self.rect.colliderect(lawn_mower_rect)