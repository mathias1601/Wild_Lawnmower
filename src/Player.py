import pygame

from .options import *
from .Projectile import Projectile
from .assets import *

class Player:
    def __init__(self):
        self.x = 540
        self.y = 640
        self.size = (PLAYER_SIZE, PLAYER_SIZE)
        self.color = BLUE
        self.image = pygame.transform.scale(MOWER_IMAGE, self.size)
        self.speed = PLAYER_SPEED
        self.length = 1000 
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

        self.regeneration_rate = REGENERATION_RATE
        self.hp = HP

    def draw(self, direction, screen):

        # Rotate the image based on the direction
        angle = direction.angle_to(pygame.Vector2(0, -1))
        rotated_image = pygame.transform.rotate(self.image, angle)
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        screen.blit(rotated_image, self.rect)

