#!/usr/bin/python

from pygame import *
import random
import math

class Particle:
	color = (0,0,255)
	thickness = 1
	angle = 0
	speed = 0
	
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.size = size
		# self.speed = random.random()
		self.speed = random.uniform(0,.003)
		self.angle = random.uniform(0,2*math.pi)

	def display(self, screen1):
		draw.circle(screen1, self.color, (int(self.x),int(self.y)),self.size, self.thickness)

	def move(particle):
		particle.x += math.sin(particle.angle)*particle.speed
		particle.y += math.cos(particle.angle)*particle.speed

def randomCircles(screen, numberofparticles, width, height):
	ListofParticles = []
	for n in range(numberofparticles):
		boolean = True
		while boolean:
			size = random.randint(5,25)
			x = random.randint(size,width-size)
			y = random.randint(size,height-size)
			boolean = _overlap(x,y,size,ListofParticles)

		newparticle = Particle(x,y,size)
		newparticle.display(screen)
		ListofParticles.append(newparticle)

	return ListofParticles

def _overlap(x,y,size,ListofParticles):
	for particle in ListofParticles:
		greaterX = _compareX(particle.x, x)
		greaterY = _compareY(particle.y, y)
		x_distance = _calculateDistance(greaterX,particle.x,x)
		y_distance = _calculateDistance(greaterY,particle.y,y)
		if _hypotenuse(particle.size,size,x_distance,y_distance) == True:
			continue
		else:
			return True

	#if no shapes overlap, return overlap will return false (to exit previous loop)
	return False

def _hypotenuse(radius1,radius2,x_distance,y_distance):
	hypotenuse = math.sqrt(x_distance**2+y_distance**2)
	if hypotenuse >= (radius1+radius2):
		#return true if not overlapping
		return True
	else:
		#return false if overlapping
		return False	

def _calculateDistance(greaterVAR,var1,var2):	
		if greaterVAR == 1:
			var_distance = var1 - var2
		elif greaterVAR == -1:
			var_distance = var2 - var1
		elif greaterVAR == 0:
			var_distance = 0
		return var_distance
		
def _compareX(x1, x2):
	if x1 > x2:
		return 1
	elif x1 < x2:
		return -1
	elif x1 == x2:
		return 0

def _compareY(y1, y2):
	if y1 > y2:
		return 1
	elif y1 < y2:
		return -1
	elif y1 == y2:
		return 0	

def hardWall(windowWidth, windowHeight, particle):
	if particle.x > windowWidth-particle.size:
		particle.x = 2*(windowWidth - particle.size) - particle.x
	elif particle.x < particle.size:
		particle.x = 2*(particle.size) - particle.x

	if particle.y > windowHeight-particle.size:
		particle.y = 2*(windowHeight - particle.size) - particle.y
	elif particle.y < particle.size:
		particle.y = 2*(particle.size) - particle.y

#set up the screen
windowWidth = 400
windowHeight = 250
backgroundcolor = (150,150,150)
screen = display.set_mode((windowWidth,windowHeight))
screen.fill(backgroundcolor)
display.set_caption('UI experiments')

#randomly generate 10 particles
particleList = randomCircles(screen, 10, windowWidth, windowHeight)

running = True
while running:
	screen.fill(backgroundcolor)
	for particle in particleList:
		# particle.speed = random.random()
		# particle.angle = random.uniform(0,2*math.pi)
		particle.move()
		hardWall(windowWidth,windowHeight,particle)
		particle.display(screen)
	display.flip()
	for occurence in event.get():
		if occurence.type == QUIT:
			running = False

