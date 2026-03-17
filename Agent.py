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
        for i,node in enumerate(modelNeighbours):
            print(f"Neighbour {i} State = {self.node.getColour()}")
            if self.node.getColour() == self.node.getColour():
                numConflicts += 1
                conflictColours.append(self.node.getColour())
            else:
                conflictColours.append(self.node.getColour())

        if numConflicts != 0:
            gapFound = False
            for i, colour in enumerate(conflictColours):
                if colour != i+1:
                    self.node.setColour(i + 1)
                    gapFound = True
            if not gapFound:
                self.node.setColour(max(conflictColours) + 1)
            print("state Changed to:", self.node.getColour())