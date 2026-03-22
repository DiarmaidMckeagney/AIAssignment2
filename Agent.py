from Node import Node
from Colour import Colour
import random

class Agent:
    node = None
    nextGenColour = 1
    def __init__(self):
        self.node = Node()

    def change_state(self, agentList):
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        for n in modeNeighboursNum:
            modelNeighbours.append(agentList[n])

        numConflicts = 0
        neighbourColours = []
        for i,agent in enumerate(modelNeighbours):
            if agent.node.getColour() == self.node.getColour():
                numConflicts += 1
            neighbourColours.append(agent.node.getColour())

        if numConflicts != 0:
            for i, colour in enumerate(Colour):
                if colour.value != self.node.getColour() and colour.value not in neighbourColours:
                    if random.random() < 0.75:
                        self.nextGenColour = colour.value
                    break

    def change_state_q2(self, agentList, numColoursAvailable):
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        for n in modeNeighboursNum:
            modelNeighbours.append(agentList[n])

        numConflicts = 0
        neighbourColours = []
        for i,agent in enumerate(modelNeighbours):
            if agent.node.getColour() == self.node.getColour():
                numConflicts += 1
            neighbourColours.append(agent.node.getColour())

        if numConflicts != 0:
            for colour in range(1, numColoursAvailable + 1):
                if colour != self.node.getColour() and colour not in neighbourColours:
                    if random.random() < 0.95:
                        self.nextGenColour = colour
                    break

    def move_to_next_gen(self):
        self.node.setColour(self.nextGenColour)