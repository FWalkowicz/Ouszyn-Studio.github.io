import os
from player import * 
from gameSettings import *
from plat import *
from Camera import *
#bedzie przechowywac gracza,wszystkie moby stwory etc
class Game(object):
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		pg.display.set_caption(TITLE)
		pg.mouse.set_visible(1)
		self.background = self.loadify("tlo.jpg")
		self.background = pg.transform.scale(self.background, (WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		self.running = True
		self.camera = Camera()
		self.display = pg.Surface((WIDTH,HEIGHT))
	def loadify(self,img):
		return pg.image.load(img).convert_alpha()

	def addEntity(self,entity):
		self.all_sprites.add(entity)
		self.entities.append(entity)
	def addPlatform(self,platform):
		self.all_sprites.add(platform)
		self.platforms.add(platform)
	def events(self):
		for event in pg.event.get():
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
	def update(self):
		self.player.handleMovment()
		self.player.checkColision(self.platforms)
	def drawScrolled(self):

		for sprite in self.all_sprites:
			self.display.blit(sprite.image,(sprite.rect.x-self.camera.pos.x,sprite.rect.y-self.camera.pos.y))

	def draw(self):
		self.camera.copyPos(self.player.pos)
		self.screen.fill(BLACK)
		self.display.blit(self.background, (0, 0))
		self.display.blit(self.player.image,(self.player.pos.x-self.camera.pos.x-self.player.rect.width/2,self.player.pos.y - self.camera.pos.y-self.player.rect.height ))
		self.drawScrolled()
		self.screen.blit(pg.transform.scale(self.display,(WIDTH,HEIGHT)),(0,0))
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



