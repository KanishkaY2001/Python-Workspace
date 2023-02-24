# grid object for searching algorithms
class grid:

    # initialize grid class
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.end = w * h - 1
        self.mtx = [[w*i + v for v in range(h)] for i in range(w)]

    # pretty-print grid matrix
    def print(self):
        for row in self.mtx:
            print(row)

    # get index-pair of given tile
    def get_idx(self, tile):
        w = self.w
        return tile % w, tile // w 

    # get adjacent tiles to given tile
    def get_adj(self, tile):
        x, y = self.get_idx(tile)
        adj = []

        # get tile to the left
        if x > 0:
            adj.append(tile - 1)

        # get tile to the right
        if x < self.w - 1:
            adj.append(tile + 1)

        # get tile to the bottom
        if y > 0:
            adj.append(tile - self.w)

        # get tile on the top
        if y < self.h - 1:
            adj.append(tile + self.w)
        
        return adj

# depth-first search function
def search(grid, start, goal, vtd=[]):
    
    # add current tile to visited
    vtd.append(start)

    # if goal is reached then end
    if start == goal: return vtd

    # recursive dfs to find next depth
    for i in grid.get_adj(start):
        if i in vtd: continue

        # if goal is found return path
        if search(grid, i, goal, vtd):
            return vtd

    # no path to goal exists
    return None

def bfs_search(grid, start, goal, vtd=[]):
    
    # initialize the queue
    q = []
    q.append(start)
    
    while len(q) > 0:
        # pop first tile from queue
        top = q.pop(0)
        
        # add current tile to visited
        vtd.append(top)
        
        # if goal is reached then end
        if top == goal: break

        # ...
        adj = grid.get_adj(top)
        for v in grid.get_adj(top):
            if v not in q and v not in vtd:
                q.append(v)
    return vtd
        
        
    
    
grid = grid(3,3)
grid.print()

path = search(grid, 7, 4)
#print(type(path))
#print(f"DFS Path: {path}")

path2 = bfs_search(grid, 0, 4)
print(path2)