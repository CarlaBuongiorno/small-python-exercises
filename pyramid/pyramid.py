# def pyramid_grid(number):
#     grid = []
#     for item in range(number):
#         row = [1 for i in range(number)]
#         grid.append(row)
#     if number == 3:
#         first_row = grid[0]
#         last_row = grid[-1]
#         row_between = grid[1:-1]
#         row_between[0][1] = 2
#         return [first_row] + row_between + [last_row]
#     else:
#         return grid

# def pyramid_grid(number): # 3
#     grid = [list(range(1, number)) + list(range(number, 0, -1)) for item in range(number)]
#     print(grid)

#     return grid


# def pyramid_grid(number): # 3
#     grid = []

#     for item in range(number):
#         row = [1 for i in range(number)]
#         grid.append(row)

#     middle_row = grid[number//2]
#     for i in middle_row:
#         list(range(1, number)) + list(range(number, 0, -1))


#     mid_grid_index = grid[number//2]
#     print('mid_grid_index', mid_grid_index)

#     print('number: ', number//2)
#     mid_row_index = row[number//2]
#     print(mid_row_index)

#     return grid

# def pyramid_grid(number): # 3
#     grid = []

#     for row_number in range(number):
#         row = []
#         for column_num in range(number):
#             value = min(row_number, column_num, number - 1 - row_number, number - 1 - column_num) + 1
#             row.append(value)
#         grid.append(row)
#     print(grid)
#     return grid



def pyramid_grid(number): # 3
    grid = []
    center_number = (number // 2) + 1
    print('center_number: ', center_number)

    number_to_multiply_by = 0

    while center_number > 0:
        center_row = list(range(1, center_number)) + ([center_number]*number_to_multiply_by) + list(range(center_number, 0, -1))
        grid.insert(0, center_row)
        center_number -= 1
        number_to_multiply_by += 2
    
    center_number = (number // 2)
    number_to_multiply_by = 2

    while center_number > 0:
        row = list(range(1, center_number)) + ([center_number]*number_to_multiply_by) + list(range(center_number, 0, -1))
        grid.append(row)
        center_number -= 1
        number_to_multiply_by += 2

    print('grid: ', grid)
    return grid
    