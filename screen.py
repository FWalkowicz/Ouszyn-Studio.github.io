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
	def setFullScreen(self):
		if not self.fullScreen:
			self.cHeight = self.monitor_size[1]
			self.cWidth = self.monitor_size[0]
			self.screen = pg.display.set_mode((self.cWidth, self.cHeight),pg.FULLSCREEN)
			self.fullScreen = True
		else:
			self.cWidth = gameSettings.WIDTH
			self.cHeight = gameSettings.HEIGHT
			self.screen = pg.display.set_mode((self.cWidth, self.cHeight))
			self.fullScreen = False
	def showScreen(self):
		self.screen.blit(pg.transform.scale(self.display,(self.cWidth,self.cHeight)),(0,0))
		pg.display.update()
