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

# Główny bohater
class Wantuch():
    def __init__(self):
        size = width, height = 100, 100
        wiktor = self.pygame.image.load("banas.png")
        self.pygame.transform.scale(wiktor, (100,100))
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

        self.level = None

    def update(self):
        self.calc_grav()



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



