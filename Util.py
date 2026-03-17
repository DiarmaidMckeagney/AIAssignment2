from enum import Enum

agentList = []
colour_map = []

class Colour(Enum):
    Red = 1
    Blue = 2
    Green = 3
    Purple = 4
    Pink = 5
    Orange = 6
    Black = 7
    White = 8

    def toString(self):
        switcher = {
            1: "Red",
            2: "Blue",
            3: "Green",
            4: "Purple",
            5: "Pink",
            6: "Orange",
            7: "Black",
            8: "White"
        }
        return switcher.get(self.value, "Invalid colour")

    def fromInt(value):
        for colour in Colour:
            if colour.value == value:
                return colour.toString()
        raise ValueError(f"No colour with value {value}")
    

def colour_Graph_Nodes(agentList, graph):
    for node in graph.nodes():
        colour_map.append(Colour.fromInt(agentList[node].node.getColour()))
    
    return colour_map