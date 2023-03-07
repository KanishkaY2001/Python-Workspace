# binary search function
def search(goal, array):
    n = len(array)

    # bounds for search space
    low = 0
    high = n - 1

    # repeat until bounds converge
    while high >= low or low <= high:

        # average value of bounds
        mid = (high + low) // 2
        item = array[mid]

        # reduce search space until found
        if goal < item:
            high = mid - 1
        elif goal > item:
            low = mid + 1
        else: return mid

    # element does not exist return -1
    return -1