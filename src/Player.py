import pygame

from .options import *
from .Projectile import Projectile
from .assets import MOWER_UP, MOWER_DOWN, MOWER_LEFT, MOWER_RIGHT

class Player:
    def __init__(self):
        self.x = 540
        self.y = 640
        self.size = (PLAYER_SIZE, PLAYER_SIZE)
        self.color = BLUE
        self.image = pygame.transform.scale(MOWER_UP, self.size)
        self.speed = PLAYER_SPEED
        self.length = 1000 
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

        self.regeneration_rate = REGENERATION_RATE
        self.hp = HP

    def draw(self, direction, screen):

        # Rotate the image based on the direction
        # Use up or down if diagonal
        if direction.x != 0 and direction.y != 0:
            if direction.y < 0:
                self.image = MOWER_UP
            else:
                self.image = MOWER_DOWN
        else:
            if direction.x > 0:
                self.image = MOWER_RIGHT
            elif direction.x < 0:
                self.image = MOWER_LEFT
            elif direction.y < 0:
                self.image = MOWER_UP
            elif direction.y > 0:
                self.image = MOWER_DOWN

        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        screen.blit(self.image, self.rect)

