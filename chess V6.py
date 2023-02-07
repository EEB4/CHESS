import pygame
import os


# initialize pygame
pygame.init()

# set initial window size
window_size = (400, 400)

# create window
screen = pygame.display.set_mode(window_size, pygame.RESIZABLE)

# set the title of the window
pygame.display.set_caption("CHESS")

# Get the path to the py file
script_dir = os.path.dirname(os.path.abspath(__file__))

# get file path for pawn sprite
image_path = os.path.join(script_dir, "sprite.png")

# Load the image for the sprite
sprite_image = pygame.image.load(image_path).convert_alpha()

#defining base position for pawn
posX = 0
posY = 6

# getting starting mouse position
mouseX, mouseY = pygame.mouse.get_pos()


# sprite spawn function
def spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, posX, posY):

    # Scale the sprite image
    sprite_image = pygame.transform.scale(sprite_image, (square_size, square_size))

    # Create a rect for the sprite (essentially spawn it in)
    sprite_rect = sprite_image.get_rect()

    # Set the sprite's position on the screen
    sprite_rect.x = (xScreenSize - square_size*8)/2 + (posX * square_size)
    sprite_rect.y = (yScreenSize - square_size*8)/2 + (posY * square_size)

    # Display the sprite on the screen
    screen.blit(sprite_image, sprite_rect)


# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # when mouse button is pressed, tries to move pawn if all the conditions are met
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouseCoordY <= posY and (posY - mouseCoordY) <= 2:
                    if (posY == 6 or (posY - mouseCoordY) <= 1) and posX == mouseCoordX:
                        posX = mouseCoordX
                        posY = mouseCoordY

    # bg colour
    screen.fill((196, 196, 196))

    #getting current screen dimentions
    xScreenSize, yScreenSize = screen.get_size()

    #adjusting size of board depending on screen dimentions
    if (xScreenSize > yScreenSize):
        square_size = yScreenSize/8
    else:
        square_size = xScreenSize/8

    #centering the board
    offsetx = (xScreenSize - square_size*8)/2
    offsety = (yScreenSize - square_size*8)/2

    # getting current mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    #converting mouse position to board coordinate space
    mouseCoordX = int((mouseX - (offsetx))/(square_size))
    mouseCoordY = int((mouseY - (offsety))/(square_size))

    #DRAWING SQUARE GRID:
    #for loop for drawing squares x-wise
    for x in range(8):
          #for loop for drawing squares y-wise
          for y in range(8):
            squarepos = pygame.Rect(offsetx + (x*square_size), offsety + (y*square_size), square_size, square_size)
            if((y+x)%2 == 0):
                pygame.draw.rect(screen, (0, 0, 0), squarepos)
            else:
                pygame.draw.rect(screen, (229, 226, 214), squarepos)

    #clamping pawn values within board
    posX = max(0, min(7, posX))
    posY = max(0, min(7, posY))

    # spawning pawn sprite
    spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, posX, posY)

    # update the display
    pygame.display.update()

# quit pygame
pygame.quit()