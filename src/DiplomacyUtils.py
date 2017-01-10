"""
    This file stores all of the core game information that the 'engine' can use
    to run the game.
    ex.) Definitions of what a province is
"""


#A province on the board,
class Province:
    def __init__(self, name, supplyCenter, owner, provType):
        self.name = name #name of the province
        self.isCenter = supplyCenter #Is the province a supply center?
        self.owner = owner #What nationality owns the province?
        self.neighbors = [] #What are the neighboring provinces?
        self.provType = provType #What type of province? Inland, Coast, Water

    #Is the province a supply center?
    def is_center(self):
        return self.isCenter

    #Adds a neighbor to the province (gamestate setup only)
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    #Is the province a neighbor of the input province?
    def check_neighbor(self, province):
        return province in self.neighbors

    #Changes the owner of the province
    def change_owner(self, power):
        self.owner = power

#A power/country, there are 7: Austria, England, France, Russia, Germany, Italy, Turkey
class GreatPower:
    def __init__(self, name):
        self.name = name #name of the power
        self.territories = [] #List of territories owned

    #adds a territory to the power's ownership
    def add_territory(self, province):
        province.change_owner(self)
        self.territories.append(province)

    #Removes a territory from ownership
    def rem_territory(self, province):
        if province in self.territories:
            self.territories.remove(province)