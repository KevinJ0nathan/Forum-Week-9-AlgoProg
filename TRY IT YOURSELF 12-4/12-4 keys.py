import pygame
import sys

def run_game():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Key Detection")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  
                sys.exit()     
            # Check for key presses
            elif event.type == pygame.KEYDOWN:
                key_pressed = event.key       
                key_name = pygame.key.name(key_pressed)  
                print(f"Key pressed: {key_name} (code: {key_pressed})") 
        
        # Update the display
        pygame.display.flip()

# Run the game
run_game()
