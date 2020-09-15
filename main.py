import os
from player import * 
from gameSettings import *
from plat import *

#bedzie przechowywac gracza,wszystkie moby stwory etc
entities = []
#wszystko co bedzie wwyswietlane na ekranie
all_sprites = pg.sprite.Group()

pg.init()
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
pg.mouse.set_visible(1)
background = pg.image.load("banas2.png")
background = pg.transform.scale(background, (WIDTH, HEIGHT))

clock = pg.time.Clock()

#chwilowy syf
player = Player()
entities.append(player)
all_sprites.add(player)
platforms = pg.sprite.Group()
p1 = Platform(-100, HEIGHT - 40, WIDTH+200, 40)
all_sprites.add(p1)
platforms.add(p1)
p2 = Platform(500, 400, 200, 1000)
all_sprites.add(p2)
platforms.add(p2)
p3 = Platform(-100, 100, WIDTH+200, 40)
all_sprites.add(p3)
platforms.add(p3)
################
while running:
    window.fill((WHITE))
    window.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == QUIT:
            sys.exit()    
    player.handleMovment()
    player.checkColision(platforms)  

    all_sprites.draw(window)
    pg.display.update()




