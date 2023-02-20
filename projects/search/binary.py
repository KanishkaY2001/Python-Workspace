# binary search function
def search(el, arr):
    size = len(arr)

    # bounds for search space
    lo = 0
    hi = size - 1

    # repeat until bounds converge
    while hi >= lo or lo <= hi:
        
        # average value of bounds
        mid = (hi + lo) // 2
        tar = arr[mid]

        # reduce search space until found
        if el < tar:
            hi = mid - 1
        elif el > tar:
            lo = mid + 1
        else: return el

    # element does not exist return -1
    return -1