# Project 1
# Contributors: Logan Garza, Timothy Kempster, Aidan Zastrow
# The problem we addressed in our project was the solving a linear maze in an [x,y] plane using python.
# When traversing in a maze, there are four basic actions you can proceed with at any given point,
# you can check for a wall and attempt to move: right, up, down, or left.
# Our project aimed to automate this decision making based on different algorithms and heuristics.
# We implemented a depth first search algorithm,
# A star heuristic, and greedy best-first heuristic to address different ways to traverse and
# solve a maze given that it has one specific entry point and one specific exit/goal point.
from bin.Maze import Maze
from bin.AStarSolver import AStarSolver
from bin.DfsSolver import DfsSolver
from bin.GreedySolver import GreedySolver
test = Maze()
test2 = AStarSolver()
test3 = DfsSolver()
test4 = GreedySolver()
print("\n")

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

print("Start of Greedy Solver")
print("Original Greedy Maze: 1 = wall, 0 = free, 2 = start, 3 = exit, X = visited")
test4.mazeM.printMaze()
print("\nPrinting locations visited by the Greedy Solver in form of [x, y]")
test4.search(test4.mazeM, test4.start, test4.goal)
print("Finished Map:")
test4.mazeM.printMaze()
print("End of Greedy Solver")

print("Start of A* Solver")
print("Original Maze: 1 = wall, 0 = free, 2 = start, 3 = exit, X = visited")
test2.mazeM.printMaze()
print()
print("Printing locations visited by the solver in form of [x, y]")
test2.solve(test2.mazeM, test2.start)
print("Finished Maze:")
test2.mazeM.printMaze()
print("End of A* Solver\n")