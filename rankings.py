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
	k1=50
	k2=50
	if winner.gamesplayed >= 10 and won == True:
		k1=30
	if loser.gamesplayed >= 10 and won == True:
		k1=30
	
	__eloCalc(winner,k1,loser,k2)
	saveRankings(playerlist)

# Applies Elo change to 1-on-1 participants based on the calculated delta and current constant (k value) for the participant 
# K value is larger for the first 10 games, then decreases. This causes players to arrive at their skill level faster
# Very private method, as it should only be called when a match is played
def __eloCalc(winner,k1,loser,k2):
		
	winner.setElo(winner.elo+k1*(1-winner.elo/(winner.elo+loser.elo)))
	loser.setElo(loser.elo+k2*(0-loser.elo/(winner.elo+loser.elo)))



	
