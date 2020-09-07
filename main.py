
import pygame
from pygame.locals import *
import os
import sys

# Init pygame
pygame.init()

# Objects #

# Character class


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        img = pygame.image.load(os.path.join('images', 'wantuch.jpg')).convert()
        self.images.append(pygame.transform.scale(img , (50 ,50)))
        self.image = self.images[0]
        self.rect = self.image.get_rect()


# Window Size


size = width, height = 900, 600
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(0)

# Background
#background = pygame.image.load("images/cool.jpg")
#background = pygame.transform.scale(background, (900, 600))

# Title and Icon
pygame.display.set_caption("Wantuch Na Kozaku")
icon = pygame.image.load("images/java.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    pygame.display.update()
    screen.fill((0, 0, 0))

    # Background Init
    #screen.blit(background, (0, 0))

    # Game Init/Quit and Main Events
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    # Character spawn
    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    player_list.draw(screen)
