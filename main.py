import pygame as pg
import os
import player
from gameSettings import *
import plat
from Camera import *

#bedzie przechowywac gracza,wszystkie moby stwory etc
class Game(object):
	def __init__(self):
		pg.init()
		SCREEN.init()
		pg.display.set_caption(TITLE)
		pg.mouse.set_visible(1)
		self.background = loadify("tlo.jpg")
		self.background = pg.transform.scale(self.background, (SCREEN.cWidth, SCREEN.cHeight))
		self.clock = pg.time.Clock()
		self.running = True
		self.camera = Camera()
		self.fullscreen = False		

	def addEntity(self,entity):
		self.all_sprites.add(entity)
		self.entities.append(entity)
	def addPlatform(self,platform):
		self.all_sprites.add(platform)
		self.platforms.add(platform)
	def events(self):
		for event in pg.event.get():
			if event.type == KEYDOWN:
				if event.key == K_f:
						SCREEN.setFullScreen()
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
			self.running = False

	def run(self):
		self.playing = True
		while self.playing:
			self.events()
			self.update()
			self.draw()
			self.clock.tick(120)
	def update(self):
		self.player.handleMovment()
		self.player.checkColision(self.platforms)
	def drawScrolled(self):

		for sprite in self.all_sprites:
			SCREEN.drawOnDisplay(sprite.image,(sprite.rect.x-self.camera.pos.x,sprite.rect.y-self.camera.pos.y))

	def draw(self):
		self.camera.moveCameraTo(self.player.pos)
		SCREEN.drawOnDisplay(self.background, (0, 0))
		self.drawScrolled()
		SCREEN.drawOnDisplay(self.player.currFrame,(self.player.pos.x-self.camera.pos.x-self.player.rect.width/2,self.player.pos.y - self.camera.pos.y-self.player.rect.height ))
		SCREEN.showScreen()
	def initNewGame(self):
		self.entities = []
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group() #z platformami sie koliduje 
		self.player = Player()
		self.addPlatform(Platform(-100, 1000, 2200, 40))
		self.addPlatform(Platform(500, 500, 200, 200))
		self.addPlatform(Platform(-100, 100, 1200, 40))
		self.run()
	def show_start_screen(self):
	# game splash/start screen
		pass
		
	def show_go_screen(self):
	# game over/continue
		pass

g = Game()
g.show_start_screen()
while g.running:
    g.initNewGame()
    g.show_go_screen()

pg.quit()



