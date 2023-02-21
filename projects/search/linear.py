# linear search function
def search(el, arr):
    # sequentially search until found
    for i, val in enumerate(arr):
        if val == el:
            return i
            
    # element does not exist return -1
    return -1