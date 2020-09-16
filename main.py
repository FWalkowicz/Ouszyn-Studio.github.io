import os
from player import * 
from gameSettings import *
from plat import *
from Camera import *
#bedzie przechowywac gracza,wszystkie moby stwory etc
class Game(object):
	def __init__(self):
		pg.init()
		self.monitor_size = [pg.display.Info().current_w, pg.display.Info().current_h]
		self.cWidth = WIDTH
		self.cHeight = HEIGHT
		self.screen = pg.display.set_mode((self.cWidth, self.cHeight))
		pg.display.set_caption(TITLE)
		pg.mouse.set_visible(1)
		self.background = loadify("tlo.jpg")
		self.background = pg.transform.scale(self.background, (self.cWidth, self.cHeight))
		self.clock = pg.time.Clock()
		self.running = True
		self.camera = Camera()
		self.display = pg.Surface((WIDTH,HEIGHT))
		self.fullscreen = False
		print(self.monitor_size[0])

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
					if not self.fullscreen:
						self.cHeight = self.monitor_size[1]
						self.cWidth = self.monitor_size[0]
						self.screen = pg.display.set_mode((self.cWidth, self.cHeight),pg.FULLSCREEN)
						self.fullscreen = True
					else:
						self.cWidth = WIDTH
						self.cHeight = HEIGHT
						self.screen = pg.display.set_mode((self.cWidth, self.cHeight))
						self.fullscreen = False
					#self.display = pg.Surface((self.cWidth, self.cHeight))
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
			self.clock.tick(60)
	def update(self):
		self.player.handleMovment()
		self.player.checkColision(self.platforms)
	def drawScrolled(self):

		for sprite in self.all_sprites:
			self.display.blit(sprite.image,(sprite.rect.x-self.camera.pos.x,sprite.rect.y-self.camera.pos.y))

	def draw(self):
		self.camera.moveCameraTo(self.player.pos)
		self.screen.fill(BLACK)
		self.display.blit(self.background, (0, 0))
		self.display.blit(self.player.currFrame,(self.player.pos.x-self.camera.pos.x-self.player.rect.width/2,self.player.pos.y - self.camera.pos.y-self.player.rect.height ))
		self.drawScrolled()
		self.screen.blit(pg.transform.scale(self.display,(self.cWidth,self.cHeight)),(0,0))
		pg.display.update()
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



