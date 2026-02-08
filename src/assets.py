import pygame
from os import path

from .options import *

# -----| IMAGES |-----
BACKGROUND_IMAGE = pygame.image.load(path.join('assets', 'background.png')).convert()
ROCKET_IMAGE = pygame.image.load(path.join('assets', 'rocket.png')).convert_alpha()
BOULDER_IMAGE = pygame.image.load(path.join('assets', 'boulder.png')).convert_alpha()

HURDLE_IMAGE = pygame.image.load(path.join('assets', 'hurdle.png')).convert_alpha()

# mole images
""" mole_angry = pygame.image.load(path.join('assets', 'mole_angry.png')).convert_alpha()
mole_l = pygame.image.load(path.join('assets', 'mole_l.png')).convert_alpha()
mole_r = pygame.image.load(path.join('assets', 'mole_r.png')).convert_alpha()
mole_throw_l = pygame.image.load(path.join('assets', 'mole_throw_l.png')).convert_alpha()
mole_throw_r = pygame.image.load(path.join('assets', 'mole_throw_r.png')).convert_alpha()

# sneilesko
sneilesko_u_bg = pygame.image.load(path.join('assets', 'sneilesko_u_bg.png')).convert_alpha()
 """

# -----| FONT |-----
FONT_TYPE = pygame.font.Font(path.join('assets', 'dpcomic.ttf'), FONT_SIZE)

# -----| SOUNDS |-----
DEATH_SOUND = pygame.mixer.Sound(path.join('assets', 'death.wav'))
DAMAGE_SOUND = pygame.mixer.Sound(path.join('assets', 'damage.wav'))
SOUNDTRACK = path.join('assets', 'soundtrack.mp3')
