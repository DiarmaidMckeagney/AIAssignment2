from Node import Node
from Colour import Colour
import random

# Agent class to represent each agent in the graph, which has a node and a next generation colour
class Agent:
    node = None
    nextGenColour = 1
    def __init__(self):
        self.node = Node()

    # Method to decide the next state for the agent based on the current state of its neighbours, for question 1
    def change_state(self, agentList):
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        # Create a list of the agent instances corresponding to the neighbours of this agent's node, based on the graph structure
        for n in modeNeighboursNum:
            modelNeighbours.append(agentList[n])

        numConflicts = 0
        neighbourColours = []
        # Count the number of conflicts (neighbours with the same colour) and create a list of the colours of the neighbours
        for i,agent in enumerate(modelNeighbours):
            if agent.node.getColour() == self.node.getColour():
                numConflicts += 1
            neighbourColours.append(agent.node.getColour())

        # If there are conflicts, try to change to a different colour that is not the same as the current colour and not used by any neighbours
        if numConflicts != 0:
            for i, colour in enumerate(Colour):
                if colour.value != self.node.getColour() and colour.value not in neighbourColours:
                    if random.random() < 0.75:
                        self.nextGenColour = colour.value
                    break

# Method to decide the next state for the agent based on the current state of its neighbours and the number of available colours, for question 2
    def change_state_q2(self, agentList, numColoursAvailable):
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        # Create a list of the agent instances corresponding to the neighbours of this agent's node, based on the graph structure
        for n in modeNeighboursNum:
            modelNeighbours.append(agentList[n])

        numConflicts = 0
        neighbourColours = []
        # Count the number of conflicts (neighbours with the same colour) and create a list of the colours of the neighbours
        for i,agent in enumerate(modelNeighbours):
            if agent.node.getColour() == self.node.getColour():
                numConflicts += 1
            neighbourColours.append(agent.node.getColour())

        # If there are conflicts, try to change to a different colour that is not used by any neighbours, and within the number of available colours
        if numConflicts != 0:
            for colour in range(1, numColoursAvailable + 1):
                if colour != self.node.getColour() and colour not in neighbourColours:
                    # Random chance added so that the agents won't flip between the same 2 colours repeatedly
                    if random.random() < 0.95:
                        self.nextGenColour = colour
                    break

# Method to update the current state of the agent's node to the next generation colour after all agents have decided their next state
    def move_to_next_gen(self):
        self.node.setColour(self.nextGenColour)