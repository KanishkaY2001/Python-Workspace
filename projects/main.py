# imports
from search import *
from graph import *


el = 357
arr = list(range(0,600,7))

a = linear.search(el, arr)
b = binary.search(el, arr)
c = jump.search(el, arr)
d = interpol.search(el, arr)

assert a == b == c == d
#print(d)







d = 10
grid = layout.grid(d, d)
grid.print()

max_v = grid.v - 1
g = grid.w * grid.h - 1
start, goal = 0,99 # 5, 0, 19
# 6 0 29
# 0, 204
#print(f"Optimal Len: {grid.w + grid.h - 1}")
#print(f"DFS Path:   {dfs.search(grid, start, goal)}")
print(f"BFS Path:   {len(bfs.search(grid, start, goal))}")
#print(f"DLS Path:   {len(dls.search(grid, start, goal, 30))}")
print(f"IDDFS Path: {len(iddfs.search(grid, start, goal))}")
#print(f"FAKE Path:  {test.search(grid, start, goal)}")