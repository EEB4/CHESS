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
image_path1 = os.path.join(script_dir, "pawn.png")
# Load the image for the sprite
sprite_image = pygame.image.load(image_path1).convert_alpha()

TupleNumber = -1
selectedValue = -1

possiblePositions = [(0, 0)]

#defining base position for pawns
posX1 = 0
posY1 = 6
posX2 = 1
posY2 = 6
posX3 = 2
posY3 = 6
posX4 = 3
posY4 = 6
posX5 = 4
posY5 = 6
posX6 = 5
posY6 = 6
posX7 = 6
posY7 = 6
posX8 = 7
posY8 = 6
posList = [(posX1, posY1), (posX2, posY2), (posX3, posY3), (posX4, posY4), (posX5, posY5), (posX6, posY6), (posX7, posY7), (posX8, posY8)]
(posX, posY) = posList[0]

# getting starting mouse position
mouseX, mouseY = pygame.mouse.get_pos()

# the variable that detects which piece is clicked / selected (0 - no piece is selected; 1-32 which piece is selected)
k = 0

# sprite spawn function
def spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, posX, posY):

    # Scale the sprite image
    sprite_image = pygame.transform.scale(sprite_image, (square_size, square_size))

    # Create a rect for the sprite (essentially spawn it in)
    sprite_rect = sprite_image.get_rect()

    # Set the sprite's position on the screen
    sprite_rect.x = offsetx + (posX * square_size)
    sprite_rect.y = offsety + (posY * square_size)

    # Display the sprite on the screen
    screen.blit(sprite_image, sprite_rect)

# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # when mouse button is pressed, tries to move pawn
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # if pawn is not selected and it is clicked on, it will select it
            if event.button == 1 and k == 0:
                # remembering what tuple (set of pawn coords) we clicked on
                TupleNumber = 0
                for CoordsTuple in posList:
                    if (mouseCoordX, mouseCoordY) == CoordsTuple:
                        k = 1
                        # setting the main posX and posY to the coords of the piece that we clicked on
                        posX = CoordsTuple[0]
                        posY = CoordsTuple[1]
                        #image_path1 = os.path.join(script_dir, "pawnSelected.png")
                        #sprite_image = pygame.image.load(image_path1).convert_alpha()
                        # making sure the program doesnt continue after finding out which piece we clicked on
                        selectedValue = TupleNumber
                        break
                    else:
                        TupleNumber += 1
                    #if pawn is in first row the pawn can move one more square
                    if posY == 6:
                        possiblePositions = [(posX, posY - 1), (posX, posY - 2)]
                    #setting the only possible move for a standard pawn in normal conditions
                    else:
                        possiblePositions = [(posX, posY - 1)]
            # if pawn is selected, then you can move it
            elif event.button == 1 and k == 1:
                #if mouseCoordY is at one of the possible positions, move the pawn
                for possiblePosition in possiblePositions:
                    if (mouseCoordX, mouseCoordY) == possiblePosition and event.button == 1 and k == 1:
                        posX = mouseCoordX
                        posY = mouseCoordY
                        posList[TupleNumber] = (posX, posY)
                    print(possiblePosition)
                    image_path1 = os.path.join(script_dir, "GreyCirclePossiblePosition.png")
                    sprite_image = pygame.image.load(image_path1).convert_alpha()
                    spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, possiblePosition[0], possiblePosition[1])

                # deselecting the pawn after moving
                k = 0
                selectedValue = -1


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

    i = 0
    # spawning pawn sprites
    for i in posList:
        if selectedValue == i[0]:
            image_path1 = os.path.join(script_dir, "pawnSelected.png")
            sprite_image = pygame.image.load(image_path1).convert_alpha()
            spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, i[0], i[1])
            if posY == 6:
                possiblePositions = [(posX, posY - 1), (posX, posY - 2)]
                #setting the only possible move for a standard pawn in normal conditions
            else:
                possiblePositions = [(posX, posY - 1)]
            for possiblePosition in possiblePositions:
                print(possiblePosition)
                image_path1 = os.path.join(script_dir, "GreyCirclePossiblePosition.png")
                sprite_image = pygame.image.load(image_path1).convert_alpha()
                spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, possiblePosition[0], possiblePosition[1])
        else:
            image_path1 = os.path.join(script_dir, "pawn.png")
            sprite_image = pygame.image.load(image_path1).convert_alpha()
            spawn_sprite(screen, yScreenSize, xScreenSize, square_size, sprite_image, i[0], i[1])


    # update the display
    pygame.display.update()
    
# quit pygame
pygame.quit()