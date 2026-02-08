""" Hovedprogrammet som skal kjores """
import pygame
from src.pause_menu import PauseMenu

from .options import *


def run(screen):
    from .assets import SOUNDTRACK, DEATH_SOUND, DAMAGE_SOUND, BACKGROUND_IMAGE, CUT_GRASS, GRASS, ROCK
    from .Player import Player
    from .Garden import Garden
    from .Projectile import Projectile

    pygame.display.set_caption("Snakeler")

    # Clock and timing
    clock = pygame.time.Clock()
    dt = 0

    pygame.mixer.music.load(SOUNDTRACK)
    pygame.mixer.music.play(-1)  # Loop the soundtrack indefinitely

    # Game objects

    p1 = Player()
    projectiles = []
    cut_grass = set()
    
    garden = Garden(p1)

    score = 0

    # Pause menu
    pause_menu = PauseMenu(screen)
    paused_time = 0

    direction = pygame.Vector2(0, -1)
    last_move_pos = (p1.x, p1.y)

    # function to draw everything
    def draw_frame():
        garden.draw(screen)

        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)

        # Update grass
        for cut_grass_position in cut_grass:
            screen.blit(CUT_GRASS, (cut_grass_position[0], cut_grass_position[1]))

        
        p1.draw(direction, screen)

        # hp bar
        hp_bar_width = 200
        hp_bar_height = 20
        hp_bar_x = 10
        hp_bar_y = 10
        hp_ratio = p1.hp / HP
        pygame.draw.rect(screen, BLACK, (hp_bar_x, hp_bar_y, hp_bar_width, hp_bar_height))
        pygame.draw.rect(screen, PINK, (hp_bar_x, hp_bar_y, hp_bar_width * hp_ratio, hp_bar_height))

        pygame.display.flip()


    # Game loop
    running = True
    quit_requested = False
    died = False

    while running:
        dt = clock.tick(FRAMERATE) / 1000
        current_time = pygame.time.get_ticks() - paused_time

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_requested = True
                running = False


        # -----| Movement |-----
        lastX = p1.x
        lastY = p1.y
            
        # Get key presses
        keys = pygame.key.get_pressed()
        input_dir = pygame.Vector2(0, 0)
        if keys[pygame.K_a]:
            input_dir.x -= 1
        if keys[pygame.K_d]:
            input_dir.x += 1
        if keys[pygame.K_w]:
            input_dir.y -= 1
        if keys[pygame.K_s]:
            input_dir.y += 1

        # Pause menu
        if keys[pygame.K_ESCAPE]:
                pause_start = pygame.time.get_ticks()
                pause_menu_result = pause_menu.run()
                if pause_menu_result != True:
                    quit_requested = True
                    running = False
                pause_end = pygame.time.get_ticks()

                paused_time += pause_end - pause_start   
                clock.tick()                             
                continue 
        
                

        # Normalize move
        if input_dir.length_squared() > 0:
            input_dir = input_dir.normalize()
            direction = input_dir

        # Move player

        # Move X
        p1.x += direction.x * p1.speed * dt
        p1.rect.topleft = (p1.x, p1.y)

        if garden.collide(p1) != -1:
            p1.x = lastX
            p1.rect.topleft = (p1.x, p1.y)

        # Move Y
        p1.y += direction.y * p1.speed * dt
        p1.rect.topleft = (p1.x, p1.y)

        if garden.collide(p1) != -1:
            p1.y = lastY
            p1.rect.topleft = (p1.x, p1.y)

        # Keep in bounds
        p1.x = max(0, min(WIDTH - p1.size[0], p1.x))
        p1.y = max(0, min(HEIGHT - p1.size[1], p1.y))

        if (p1.x, p1.y) != last_move_pos:
            cut_grass.add((lastX, lastY, current_time))
            last_move_pos = (p1.x, p1.y)


        # Regenerate HP
        if p1.hp < HP:
            p1.hp += p1.regeneration_rate * dt
            if p1.hp > HP:
                p1.hp = HP


        # -----| Collisions |-----
        # damage proportional to overlap with cut grass
        old_cut_grass = set()

        for cut_grass_position in cut_grass:
            # Remove old cut grass
            if current_time - cut_grass_position[2] > p1.length:  # Grass regrows after 5 seconds
                old_cut_grass.add(cut_grass_position)
                continue
            if current_time - cut_grass_position[2] < 300:  # skip damage for 1 second after cutting
                continue

            grass_rect = pygame.Rect(cut_grass_position[0], cut_grass_position[1], TILE_SIZE, TILE_SIZE)
            
            if grass_rect.colliderect(p1.rect):
                overlap_area = grass_rect.clip(p1.rect).width * grass_rect.clip(p1.rect).height
                damage = overlap_area / (p1.size[0] * p1.size[1]) * 20 * dt  # Max 20 damage per second
                p1.hp -= damage
                if p1.hp <= 0:
                    died = True


                    # Play death sound
                    DEATH_SOUND.play()
                    running = False

        # Increase the timers on the moles
        for mole in garden.moles:
            mole.process(dt, p1)

        # Spawn moles
        chance_for_mole = random.randint(0, 100)
        if chance_for_mole == 0:
            garden.generate_enemy()


        for cut_grass_position in old_cut_grass:
            cut_grass.remove(cut_grass_position)

        # Slowly increase the amount of grass cut by increasing length
        p1.length += 3
        

        # Update display
        draw_frame()

    pygame.mixer.music.stop()

    if quit_requested:
        return "quit"
    if died:
        return "menu"
    return "menu"

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run(screen)
