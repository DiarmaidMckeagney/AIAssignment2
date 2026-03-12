from random import randint

class Node:
    colour = None
    neighbours = []

    def __init__(self, chromaticNum):
        self.colour = randint(1, chromaticNum)

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def getNeighbours(self):
        return self.neighbours

    def setColour(self, colour):
        self.colour = colour
    
    def getColour(self):
        return self.colour
    