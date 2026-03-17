from Node import Node
import Util


class Agent:
    node = None
    def __init__(self):
        self.node = Node()

    def change_state(self):
        print("state starts as:", self.node.getColour())
        modeNeighboursNum = self.node.getNeighbours()
        modelNeighbours = []
        for n in modeNeighboursNum:
            modelNeighbours.append(Util.agentList[n])

        numConflicts = 0
        conflictColours = []
        for agent in modelNeighbours:
            print(f"Neighbour {modelNeighbours.index(agent)} State = {agent.node.getColour()}")
            if self.node.getColour() == agent.node.getColour():
                numConflicts += 1
                conflictColours.append(agent.node.getColour())
            else:
                conflictColours.append(agent.node.getColour())

        if numConflicts != 0:
            gapFound = False
            for i, colour in enumerate(Util.Colour):
                if colour != self.node.getColour() and colour.value not in conflictColours:
                    self.node.setColour(colour.value)
                    gapFound = True
                    break
            if not gapFound:
                self.node.setColour(max(conflictColours) + 1)
            print("state Changed to:", self.node.getColour())