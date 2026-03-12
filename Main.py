from enum import Enum
from Node import Node

class Colour(Enum):
    Red = 1
    Blue = 2
    Green = 3
    Purple = 4
    Pink = 5
    Orange = 6
    Black = 7
    White = 8

    def fromInt(value):
        for colour in Colour:
            if colour.value == value:
                return colour
        raise ValueError(f"No colour with value {value}")