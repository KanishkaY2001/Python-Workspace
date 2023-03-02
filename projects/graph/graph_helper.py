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