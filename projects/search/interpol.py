# imports
import math

# interpolation search function
def search(el, arr):
    n = len(arr)

    # bounds for search space
    lo = 0
    hi = n - 1

    # repeat until bound exceeds search element
    while lo <= hi and el >= arr[lo] and el <= arr[hi]:

        # calculate probe for search space
        probe = lo + ((hi - lo) / (arr[hi] - arr[lo])) * (el - arr[lo])
        mid = math.floor(probe)
        tar = arr[mid]

        # restrict search space to left-side
        if tar > el:
            hi = mid - 1

        # restrict search space to right-side
        elif tar < el:
            lo = mid + 1

        # element found return index
        else: return mid
    
    # element does not exist return -1
    return -1