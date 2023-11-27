import pygame
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
STAR_SIZE = 30
GRID_SPACING = 50

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stars Grid")

# Load star image
star_img = pygame.image.load("images/star.bmp")  
star_img = pygame.transform.scale(star_img, (STAR_SIZE, STAR_SIZE))

# Function to draw stars on the screen
def draw_stars():
    for y in range(0, SCREEN_HEIGHT, GRID_SPACING):
        for x in range(0, SCREEN_WIDTH, GRID_SPACING):
            screen.blit(star_img, (x, y))

# Main loop
running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_stars()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
