import pygame
import random

from src.mole import Mole
from .assets import *
from .options import *

#gjerder, generer steiner, generer gress, gjerdet er ødelagt der man kan gå til neste bane

class Garden():
    def __init__(self, p1):
        self.rock_count = ROCK_COUNT
        self.hurdle_image = HURDLE_IMAGE
        self.hurdle_size = (TILE_SIZE, TILE_SIZE)

        self.moles = []
        self.hurdles = self._generate_hurdles()

        self.p1 = p1
    
    def _generate_hurdles(self):  #setup seq 
        hurdles = []
        for _ in range(self.rock_count):
            posx = random.randint(0, WIDTH - self.hurdle_size[0])
            posy = random.randint(0, HEIGHT - 2*TILE_SIZE)
            hurdle = pygame.Rect(posx, posy, self.hurdle_size[0], self.hurdle_size[1])

            if hurdle.collidelist(hurdles) == -1: #søkte opp
                hurdles.append(hurdle)
        return hurdles
        
    def generate_enemy(self, projectiles): 
        spaceOccupied = True
        while spaceOccupied:
            posx = random.randint(0, WIDTH - TILE_SIZE)
            posy = random.randint(0, HEIGHT - TILE_SIZE)
            lil_enemy = pygame.Rect(posx, posy, TILE_SIZE, TILE_SIZE) # Candidate for mole spawn

            if lil_enemy.collidelist(self.hurdles) != -1:
                continue

            spaceOccupied = False
            for mole in self.moles:
                if mole.rect.colliderect(lil_enemy):
                    spaceOccupied = True
                    break

        self.moles.append(Mole(self, pygame.Rect(posx, posy, TILE_SIZE, TILE_SIZE), self.p1, projectiles))
    
    def collide(self, lawn_mower): 
        return lawn_mower.rect.collidelist(self.hurdles)

    def draw(self, screen):
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        for h in self.hurdles:
            screen.blit(self.hurdle_image, h)

        for mole in self.moles:
            mole.draw(screen)

        
