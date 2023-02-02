import pygame as pg

pg.init()

WIDTH, HEIGHT = 800, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (255, 218, 145)
COLOURS = [BEIGE, BLACK]
POS = [WIDTH/2, HEIGHT/2]
pg.display.set_caption("Chess")
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()

#positions for where the square is placed
squarex = 0
squarey = 0
#size of a side of the sqare
square_size = 100

while True:
    clock.tick(60)

    #background
    screen.fill(WHITE)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                exit()
        if event.type == pg.VIDEORESIZE:
            screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            #changing the position of the board depending on the size of the window
            POS = [event.w/2, event.h/2]
            squarex = POS[0]
            squarex = POS[1]

    #adding the squares 
    for i in range(8):
        for j in range(8):
            square = pg.Rect(squarex + i*100, squarey + j*100, square_size, square_size)
            #if i is odd, then it is a row that starts with beige, if it's even, the row starts with black
            if (i%2==1):
                if(j%2==1):
                    pg.draw.rect(screen, BEIGE, square)
                else:
                    pg.draw.rect(screen, BLACK, square)
            else:
                if(j%2==1):
                    pg.draw.rect(screen, BLACK, square)
                else:
                    pg.draw.rect(screen, BEIGE, square)
        

    pg.display.update()