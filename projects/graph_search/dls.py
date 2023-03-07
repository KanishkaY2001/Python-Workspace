# private depth limited search function
def __search(grid, node, goal, depth, visited):
    # return node if goal has been reached
    if node == goal: return [node]

    # return empty if max depth is reached
    if depth == 0: return []

    # add latest node to the visited set
    visited.add(node)

    # recurse on node's unvisited neighbors
    for adj in grid.get_adj(node):
        # ignore if neighbour is already visited
        if adj in visited: continue

        # recurse deeper into all neighbours to find goal
        d_visited = set(visited)
        path = __search(grid, adj, goal, depth-1, d_visited)

        # ignore if path reaches depth limit
        if not path: continue

        # return the path if path to goal exists
        return [node] + path
    
    # return empty as no path to goal exists
    return []


# public search function for dls
def search(grid, start, goal, depth):
    
    # check if goal and start tiles are valid
    if not (grid.valid(start) and grid.valid(goal)):
        return []

    # perform dls search from start to goal with depth
    return __search(grid, start, goal, depth, set())