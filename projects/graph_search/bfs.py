# converts parent->child hierarchy to path
def dict_to_path(path_dict, goal):

    # initialize path and set parent
    path = []
    parent = goal

    # get path from goal -> start
    while parent is not None:
        path.append(parent)
        parent = path_dict[parent]

    # reverse to show start -> goal
    path.reverse()
    return path


# grid object for searching algorithms
def search(grid, start, goal):

    # check if goal and start tiles are valid
    if not (grid.valid(start) and grid.valid(goal)):
        return []

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
            return dict_to_path(path_dict, node)

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