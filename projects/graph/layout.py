# grid object for searching algorithms
class grid:

    # initialize grid class
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.end = w * h - 1
        self.mtx = [[w*i + v for v in range(w)] for i in range(h)]

    # pretty-print grid matrix
    def print(self):
        for row in self.mtx:
            print(row)
    
    # check if a tiles exists in grid
    def valid_pair(self, t1, t2):
        return self.valid(t1) and self.valid(t2)

    # check if a tile exists in grid
    def valid(self, tile):
        x, y = self.get_idx(tile)
        return 0 <= y < self.h and 0 <= x < self.w

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