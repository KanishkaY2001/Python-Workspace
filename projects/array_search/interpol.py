# imports
import math

def get_probe(goal, arr, h, l):
    return l + ((h - l) / (arr[h] - arr[l])) * (goal - arr[l])

# interpolation search function
def search(goal, array):
    n = len(array)

    # bounds for search space
    low = 0
    high = n - 1

    # repeat until bound exceeds search element
    while low <= high and goal >= array[low] and goal <= array[high]:

        # calculate probe for search space
        probe = get_probe(goal, array, high, low)
        mid = math.floor(probe)
        item = array[mid]

        # restrict search space to left-side
        if item > goal:
            high = mid - 1

        # restrict search space to right-side
        elif item < goal:
            low = mid + 1

        # element found return index
        else: return mid
    
    # element does not exist return -1
    return -1