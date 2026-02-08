import pygame
import random
from Projectile import Projectile
from Garden import Garden
from assets.mole import * 

from options import *

#SNEILESKOOOOOOO
class Mole():
    def __init__(self, garden):
        self.garden = garden
        self.size = (60,60)

        self.rect = garden.generate_enemy()

        self.pause = 5 #seconds
        self.counter = 0
        self.mode = 0
        self.peekabo = pygame.transform.scale(pygame.image.load("src/mole.png").convert_alpha(), self.size)
        self.throw = pygame.transform.scale(pygame.image.load("src/mole_throw.png").convert_alpha(), self.size)
        self.death = pygame.transform.scale(pygame.image.load("src/mole_dead.png").convert_alpha(), self.size)
        self.projectile = []

    def _throw_projectile(self, lawnmower_cx, lawnmower_cy):
        x,y = (lawnmower_cx - self.rect.centerx, lawnmower_cy - self.rect.centery)
        vx = x/FRAMERATE
        vy = y/FRAMERATE
        snailshoe = Projectile(self.rect.centerx, self.rect.centery, vx, vy, self.garden)
        self.projectile.append(snailshoe)
        return snailshoe

    def _throw_and_wait(self, lawnmower_rect, dt):
        self.counter -= dt
        if self.counter <= 0:
            self._throw_projectile(lawnmower_rect.centerx, lawnmower_rect.centery)
            self.counter = self.pause

    def collision_w_lawnmower(self, lawnmower):
        return self.rect.colliderect(lawnmower)

    def draw(self, screen):
        if self.mode == 0: 
            screen.blit(self.peekabo, self.garden.transform(self.rect))
        elif self.mode == 1: 
            screen.blit(self.throw, self.garden.transform(self.rect))
        elif self.mode == 2: 
            screen.blit(self.death, self.garden.transform(self.rect))
