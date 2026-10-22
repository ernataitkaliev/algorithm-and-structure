# Task 18. Maze Solver
def solve(maze, r, c, path):
    if r < 0 or c < 0 or r >= len(maze) or c >= len(maze[0]):
        return False
    if maze[r][c] != 0:
        return False
    maze[r][c] = 2
    path.append((r, c))
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        return True
    if (solve(maze, r, c + 1, path) or solve(maze, r + 1, c, path) or
            solve(maze, r, c - 1, path) or solve(maze, r - 1, c, path)):
        return True
    path.pop()
    return False

maze = [[0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0]]
path = []
if solve(maze, 0, 0, path):
    print(path)
