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
background = pygame.image.load("tlo.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# fps
clock = pygame.time.Clock()

# player position
player_pos = [0, 800]
player_size = [100, 100]

########################################################################################################################

# character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 15):
            img = pygame.image.load(os.path.join('png', 'Walk (' + str(i) + ').png')).convert()
            self.images.append(pygame.transform.scale(img, (player_size[0], player_size[1])))
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.frame = 0





player = Player()
player.rect.x = player_pos[0]
player.rect.y = player_pos[1]





# Pętla gry
running = True
while running:

    window.fill((WHITE))

    #ładowanie tła
    window.blit(background, (0, 0))


    for event in pygame.event.get():

        # exit
        if event.type == QUIT:
            sys.exit()

        # player movement
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x -= 100
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                x += 100

            player_pos = [x, y]

    pygame.draw.rect(window, RED, (player_pos[0], player_pos[1], player_size[0], player_size[1]))
    #player.draw(window)

    player.update()
    pygame.display.update()






