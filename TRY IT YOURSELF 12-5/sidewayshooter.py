import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sideways Shooter")
ship_image = pygame.image.load('ship.png').convert_alpha()

WHITE = (255,255,255)

# Player's ship
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_image
        self.rect = self.image.get_rect()
        self.rect.left = 50  
        self.rect.centery = screen_height // 2  

    def update(self):
        # Handle ship movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 1
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += 1

# Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))  
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self):
        self.rect.x += 7  # Bullet's speed towards the right side

# Sprite Groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Create the player's ship
player = Ship()
all_sprites.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Create a bullet when space bar is pressed
            bullet = Bullet(player.rect.right, player.rect.centery)
            all_sprites.add(bullet)
            bullets.add(bullet)
    
    # Update
    all_sprites.update()
    
    # Remove bullets when they go off-screen
    for bullet in bullets.copy():
        if bullet.rect.left > screen_width:
            bullets.remove(bullet)
            all_sprites.remove(bullet)
    
    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    all_sprites.draw(screen)
    pygame.display.flip()


