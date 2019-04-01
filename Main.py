from bin.Maze import Maze
#from bin.AStarSolver import AStarSolver
from bin.DfsSolver import DfsSolver

# Declarations
test = Maze()
#test2 = AStarSolver()
test3 = DfsSolver()
#print(test2.goal)
print()
#print(test2.start)
left = [1]
right = [1]

# Main Body. Runs through all the algorithms.
print("Start of DFS Solver")
print("Original Maze: 1 = wall, 0 = free, 2 = start, 3 = exit, X = visited")
test3.printDfsMaze()
print()
print("Printing locations visited by the solver in form of [x, y]")
test3.solve(test3.start[1], test3.start[0])
print("Finished Maze:")
test3.printDfsMaze()
print("End of DFS Solver\n")