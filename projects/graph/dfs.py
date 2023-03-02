# imports
from graph import dls

# init function for dfs algorithm
def search(grid, start, goal):
    
    # dfs is just dls with a maximum depth
    vertices = grid.v + 1
    print(vertices)
    return dls.search(grid, start, goal, vertices)