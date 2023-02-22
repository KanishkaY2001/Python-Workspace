# imports

# array searching algorithms
from projects.search import linear
from projects.search import binary
from projects.search import jump
from projects.search import interpol

# graph searching algorithms
from projects.graph import dfs
from projects.graph import grid

el = 357
arr = list(range(0,600,7))

a = linear.search(el, arr)
b = binary.search(el, arr)
c = jump.search(el, arr)
d = interpol.search(el, arr)

assert a == b == c == d
#print(d)

#dfs.search()
grid.new(5,5)