#!/usr/bin/python

from pygame import *
import random
import math

class Particle:
	color = (0,0,255)
	thickness = 1
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.size = size

	def display(self, screen1):
		draw.circle(screen1, self.color, (self.x,self.y),self.size, self.thickness)


def randomCircles(screen, numberofparticles, width, height):
	ListofParticles = []
	for n in range(numberofparticles):
		boolean = True
		while boolean:
			size = random.randint(5,25)
			x = random.randint(size,width-size)
			y = random.randint(size,height-size)

			#compare
			boolean = _overlap(x,y,size,ListofParticles)
			print(boolean) #boolean is returning None

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
		# if greaterX == 1 and greaterY == 1 and _hypotenuse(particle.size,size,x_distance,y_distance) == True:
		# 	continue
		# elif greaterX == 1 and greaterY == 0 and _hypotenuse(particle.size,size,x_distance,y_distance) == True:
		# 	continue
		# elif greaterX == 1 and greaterY == -1:
		# 	continue
		# elif greaterX == 0 and greaterY == 1:
		# 	continue
		# elif greaterX == 0 and greaterY == 0:
		# 	boolean = True
		# 	break
		# elif greaterX == 0 and greaterY == -1:
		# 	continue
		# elif greaterX == -1 and greaterY == 1:
		# 	continue
		# elif greaterX == -1 and greaterY == 0:
		# 	continue
		# elif greaterX == -1 and greaterY == -1:
		# 	continue
		else:
			return True

		#if no shapes overlap, return overlap will return false (to exit previous loop)
		return False

def _hypotenuse(radius1,radius2,x_distance,y_distance):
	hypotenuse = math.sqrt(x_distance**2+y_distance**2)
	print("\nhypotenuse: ",hypotenuse)
	print("added radius",radius1+radius2)
	if hypotenuse >= (radius1+radius2):
		#return true if not overlapping
		return True
	else:
		# print("****************************************")
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

#set up the screen
width = 400
height = 250
backgroundcolor = (150,150,150)
screen = display.set_mode((width,height))
screen.fill(backgroundcolor)
display.set_caption('UI experiments')

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

