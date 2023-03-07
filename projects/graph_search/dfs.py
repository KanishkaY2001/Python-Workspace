# imports
from graph_search import dls

# depth first search function
def search(grid, start, goal):
    
    # check if goal and start tiles are valid
    if not (grid.valid(start) and grid.valid(goal)):
        return []

    # dfs is just dls with a max depth (vertices count)
    return dls.search(grid, start, goal, grid.v + 1)