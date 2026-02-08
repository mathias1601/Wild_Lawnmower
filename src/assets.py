import pygame
from os import path

from .options import *

# -----| IMAGES |-----
MOWER_IMAGE = pygame.image.load(path.join('assets', 'mower.png')).convert_alpha()

HURDLE_IMAGE = pygame.image.load(path.join('assets', 'hurdle.png')).convert_alpha()

# dirt
dirt_destroyed = pygame.image.load(path.join('assets', 'dirt', 'destroyed.png')).convert_alpha()
dirt_spawn_alert = pygame.image.load(path.join('assets', 'dirt', 'spawn_alert.png')).convert_alpha()
dirt_spawning = pygame.image.load(path.join('assets', 'dirt', 'spawning.png')).convert_alpha()

# garden
BACKGROUND_IMAGE = pygame.image.load(path.join('assets', 'garden', 'background.png')).convert()
CUT_GRASS = pygame.image.load(path.join('assets', 'garden', 'cut_grass.png')).convert()
GRASS = pygame.image.load(path.join('assets', 'garden', 'grass.png')).convert()
ROCK = pygame.image.load(path.join('assets', 'garden', 'rock.png')).convert()

# mole
mole_angry = pygame.image.load(path.join('assets', 'mole', 'angry.png')).convert_alpha()
mole = pygame.image.load(path.join('assets', 'mole', 'mole.png')).convert_alpha()
mole_throw = pygame.image.load(path.join('assets', 'mole', 'throw.png')).convert_alpha()

# mower
MOWER_UP = pygame.image.load(path.join('assets', 'mower', 'up.PNG')).convert_alpha()
MOWER_DOWN = pygame.image.load(path.join('assets', 'mower', 'down.PNG')).convert_alpha()
MOWER_LEFT = pygame.image.load(path.join('assets', 'mower', 'left.PNG')).convert_alpha()
MOWER_RIGHT = pygame.image.load(path.join('assets', 'mower', 'right.PNG')).convert_alpha()

# sneilesko
SNEILESKO = pygame.image.load(path.join('assets', 'sneileskooo', 'sneilesko_u_bg.png')).convert_alpha()


# -----| FONT |-----
FONT_TYPE = pygame.font.Font(path.join('assets', 'dpcomic.ttf'), FONT_SIZE)

# -----| SOUNDS |-----
DEATH_SOUND = pygame.mixer.Sound(path.join('assets', 'death_link.wav'))
DEATH_SOUND.set_volume(0.1)
DAMAGE_SOUND = pygame.mixer.Sound(path.join('assets', 'damage.wav'))
SOUNDTRACK = path.join('assets', 'soundtrack.mp3')
