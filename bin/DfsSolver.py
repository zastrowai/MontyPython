from bin.Maze import Maze
class DfsSolver:
    def __init__(self):
        self.mazeDFS = Maze()
        self.goalX = [0]
        self.goalY = [0]
        self.end = Maze.findEnd(self.goalX, self.goalY)
        self.startX = [0]
        self.startY = [0]
        self.start = Maze.findStart(self.startX, self.startY)
        self.free = False

    def solve(self, x, y):
        if self.mazeDFS[x][y] == Maze.EXIT:
            self.free = True
            return
        if self.mazeDFS[x][y - 1] == Maze.OPEN or self.mazeDFS[x][y -1] == Maze.EXIT:  # Logic for moving down
            if self.free:
                return
            if self.mazeDFS[x][y] != Maze.START:
                self.mazeDFS[x][y] = Maze.VISITED
            self.solve(self, x, y - 1)
        if self.mazeDFS[x + 1][y] == Maze.OPEN or self.mazeDFS[x + 1][y] == Maze.EXIT:  # Logic for moving right
            if self.free:
                return
            if self.mazeDFS[x][y] != Maze.START:
                self.mazeDFS[x][y] = Maze.VISITED
            self.solve(self, x + 1, y)
        if self.mazeDFS[x - 1][y] == Maze.OPEN or self.mazeDFS[x - 1][y] == Maze.EXIT:  # Logic for moving left
            if self.free:
                return
            if self.mazeDFS[x][y] != Maze.START:
                self.mazeDFS[x][y] = Maze.VISITED
            self.solve(self, x - 1, y)
        if self.mazeDFS[x][y + 1] == Maze.OPEN or self.mazeDFS[x][y + 1] == Maze.EXIT:  # Logic for moving up
            if self.free:
                return
            if self.mazeDFS[x][y] != Maze.START:
                self.mazeDFS[x][y] = Maze.VISITED
            self.solve(self, x, y + 1)


