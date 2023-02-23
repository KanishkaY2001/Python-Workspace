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


grid = layout.grid(5,5)
grid.print()

path = dfs.search(grid, 7, 23, [])
print(f"DFS Path: {path}")