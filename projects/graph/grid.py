def new(x, y):
    grid = []
    for i in range(x):
        row = [x*i + v for v in range(y)]
        print(row)