# imports
from projects.search import linear
from projects.search import binary
from projects.search import jump

el = 23
arr = [2,4,6,8,10,19,23,44,101]

x = linear.search(el, arr)
y = binary.search(el, arr)
z = jump.search(el, arr)

assert x == y == z
print(x)