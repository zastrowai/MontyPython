# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# DFS solver
# In the form of the Maze Solver, the algorithm goes through the maze by checking if it can go left,
# down, right, and up in that order. It goes through this process recursively, if it reaches a dead end,
# then it goes back to the last intersection and goes from there.
# Like Depth First Search, it goes as deep as it can,
# and goes back to the first level it splits from and continues down that branch until it finds the exit.
from bin.Maze import Maze


class DfsSolver:

    # Constructor
    # initializes a maze to use
    # A variable to know if it is free
    # and where the goal and start are
    def __init__(self):
        self.mazeDFS = Maze()
        self.free = False
        self.goal = []
        self.mazeDFS.findEnd(self.goal)
        self.start = []
        self.mazeDFS.findStart(self.start)

    # The main body for the DFS search
    # Uses entered coordinates being the start and solves for the end
    # uses recursion
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
            print("[" + str(x) + ", " + str(y) + "]")
            self.solve(y, x - 1)
        if self.mazeDFS.maze[y + 1][x] == Maze.OPEN or self.mazeDFS.maze[y + 1][x] == Maze.EXIT:  # Logic for moving down
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            print("[" + str(x) + ", " + str(y) + "]")
            self.solve(y + 1, x)
        if self.mazeDFS.maze[y - 1][x] == Maze.OPEN or self.mazeDFS.maze[y - 1][x] == Maze.EXIT:  # Logic for moving up
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            print("[" + str(x) + ", " + str(y) + "]")
            self.solve(y - 1, x)
        if self.mazeDFS.maze[y][x + 1] == Maze.OPEN or self.mazeDFS.maze[y][x + 1] == Maze.EXIT:  # Logic for moving right
            if self.free:
                return
            if self.mazeDFS.maze[y][x] != Maze.START:
                self.mazeDFS.maze[y][x] = Maze.VISITED
            print("[" + str(x) + ", " + str(y) + "]")
            self.solve(y, x + 1)

    # prints the maze that the dfs solver initialized
    def printDfsMaze(self):
        for i in range(len(self.mazeDFS.maze)):
            for j in range(len(self.mazeDFS.maze[i])):
                print(self.mazeDFS.maze[i][j], end='')
            print()


