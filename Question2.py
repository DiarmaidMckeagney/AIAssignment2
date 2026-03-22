import Util

def question2Flow():
    agentList_question2 = []
    graph2 = Util.initGraph(10, 0.3, agentList_question2)
    Util.initNeighbours(graph2, agentList_question2)

    for i in range(20):
        print(f"\nGENERATION {i}\n")
        for agent in agentList_question2:
            agent.change_state(agentList_question2)

        for agent in agentList_question2:
            agent.move_to_next_gen()

    
    Util.colourAndDrawGraph(graph2, agentList_question2)

if __name__ == "__main__":
    question2Flow()