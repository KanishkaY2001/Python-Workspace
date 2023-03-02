# imports
from graph import dls

# init function for dfs algorithm
def search(grid, start, goal):

    # check if goal tile is valid
    if not grid.valid_pair(start, goal): return []
    
    path = []
    # iterate `number of vertices` times
    for lim in range(grid.v):
        #print(f"Searching at max depth: {lim}")
        # deepen the search limit iteratively
        #print(f"------------------------------------------------- Can Support Up To Depth: {lim}")
        path = dls.search(grid, start, goal, lim, set())
        if path: break

    # return iddfs path to goal, if it exists
    return path