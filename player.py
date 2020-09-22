import pygame as pg
from pygame.locals import *
import sys
import os
from animator import *
from entity import *
class Player(entity):
	def __init__(self,x,y,sc=1,cW=0,cH=0):
		self.tag = "player"
		self.animFolder ="player"
		super().__init__(x,y,sc,cW,cH)


	def drawSelf(self,windowHandle):
		windowHandle.blit(self.image,self.rect)
	def handleMovment(self,cam):
		self.acc = vec(0,self.gravity)
		if self.grounded:
			self.spMultiplayer = 1
			self.curJumps = 0
		else:
			self.spMultiplayer = self.airControl

		if KEYBOARD.keyHold(pg.K_d):
			self.acc.x = self.speed * self.spMultiplayer
			self.left = False
		if KEYBOARD.keyHold(K_a):
			self.acc.x = -self.speed *self.spMultiplayer
			self.left = True
		if KEYBOARD.keyPresssed(pg.K_w) and ((self.grounded or self.curJumps<self.maxJumps and self.canJump) or self.enableFlight):
			self.vel.y = 0
			self.acc.y = -self.jumpAccel
			self.curJumps+=1
		if KEYBOARD.keyPresssed(pg.K_s):
			self.acc.y = self.jumpAccel
		else:
			self.animator.play('idle')
		if KEYBOARD.keyReleased(pg.K_l):
			if self.left:
				self.acc.x-=200
				cam.shakeScreen(20,500)
			else:
				cam.shakeScreen(20,500)
				self.acc.x+=200
		self.image = self.animator.currentFrame()
		self.currFrame = pg.transform.flip(self.image,self.left,False)
		self.rect = self.image.get_rect()
		##do skopiowania
		self.acc.x += self.vel.x * self.friction
		self.vel += self.acc
		self.pos += self.vel