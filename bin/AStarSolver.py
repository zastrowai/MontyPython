from bin.Maze import Maze
class AStarSolver:

    def __init__(self):
        self.mazeP = Maze()
        self.goalX = [0]
        self.goalY = [0]
        self.findEnd(self.goalX, self.goalY)
        self.startX = [0]
        self.startY = [0]
        self.findStart(self.startX,self.startY)

    def findEnd(self, posX, posY):
        for i in range(len(self.mazeP.maze)):
            for j in range(len(self.mazeP.maze[i])):
                if self.mazeP.checkExit(i, j):
                    posX[0] = j
                    posY[0] = i
                    break

    def findStart(self, posX, posY):
        for i in range(len(self.mazeP.maze)):
            for j in range(len(self.mazeP.maze[i])):
                if self.mazeP.checkStart(i, j):
                    posX[0] = j
                    posY[0] = i
                    break

    ##def heuristic(posX, posY):
