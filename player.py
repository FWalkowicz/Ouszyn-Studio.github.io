import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
#wszystkie poruszajace sie obiekty
class entity(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.grounded = True
		self.canJump = True
		self.speed = 5		#maksymalna predkosc gracza
		self.pos = vec(0,0) #pozycja
		self.acc = vec(0,0) #przyspieszenie
		self.vel = vec(0,0)	#obecna predkosc
		#sztywne ustawienie obrazu na 100 na 100
		self.image = pg.image.load('kaniarz.png')
		self.rect = self.image.get_rect()
		if self.rect.height>100 or rect.width>100:
			self.image = pg.transform.scale(self.image, (100, 100))
			self.rect = self.image.get_rect()
	def checkColision(self,colliders):
		self.grounded =False
		for i in colliders:
			if pg.sprite.collide_rect(self,i):
				#50 zamienic pozniej na polowe wysokosci gracza
				if self.vel.y < 0 and self.pos.y+55 > i.rect.bottom:
					self.pos.y = i.rect.bottom+100
					self.vel.y = 0
					self.acc.y = 0
				if self.vel.y > 0 and self.pos.y-55 <= i.rect.top:
					self.pos.y = i.rect.top+1
					self.grounded =True
					self.vel.y = 0
					self.acc.y = 0
				if self.vel.x > 0 and self.pos.y> i.rect.top+1 and self.pos.x<=i.rect.left:
					self.pos.x = i.rect.left-51
				if self.vel.x < 0 and self.pos.y> i.rect.top+1 and self.pos.x>=i.rect.right:
					self.pos.x = i.rect.right+51
	def handleMovement(self):
		pass
#klasa gracza
class Player(entity):
	def __init__(self):
		super().__init__()
		self.pos = vec(PLAYER_START.x,PLAYER_START.y)
		self.rect = self.image.get_rect()
	def drawSelf(self,windowHandle):
		windowHandle.blit(self.image,self.rect)
	def handleMovment(self):
		keys=pg.key.get_pressed()
		self.acc = vec(0,0.7)
		if self.pos.y<=100:
			self.canJump = False
			self.pos.y = 100
			self.vel.y = 0
		else:
			self.canJump = True
		if keys[ord('d')]:
			self.acc.x = self.speed
		if keys[ord('a')]:
			self.acc.x = -self.speed
		if keys[ord('w')] and self.canJump:
			self.acc.y = -1
		self.acc.x += self.vel.x * -0.5
		self.vel += self.acc
		self.pos += self.vel+0.5*self.acc
		if self.pos.x > WIDTH:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = WIDTH
		self.rect.midbottom = self.pos