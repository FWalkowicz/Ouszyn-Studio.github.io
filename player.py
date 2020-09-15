import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
#wszystkie poruszajace sie obiekty
class entity(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.curJumps = 0
		self.maxJumps = 2
		self.grounded = True
		self.canJump = True
		self.enableFlight = False
		self.airControl = 0.7 #range (0,1)
		self.spMultiplayer = 1
		self.jumpAccel  = 20
		self.friction = -0.5
		self.speed = 5		#maksymalna predkosc gracza
		self.pos = vec(0,0) #pozycja
		self.acc = vec(0,0) #przyspieszenie
		self.vel = vec(0,0)	#obecna predkosc
		self.tag = "empty"
		


		#sztywne ustawienie obrazu na 100 na 100
		self.image = pg.image.load('banas.png')
		self.rect = self.image.get_rect()
		if self.rect.height>100 or rect.width>100:
			self.image = pg.transform.scale(self.image, (100, 100))
			self.rect = self.image.get_rect()
	def checkColision(self,colliders):
		self.grounded =False
		for i in colliders:
			if pg.sprite.collide_rect(self,i):
				if self.vel.x > 0 and self.pos.y> i.rect.top+5 and self.pos.x-10<=i.rect.left:
					self.pos.x = i.rect.left-self.rect.width/2+1
				if self.vel.x < 0 and self.pos.y> i.rect.top+5 and self.pos.x+10>=i.rect.right:
					self.pos.x = i.rect.right+self.rect.width/2+1
				if self.vel.y < 0 and self.pos.y+self.rect.height/2+5 >= i.rect.bottom:
					self.pos.y = i.rect.bottom+self.rect.height
					self.vel.y = 0
				if self.vel.y > 0 and self.pos.y-self.rect.height/2+20 <= i.rect.top:
					self.pos.y = i.rect.top+1
					self.grounded =True
					self.vel.y = 0
				self.rect.midbottom = self.pos		
	def handleMovement(self):
		pass
#klasa gracza
class Player(entity):
	def __init__(self):
		super().__init__()
		self.pos = vec(PLAYER_START.x,PLAYER_START.y)
		self.rect = self.image.get_rect()
		self.holdedKeys = pg.key.get_pressed()
		self.lastKeys = pg.key.get_pressed()
	def keyPresssed(self,key):
		k = ord(key)
		if self.holdedKeys[k] and self.holdedKeys[k]!=self.lastKeys[k]:
			return True
		else:
			return False
	def keyReleased(self,key):
		k = ord(key)
		if not self.holdedKeys[k] and self.holdedKeys[k]!=self.lastKeys[k]:
			return True
		else:
			return False
	def keyHold(self,key):
		k = ord(key)
		if self.holdedKeys[k]:
			return True
		else:
			return False
	def drawSelf(self,windowHandle):
		windowHandle.blit(self.image,self.rect)
	def handleMovment(self):
		self.holdedKeys=pg.key.get_pressed()
		self.acc = vec(0,1)
		if self.pos.y<=100:
			self.canJump = False
			self.pos.y = 100
			self.vel.y = 0
		else:
			self.canJump = True	
		if self.grounded:
			self.spMultiplayer = 1
			self.curJumps = 0
		else:
			self.spMultiplayer = self.airControl

		if self.keyHold('d'):
			self.acc.x = self.speed * self.spMultiplayer
		if self.keyHold('a'):
			self.acc.x = -self.speed *self.spMultiplayer
		if self.keyPresssed('w') and ((self.grounded or self.curJumps<self.maxJumps and self.canJump) or self.enableFlight):
			self.vel.y = 0
			self.acc.y = -self.jumpAccel
			self.curJumps+=1
		self.acc.x += self.vel.x * self.friction
		self.vel += self.acc
		self.pos += self.vel+self.acc

		if self.pos.x > WIDTH:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = WIDTH
		self.rect.midbottom = self.pos
		self.lastKeys = self.holdedKeys