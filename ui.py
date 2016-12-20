#!/usr/bin/python

from pygame import *
import random
import math

# set up the screen
windowWidth = 600
windowHeight = 600
backgroundcolor = (150,150,150)
screen = display.set_mode((windowWidth,windowHeight))
screen.fill(backgroundcolor)
display.set_caption('UI experiments')

gravity = (math.pi,.001)

# Particle Class
class Particle:
	color = (0,0,255)
	thickness = 1
	angle = 0
	speed = 0
	drag = 0
	elasticity = 0
	
	def __init__(self,x,y,size):
		self.x = x
		self.y = y
		self.size = size
		# self.speed = random.random()
		self.speed = random.uniform(0,1)
		self.angle = random.uniform(0,2*math.pi)
		self.elasticity = .75
		self.drag = .9999999999

	
	def display(self, screen1):
		# draw the circle using these characteristics
		draw.circle(screen1, self.color, (int(self.x),int(self.y)),self.size, self.thickness)

	def move(self):
		#factor in gravity's vector
		(self.angle, self.speed) = self.addVectors(self.angle,self.speed,gravity[0], gravity[1])
		
		#move shape accordingly
		self.x += math.sin(self.angle)*self.speed
		self.y -= math.cos(self.angle)*self.speed
		
		#simulate drag according to shape size
		self.speed *= (1-self.size/1000000000)

	def fling(self,mouseAngle,mouseSpeed):
		#factor in mouse fling vector
		(self.angle, self.speed) = self.addVectors(self.angle,self.speed,mouseAngle,mouseSpeed)
		
		#move shape accordingly
		self.x += math.sin(self.angle)*self.speed
		self.y -= math.cos(self.angle)*self.speed
		
		#simulate drag according to shape size
		self.speed *= (1-self.size/1000000000)

	def addVectors(self,angle1,length1,angle2,length2):
			tempx = math.sin(angle1)*length1+math.sin(angle2)*length2
			tempy = math.cos(angle1)*length1+math.cos(angle2)*length2
			length = math.hypot(tempx,tempy)
			angle = .5*math.pi-math.atan2(tempy,tempx)
			return (angle, length)

# draws circles
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

#prevent circles from being drawn on top of each other or inside each other when created
def _overlap(x,y,size,ListofParticles):
	for particle in ListofParticles:
		greaterX = _compareX(particle.x, x)
		greaterY = _compareY(particle.y, y)
		x_distance = _calculateDistance(greaterX,particle.x,x)
		y_distance = _calculateDistance(greaterY,particle.y,y)
		if _hypotenuse(particle.size,size,x_distance,y_distance) == True:
			continue
		else:
			#if shapes overlap, returns true (to continue previous loop)
			return True

	#if no shapes overlap, return overlap will return false (to exit previous loop)
	return False

# calculate the hypotenuse distance between object 1 and object 2 (to determine if overlapping)
def _hypotenuse(radius1,radius2,x_distance,y_distance):
	hypotenuse = math.sqrt(x_distance**2+y_distance**2)
	if hypotenuse >= (radius1+radius2):
		#return true if not overlapping
		return True
	else:
		#return false if overlapping
		return False	

# calculate the distance between x,y of shape 1 and x,y of shape 2. Could be simplified or omitted with abs()
def _calculateDistance(greaterVAR,var1,var2):	
		if greaterVAR == 1:
			var_distance = var1 - var2
		elif greaterVAR == -1:
			var_distance = var2 - var1
		elif greaterVAR == 0:
			var_distance = 0
		return var_distance
		
# compares x values to see which is greater. Could be combined with _compareY or refactor code to remove
def _compareX(x1, x2):
	if x1 > x2:
		return 1
	elif x1 < x2:
		return -1
	elif x1 == x2:
		return 0

#compares y values to see which is greater. could be combined with _compareX
def _compareY(y1, y2):
	if y1 > y2:
		return 1
	elif y1 < y2:
		return -1
	elif y1 == y2:
		return 0	

# makes the walls "hard" and "elastic" so they reflect forces
def hardWall(windowWidth, windowHeight, particle):
	#handle x
	if particle.x > windowWidth-particle.size:
		particle.x = 2*(windowWidth - particle.size) - particle.x
		particle.angle = -particle.angle
		particle.speed *= particle.elasticity
	elif particle.x < particle.size:
		particle.x = 2*(particle.size) - particle.x
		particle.angle = -particle.angle
		particle.speed *= particle.elasticity
	#handle y
	if particle.y > windowHeight-particle.size:
		particle.y = 2*(windowHeight - particle.size) - particle.y
		particle.angle = math.pi-particle.angle
		particle.speed *= particle.elasticity
	elif particle.y < particle.size:
		particle.y = 2*(particle.size) - particle.y
		particle.angle = math.pi-particle.angle
		particle.speed *= particle.elasticity

def selectParticle(particleList,xMouse,yMouse):
	for particle in particleList:
		if math.hypot(particle.x-xMouse, particle.y-yMouse) <= particle.size:
			return particle
	return None

def collision(particle1,particle2):
	deltaX = particle1.x-particle2.x
	deltaY = particle1.y-particle2.y
	distance = math.hypot(deltaX,deltaY)
	if distance < particle1.size + particle2.size:
		tangent = math.atan2(deltaY,deltaX)
		particle1.angle = 2*tangent-particle1.angle
		particle2.angle = 2*tangent-particle1.angle
		particle1.speed,particle2.speed = particle2.speed,particle1.speed

		#move the particles away from each other so they don't stick
		tempAngle = .5*math.pi+tangent
		particle1.x += math.sin(tempAngle)
		particle1.y -= math.cos(tempAngle)
		particle2.x -= math.sin(tempAngle)
		particle2.y += math.cos(tempAngle)

#randomly generate a certain number of particles
particleList = randomCircles(screen, 3, windowWidth, windowHeight)
selected_Particle=None
running = True
while running:
	screen.fill(backgroundcolor)
	for i, particle in enumerate(particleList):
		if particle != selected_Particle:
			particle.move()
			hardWall(windowWidth,windowHeight,particle)
			for second_particle in particleList[i+1:]:
				collision(particle, second_particle)
		particle.display(screen)
	display.flip()
	for occurence in event.get():
		if occurence.type == QUIT:
			running = False
		if occurence.type == MOUSEBUTTONDOWN:
			(xMouse,yMouse) = mouse.get_pos()
			selected_Particle = selectParticle(particleList,xMouse,yMouse)
		if occurence.type == MOUSEBUTTONUP:
			(xMouseMoved,yMouseMoved) = mouse.get_pos()
			if selected_Particle != None:
				mouseSpeed = math.hypot(xMouseMoved-xMouse,yMouseMoved-yMouse)
				mouseAngle = math.atan((xMouseMoved-xMouse)/(yMouseMoved-yMouse))
				selected_Particle.fling(mouseAngle,mouseSpeed/80)

			selected_Particle = None
