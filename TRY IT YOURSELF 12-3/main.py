import pygame

from rocket import Rocket

import game_functions as gf

from settings import Settings

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # Update the display
    pygame.display.flip()
    rocket = Rocket(ai_settings, screen)


    # game loop 
    while True: 
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)

run_game()