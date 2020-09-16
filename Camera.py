import os
from player import * 
from gameSettings import *
from plat import *


class Camera(object):
	def __init__(self):
		self.pos = vec(0,0)
		self.maxSpeed = 1000
	def moveCameraTo(self,playerPos,speed = 50):
		speed = clamp(speed,1,self.maxSpeed)
		self.pos += vec(playerPos.x - self.pos.x-WIDTH/2,playerPos.y -self.pos.y - HEIGHT/2-50)*speed/self.maxSpeed #50 to player height aby idealnie wycentrowac
		