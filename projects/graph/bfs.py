# grid object for searching algorithms
def search(grid, start, goal, vtd=[]):

    # check if goal tile is valid
    if not grid.valid_pair(start, goal):
        return None

    # initialize the queue
    q = []
    q.append(start)
    
    while len(q) > 0:
        # pop first tile and mark visited
        top = q.pop(0)
        vtd.append(top)
        
        # if goal is reached then end
        if top == goal: break

        # Add adj tiles to queue if unique
        for v in grid.get_adj(top):
            if v not in q and v not in vtd:
                q.append(v)
    
    # return bfs path to goal
    return vtd