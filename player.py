#player class

class Player(object):
	'''The default values for a new player should be elo = 1000 and gamesplayed = 0 '''
	def __init__(self, playername, elo, gamesplayed):
		self.playername = str(playername)
		self.elo = int(elo)
		self.gamesplayed = int(gamesplayed)

	def subtractElo(self,delta):
		self.elo -= delta
		self.gamesplayed += 1

	def addElo(self,delta):
		self.elo += delta
		self.gamesplayed += 1

	def getInfo(self):
		import math
		list1 = [self.playername,math.floor(self.elo),self.gamesplayed]
		return list1

	def getElo(self):
		return self.elo

	def setElo(self,elo):
		self.elo = elo
		self.gamesplayed += 1