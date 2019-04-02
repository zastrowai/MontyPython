class Maze:
    ## 1 is wall
    ## 0 is path
    ## 2 is start
    ## 3 is goal
    WALL = 1
    OPEN = 0
    START = 2
    EXIT = 3
    VISITED = 'X'
    def __init__(self):
        self.width = 12
        self.height = 12
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
        posX[0] = posX[0] - 1
        posY[0] = posY[0] + 0

    def moveRight(self, posX, posY):
        posX[0] = posX[0] + 1
        posY[0] = posY[0] + 0

    def moveUp(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] - 1

    def moveDown(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] + 1

    def checkOpen(self, posX, posY):
        return self.maze[posY][posX] == 0

    def checkWall(self, posX, posY):
        return self.maze[posY][posX] == 1

    def checkExit(self, posX, posY):
        return self.maze[posY][posX] == 3

    def checkStart(self, posX, posY):
        return self.maze[posY][posX] == 2

    def printMaze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                print(self.maze[i][j], end='')
            print()

    def visited(self, posX, posY):
        self.maze[posX][posY] = 'X'

    def findEnd(self, lst):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.checkExit(i, j):
                    lst.append(i)
                    lst.append(j)
                    break

    def findStart(self, lst):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.checkStart(i, j):
                    lst.append(i)
                    lst.append(j)
                    break

    def moveable(self, posX, posY):
        if self.checkOpen(posX, posY) or self.checkExit(posX, posY):
            return True
        return False
