import Util

def question2Flow():
    agentList_question2 = []
    graph2 = Util.initGraph(10, 0.3, agentList_question2)
    Util.initNeighbours(graph2, agentList_question2)

    for i in range(180):
        print(f"\nGENERATION {i}\n")
        numColoursAvailable = i // 20
        if numColoursAvailable < 2:
            numColoursAvailable = 2

        for agent in agentList_question2:
            agent.change_state_q2(agentList_question2, numColoursAvailable)

        for agent in agentList_question2:
            agent.move_to_next_gen()

    
    Util.colourAndDrawGraph(graph2, agentList_question2)

if __name__ == "__main__":
    question2Flow()