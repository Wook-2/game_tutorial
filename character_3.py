import pygame as pg

pg.init()

SIZE = [500, 489]
screen = pg.display.set_mode(SIZE)

pg.display.set_caption("My First Game")

clock = pg.time.Clock()

x = 50
y = 425
width = 64
height = 64
vel = 5

# walkRight = [pg.image.load('./character/R1.png'), pg.image.load('./character/R2.png'), pg.image.load('./character/R3.png'), pg.image.load('./character/R4.png'), pg.image.load('./character/R5.png'), pg.image.load('./character/R6.png'), pg.image.load('./character/R7.png'),pg.image.load('./character/R8.png'),pg.image.load('./character/R9.png')]
# walkLeft = [pg.image.load('./character/L1.png'), pg.image.load('./character/L2.png'), pg.image.load('./character/L3.png'), pg.image.load('./character/L4.png'), pg.image.load('./character/L5.png'), pg.image.load('./character/L6.png'), pg.image.load('./character/L7.png'),pg.image.load('./character/L8.png'),pg.image.load('./character/L9.png')]
walkRight = [pg.image.load('./character/R%s.png' %frame) for frame in range(1, 10)]
walkLeft = [pg.image.load('./character/L%s.png' %frame) for frame in range(1, 10)]
bg = pg.image.load('./character/bg.jpg')
char = pg.image.load('./character/standing.png')

isJump = True
JUMP_VALUE = 7
jumpCount = JUMP_VALUE
left = False
right = False
walkCount = 0


run = True

def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        screen.blit(char, (x,y))
    
    pg.display.update()


while run:
    clock.tick(27)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False


    elif keys[pg.K_RIGHT] and x < (SIZE[0]-width):
        x += vel
        right = True
        left = False
    
    else:
        right = False
        left = False
        walkCount = 0


    if not (isJump):
        
        if keys[pg.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -1 * (JUMP_VALUE):
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= 0.5 * (jumpCount ** 2) * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = JUMP_VALUE
    
    redrawGameWindow()
    
    

pg.quit()
    