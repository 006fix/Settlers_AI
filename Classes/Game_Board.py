
class GameBoard:

    def __init__(self):

        #this is going to serve to maintain a hold file of the various verticies present on the board
        #roads will be determined via items within a list
        #each vertex will be a dict, with a value of a list of 6
        #[owner, port, road1 (left), road2 (right), road3 (vertical axis), linked points]
        #the logic will be left to right, top down, based on this pic
        #ports are named logically left top right top down
        #https://www.belloflostsouls.net/wp-content/uploads/2022/02/Catan-Beginner-Map.png
        #for copying
        #'p7': [False, False, False, False, False],
        gameboard = {
            #MAKE SURE TO ADD THE LINKED POINTS AFTERWARDS
            #top row
            'p1': [False, 'port1', False, False, 'Invalid'],
            'p2': [False, 'port2', False, False, 'Invalid'],
            'p3': [False, False, False, False, 'Invalid'],
            #row2
            'p4': [False, 'port1', 'Invalid', False, False],
            'p5': [False, False, False, False, False],
            'p6': [False, 'port2', False, False, False],
            'p7': [False, False, False, 'Invalid', False],
            #row3
            'p8': [False, False, False, False, False],
            'p9': [False, False, False, False, False],
            'p10': [False, False, False, False, False],
            'p11': [False, 'port4', False, False, False],
            #row4
            'p12': [False, 'port3', 'Invalid', False, False],
            'p13': [False, False, False, False, False],
            'p14': [False, False, False, False, False],
            'p15': [False, False, False, False, False],
            'p16': [False, 'port4', False, 'Invalid', False],
            #row5

        }