# linear search function
def search(goal, array):
    # sequentially search until found
    for idx, item in enumerate(array):
        
        # element found return index
        if item == goal: return idx

    # element does not exist return -1
    return -1