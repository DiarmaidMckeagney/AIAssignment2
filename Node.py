import random

# Node class to represent each node in the graph, which has a colour and a list of neighbours
class Node:
    colour = None
    neighbours = None

    # Initialize the node with a random colour (1 or 2) and an empty list of neighbours
    def __init__(self):
        self.colour = random.randint(1,2)
        self.neighbours = []

    # Method to add a single neighbour to the node's list of neighbours
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    # Method to add multiple neighbours to the node's list of neighbours
    def addNeighbours(self, neighbours):
        self.neighbours += neighbours

    # Method to get the list of neighbours for the node
    def getNeighbours(self):
        return self.neighbours

    # Method to set the colour of the node
    def setColour(self, colour):
        self.colour = colour
    
    # Method to get the current colour of the node
    def getColour(self):
        return self.colour
    