"""
    This file stores all of the core game information that the 'engine' can use
    to run the game.
    ex.) Definitions of what a province is
"""


#A province on the board,
class Province:
    def __init__(self, name, supplyCenter, owner):
        self.name = name
        self.isCenter = supplyCenter
        self.owner = owner
        self.neighbors = []

    def is_center(self):
        return self.isCenter

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def check_neighbor(self, province):
        return province in self.neighbors