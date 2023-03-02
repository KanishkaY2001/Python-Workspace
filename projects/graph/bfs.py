# imports
from graph import graph_helper as g_h

# grid object for searching algorithms
def search(grid, start, goal):

    # check if start/goal tiles are valid
    if not grid.valid_pair(start, goal): return []

    # initialize the stack and visited set
    queue = [start]
    visited = set()

    # contains parent->child node hierarchy
    path_dict = {start: None}
    
    while queue:
        # pop first node from queue
        node = queue.pop(0)
        if node in visited: continue

        # start to goal node is reached return path
        if node == goal:
            return g_h.dict_to_path(path_dict, node)

        # add to visited set
        visited.add(node)

        # add adjacent nodes to queue
        for adj in grid.get_adj(node):
            if adj in visited: continue

            # assign parent and add to queue
            queue.append(adj)
            path_dict[adj] = node
    
    # no path found return empty
    return []