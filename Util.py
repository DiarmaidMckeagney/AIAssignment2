from matplotlib import pyplot as plt
from Agent import Agent
import networkx as nx
from Colour import Colour

def initGraph(numNodes, edgeProbability, agentList):
    graph = nx.erdos_renyi_graph(numNodes, edgeProbability, seed=42)
    for i in range(numNodes):
        agent = Agent()
        agentList.append(agent)
    return graph

def initNeighbours(graph, agentList):
    for i in graph.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]
        agentList[nodeIndex].node.addNeighbours(list(neighbours.keys()))

def colourAndDrawGraph(graph, agentList):
    colour_map = []
    for agent in agentList:
        colour_map.append(Colour.fromInt(agent.node.getColour()))
    nx.draw(graph, with_labels=True, node_color=colour_map)
    plt.show()