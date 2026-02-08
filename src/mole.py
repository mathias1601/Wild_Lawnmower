import pygame
import random
from Projectile import Projectile
from Garden import Garden
from assets.mole import * 
from assets.dirt import destroyed, spawn_alert

from options import *

#SNEGLESKOOOOOOO
class Mole():
    IDLE = "idle"
    WAKEY = "wakey"
    AGGRESSION = "aggression"
    DEFEAT = "defeat"
    ANGER = "anger"
    
    def __init__(self, garden, rect):
        self.garden = garden
        self.size = (60,60)

        self.rect = rect

        self.pause = 5 #seconds
        self.counter = 0
        self.state = Mole.IDLE
        self.rounds = 2

        self.img = {Mole.IDLE: pygame.image.load("spawn_alert.png"), 
                    Mole.WAKEY: pygame.image.load("mole.png"),
                    Mole.AGGRESSION: pygame.image.load("throw.png"),
                    Mole.DEFEAT: pygame.image.load("destroyed.png"),
                    Mole.ANGER: pygame.image.load("angry.png")}

        self.flip = True
        self.projectile = []
        self.state_trans = 0.0
        self.throw_time = 3.0

    def _load(self, img):
        s = pygame.image.load(img).convert_alpha()  
        return pygame.transform.smoothscale(s, self.size)

    def turn(self, lawnmower):
        if lawnmower.rect.centerx < self.rect.centerx: 
            self.flip = False
        else:
            self.flip = True

    def next_state_logic(self, next_state):
        if next_state != self.state: 
            self.state = next_state
            self.state_trans = 0.0

    def check_collision(self, lawnmower):
        return self.rect.colliderect(lawnmower.rect)

    def _throw_projectile(self, lawnmower_cx, lawnmower_cy):
        x,y = (lawnmower_cx - self.rect.centerx, lawnmower_cy - self.rect.centery)
        speed = 80
        vx = x/FRAMERATE * speed
        vy = y/FRAMERATE * speed
        snailshoe = Projectile(self.rect.centerx, self.rect.centery, vx, vy, self.garden)
        self.projectiles.append(snailshoe)
        return snailshoe

    # def _throw_and_wait(self, lawnmower_rect, dt):
    #     self.counter -= dt
    #     if self.counter <= 0:
    #         self._throw_projectile(lawnmower_rect.centerx, lawnmower_rect.centery)
    #         self.counter = self.pause

    def process(self, dt, limit, lawnmower): #repeatedly called in main
        self.state_trans += dt
        self.turn(lawnmower)  
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
            if len(self.projectile) < 2 and self.state_trans >= 0.5: #settling time
                self._throw_projectile(self, lawnmower.rect.x, lawnmower.rect.y)

            if self.state_trans >= 1.5:
                self.rounds -= 1
                self.next_state_logic(Mole.WAKEY)

            for p in self.projectiles:
                p.update(dt)

                    

                self.projectiles = [p for p in self.projectiles if not p.is_offscreen()]

            



    def draw(self, screen):
        img = self.img[self.state]
        if not self.flip: 
            pygame.transform.flip(img, True, False)
        screen.blit(img, self.garden.transform(self.rect))

        for p in self.projectile:
            p.draw(screen)
