import pygame as pg
from pygame.locals import *
import sys
import os
from gameSettings import *
#kwadratowe animacje
class Animator(object):
	def __init__(self, animationFolderName,scaler = 1):
		self.animations = {}
		self.animDiv = 20
		self.cFrame = 0 
		self.currAnimation = []
		self.currAnimationName = ""
		self.baseAnimation = ""
		self.recentAnimation = ""
		self.isLooped = True
		print(os.getcwd())
		path  = os.path.join(Animations_PATH,animationFolderName)
		os.chdir(path)
		for directory in os.listdir():
			if not os.path.isdir(directory):
				forceExitGame("Blad w plikach w folderze " + path + "nie dodawaj tam obrazow cepie")
			os.chdir(directory)
			arr = []
			for image in os.listdir():
				im = loadify(image)
				arr.append(pg.transform.scale(im, (100 * scaler, 100*scaler)))
			self.animations[directory] = arr
			os.chdir("..")
		os.chdir("..")
		os.chdir("..")
		if not "idle" in self.animations:
			forceExitGame("nie ma base animacji idle")
		print("Ladowanie imagow ok")
		self.play("idle")
	def play(self,animationName,looped = True):
		if not animationName in self.animations: 
			forceExitGame("animacja "+ animationName+" nie zostala wczytana do tablicy")
		if animationName==self.currAnimationName: #jezeli jest juz grana ta sama animacja nie resetuj jej
			return
		if not looped and self.isLooped:
			self.baseAnimation = animationName
		self.isLooped = looped
		self.currAnimation = self.animations[animationName]
		self.currAnimationName = animationName
		self.cFrame = 0
	def animationEnded(self,animationName):
		if self.recentAnimation!= animationName and self.currAnimation!=animationName:
			print("Ani obecna ani poprzedna animacja nie jest ta oczekiwana ktora ma sie zakonczyc")
			return False
		if self.recentAnimation==animationName and self.currAnimation!=animationName:
			return True
		else:
			print("Animacja "+animationName+" jeszcze sie nie skonczyla")
			return False
	def isPlaying(self,animationName):
		if self.currAnimation == animationName:
			return True
		else:
			return False
	def currentFrame(self):
		self.cFrame+=1
		if self.cFrame//self.animDiv > len(self.currAnimation)-1 and self.isLooped:
			self.cFrame = 0
		elif self.cFrame//self.animDiv > len(self.currAnimation)-1 and not self.isLooped:
			self.recentAnimation = self.currAnimation
			self.play(self.baseAnimation)
		return self.currAnimation[self.cFrame//self.animDiv]




