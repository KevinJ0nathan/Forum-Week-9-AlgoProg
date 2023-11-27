import pygame

import sys

from game_character import Character

# Defining the background colour
background_colour = (33, 166, 255)
# Define the dimension of screen object(width,height)
screen = pygame.display.set_mode((500,500))
# Set the caption of the screen
pygame.display.set_caption('12-1 12-2 Try It Yourself')
# Fill the background colour to the screen
screen.fill(background_colour)

# Update the display
pygame.display.flip()

Char = Character(screen)

# game loop 
while True: 
    screen.fill(background_colour)
    Char.blitme()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.flip()