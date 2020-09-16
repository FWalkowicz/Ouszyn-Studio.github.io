import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *

class Animator(object):
	def __init__(self, animationFolderName):
		self.animations = {}

