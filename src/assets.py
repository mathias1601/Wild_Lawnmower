import pygame
from os import path

from .options import *

# -----| IMAGES |-----
ROCKET_IMAGE = pygame.image.load(path.join('assets', 'rocket.png')).convert_alpha()

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
mole_l = pygame.image.load(path.join('assets', 'mole', 'mole_l.png')).convert_alpha()
mole_r = pygame.image.load(path.join('assets', 'mole', 'mole_r.png')).convert_alpha()
mole_throw_l = pygame.image.load(path.join('assets', 'mole', 'throw_l.png')).convert_alpha()
mole_throw_r = pygame.image.load(path.join('assets', 'mole', 'throw_r.png')).convert_alpha()

# sneilesko
sneilesko_u_bg = pygame.image.load(path.join('assets', 'sneileskooo', 'sneilesko_u_bg.png')).convert_alpha()


# -----| FONT |-----
FONT_TYPE = pygame.font.Font(path.join('assets', 'dpcomic.ttf'), FONT_SIZE)

# -----| SOUNDS |-----
DEATH_SOUND = pygame.mixer.Sound(path.join('assets', 'death_link.wav'))
DEATH_SOUND.set_volume(0.1)
DAMAGE_SOUND = pygame.mixer.Sound(path.join('assets', 'damage.wav'))
SOUNDTRACK = path.join('assets', 'soundtrack.mp3')
