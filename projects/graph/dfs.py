# depth-first search function
def search(grid, start, goal, vtd=[]):
    
    # add current tile to visited
    vtd.append(start)

    # if goal is reached then end
    if start == goal:
        return vtd

    # recursive dfs to find next depth
    for i in grid.get_adj(start):
        if i in vtd: continue

        # if goal is found return path
        if search(grid, i, goal, vtd):
            return vtd

    # no path to goal exists
    return None