import pygame   #Import pygame
import r_colours #import colour values from seperate file
import math #import math module

pygame.init() #boot up pygame

PI = math.pi #because im lazy

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

    ##Draws a "P"
    # pygame.draw.rect(game_window, r_colours.BLACK, [25, 25, 5, 50])
    # pygame.draw.arc(game_window, r_colours.BLACK, [0, 25, 55, 25], 3*PI/2, (5*PI/2), 5)
    #
    # #Draws lots of "P"
    # for i in range(100, 500, 100):
    #     pygame.draw.rect(game_window, r_colours.BLACK, [25+i, 25, 5, 50])
    #     pygame.draw.arc(game_window, r_colours.BLACK, [i, 25, 55, 25], 3*PI/2, (5*PI/2), 5)
    #
    # #Draws a Polygon
    #
    # pygame.draw.polygon(game_window, r_colours.BLUE, [[200,200], [400,200], [400,400], [300, 500], [200,400]])

    #draws face base
    pygame.draw.ellipse(game_window, r_colours.PINK, [200, 100, 400, 400])

    #draws left eye
    pygame.draw.ellipse(game_window, r_colours.L_PINK, [275, 175, 100, 100])

    #draws left pupil
    pygame.draw.ellipse(game_window, r_colours.BLACK, [310, 210, 30, 30])

    #draws right eye
    pygame.draw.ellipse(game_window, r_colours.L_PINK, [425, 175, 100, 100])

    #draws right pupil
    pygame.draw.ellipse(game_window, r_colours.BLACK, [460, 210, 30, 30])

    #draws nose
    pygame.draw.ellipse(game_window, r_colours.BLACK, [360, 260, 80, 80])

    #draws mouth
    pygame.draw.arc(game_window, r_colours.WHITE, [250, 300, 300, 125], PI, (2*PI), 30)

    #draws upper lip
    pygame.draw.arc(game_window, r_colours.BLACK, [250, 300, 300, 100], PI, (2*PI), 5)

    #draws lower lip
    pygame.draw.arc(game_window, r_colours.BLACK, [250, 280, 300, 150], PI, (2*PI), 5)

    #image annotation
    font = pygame.font.SysFont("Calibri", 50, True, False) #sets font
    text = font.render("THIS IS PAUL", True, r_colours.BLACK) #sets string to be printed
    game_window.blit(text, [250, 500]) #prints text

    # --- Update screen
    pygame.display.flip()

    # --- set FPS
    clock.tick(60)
#Close window and QUIT
pygame.quit()
