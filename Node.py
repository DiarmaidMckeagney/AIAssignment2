import random


class Node:
    colour = None
    neighbours = None

    def __init__(self):
        self.colour = random.randint(1,2)
        self.neighbours = []

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def addNeighbours(self, neighbours):
        self.neighbours += neighbours

    def getNeighbours(self):
        return self.neighbours

    def setColour(self, colour):
        self.colour = colour
    
    def getColour(self):
        return self.colour
    