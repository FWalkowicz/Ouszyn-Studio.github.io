import gameSettings
import pygame as pg
class screen(object):
	def init(self):
		self.monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
		self.cWidth = gameSettings.WIDTH
		self.cHeight = gameSettings.HEIGHT
		self.screen = pg.display.set_mode((self.cWidth, self.cHeight))
		self.display = pg.Surface((gameSettings.WIDTH,gameSettings.HEIGHT))
		self.fullScreen = False
	def drawOnDisplay(self,sprite,x,y):
		self.display.blit(sprite,x,y)
	def drawOnDisplay(self,sprite,vec):
		self.display.blit(sprite,(vec.x,vec.y))
	def drawOnDisplay(self,sprite,arr):
		self.display.blit(sprite,arr)
	def drawRectBordered(self,rect,color,borderW):
		pg.draw.rect(self.display,color,rect,borderW)
	def setFullScreen(self):
		if not self.fullScreen:
			self.screen = pg.display.set_mode((0, 0),pg.FULLSCREEN)
			self.display = pg.Surface((gameSettings.WIDTH, gameSettings.HEIGHT))
			self.cHeight = self.screen.get_height()
			self.cWidth = self.screen.get_width()
			self.smallestSide = min(self.cWidth,self.cHeight)
			self.screenSurface = pg.Surface((self.cWidth,self.cHeight))
			self.fullScreen = True
		else:
			self.cWidth = gameSettings.WIDTH
			self.cHeight = gameSettings.HEIGHT
			self.screen = pg.display.set_mode((self.cWidth, self.cHeight))
			self.display = pg.Surface((self.cWidth, self.cHeight))
			self.fullScreen = False
	def showScreen(self):
		self.screen.fill((0,0,0))
		if self.fullScreen:
			pg.transform.scale(self.display,(self.cWidth,self.cHeight),self.screenSurface)
			self.screen.blit(self.screenSurface,
			(0,0))
		else:
			self.screen.blit(self.display,(0,0))
		pg.display.update()
