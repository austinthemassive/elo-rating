#!/usr/bin/python

import read
from player import *

# Sorts player list by rankings, then prints the sorted rankings
def displayRankings(playerlist):
	import operator
	print("Rank","Name","Elo","Games")
	rank = 1
	for player in sorted(playerlist, key=lambda player: player.elo, reverse=True):
		print(rank, player.getInfo())
		rank += 1

# Saves the player list
def saveRankings(playerlist):
	from write import writeplayers
	writeplayers(playerlist)

# Add a new player
def newPlayer(name, elo, gamesplayed):
	playerlist.append(Player(name, elo, gamesplayed))

#want to turn into a main method
playerlist = list(read.readplayers())

displayRankings(playerlist)

saveRankings(playerlist)


'''
This is elo for foosball. Steps:
		(X) Read file
		(X) Create Objects
		(X) Display rankings

	Enter winner
	Enter loser
	Enter score differential?
	Calculate elo delta (using gamesplayed and appropriate K value)
		(X) Apply elo delta
	

		(X) Add player
		(X) Record list of participants, wins losses
		(X) Write file



	Reset season
	keep a running history
	ability to see the record between 2 players

	handle 4 player stuff?

	include magnitude of the win? need to research
	include decay? Probably
'''


