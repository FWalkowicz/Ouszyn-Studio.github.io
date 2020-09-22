import pygame as pg
import os
import player
from gameSettings import *
import plat
from Camera import *
from collider import *
from enemy import *
#bedzie przechowywac gracza,wszystkie moby stwory etc
class Game(object):
	def __init__(self):
		pg.init()
		SCREEN.init()
		KEYBOARD.init()
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
	def addCollidable(self,platform):
		self.all_sprites.add(platform)
		self.collidable.add(platform)
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
			KEYBOARD.getInput()
			self.events()
			self.update()
			self.draw()
			self.clock.tick(120)
			KEYBOARD.updateInput()
	def update(self):
		self.player.handleMovment(self.camera)
		self.player.checkColision(self.collidable)
	def drawEnviroment(self):
		for sprite in self.all_sprites:
			SCREEN.drawOnDisplay(sprite.image,(sprite.rect.x-self.camera.pos.x,sprite.rect.y-self.camera.pos.y))

	def draw(self):
		self.camera.moveCameraTo(self.player.pos)
		SCREEN.drawOnDisplay(self.background, (0, 0))
		self.drawEnviroment()	
		SCREEN.drawOnDisplay(self.player.currFrame,self.player.getAbsLeftTop(self.camera.pos))
		self.player.drawCollider(self.camera.pos)
		self.entities[0].drawCollider(self.camera.pos)	
		SCREEN.showScreen()
	def initNewGame(self):
		self.entities = []
		self.all_sprites = pg.sprite.Group()
		self.collidable = pg.sprite.Group() #z platformami sie koliduje 
		self.player = Player(0,0,cW=100,cH=100)
		self.addEntity(Enemy(0,0))
		self.addCollidable(Platform(-100, 1000, 2200, 40))
		self.addCollidable(Platform(500, 500, 200, 200))
		self.addCollidable(Platform(-100, 100, 1200, 40))
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



