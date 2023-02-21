# imports
from projects.search import linear
from projects.search import binary
from projects.search import jump
from projects.search import interpol

el = 357
arr = list(range(0,600,7))

a = linear.search(el, arr)
b = binary.search(el, arr)
c = jump.search(el, arr)
d = interpol.search(el, arr)

assert a == b == c == d
print(d)
