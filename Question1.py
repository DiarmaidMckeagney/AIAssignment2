import Util

def question1Flow():
    agentList_question1 = []
    graph = Util.initGraph(10, 0.3,agentList_question1)
    Util.initNeighbours(graph, agentList_question1)

    for i in range(150):
        print(f"\nGENERATION {i}\n")
        for agent in agentList_question1:
            agent.change_state(agentList_question1)

        for agent in agentList_question1:
            agent.move_to_next_gen()

    Util.colourAndDrawGraph(graph, agentList_question1)

if __name__ == "__main__":
    question1Flow()