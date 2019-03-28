class Maze:
    ## 1 is wall
    ## 0 is path
    ## 2 is start
    ## 3 is goal
    def __init__(self):
        self.width = 10
        self.height = 10
        self.maze = [
                [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 3],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def moveLeft(self, posX, posY):
        posX[0] = posX[0] + 1
        posY[0] = posY[0] + 0

    def moveRight(self, posX, posY):
        posX[0] = posX[0] - 1
        posY[0] = posY[0] + 0

    def moveUp(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] + 1

    def moveDown(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] - 1

    def checkOpen(self, posX, posY):
        return self.maze[posX][posY] == 0

    def checkWall(self, posX, posY):
        return self.maze[posX][posY] == 1

    def checkExit(self, posX, posY):
        return self.maze[posX][posY] == 3
