from bin.Maze import Maze
from bin.MazeInfo import MazeInfo


class GreedySolver:

    LARGE_NUM = 65234

    def __init__(self):
        self.mazeM = Maze()
        self.goal = []
        self.mazeM.findEnd(self.goal)
        self.start = []
        self.mazeM.findStart(self.start)
        self.search(self.mazeM, self.start, self.goal)
        self.mazeM.printMaze()

    def heuristic(self, posX, posY):
        return abs(posX - self.goal[0]) + abs(posY - self.goal[1])

    def search(self, maze, start, goal):
        opened = []
        closed = []
        opened.append(MazeInfo(start[1], start[0], 0, self.heuristic(start[0], start[1])))

        while len(opened):
            h = self.LARGE_NUM
            tocheck = -1
            for x in range(len(opened)):
                if (opened[x].h <= h):
                    h = opened[x].h
                    tocheck = x
            checking = opened[tocheck]

            maze.printMaze()
            closed.append(checking)

            ## go left
            tempX = checking.x
            tempY = checking.y
            if maze.checkExit(checking.x, checking.y):
                print("gucci gang")
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
            if maze.checkExit(checking.x, checking.y):
                break
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
            if maze.checkExit(checking.x, checking.y):
                break
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
            if maze.checkExit(checking.x, checking.y):
                break
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
            print(checking.x, checking.y)


