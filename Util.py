from matplotlib import pyplot as plt
from Agent import Agent
import networkx as nx
from Colour import Colour

# Utility functions for initializing the graph, setting up the neighbours, and colouring/drawing the graph
def initGraph(numNodes, edgeProbability, agentList):
    # Create a random graph using the Erdős-Rényi model, where each edge is included with a certain probability
    graph = nx.erdos_renyi_graph(numNodes, edgeProbability, seed=42)
    # Initialize the agent list with Agent instances corresponding to each node in the graph
    for i in range(numNodes):
        agent = Agent()
        agentList.append(agent)
    return graph

# Function to initialize the neighbours for each agent based on the graph structure
def initNeighbours(graph, agentList):
    # Iterate through the adjacency list of the graph and set the neighbours for each agent's node based on the graph's edges
    for i in graph.adjacency():
        nodeIndex = i[0]
        neighbours = i[1]
        agentList[nodeIndex].node.addNeighbours(list(neighbours.keys()))

# Function to colour the graph based on the agents' node colours and draw it using Matplotlib
def colourAndDrawGraph(graph, agentList):
    colour_map = []
    # Create a colour map for the nodes based on the current colour of each agent's node, and then draw the graph with these colours
    for agent in agentList:
        colour_map.append(Colour.fromInt(agent.node.getColour()))
    pos = nx.circular_layout(graph)
    # Draw the graph with labels and the specified node colours, and then display it
    nx.draw(graph, with_labels=True, node_color=colour_map, pos=pos)
    plt.show()