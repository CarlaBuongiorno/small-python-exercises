'''Write a function that takes as a list as input and
returns that list with all the zeros moved to the end.

Example:
[1, 0, "bob", [3]] returns [1, "bob", [3], 0]
[1, [0], 0, 0, "bob", [3]] returns [1, [0] "bob", [3], 0, 0]'''


def zero_to_end(list_input):
    reordered_list = []
    zero_list = []
    for i in list_input:
        if i == 0:
            zero_list.append(i)
        else:
            reordered_list.append(i)
    return reordered_list + zero_list

        