""" Hovedprogrammet som skal kjøres """
import sys
import pygame

from .options import *


def run(screen):
    from .assets import BACKGROUND_IMAGE, FONT_TYPE, SOUNDTRACK
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
    garden = Garden()

    p1 = Player()
    projectiles = []
    cut_grass = set()

    score = 0

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
            pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(cut_grass_position[0], cut_grass_position[1], 64, 64))
            # TODO Cut grass texture
        
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

    while running:
        dt = clock.tick(FRAMERATE) / 1000
        current_time = pygame.time.get_ticks()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        # Normalize move
        if input_dir.length_squared() > 0:
            input_dir = input_dir.normalize()
            direction = input_dir

        # Move player
        p1.x += direction.x * p1.speed * dt
        p1.y += direction.y * p1.speed * dt

        # Keep in bounds
        p1.x = max(0, min(WIDTH - p1.size[0], p1.x))
        p1.y = max(0, min(HEIGHT - p1.size[1], p1.y))

        if (p1.x, p1.y) != last_move_pos:
            cut_grass.add((lastX, lastY, current_time))
            last_move_pos = (p1.x, p1.y)


        # -----| Collisions |-----
        # damage proportional to overlap with cut grass
        old_cut_grass = set()

        for cut_grass_position in cut_grass:
            # Remove old cut grass
            if current_time - cut_grass_position[2] > 5000:  # Grass regrows after 5 seconds
                old_cut_grass.add(cut_grass_position)
                continue
            if current_time - cut_grass_position[2] < 300:  # skip damage for 1 second after cutting
                continue

            grass_rect = pygame.Rect(cut_grass_position[0], cut_grass_position[1], TILE_SIZE, TILE_SIZE)
            player_rect = pygame.Rect(p1.x, p1.y, p1.size[0], p1.size[1])
            if grass_rect.colliderect(player_rect):
                overlap_area = grass_rect.clip(player_rect).width * grass_rect.clip(player_rect).height
                damage = overlap_area / (p1.size[0] * p1.size[1]) * 20 * dt  # Max 20 damage per second
                p1.hp -= damage
                if p1.hp <= 0:
                    running = False
                    # main menu


        for cut_grass_position in old_cut_grass:
            cut_grass.remove(cut_grass_position)


        # Update display
        draw_frame()

    # Clean up
    pygame.time.wait(2000)  # Wait for 2 seconds before quitting
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    run(screen)
