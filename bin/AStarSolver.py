from bin.Maze import Maze
from bin.MazeInfo import MazeInfo
class AStarSolver:

    def __init__(self):
        self.mazeM = Maze()
        self.goal = []
        self.mazeM.findEnd(self.goal)
        self.start = []
        self.mazeM.findStart(self.start)
        #self.search(self.mazeM, self.start, self.goal)

    def heuristic(self, posX, posY):
        return abs(posX - self.goal[0]) + abs(posY - self.goal[1])

   def search(self, maze, start, goal):
        opened = []
        closed = []
        opened.append(MazeInfo(start[0], start[1], 0, self.heuristic(start[0], start[1])))

        while not opened.empty():
            checking = opened[0]

            if checking.x == goal[0] and checking.y == goal[1]:
                break

            if maze.left(checking.x, checking.y).moveable and maze.left(checking.x, checking.y) not in closed:
                if checking.left

