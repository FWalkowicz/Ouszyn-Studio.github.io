import os
from player import * 
from gameSettings import *
from plat import *
import random

class Camera(object):
	def __init__(self):
		self.pos = vec(0,0)
		self.maxSpeed = 1000
		self.shakeTime = 0
		self.strength = 0
	def shakeScreen(self,time,strength):
		if self.shakeTime >0:
			return
		self.shakeTime = time
		self.strength = strength
	def moveCameraTo(self,playerPos,speed = 50):
		x = 0
		y = 0
		if self.shakeTime>0:
			x = random.randrange(-self.strength,self.strength)
			y = random.randrange(-self.strength,self.strength)
			self.shakeTime-=1
		speed = clamp(speed,1,self.maxSpeed)
		self.pos += vec(playerPos.x - self.pos.x-WIDTH/2+x,playerPos.y -self.pos.y - HEIGHT/2-50+y)*speed/self.maxSpeed #50 to player height aby idealnie wycentrowac
		