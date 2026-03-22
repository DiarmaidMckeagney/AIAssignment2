import Util

# This is the flow for question one
def question1Flow():
    agentList_question1 = []
    # Create a graph with 40 nodes and edge probability of 0.3, and initialize the agent list
    graph = Util.initGraph(40, 0.3,agentList_question1)
    # Initialize the neighbours for each agent based on the graph structure
    Util.initNeighbours(graph, agentList_question1)

    # Main loop
    for i in range(150):
        # Decide the next state for each agent based on the current state of its neighbours
        for agent in agentList_question1:
            agent.change_state(agentList_question1)

        # Once all agents have decided their next state, update their current state to the next state
        for agent in agentList_question1:
            agent.move_to_next_gen()

    # After the loop, visualize the graph with the final colours of the nodes'
    Util.colourAndDrawGraph(graph, agentList_question1)

# Call main to run the flow for question one
if __name__ == "__main__":
    question1Flow()