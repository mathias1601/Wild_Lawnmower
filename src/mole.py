import pygame
import random

from .Projectile import Projectile

from .assets import * 

from .options import *

#SNEGLESKOOOOOOO
class Mole:
    IDLE = "idle"
    WAKEY = "wakey"
    AGGRESSION = "aggression"
    DEFEAT = "defeat"
    ANGER = "anger"
    
    def __init__(self, garden, rect, p1, projectiles):
        self.garden = garden
        self.size = (TILE_SIZE, TILE_SIZE)

        self.rect = rect

        self.pause = 5 #seconds
        self.counter = 0
        self.state = Mole.IDLE
        self.rounds = 2

        self.img = {Mole.IDLE: dirt_spawn_alert, 
                    Mole.WAKEY: mole,
                    Mole.AGGRESSION: mole_throw,
                    Mole.DEFEAT: dirt_destroyed,
                    Mole.ANGER: mole_angry}
        
        self.projectile = projectiles
        self.state_trans = 0.0
        self.throw_time = 3.0
        self.threw = False

        self.p1 = p1

    def _load(self, img):
        s = pygame.image.load(img).convert_alpha()  
        return pygame.transform.smoothscale(s, self.size)

    def next_state_logic(self, next_state):
        if next_state != self.state: 
            self.state = next_state
            self.state_trans = 0.0
            if next_state == Mole.AGGRESSION:
                self.threw = False

    def check_collision(self, lawnmower):
        return self.rect.colliderect(lawnmower.rect)

    def _throw_projectile(self, lawnmower_cx, lawnmower_cy):
        x,y = (lawnmower_cx - self.rect.centerx, lawnmower_cy - self.rect.centery)
        dist = max(0.01, (x*x + y*y) ** 0.5)
        speed = 60
        vx = x/dist * speed
        vy = y/dist * speed
        snailshoe = Projectile(self.rect.centerx, self.rect.centery, vx, vy, self.garden)
        self.projectile.append(snailshoe)

    def process(self, dt, lawnmower): #repeatedly called in main
        self.state_trans += dt

        if(self.check_collision(lawnmower) and self.state not in (Mole.DEFEAT, Mole.ANGER)):
            self.next_state_logic(Mole.DEFEAT)
            self.state_trans = 0.0

        if self.state == Mole.IDLE and self.state_trans >= 1: 
            self.next_state_logic(Mole.WAKEY)

        elif self.state == Mole.WAKEY:
            self.throw_time -= dt
            if self.throw_time <= 0 and self.rounds > 0:
                self.next_state_logic(Mole.AGGRESSION)

        elif self.state == Mole.DEFEAT: 
            if self.state_trans >= 2: 
                self.next_state_logic(Mole.ANGER)
        
        elif self.state == Mole.AGGRESSION: 
            self.throw_time = 3.0
            if self.threw == False and self.state_trans >= 0.5: #settling time
                self._throw_projectile(lawnmower.rect.centerx, lawnmower.rect.centery)
                self.threw = True

            if self.state_trans >= 1.5:
                self.rounds -= 1
                self.next_state_logic(Mole.WAKEY)

        for p in self.projectile:
            p.update(dt)
        for i in range(len(self.projectile) - 1, -1, -1):
            if self.projectile[i].is_offscreen():
                del self.projectile[i]

    def draw(self, screen):
        img = self.img[self.state]

        if self.p1.x > self.rect.x:
            img = pygame.transform.flip(img, True, False)

        screen.blit(img, self.rect)
