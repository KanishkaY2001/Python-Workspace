# imports
from graph_search import *
from array_search import *

# testing for array searching algorithms
print("\ntesting for array searching algorithms")
el = 357
arr = list(range(0,600,7))

a = linear.search(el, arr)
b = binary.search(el, arr)
c = jump.search(el, arr)
d = interpol.search(el, arr)

assert a == b == c == d
print(f"array search idx: {d}\n")


# testing for grid path finding algorithms
print("testing for grid path finding algorithms")
d = 8
grid = layout.grid(d, d)
grid.print()

max_v = grid.v - 1
g = grid.w * grid.h - 1
start, goal = 0,63

print(f"DFS Path:   {len(dfs.search(grid, start, goal))}")
print(f"BFS Path:   {len(bfs.search(grid, start, goal))}")
print(f"DLS Path:   {len(dls.search(grid, start, goal, 14))}")
print(f"IDDFS Path: {len(iddfs.search(grid, start, goal))}")