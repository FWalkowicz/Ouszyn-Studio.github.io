import pygame
from pygame.locals import *
import sys
import os


pygame.init()

########################################################################################################################
# properties
########################################################################################################################

WIDTH = 1280
HEIGHT = 900

TITLE = "Wantuch's game"

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# title
pygame.display.set_caption(TITLE)

# visibility of mouse
pygame.mouse.set_visible(1)

# background image
background = pygame.image.load("zsme.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background.set_colorkey(BLACK)
grass = pygame.image.load('grass.png')
grass = pygame.transform.scale(grass, (100, 100))
dirt = pygame.image.load('dirt.jpg')
dirt = pygame.transform.scale(dirt, (100, 100))

# fps
clock = pygame.time.Clock()
fps = 60

# player position
player_pos = [0, 600]
player_size = [100, 100]
moving_right = False
moving_left = False
vertical_momentum = 0
air_timer = 0

# player
player_img = pygame.image.load('wantuch.jpg')
player_img = pygame.transform.scale(player_img, player_size)

game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2', '2'],
            ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]
########################################################################################################################

# game loop
running = True
while running:

    window.blit(background, (0, 0))
    title_recs = []
    y = 0
    for layer in game_map:
        x = 0
        for title in layer:
            if title == '1':
                window.blit(dirt, (x*100, y*100))
            if title == '2':
                window.blit(grass, (x*100, y*100))
            if title != '0':
                title_recs.append(pygame.Rect(x*100, y*100, 100, 100))
            x += 1
        y += 1

    window.blit(player_img, player_pos)

    # move
    if moving_right == True:
        player_pos[0] += 10
    if moving_left == True:
        player_pos[0] -= 10

    # exit
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                moving_right = True
            if event.key == K_LEFT or event.key == ord('a'):
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT or event.key == ord('d'):
                moving_right = False
            if event.key == K_LEFT or event.key == ord('a'):
                moving_left = False

    pygame.display.update()
    clock.tick(fps)



