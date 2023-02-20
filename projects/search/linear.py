# linear search function
def search(el, arr):
    for idx, val in enumerate(arr):

        # sequentially search until found
        if val == el:
            return idx
            
    # element does not exist return -1
    return -1