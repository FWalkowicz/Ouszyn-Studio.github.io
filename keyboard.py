import pygame as pg

#0 - left click
#1 - middle
#2 - right click
class keyboard(object):
	def init(self):
		self.holdedKeys=pg.key.get_pressed()
		self.lastKeys=pg.key.get_pressed()
		self.holdedMouse = pg.mouse.get_pressed()
		self.lastMouse = pg.mouse.get_pressed()
	def keyPresssed(self,key):
		if self.holdedKeys[key] and self.holdedKeys[key]!=self.lastKeys[key]:
			return True
		else:
			return False
	def keyReleased(self,key):
		if not self.holdedKeys[key] and self.holdedKeys[key]!=self.lastKeys[key]:
			return True
		else:
			return False
	def keyHold(self,key):
		if self.holdedKeys[key]:
			return True
		else:
			return False
	def getInput(self):
		self.holdedKeys=pg.key.get_pressed()
		self.holdedMouse = pg.mouse.get_pressed()
	def updateInput(self):
		self.lastKeys = self.holdedKeys
		self.lastMouse = self.holdedMouse
	def mouseHold(self,button): #button to jeden,dwa lub 3
		if not button in [0,1,2]:
			forceExitGame("argument mouseButton musi byc liczba 0,1 lub 2")
		if self.holdedMouse[button]:
			return True
		else:
			return False
	def mousePressed(self,button): #button to jeden,dwa lub 3
		if not button in [0,1,2]:
			forceExitGame("argument mouseButton musi byc liczba 0,1 lub 2")
		if self.holdedMouse[button] and self.holdedMouse[button]!=self.lastMouse[button]:
			return True
		else:
			return False
	def mouseReleased(self,button): #button to jeden,dwa lub 3
		if not button in [0,1,2]:
			forceExitGame("argument mouseButton musi byc liczba 0,1 lub 2")
		if not self.holdedMouse[button] and self.holdedMouse[button]!=self.lastMouse[button]:
			return True
		else:
			return False
	