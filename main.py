import pygame
from pygame.locals import *
import sys

pygame.init()

# wielkość okna
size = width, height = 1280, 900
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)

# tło
background = pygame.image.load("tlo.jpg")
background = pygame.transform.scale(background, (1280, 900))

# Pętla gry
running = True
while running:
    pygame.display.update()
    screen.fill((120,0,0))

    #ładowanie tła
    screen.blit(background,(0,0))

    # wyłączanie gry
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

print("WAntuch na kozaku")



