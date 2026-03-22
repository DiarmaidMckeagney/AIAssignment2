import Util

# Question 2 flow, similar to question 1 but varying the number of available colours as an experiment
def question2Flow():
    agentList_question2 = []
    # Create a graph with 30 nodes and edge probability of 0.3, and initialize the agent list
    graph2 = Util.initGraph(30, 0.3, agentList_question2)
    # Initialize the neighbours for each agent based on the graph structure
    Util.initNeighbours(graph2, agentList_question2)

    file = open("question2_output.txt", "w")
    file.write(f"Generation, Total number of conflicts\n")
    # Main loop
    for i in range(180):
        # Limiting the number of available colours based on generation
        numColoursAvailable = i // 20
        if numColoursAvailable < 2:
            numColoursAvailable = 2

        # Decide the next state for each agent based on the current state of its neighbours and the number of available colours
        for agent in agentList_question2:
            agent.change_state_q2(agentList_question2, numColoursAvailable)

        # Once all agents have decided their next state, update their current state to the next state
        for agent in agentList_question2:
            agent.move_to_next_gen()

        conflicts = Util.countConflicts(agentList_question2)
        file.write(f"{i}, {conflicts}\n")
    
    file.close()
    # After the loop, visualize the graph with the final colours of the nodes'
    Util.colourAndDrawGraph(graph2, agentList_question2)

# Call main to run the flow for question two
if __name__ == "__main__":
    question2Flow()
    Util.drawConflictGraphs("question2_output.txt")