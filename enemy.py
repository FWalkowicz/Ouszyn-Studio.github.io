from entity import *
from pygame.locals import *


class Enemy(entity):
	"""docstring for Enemy"""
	def __init__(self, x,y,sc=1,cW=0,cH=0):
		self.tag = "enemy"
		self.animFolder = "enemy"
		super().__init__(x,y,sc,cW,cH)

		