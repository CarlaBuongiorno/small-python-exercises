'''Write a function that takes a grid as argument.
Every location on grid will be a number.

Return the number of elements in the grid where the
value matches either the row or column number.

Example:
  01234
 +-----
0|00000
1|00000
2|00000
3|00000
4|00000
'''

# def matching_numbers(grid):
#     match = 0
#     for row in range(len(grid)):
#         for col in range(len(grid[row])):
#             if grid[row][col] == row or grid[row][col] == col:
#                 match += 1
#     return match

def matching_numbers(grid):
    match = 0
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if item == i or item == j:
                match += 1
    return match
