# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# Storage for Heuristic
class MazeInfo:

    def __init__(self, posX, posY, costToStart, costToEnd):
        self.x = posX
        self.y = posY
        self.g = costToStart
        self.h = costToEnd
        self.f = costToEnd + costToStart