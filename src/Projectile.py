from .options import *

class Projectile:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = (4, 30)
        self.speed = BULLET_SPEED
        self.color = GREEN
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.topleft = (self.x, self.y)

    def is_offscreen(self):
        return (self.rect.right < 0 or self.rect.left > WIDTH or 
                self.rect.top < 0 or self.rect.bottom > HEIGHT)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collides_with(self, lawn_mower_rect):
        return self.rect.colliderect(lawn_mower_rect)