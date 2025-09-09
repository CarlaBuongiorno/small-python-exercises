from matching_numbers_grid import matching_numbers


def test_matching_numbers_exists():
    assert matching_numbers


def test_one_row_one_column_no_elements_match():
    assert matching_numbers([[1]]) == 0


def test_one_row_one_column_match():
    assert matching_numbers([[0]]) == 1


def test_one_row_two_columns_match():
    assert matching_numbers([[0, 0]]) == 2


def test_two_rows_one_column_match():
    assert matching_numbers([[0], [0]]) == 2


def test_two_rows_two_columns_match():
    assert matching_numbers(
        [[0, 0],
         [0, 0]]
    ) == 3


def test_five_rows_five_columns_match():
    assert matching_numbers(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
    ) == 9


def test_two_rows_two_columns_two_match():
    assert matching_numbers(
        [
            [0, 1],
            [2, 3]
        ]
) == 2