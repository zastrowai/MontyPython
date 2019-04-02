# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# A* solver uses the maze class and determines where the start and goal are
# Uses the goal to find the heuristic value of each cell once it examines a cell
# Uses the start as the starting location and then looks left, down, right, up
# Replaces the start and opens spaces with X to show the path that was taken
# Some open spaces are examined before the goal at the very end of the search
# As their path cost function is less the goals.

from bin.Maze import Maze
from bin.MazeInfo import MazeInfo


class AStarSolver:
    # used to determine the object in opened with the lowest path cost function
    LARGE_NUM = 65234

    # Constructor of A*
    # initializes goal and start then runs the search and print of the maze
    def __init__(self):
        self.mazeM = Maze()
        self.goal = []
        self.mazeM.findEnd(self.goal)
        self.start = []
        self.mazeM.findStart(self.start)


    # Finds the heuristic value from the current position to the goal
    # Returns the heuristic
    def heuristic(self, posX, posY):
        return abs(posX - self.goal[0]) + abs(posY - self.goal[1])

    # The main body for the A* search
    # Uses an entered maze and start position
    # Searches through the maze using A* until it finds the goal
    # Will print out the path taken as it goes
    def solve(self, maze, start):
        opened = []
        closed = []
        opened.append(MazeInfo(start[0], start[1], 0, self.heuristic(start[0], start[1])))

        while len(opened):
            f = self.LARGE_NUM
            tocheck = -1
            for x in range(len(opened)):
                if (opened[x].f < f):
                    f = opened[x].f
                    tocheck = x
            checking = opened[tocheck]

            print("[", checking.x, ",", checking.y, "]")
            closed.append(checking)

            ## go left
            tempX = checking.x
            tempY = checking.y
            if maze.checkExit(checking.x, checking.y):
                return

            maze.maze[checking.y][checking.x] = 'X'
            tempX = tempX - 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                    if tempChecking.g >= checking.g + 1:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            ## go down
            tempX = checking.x
            tempY = checking.y

            tempY = tempY + 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                    if tempChecking.g >= checking.g + 1:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            ##right

            tempX = checking.x
            tempY = checking.y

            tempX = tempX + 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                    if tempChecking.g >= checking.g + 1:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            ## up
            tempX = checking.x
            tempY = checking.y

            tempY = tempY - 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                    if tempChecking.g >= checking.g + 1:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)


            opened.remove(checking)


