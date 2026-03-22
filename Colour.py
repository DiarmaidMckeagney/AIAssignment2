from enum import Enum

# Enum class to represent the different colours that can be assigned to the nodes in the graph
class Colour(Enum):
    red = 1
    blue = 2
    green = 3
    purple = 4
    pink = 5
    orange = 6
    black = 7
    white = 8

    # Static method to convert an integer value to the corresponding colour name
    @staticmethod
    def fromInt(value):
        for colour in Colour:
            if colour.value == value:
                return str(colour.name)
        raise ValueError(f"No colour with value {value}")