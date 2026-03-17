from Agent import Agent

import networkx as nx
import matplotlib.pyplot as plt
import Util


def initGraph(numNodes, edgeProbability):
    graph = nx.erdos_renyi_graph(numNodes, edgeProbability, seed=42)
    for i in range(numNodes):
        agent = Agent()
        Util.agentList.append(agent)

    return graph

def initNeighbours(graph):
    for i in graph.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]

        Util.agentList[nodeIndex].node.addNeighbours(list(neighbours.keys()))

if __name__ == "__main__":
    graph = initGraph(10, 0.3)
    initNeighbours(graph)

    # Main loop
    for i in range(10) :
        for agent in Util.agentList:
            agent.change_state()


    # Print final states and visualise graph
    for agent in Util.agentList:
        print(f"Node {Util.agentList.index(agent)} colour: {Util.Colour.fromInt(agent.node.getColour())}, in final state")

    pos = nx.circular_layout(graph)
    colour_map = Util.colour_Graph_Nodes(Util.agentList, graph)

    chromaticNum = nx.greedy_color(graph, strategy="largest_first")
    chromaticNum = max(chromaticNum.values()) + 1
    print(f"Chromatic number of the graph: {chromaticNum}")

    nx.draw(graph, with_labels=True, node_color=colour_map, pos=pos)
    plt.show()