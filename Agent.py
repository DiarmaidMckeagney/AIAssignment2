import random


class Agent:
    node = None
    chromaticNumber = 1
    def __init__(self, node, chromatic_number):
        self.node = node
        self.chromaticNumber = chromatic_number

    def change_state(self):
        nodeNeighbours = self.node.getNeighbours()
        numConflicts = 0
        conflictColours = []
        for node in nodeNeighbours:
            if node.getColour() == self.node.getColour():
                numConflicts += 1
                conflictColours.append(node.getColour())
            else:
                conflictColours.append(node.getColour())

        if numConflicts != 0:
            self.node.setColour(random.randint(1,self.chromaticNumber) not in conflictColours)