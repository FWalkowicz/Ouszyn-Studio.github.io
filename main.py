
import pygame
from pygame.locals import *
#from tkinter import * GUI!
import sys


# Init pygame
pygame.init()

# Window Size
size = width, height = 900, 600
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)

# Background
background = pygame.image.load("cool.jpg")
background = pygame.transform.scale(background, (900, 600))

# Title and Icon
pygame.display.set_caption("Wantuch Na Kozaku")
icon = pygame.image.load("java.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    pygame.display.update()
    #screen.fill((120,0,0))

    # Background Init
    screen.blit(background, (0, 0))

    # Game Init/Quit and Main Events
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
