'''Write a function that takes a list as input and 
returns the number of times each item matches the item to the right.
The last item is compared to the first item.

Example:
[1, 1, 2]
[1, 1]
[1]
[4, 4, 4, 5, 5, 4]'''


def items_match(input_list):
    count = 0
    if len(input_list) > 1 and input_list[-1] == input_list[0]:
        count += 1
    for i, item in enumerate(input_list):
        if i + 1 < len(input_list) and item == input_list[i+1]:
            count += 1
    return count
