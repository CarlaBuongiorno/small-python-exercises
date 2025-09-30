def pyramid_grid(number):
    grid = []
    center_number = (number // 2) + 1 # math floor gets 2, therefore add 1 for the center number
    number_to_multiply_by = 0
    
    # This function only modifies the grid, therefore it does not need to be assigned to anything
    _function(grid, center_number, number_to_multiply_by, position_on_grid=lambda g: 0)

    # reset center_number and second list to begin creating rows after the middle row 
    center_number = number // 2
    number_to_multiply_by = 2

    _function(grid, center_number, number_to_multiply_by, position_on_grid=lambda g: len(g))
    return grid
    

def _function(grid, center_number, number_to_multiply_by, position_on_grid):
    '''This function does not need to return anything because
    all it does is modify the list in place'''
    # Find the center row and insert rows before that
        # add 3 lists together -> [numbers before center number] + [center number] + [numbers after center number]
            # first list -> range is from zero to the number before specified number
            # second list is not necessary the first iteration, therefore it is multiplied by zero
            # third list -> 3rd parameter of range (-1) - counts beackwards from the center_number
    while center_number > 0:
        row = list(range(1, center_number)) + ([center_number]*number_to_multiply_by) + list(range(center_number, 0, -1))
        grid.insert(position_on_grid(grid), row) # insert the row created above into the grid
        center_number -= 1
        number_to_multiply_by += 2 # this is for the second list to adjust the repeated number accordingly
    