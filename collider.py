import pygame as pg
from screen import *
from gameSettings import *
class Collider(object):
	def onCollision(self,object):
		pass
	def drawCollider(self):
		pass
class boxCollider(Collider):
	def __init__(self, pos,width,height):
		self.owidth = width
		self.oheight = height
		self.width = width
		self.height = height
		self.hitbox = pg.Rect(pos.x,pos.y,width,height)
	def onCollision(self,object):
		if self.hitbox.colliderect(object):
			return True
		else:
			return False
	def orginalSize(self):
		self.width = self.owidth
		self.height = self.oheight
	def changeSize(self,w,h):
		self.width = w
		self.height = h
	def update(self,pos,rect):
		self.hitbox = pg.Rect(pos.x+(rect.width-self.width)/2,pos.y+(rect.height-self.height)/2,self.width,self.height)	
	
	def draw(self,cam,color=BLACK,border=3):
		toDraw = pg.Rect(self.hitbox.x - cam.x,self.hitbox.y-cam.y,self.width,self.height)
		gameSettings.SCREEN.drawRectBordered(toDraw,color,border)

		
		