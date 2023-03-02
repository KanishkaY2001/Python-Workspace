def search(grid, node, goal, depth, visited):
    
    if node == goal: return [node]
    if depth == 0: return []

    visited.add(node)

    for adj in grid.get_adj(node):
        if adj in visited: continue
        path = search(grid, adj, goal, depth-1, visited.copy())
        if not path: continue
        return [node] + path
    
    return []

    # working code with iteration instead of recursion
    '''
    stack = [node]
    paths = [([node], {node})]
    visited = {node}

    while stack:
        #for i in range(len(stack)): print(f"stack [{i}]: {stack[len(stack) - i - 1]} | {paths[len(stack) - i - 1]}")
        node = stack.pop()
        path, vtd = paths.pop()

        #print(f"popping: {node} from stack | path: {path} | visited: {vtd}\n")

        if node == goal: return path

        if len(path) > limit:
            #print(f"\ndepth reached for node {node} | backtracking: {path}\n")
            continue

        visited.add(node)
        x = set(vtd)
        x.add(node)
        #print(f"adjacents: {grid.get_adj(node)}")
        for adj in grid.get_adj(node):
            if adj in vtd: 
                #print(f"not processing: {adj} because it's visited already")
                continue
            if adj in stack:
                #print(f"not processing: {adj} because it's in the stack already")
                continue
            #print(f"processing: {adj}")
            stack.append(adj)
            paths.append((path + [adj], x))
        #print("\n")

    return []
    '''
    
    
        
'''
def search(grid, node, goal, limit):
    
    stack = [(node, [node])]
    visited = set()
    cost_dict = {node: 1}

    while stack:
        #for e in stack: print(e[0], end=",")
        print(f"stack: {stack}")
        node, path = stack.pop()
        
        print(f"popping: {node} from stack | path: {path} | visited: {visited}\n")
        
        if len(path) > limit:
            cost_dict[node] = len(path)
            print(f"\ndepth reached for node {node} | backtracking: {path}\n")
            continue
        else:
            visited.add(node)

        for adj_node in grid.get_adj(node):
            if adj_node in path: continue
            if adj_node in cost_dict and len(path) + 1 >= cost_dict[adj_node]: continue
                #print(f"ignoring: {adj_node} for path: {path + [adj_node]} (len: {len(path)}) because we already have: {cost_dict[adj_node]}")
                    #continue
            new_path = path + [adj_node]
            if adj_node == goal: return new_path
            stack.append((adj_node, new_path))

    return []
'''










'''
# Initialize visited list if not already done
if visited is None:
    visited = []

# Check if goal node has been reached
if node == goal:
    return [node]

# Add current node to visited list
visited.append(node)
#print(f"node: {node} | limit: {lim} | visited: {visited}\n")

# Recurse on unvisited neighbors within limit
for adj in grid.get_adj(node):
    if adj not in visited and lim > 0:
        #print(f"parent: {node}")
        path = search(grid, adj, goal, lim-1, visited)
        if path:
            return [node] + path

# Backtrack if no path found from current node
visited.pop()
#print(f"backtracked... | visited: {visited} | lim: {lim}\n")
return []
'''
    
    



# Semi-working (very long runs, and backtracks for DFS when it's not meant to)
'''
# ...
if node == goal:
    return [node]

# ...
visited.append(node)
#print(f"node: {node} | limit: {lim} | visited: {visited}\n")

# ...
if lim == 0:
    return []

# ...
for adj in grid.get_adj(node):
    
    # ...
    if adj in visited: continue

    # ...
    #print(f"parent: {node}")
    path = search(grid, adj, goal, lim-1, visited)
    if not path:
        visited.pop()
        #print(f"backtracked... | visited: {len(visited)} | lim: {lim}\n")
        continue
    return [node] + path

# ... (this is what's returning out almost all the time) <- fix it
return []
'''