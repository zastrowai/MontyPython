from bin.Maze import Maze
class DfsSolver:
    def __init__(self):
        self.mazeDFS = Maze()
        self.free = False

    def solve(self, y, x):
        if self.mazeDFS.maze[y][x] != Maze.EXIT and self.mazeDFS.maze[y][x] != Maze.START:
            self.mazeDFS.maze[y][x] = Maze.VISITED
        if self.mazeDFS.maze[y][x] == Maze.EXIT:
            self.free = True
            return
        if self.mazeDFS.maze[y][x - 1] == Maze.OPEN or self.mazeDFS.maze[y][x - 1] == Maze.EXIT:  # Logic for moving left
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            self.printDfsMaze()
            print("\n")
            self.solve(y, x - 1)
        if self.mazeDFS.maze[y + 1][x] == Maze.OPEN or self.mazeDFS.maze[y + 1][x] == Maze.EXIT:  # Logic for moving down
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            self.printDfsMaze()
            print("\n")
            self.solve(y + 1, x)
        if self.mazeDFS.maze[y - 1][x] == Maze.OPEN or self.mazeDFS.maze[y - 1][x] == Maze.EXIT:  # Logic for moving up
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            self.printDfsMaze()
            print("\n")
            self.solve(y - 1, x)
        if self.mazeDFS.maze[y][x + 1] == Maze.OPEN or self.mazeDFS.maze[y][x + 1] == Maze.EXIT:  # Logic for moving right
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            self.printDfsMaze()
            print("\n")
            self.solve(y, x + 1)

    def printDfsMaze(self):
        for i in range(len(self.mazeDFS.maze)):
            for j in range(len(self.mazeDFS.maze[i])):
                print(self.mazeDFS.maze[i][j], end='')
            print()


