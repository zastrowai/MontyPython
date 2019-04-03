# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# Contains all contents associated with a maze and all common
# methods that the solving classes might use
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

    # Constructor
    # initializes a specified maze
    def __init__(self):
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

    # inputs the X position, and Y position of the cell to move left from
    # modifies the values by reference must be passed in a list
    def moveLeft(self, posX, posY):
        posX[0] = posX[0] - 1
        posY[0] = posY[0] + 0

    # inputs the X position, and Y position of the cell to move right from
    # modifies the values by reference must be passed in a list
    def moveRight(self, posX, posY):
        posX[0] = posX[0] + 1
        posY[0] = posY[0] + 0

    # inputs the X position, and Y position of the cell to move up from
    # modifies the values by reference must be passed in a list
    def moveUp(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] - 1

    # inputs the X position, and Y position of the cell to move down from
    # modifies the values by reference must be passed in a list
    def moveDown(self, posX, posY):
        posX[0] = posX[0] + 0
        posY[0] = posY[0] + 1

    # inputs the X position, and Y position of the cell to check
    # returns true if the cell is open, false otherwise
    def checkOpen(self, posX, posY):
        return self.maze[posY][posX] == self.OPEN

    # inputs the X position, and Y position of the cell to check
    # returns true if the cell is a wall, false otherwise
    def checkWall(self, posX, posY):
        return self.maze[posY][posX] == self.WALL

    # inputs the X position, and Y position of the cell to check
    # returns true if the cell is the exit, false otherwise
    def checkExit(self, posX, posY):
        return self.maze[posY][posX] == self.EXIT

    # inputs the X position, and Y position of the cell to check
    # returns true if the cell is the start, false otherwise
    def checkStart(self, posX, posY):
        return self.maze[posY][posX] == self.START

    # no inputs
    # prints to the command line the maze stored
    def printMaze(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                print(self.maze[i][j], end='')
            print()

    # inputs the Y position, and X position of the cell to mark
    # sets the spot in the maze to X
    def visited(self, posY, posX):
        self.maze[posY][posX] = self.VISITED

    # inputs a lst to store the end position to in X, Y format
    # finds the goal node
    def findEnd(self, lst):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.checkExit(i, j):
                    lst.append(i)
                    lst.append(j)
                    break

    # inputs a lst to store the end position to in X, Y format
    # finds the start state
    def findStart(self, lst):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.checkStart(i, j):
                    lst.append(i)
                    lst.append(j)
                    break

    # inputs the X position, and Y position of the cell to check
    # returns true if the position is open or the exit and false otherwise
    def moveable(self, posX, posY):
        if self.checkOpen(posX, posY) or self.checkExit(posX, posY):
            return True
        return False
