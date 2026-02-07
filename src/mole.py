import pygame
import random
from Projectile import Projectile
from Garden import Garden

from options import *

#SNEILESKOOOOOOO
class Mole():
    def __init__(self, garden):
        self.garden = garden
        self.size = (60,60)
        self.rect = garden.generate_enemy()
        self.counter = 0
        self.pause = 5 #seconds
        self.peekabo = pygame.transform.scale(pygame.image.load("src/mole.png").convert_alpha(), self.size)
        self.throw = pygame.transform.scale(pygame.image.load("src/mole_throw.png").convert_alpha(), self.size)
        self.death = pygame.transform.scale(pygame.image.load("src/mole_dead.png").convert_alpha(), self.size)
        self.projectile = []

    def _throw_projectile(self, lawnmower_x, lawnmower_y):
        x,y = (lawnmower_x - self.x, lawnmower_y - self.y)
        vx = x//FRAMERATE
        vy = y//FRAMERATE
        snailshoe = Projectile(self.x,self.y, vx, vy)
        self.projectile.append(snailshoe)
        return snailshoe

    def _throw_and_wait(self):
        self.throw_projectile()
        while(self.counter <= self.pause):
            self.counter+=1
        return True

    def collision_w_lawnmower(self, lawnmower):
        return self.rect.colliderect(lawnmower)
           
    def draw(self, screen):
        pass
