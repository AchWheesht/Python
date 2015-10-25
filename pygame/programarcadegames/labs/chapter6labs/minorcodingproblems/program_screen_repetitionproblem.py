import pygame   #Import pygame
import math #import math module

pygame.init() #boot up pygame

PI = math.pi #because im lazy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Creating a window of resolution 800x600
display_size = (800, 600)
game_window = pygame.display.set_mode(display_size)

#naming the window
pygame.display.set_caption("Phil's bad art")

#Loop until close
done = False

#Screen refresh rate
clock = pygame.time.Clock()

#----- Main Program Loop -----
while not done:
    # --- Main event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game Logic Here

    # --- Drawing Code Here

    #First, always clear the Screen
    game_window.fill(BLACK)

    for i in range(0, 600, 10):
        for n in range(0, 800, 10):
            pygame.draw.rect(game_window, GREEN, [n, i, 5, 5])

    #Actual Drawing Here

    # --- Update screen
    pygame.display.flip()

    # --- set FPS
    clock.tick(60)
#Close window and QUIT
pygame.quit()
