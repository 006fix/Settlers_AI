
class Frame_Slots:

    def __init__(self, typevar, port_type):

        #typevar determines is port type is 1 or 2 port
        self.typevar = typevar
        self.port_type = port_type

        #regardess of type, each frame slot has 6 verticies.
        #v1 and v6 are shared between frame slots

        # value of vertex point will be a 3 part list. p1 = owner, p2 = road to next vertex
        # p3 = road to prior vertex.
        # verticies loop i.e 1-2-3-4-5-6-1-2-3.....
        # null values are always "False" bool
        self.v1 = [False, False, False]
        self.v2 = [False, False, False]
        self.v3 = [False, False, False]
        self.v4 = [False, False, False]
        self.v5 = [False, False, False]
        self.v6 = [False, False, False]

