import pygame
import random
from .assets import *
#from .options import *

#gjerder, generer steiner, generer gress, gjerdet er ødelagt der man kan gå til neste bane

class Garden():
    def __init__(self):
        self.size = (60, 60)
        self.grid = 60
        self.diff = 30
        self.rowgrid = 1200 // self.grid
        self.colgrid = 660 // self.grid
        self.hurdle_image = HURDLE_IMAGE

        self.last_enemy = []
        self.hurdles = self._generate_hurdles()
        self.field = self._fill() #hvert element tilsvarer 60x60 blokker
        self._fill_in_hurdles()
    
    def _generate_hurdles(self):  #setup seq 
        hurdles = []
        for _ in range(self.diff):
            posx = random.randint(0, self.rowgrid - 1)
            posy = random.randint(0, self.colgrid - 1)
            hurdle = pygame.Rect(posx, posy, 1, 1) #Projectile klassen hjalp :^)

            if hurdle.collidelist(hurdles) == -1: #søkte opp
                hurdles.append(hurdle)
        return hurdles
        
    def generate_enemy(self): 
        update = 0
        while(not update):
            posx = random.randint(0, self.rowgrid - 1)
            posy = random.randint(0, self.colgrid - 1) 
            lil_enemy = pygame.Rect(posx, posy, 1, 1)
            if (lil_enemy.collidelist(self.last_enemy) == -1 and lil_enemy.collidelist(self.hurdles) == -1):
                update = 1
                if len(self.last_enemy) == 0: 
                    self.last_enemy.append(lil_enemy)
                    continue
                self.last_enemy[0] = lil_enemy
        return lil_enemy
    
    def add_enemy(self): #button press to avoid enemy attack? ... don't use before enemy is made
        x, y = self.last_enemy[0].left, self.last_enemy[0].top 
        if self.field[y][x] == 1: 
                self.field[y][x] = 2 #enemy = 2

    def remove_enemy(self): # ... don't use before enemy is made
        x, y = self.last_enemy[0].left, self.last_enemy[0].top 
        if self.field[y][x] == 2: 
                self.field[y][x] = 1
    
    def collide(self, lawn_mower): 
        return lawn_mower.collidelist(self.hurdles) #Projectile klassen hjalp :^) 
                                                    #must use Rect, also should be in grid units
    
    def _fill(self): #setup seq
        field = []
        for _ in range(self.colgrid):
            temp = [1]*self.rowgrid
            field.append(temp)
        return field

    def _fill_in_hurdles(self): #setup seq
        for elem in self.hurdles: 
            x, y = elem.left, elem.top
            if self.field[y][x] == 1: 
                self.field[y][x] = 0 #stein = 0

    def transform(self, rect): #transform grid positions to screen
        return pygame.Rect(rect.left*self.grid, rect.top*self.grid, 
                           rect.width*self.grid, rect.height*self.grid)
    
    def advance_lvl(self):
        self.field[5][-1] = 1
        self.field[6][-1] = 1

    def draw(self, screen):
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        for h in self.hurdles:
                proj = self.transform(h)
                screen.blit(self.hurdle_image, proj)

# def run(): #testbenk fra GPT
#     pygame.init()

#     screen = pygame.display.set_mode((1200, 660))
#     pygame.display.set_caption("Garden Test")

#     clock = pygame.time.Clock()
#     garden = Garden()

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill((0, 0, 0))
#         garden.draw(screen)
#         pygame.display.flip()
#         clock.tick(60)

#     pygame.quit()

# run()

        
