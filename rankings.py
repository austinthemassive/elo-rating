# Sorts player list by rankings, then prints the sorted rankings
def displayRankings(playerlist):
	import operator
	print("\nRank","Name","Elo","Games")
	rank = 1
	for player in sorted(playerlist, key=lambda player: player.elo, reverse=True):
		print(rank, player.getInfo())
		rank += 1

# Saves the player list
def saveRankings(playerlist):
	from write import writeplayers
	writeplayers(playerlist)

# Add a new player to rankings
# needs to prevent new players with same name as other players
def newPlayertoRanking(playerlist, name, elo, gamesplayed):
	playerlist.append(Player(name.lower(), elo, gamesplayed))

# Calculates elo delta and saves the rankings
def matchPlayed(playerlist,winner,loser,differential):
	import player
	if winner.elo >= loser.elo:
		delta = 1/(1+10**(winner.elo-int(loser.elo)/400))
	else:
		delta = 1/(1+10**(loser.elo-int(winner.elo)/400))
	__eloCalc(winner,delta,True)
	__eloCalc(loser,delta,False)
	saveRankings(playerlist)

# Applies Elo change to 1-on-1 participants based on the calculated delta and current constant (k value) for the participant 
# K value is 2.5x larger for the first 10 games, then decreases. This causes players to arrive at their skill level faster
# Very private method, as it should only be called when a match is played and a delta is calculated
def __eloCalc(participant,delta,won):
	if participant.gamesplayed <= 10 and won == True:
		participant.setElo(participant.elo+25*(1-delta))
		print(delta)
		# participant.elo += 25(1-delta)
	elif participant.gamesplayed >= 10 and won == True:
		participant.setElo(participant.elo+10*(1-delta))
		# participant.elo += 10(1-delta)
	elif participant.gamesplayed <= 10 and won == False:
		participant.setElo(participant.elo+25*(0-delta))
		print(delta)
		# participant.elo += 25(0-delta)
	elif participant.gamesplayed >= 10 and won == False:
		participant.setElo(participant.elo+10*(0-delta))
		# participant.elo += 10(0-delta)
	