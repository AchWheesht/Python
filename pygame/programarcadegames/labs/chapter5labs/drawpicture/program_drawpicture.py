import pygame   #Boot up pygame
import r_colours #import colour values from seperate file

pygame.init()

PI = 3.141

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
    game_window.fill(r_colours.WHITE)

    #Actual Drawing Here

    #Draws a "P"
    pygame.draw.rect(game_window, r_colours.BLACK, [25, 25, 5, 50])
    pygame.draw.arc(game_window, r_colours.BLACK, [0, 25, 55, 25], 3*PI/2, (5*PI/2), 5)

    #Draws lots of "P"
    for i in range(100, 500, 100):
        pygame.draw.rect(game_window, r_colours.BLACK, [25+i, 25, 5, 50])
        pygame.draw.arc(game_window, r_colours.BLACK, [i, 25, 55, 25], 3*PI/2, (5*PI/2), 5)

    # --- Update screen
    pygame.display.flip()

    # --- set FPS
    clock.tick(60)
#Close window and QUIT
pygame.quit()
