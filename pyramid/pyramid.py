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


def pyramid_grid(number): # 5
    grid = []
    center_number = (number // 2) + 1 # math floor gets 2, therefore add 1 for the center number
    number_to_multiply_by = 0

    # Find the center row and insert rows before that
    while center_number > 0: # center_number = 3
        # add 3 lists together -> [numbers before center number] + [center number] + [numbers after center number]
            # first list -> range is from zero to the number before specified number
            # second list is not necessary the first iteration, therefore it is multiplied by zero
            # third list -> 3rd parameter of range (-1) - counts beackwards from the center_number
        center_row = list(range(1, center_number)) + ([center_number]*number_to_multiply_by) + list(range(center_number, 0, -1))
        grid.insert(0, center_row) # insert the row created above into the grid
        center_number -= 1 # minus 1 from the current number
        number_to_multiply_by += 2 # this is for the second list to adjust the repeated number accordingly
    
    # reset center_number and second list to begin creating rows after the middle row 
    center_number = (number // 2)
    number_to_multiply_by = 2

    # Append rows after the center row
    while center_number > 0:
        row = list(range(1, center_number)) + ([center_number]*number_to_multiply_by) + list(range(center_number, 0, -1))
        grid.append(row) # append the row created above into the grid
        center_number -= 1 # minus 1 from the current number
        number_to_multiply_by += 2

    return grid
    