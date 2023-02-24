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


grid = layout.grid(4,2)
grid.print()


print(f"DFS Path: {dfs.search(grid, -1, 7)}")
print(f"BFS Path: {bfs.search(grid, 8, 7)}")
#print(grid.is_valid(7))