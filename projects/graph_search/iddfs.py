# imports
from graph_search import dls

# iterative deepening depth first search function
def search(grid, start, goal):

    # check if goal and start tiles are valid
    if not (grid.valid(start) and grid.valid(goal)):
        return []
    
    path = []
    # iterate `number of vertices` times
    for lim in range(grid.v):
        path = dls.search(grid, start, goal, lim)
        if path: break

    # return iddfs path to goal, if it exists
    return path