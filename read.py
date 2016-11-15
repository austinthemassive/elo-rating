#!/usr/bin/python

import player
from player import Player

#	Read file
def readplayers():
	filename = "users.txt"
	file = open(filename,"r")
	playerlist = []

	#	Create Objects
	first = True
	for line in file:
		if first == True:
			first = None
			continue
		else:
			playerinfo = line.split('/')
			playerlist.append(Player(str(playerinfo[0]),playerinfo[1],playerinfo[2]))

	#close the file, return the list
	file.close()
	return playerlist


