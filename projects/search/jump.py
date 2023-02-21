# imports
import math
from projects.search import linear

# jump search function
def search(el, arr):
    n = len(arr)
    
    # index jump between each block
    blk = math.isqrt(n)
    
    # repeat until all blocks are checked
    for i in range(blk + 1):
        jump = min(i * blk, n - 1)
        tar = arr[jump]

        # element found, return index
        if el == tar: return jump

        # perform linear search until found
        elif el < tar:
            lo = jump - blk + 1

            # search between last and current block
            sub = arr[lo : jump]

            # element found return index using linear
            idx = linear.search(el, sub)
            return idx if idx == -1 else lo + idx

    # element does not exist return -1
    return -1