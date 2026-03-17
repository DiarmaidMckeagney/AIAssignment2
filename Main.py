from enum import Enum
from Agent import Agent

import networkx as nx
import matplotlib.pyplot as plt
import Util

class Colour(Enum):
    Red = 1
    Blue = 2
    Green = 3
    Purple = 4
    Pink = 5
    Orange = 6
    Black = 7
    White = 8

    def fromInt(value):
        for colour in Colour:
            if colour.value == value:
                return colour
        raise ValueError(f"No colour with value {value}")


def initGraph(numNodes, edgeProbability):
    graph = nx.erdos_renyi_graph(numNodes, edgeProbability, seed=42)
    for i in range(numNodes):
        agent = Agent()
        Util.agentList.append(agent)


    return graph

if __name__ == "__main__":
    graph = initGraph(10, 0.3)

    for i in graph.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]

        Util.agentList[nodeIndex].node.addNeighbours(list(neighbours.keys()))

    for agent in Util.agentList:
        print(f"Node colour: {Colour.fromInt(agent.node.getColour())}, Neighbours: {agent.node.getNeighbours()}")

    nx.draw(graph, with_labels=True)
    plt.show()