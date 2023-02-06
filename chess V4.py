import pygame

# initialize pygame
pygame.init()

# set initial window size
window_size = (400, 400)

# create window
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

# set the title of the window
pygame.display.set_caption("CHESS")

# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # bg colour
    screen.fill((196, 196, 196))

    # draw a square on the screen
    square_size = 50


    #DRAWING SQUARE GRID:
    #for loop for drawing squares x-wise
    for x in range(8):
          #for loop for drawing squares
          for y in range(8):
            squarepos = pygame.Rect(x*50, y*50, square_size, square_size)
            if((y+x)%2 == 0):
                pygame.draw.rect(screen, (0, 0, 0), squarepos)
            else:
                pygame.draw.rect(screen, (229, 226, 214), squarepos)

    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()