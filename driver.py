#!/usr/bin/python

import read
import rankings
from player import *


#want to turn into a main method
playerlist = list(read.readplayers())

rankings.displayRankings(playerlist)

while True:
	selection = input("\nInput the winner of a match (ex 'Austin') or say 'display rankings' ")
	if selection.lower() == "display rankings":
		displayRankings(playerlist)
	else:
		for player1 in playerlist:
			if selection.lower() == player1.playername.lower():
				loser = input("\nInput the loser of the match (ex 'Giuseppe') ")
				for player2 in playerlist:
					if loser.lower() == player2.playername.lower():
						differential = input("\nInput score differential (ex if the score is 3-1 enter '2' ")
						rankings.matchPlayed(playerlist,player1,player2,differential)
	rankings.displayRankings(playerlist)

saveRankings(playerlist)


'''
This is elo for foosball. Steps:
		(X) Read file
		(X) Create Objects
		(X) Display rankings

		(X) Enter winner
		(X) Enter loser
		(X) Enter score differential?
	Calculate elo delta (using gamesplayed and appropriate K value)
	handle 2 on 2
	handle 1 on 1 on 1 on 1
		(X) Apply elo delta
	

		(X) Add player
		(X) Write file


	prevent new players of the same name
	Reset season
	keep a running history
	ability to see the record between 2 players

	handle 4 player stuff?

	include magnitude of the win? need to research
	include decay? Probably
'''


