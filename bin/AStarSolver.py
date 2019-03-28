from bin.Maze import Maze
class AStarSolver:

    def __init__(self):
        self.mazeP = Maze()
        self.goal = []
        self.mazeP.findEnd(self.goal)
        self.start = []
        self.mazeP.findStart(self.start)
        self.h = 0
        self.f = 0



    def heuristic(self, posX, posY):
        return abs(posX - self.goal[0]) + abs(posY - self.goal[1])

  #  def search(self, maze, start, goal):
