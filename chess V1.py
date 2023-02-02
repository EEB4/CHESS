import pygame

# initialize pygame
pygame.init()

# set the window size
window_size = (400, 400)

# create the window
screen = pygame.display.set_mode(window_size)

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
    for x in range(8):
          squarex = pygame.Rect(square_x + x*100, square_y, square_size, square_size)
          pygame.draw.rect(screen, (0, 0, 0), squarex) 
          #for loop for drawing squares y-wise offset by 1 unit on x axis (every second row)
          for y in range(8):
              squarey = pygame.Rect(square_x + 50 + (x*100), square_y + 50 + y*100, square_size, square_size)
              pygame.draw.rect(screen, (0, 0, 0), squarey)
          #for loop for drawing squares normally y-wise (every second row)
          for y in range(8):
              squarey = pygame.Rect(square_x + (x*100), square_y + 100 + y*100, square_size, square_size)
              pygame.draw.rect(screen, (0, 0, 0), squarey)



    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()