# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# Storage for Heuristic
class MazeInfo:

    # Constructor for maze info
    # takes in a X coordinate, Y Coordinate, The cost to the start, and the Cost to the end
    # And Calculates f by adding h and g
    def __init__(self, posX, posY, costToStart, costToEnd):
        self.x = posX
        self.y = posY
        self.g = costToStart
        self.h = costToEnd
        self.f = costToEnd + costToStart