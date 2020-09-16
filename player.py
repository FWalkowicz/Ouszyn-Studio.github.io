import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
from animator import *
#wszystkie poruszajace sie obiekty
class entity(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.curJumps = 0
		self.maxJumps = 2
		self.grounded = True
		self.canJump = True
		self.enableFlight = True
		self.airControl = 0.7 #range (0,1)
		self.spMultiplayer = 1
		self.jumpAccel  = 9
		self.friction = -0.5
		self.speed = 4		#maksymalna predkosc gracza
		self.pos = vec(0,0) #pozycja
		self.acc = vec(0,0) #przyspieszenie
		self.vel = vec(0,0)	#obecna predkosc
		self.tag = "empty"
		self.gravity = 0.3 #range (0,1)
		self.left = False


		#sztywne ustawienie obrazu na 100 na 100
		self.image = loadify('character.jpg')
		self.rect = self.image.get_rect()
		if self.rect.height>100 or rect.width>100:
			self.image = pg.transform.scale(self.image, (100, 100))
			self.rect = self.image.get_rect()
		self.currFrame = self.image

	def setCollider(self):
		self.collider = pg.Rect(self.rect.x,self.rect.y,self.rect.width,self.rect.height)
	def checkColision(self,colliders):#jeszcze do poprawienia
		self.grounded =False
		for i in colliders:
			if pg.sprite.collide_rect(self,i):
				if self.vel.x > 0 and self.pos.y> i.rect.top+5 and self.pos.x+self.rect.width/2-10<=i.rect.left: # kolizja w lewo
					self.pos.x = i.rect.left-self.rect.width/2+1
				if self.vel.x < 0 and self.pos.y> i.rect.top+5 and self.pos.x-self.rect.width/2+10>=i.rect.right: # kolizja w prawo
					self.pos.x = i.rect.right+self.rect.width/2+1
				if self.vel.y < 0 and self.pos.y-self.rect.height/2-30 >= i.rect.bottom: # kolizja w gore
					self.pos.y = i.rect.bottom+self.rect.height
					self.vel.y = 0
				if self.vel.y > 0 and self.pos.y-self.rect.height/2+20 <= i.rect.top: # kolizja w dol
					self.pos.y = i.rect.top+1
					self.grounded =True
					self.vel.y = 0
				self.rect.midbottom = self.pos		
	def handleMovement(self):
		pass
	def handleAnimations(self):
		pass
#klasa gracza
class Player(entity):
	def __init__(self):
		super().__init__()
		self.pos = vec(PLAYER_START.x,PLAYER_START.y)
		self.rect = self.image.get_rect()
		self.holdedKeys = pg.key.get_pressed()
		self.lastKeys = pg.key.get_pressed()
		self.tag = "player"
		self.animator = Animator(self.tag)

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
		self.acc = vec(0,self.gravity)
		if self.grounded:
			self.spMultiplayer = 1
			self.curJumps = 0
		else:
			self.spMultiplayer = self.airControl

		if self.keyHold('d'):
			self.acc.x = self.speed * self.spMultiplayer
			self.left = False
		if self.keyHold('a'):
			self.acc.x = -self.speed *self.spMultiplayer
			self.left = True
		if self.keyPresssed('w') and ((self.grounded or self.curJumps<self.maxJumps and self.canJump) or self.enableFlight):
			self.vel.y = 0
			self.acc.y = -self.jumpAccel
			self.curJumps+=1
		else:
			self.animator.play("idle")
		self.image = self.animator.currentFrame()
		self.currFrame = pg.transform.flip(self.image,self.left,False)
		self.acc.x += self.vel.x * self.friction
		self.vel += self.acc
		self.pos += self.vel+self.acc
		self.rect.midbottom = self.pos	
		self.lastKeys = self.holdedKeys