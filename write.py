from player import *

# initialize the file (clearing old data)
def _initializePlayerFile(filename):
	file = open(filename,"w")
	file.write("Player List")
	file.close()

# append player data to newly initialized file
def writeplayers(listofplayers):
	filename = "users.txt"
	_initializePlayerFile(filename)
	file = open(filename,"a")

	for player in listofplayers:
		line = "\n"
		for attribute in list(player.getInfo()):
			line += str(attribute)
			line += "/"
		file.write(line)

	file.close()