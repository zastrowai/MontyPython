# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# Greedy solver uses the maze class and determines where the start and goal are
# Uses the goal to find the heuristic value of each cell once it examines a cell
# Uses the start as the starting location and then looks left, down, right, up
# Replaces the start and opens spaces with X to show the path that was taken
# It follows the greedy best first path using by taking the lowest heuristic path

from bin.Maze import Maze
from bin.MazeInfo import MazeInfo


class GreedySolver:
    # initial value that should always be greater than heuristic
    LARGE_NUM = 65234

    # Constructor of GreedySolver
    # duplicates the maze and initializes goal and start
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

    # The main body (search method) for the GreedySolver
    # Uses an entered maze and start position
    # Searches through the maze by following the best heuristic path found
    # It also prints out the location on the map as it traverses toward the exit.
    def search(self, maze, start, goal):
        opened = []
        closed = []
        opened.append(MazeInfo(start[0], start[1], 0, self.heuristic(start[0], start[1])))

        while len(opened):
            h = self.LARGE_NUM
            tocheck = -1
            for x in range(len(opened)):
                if opened[x].h <= h:
                    h = opened[x].h
                    tocheck = x
            checking = opened[tocheck]
            closed.append(checking)

            if maze.checkExit(checking.x, checking.y):
                print(self.goal)
                print("Exit Found!\n")
                return

            # go left
            tempX = checking.x
            tempY = checking.y
            maze.maze[checking.y][checking.x] = 'X'
            tempX = tempX - 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            # go down
            tempX = checking.x
            tempY = checking.y
            tempY = tempY + 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            # go right
            tempX = checking.x
            tempY = checking.y
            tempX = tempX + 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            # go up
            tempX = checking.x
            tempY = checking.y
            tempY = tempY - 1
            tempChecking = MazeInfo(tempX, tempY, checking.g + 1, self.heuristic(tempX, tempY))
            if maze.moveable(tempX, tempY) and tempChecking not in closed:
                if tempChecking in opened:
                        for j in range(len(opened)):
                            if opened[j] == tempChecking:
                                opened[j] = tempChecking
                else:
                    opened.append(tempChecking)

            opened.remove(checking)
            print("[" + str(checking.x) + ", " + str(checking.y) + "]")
