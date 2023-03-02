# imports
import math
from search import linear

# jump search function
def search(goal, array):
    n = len(array)
    
    # index jump between each block
    block = math.isqrt(n)
    
    # repeat until all blocks are checked
    for i in range(block + 1):
        jump = min(i * block, n - 1)
        item = array[jump]

        # element found, return index
        if item == goal: return jump

        # perform linear search until found
        elif goal < item:
            low = jump - block + 1

            # search between last and current block
            sub = array[low : jump]

            # element found return index using linear
            idx = linear.search(goal, sub)
            return idx if idx == -1 else low + idx

    # element does not exist return -1
    return -1