import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
from animator import *
from collider import *

class entity(pg.sprite.Sprite):
	def __init__(self,x,y,scaler =1,colliderWidth =100,colliderHeight =100):
		pg.sprite.Sprite.__init__(self)
		self.curJumps = 0
		self.maxJumps = 2
		self.grounded = True
		self.canJump = True
		self.enableFlight = True
		self.airControl = 0.7 #range (0,1)
		self.spMultiplayer = 1
		self.jumpAccel  = 15
		self.friction = -0.6
		self.speed = 4		#maksymalna predkosc gracza
		self.pos = vec(x,y) #pozycja prawy dolny rog spritu
		self.acc = vec(0,0) #przyspieszenie
		self.vel = vec(0,0)	#obecna predkosc
		#self.tag = "empty"
		self.gravity =0.4 #range (0,1)
		self.left = False
		self.envCollider = Collider()
		self.animator = Animator(self.animFolder,scaler)
		self.image = self.animator.currentFrame()
		self.rect = self.image.get_rect()
		if colliderWidth  == 0:
			colliderWidth = self.rect.width
		if colliderHeight == 0:
			colliderHeight= self.rect.height
		self.envCollider = boxCollider(self.pos,colliderWidth,colliderHeight)
		#self.getLeftTop().x + (rect.width - colliderWidth)/2 - lewy gorny rog collidera x 
	def drawCollider(self,cam):
		self.envCollider.draw(cam)
	def getAbsLeftTop(self,cam): #dotyczy spritu
		return vec(self.pos.x-cam.x - self.rect.width,  self.pos.y-cam.y - self.rect.height)
	def getCenter(self): #dotyczy spritu
		return vec(self.pos.x - self.rect.width/2,  self.pos.y - self.rect.height/2)
	def getLeftTop(self): #dotyczy spritu
		return vec(self.pos.x - self.rect.width,  self.pos.y - self.rect.height)
	def checkColision(self,colliders):
		self.grounded =False
		self.envCollider.update(self.getLeftTop(),self.rect) #wycentrowanie collidera terenu
		for i in colliders:
			if self.envCollider.onCollision(i):
				if self.vel.x < 0 and isBeetwen(self.envCollider.hitbox.left,i.rect.right+self.vel.x-1,i.rect.right+5): # kolizja w prawo
					self.pos.x = i.rect.right+(self.rect.width-self.envCollider.width)/2+self.envCollider.width

				if self.vel.x > 0 and isBeetwen(self.envCollider.hitbox.right,i.rect.left,i.rect.left+self.vel.x+1): # kolizja w lewo
					self.pos.x = i.rect.left+(self.rect.width-self.envCollider.width)/2
				if self.vel.y < 0 and isBeetwen(self.envCollider.hitbox.midtop[1],i.rect.bottom+self.vel.y-1,i.rect.bottom): # kolizja w gore
					self.pos.y = i.rect.bottom+(self.rect.height + self.envCollider.height)//2
					self.vel.y = 0
				if self.vel.y > 0 and isBeetwen(self.envCollider.hitbox.midbottom[1],i.rect.top,i.rect.top+self.vel.y+1): # kolizja w dol
					self.pos.y = i.rect.top + (self.rect.height - self.envCollider.height)//2 +1
					self.grounded =True
					self.vel.y = 0	
	def handleMovement(self):
		pass
	def handleAnimations(self):
		pass
