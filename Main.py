from bin.Maze import Maze
from bin.AStarSolver import AStarSolver
from bin.DfsSolver import DfsSolver
test = Maze()
test2 = AStarSolver()
test3 = DfsSolver()
print(test2.goal)
print("\n")
print(test2.start)
left = [1]
right = [1]



#test.printMaze()
test3.printDfsMaze()
print("\n")
test3.solve(0, 1)
test3.printDfsMaze()