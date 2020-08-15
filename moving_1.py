import pygame as pg

pg.init()

SIZE = [500, 500]
screen = pg.display.set_mode(SIZE)

pg.display.set_caption("My First Game")

x = 50
y = 50
width = 20
height = 20
vel = 5

run = True

while run:
    pg.time.delay(80)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
        x -= vel
        pass
    if keys[pg.K_RIGHT]:
        x += vel
        pass
    if keys[pg.K_UP]:
        y -= vel
        pass
    if keys[pg.K_DOWN]:
        y += vel
        pass
    
    
    screen.fill((0, 0, 0))
    pg.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pg.display.update()

pg.quit()
    