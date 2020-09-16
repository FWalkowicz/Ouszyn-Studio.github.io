import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *

class Animator(object):
	def __init__(self, animationFolderName):
		self.animations = {}
		self.animDiv = 60
		self.cFrame = 0 
		self.currAnimation = []
		self.currAnimationName = ""
		path  = Animations_PATH+"/"+animationFolderName
		os.chdir(path)
		for directory in os.listdir():
			if not os.path.isdir(directory):
				forceExitGame("Blad w plikach w folderze " + path + "nie dodawaj tam obrazow cepie")
			os.chdir(directory)
			arr = []
			for image in os.listdir():
				im = loadify(image)
				arr.append(pg.transform.scale(im, (100, 100)))
			self.animations[directory] = arr
			os.chdir("..")
		os.chdir("..")
		if not "idle" in self.animations:
			forceExitGame("nie ma base animacji idle")
		print("Ladowanie imagow ok")
	def play(self,animationName):
		if not animationName in self.animations: 
			forceExitGame("animacja "+ animationName+" nie zostala wczytana do tablicy")
		if animationName==self.currAnimationName: #jezeli jest juz grana ta sama animacja nie resetuj jej
			return
		self.currAnimation = self.animations[animationName]
		self.currAnimationName = animationName
		self.cFrame = 0
	def currentFrame(self):
		self.cFrame+=1
		if self.cFrame//self.animDiv > len(self.currAnimation)-1:
			self.cFrame = 0
		return self.currAnimation[self.cFrame//self.animDiv]




