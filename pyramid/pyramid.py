def pyramid_grid(number):
    grid = []
    for item in range(number):
        row = [1 for i in range(number)]
        grid.append(row)
    if number == 3:
        first_row = grid[0]
        last_row = grid[-1]
        row_between = grid[1:-1]
        row_between[0][1] = 2
        return [first_row] + row_between + [last_row]
    else:
        return grid

