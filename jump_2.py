import pygame as pg

pg.init()

SIZE = [400, 400]
screen = pg.display.set_mode(SIZE)

pg.display.set_caption("My First Game")

x = 50
y = 50
width = 20
height = 20
vel = 5

isJump = True
JUMP_VALUE = 7
jumpCount = JUMP_VALUE

run = True

while run:
    pg.time.delay(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT] and x > 0:
        x -= vel

    if keys[pg.K_RIGHT] and x < (SIZE[0]-width):
        x += vel

    if not (isJump):
        if keys[pg.K_UP] and y > 0:
            y -= vel

        if keys[pg.K_DOWN] and y < (SIZE[1]-height):
            y += vel
        if keys[pg.K_SPACE]:
            isJump = True
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

    
    
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()
    