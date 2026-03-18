
from matplotlib import pyplot as plt

from Agent import Agent

import networkx as nx
import Util


def initGraph(numNodes, edgeProbability):
    graph = nx.erdos_renyi_graph(numNodes, edgeProbability, seed=42)
    for i in range(numNodes):
        agent = Agent()
        Util.agentList.append(agent)


    return graph

def question1Flow():
    graph = initGraph(10, 0.3)

    for i in graph.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]

        Util.agentList_question1[nodeIndex].node.addNeighbours(list(neighbours.keys()))
    for agent in Util.agentList_question1:
        print(f"Node colour: {Util.Colour.fromInt(agent.node.getColour())}, Neighbours: {agent.node.getNeighbours()}")
    for i in range(150):
        print(f"\nGENERATION {i}\n")
        for agent in Util.agentList_question1:
            agent.change_state()

        for agent in Util.agentList_question1:
            agent.move_to_next_gen()

    colour_map = []
    for agent in Util.agentList_question1:
        colour_map.append(Util.Colour.fromInt(agent.node.getColour()))

    nx.draw(graph, with_labels=True, node_color=colour_map)
    plt.show()

def question2Flow():
    graph2 = initGraph(10, 0.3)

    for i in graph2.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]

        Util.agentList_question2[nodeIndex].node.addNeighbours(list(neighbours.keys()))
    for agent in Util.agentList_question2:
        print(f"Node colour: {Util.Colour.fromInt(agent.node.getColour())}, Neighbours: {agent.node.getNeighbours()}")
    for i in range(150):
        print(f"\nGENERATION {i}\n")
        for agent in Util.agentList_question2:
            agent.change_state()

        for agent in Util.agentList_question2:
            agent.move_to_next_gen()

    colour_map = []
    for agent in Util.agentList_question2:
        colour_map.append(Util.Colour.fromInt(agent.node.getColour()))

    nx.draw(graph2, with_labels=True, node_color=colour_map)
    plt.show()
if __name__ == "__main__":
    question1Flow()
    question2Flow()