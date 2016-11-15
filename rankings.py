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

# Add a new player to rankings
def newPlayertoRanking(playerlist, name, elo, gamesplayed):
	playerlist.append(Player(name, elo, gamesplayed))

