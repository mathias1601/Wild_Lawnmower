import pygame
import random
from Projectile import Projectile
from Garden import Garden
from assets.mole import * 
from assets.dirt import destroyed, spawn_alert

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
        self.spawn = pygame.transform.scale(pygame.image.load("spawn_alert.png").convert_alpha(), self.size)
        self.peekabo = pygame.transform.scale(pygame.image.load("mole.png").convert_alpha(), self.size)
        self.throw = pygame.transform.scale(pygame.image.load("throw.png").convert_alpha(), self.size)
        self.crushed = pygame.transform.scale(pygame.image.load("destroyed.png").convert_alpha(), self.size)
        self.angry = pygame.transform.scale(pygame.image.load("angry.png").convert_alpha(), self.size)
        self.active = self.spawn
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

    def turn(self, lawnmower):
        if lawnmower.rect.left < self.rect.centerx: 
            pygame.transform.flip()

    def collision_w_lawnmower(self, lawnmower):
        return self.rect.colliderect(lawnmower)

    def draw(self, screen):
        if self.mode == 0: 
            self.active = self.spawn
            self.mode = 1
        elif self.mode == 1: 
            self.active = self.peekabo
            self.mode = 1
        elif self.mode == 2: 
            self.active = self.throw
            screen.blit(self.active, self.garden.transform(self.rect))
