# simple class for storing the name and colour choice of each
# player

class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.is_turn = None

