from enum import Enum

agentList_question1 = []
agentList_question2 = []

class Colour(Enum):
    red = 1
    blue = 2
    green = 3
    purple = 4
    pink = 5
    orange = 6
    black = 7
    white = 8

    def fromInt(value):
        for colour in Colour:
            if colour.value == value:
                return str(colour.name)
        raise ValueError(f"No colour with value {value}")