from bin.Maze import Maze

test = Maze()
left = [1]
right = [1]


print(test.checkOpen(int(left[0]), int(right[0])))
print(test.checkWall(left[0], right[0]))
print(test.checkExit(left[0], right[0]))
