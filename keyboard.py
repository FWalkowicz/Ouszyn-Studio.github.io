import pygame as pg


class keyboard(object):
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
			