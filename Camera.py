import os
from player import * 
from gameSettings import *
from plat import *


class Camera(object):
	def __init__(self):
		self.pos = vec(0,0)
	def copyPos(self,playerPos):
		self.pos += vec(playerPos.x - self.pos.x-WIDTH/2,playerPos.y -self.pos.y - HEIGHT/2-50)/20 #50 to player height aby idealnie wycentrowac
		