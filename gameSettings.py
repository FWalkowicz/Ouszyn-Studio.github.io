import pygame as pg
from pygame.locals import *

#ogolne ustawienia do gry
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
vec = pg.math.Vector2
WIDTH = 1280
HEIGHT = 1080
TITLE = "Wantuch's game"
PLAYER_START = vec(200,600)
running = True
Animations_PATH = ""
def loadify(img):
	return pg.image.load(img).convert_alpha()
def clamp(val,minv,maxv):
	val = max(min(val, maxv), minv)
	return val
