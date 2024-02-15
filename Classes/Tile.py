
class Tile:

    def __init__(self, type, value):

        #these represent type (resource) and value (numerical value that triggers)
        self.type = type
        self.value = value

        #baseline instantiated as false. Will become populated by a list of players who are linked
        self.owner = False

        #now we need to control for vertex points. Each vertex point will have a potential owner
        #HARD PART : vertex points are shared across several tiles. How to control??

        #value of vertex point will be a 3 part list. p1 = owner, p2 = road to next vertex
        #p3 = road to prior vertex.
        #verticies loop i.e 1-2-3-4-5-6-1-2-3.....
        #null values are always "False" bool
        self.v1 = [False, False, False]
        self.v2 = [False, False, False]
        self.v3 = [False, False, False]
        self.v4 = [False, False, False]
        self.v5 = [False, False, False]
        self.v6 = [False, False, False]

        #this is probably incomplete but we can revist it later

