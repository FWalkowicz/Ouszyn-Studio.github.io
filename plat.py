import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
#platforma
class Platform (pg.sprite.Sprite):
	def __init__(self, x,y,w,h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(BLUE)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
