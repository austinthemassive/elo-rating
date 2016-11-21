#!/usr/bin/python

from pygame import *
import random

class Particle:
	color = (0,0,255)
	thickness = 1
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.size = size
		# self.color = (0,0,255)
		# self.thickness = 1

	def display(self, screen1):
		draw.circle(screen1, self.color, (self.x,self.y),self.size, self.thickness)

def randomCircles(screen, numberofcircles, width, height):
	for n in range(numberofcircles):
		size = random.randint(5,25)
		x = random.randint(size,width-size)
		y = random.randint(size,height-size)
		newparticle = Particle(x,y,size)
		newparticle.display(screen)

#set up the screen
width = 400
height = 250
backgroundcolor = (150,150,150)
screen = display.set_mode((width,height))
screen.fill(backgroundcolor)
display.set_caption('Foosball Elo')

# #draw a circle at these coordinates and this size
# myparticle = Particle(150,50,50)
# myparticle.display(screen)

#randomly generate 10 particles
randomCircles(screen, 10, width, height)

display.flip()

running = True
while running:
	for occurence in event.get():
		if occurence.type == QUIT:
			running = False

