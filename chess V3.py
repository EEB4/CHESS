import pygame

# initialize pygame
pygame.init()

# set the window size
window_size = (400, 400)

# Create a font object
font = pygame.font.Font(None, 36)

# create the window
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

# set the title of the window
pygame.display.set_caption("Square")

# run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a white color
    screen.fill((255, 255, 255))

    # draw a square on the screen
    square_size = 50
    square_x = 0
    square_y = 0


    #DRAWING SQUARE GRID:
    #for loop for drawing squares x-wise
    for x in range(4):
          #for loop for drawing squares y-wise offset by 1 unit on x axis (every second row)
          for y in range(4):
              squarey = pygame.Rect(square_x + 50 + (x*100), square_y + y*100, square_size, square_size)
              pygame.draw.rect(screen, (0, 0, 0), squarey)
              text = font.render((chr(65+y*2) + str((x+1)*2)), True, (0, 0, 255))
              screen.blit(text, (square_x + 50 + (x*100), square_y + y*100, square_size, square_size))
          #for loop for drawing squares normally y-wise (every second row)
          for y in range(4):
              squarey = pygame.Rect(square_x + (x*100), square_y + 50 + y*100, square_size, square_size)
              pygame.draw.rect(screen, (0, 0, 0), squarey)
              text = font.render((chr(66+y*2) + str(int((x+0.5)*2))), True, (0, 0, 255))
              screen.blit(text, (square_x + (x*100), square_y + 50 + y*100, square_size, square_size))



    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()