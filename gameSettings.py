import pygame as pg
import screen
from pygame.locals import *
from keyboard import *

import sys

#ogolne ustawienia do gry
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
vec = pg.math.Vector2
WIDTH =  1280
HEIGHT = 720
TITLE = "Wantuch's game"
running = True
Animations_PATH = "Animations"
SCREEN = screen.screen()
KEYBOARD = keyboard()
def loadify(img):
	return pg.image.load(img).convert_alpha()
def clamp(val,minv,maxv):
	val = max(min(val, maxv), minv)
	return val
def forceExitGame(debugLog):
	print(debugLog)
	sys.exit() 
def isBeetwen(val,mi,ma):
	if val>=mi and val<=ma:
		return True
	else:
		return False