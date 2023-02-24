# depth-first search function
def __search(grid, start, goal, vtd=[]):
    # add current tile to visited
    vtd.append(start)

    # if goal is reached then end
    if start == goal:
        return vtd

    # recursive dfs to find next depth
    for i in grid.get_adj(start):
        if i in vtd: continue

        # if goal is found return path
        if __search(grid, i, goal, vtd):
            return vtd

    # no path to goal exists
    return None

# init function for dfs algorithm
def search(grid, start, goal):
    
    # check if goal tile is valid
    if not grid.valid_pair(start, goal):
        return None
    
    # return dfs path to goal
    return __search(grid, start, goal)