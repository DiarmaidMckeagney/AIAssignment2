from Node import Node
import Util
import random

class Agent:
    node = None
    nextGenColour = 1
    def __init__(self):
        self.node = Node()

    def change_state(self):
        print("state starts as:", self.node.getColour())
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        for n in modeNeighboursNum:
            modelNeighbours.append(Util.agentList[n])

        numConflicts = 0
        neighbourColours = []
        for i,agent in enumerate(modelNeighbours):
            print(f"Neighbour {i} State = {agent.node.getColour()}")
            if agent.node.getColour() == self.node.getColour():
                numConflicts += 1
            neighbourColours.append(agent.node.getColour())

        print(neighbourColours)
        if numConflicts != 0:
            for i, colour in enumerate(Util.Colour):
                if colour.value != self.node.getColour() and colour.value not in neighbourColours:
                    if random.random() < 0.75:
                        self.nextGenColour = colour.value
                    break



    def move_to_next_gen(self):
        if self.node.getColour() == self.nextGenColour:
            print("Stagnant Gen")
        else:
            print("state Changed to:", self.nextGenColour)
        self.node.setColour(self.nextGenColour)