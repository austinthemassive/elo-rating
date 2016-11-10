#!/usr/bin/python

'''
This is elo for foosball. Steps:
	Read file
	decode 64 bit?
	Create Objects
	Display rankings

	Enter winner
	Enter loser
	Enter score differential?
	Calculate elo delta (using gamesplayed and appropriate K value)
	(X) Apply elo delta
	

	Add player

	Reset season

	encode 64 bit?
	Write file
	Display Rankings


	
	

	include magnitude of the win? need to research
	include decay? Probably
'''

#player class

class Player:
	'''The default values for a new player should be elo = 1000 and gamesplayed = 0 '''
	def __init__(self, playername, elo, gamesplayed):
		self.playername = playername
		self.elo = elo
		self.gamesplayed = gamesplayed

	def subtractElo(delta):
		elo -= delta
		gamesplayed += 1

	def addElo(delta):
		elo += delta
		gamesplayed += 1
