from items_match import items_match


def test_items_match():
    assert items_match


def test_empty_list():
    assert items_match([]) == 0


def test_one_item_no_match():
    assert items_match([1]) == 0


def test_two_items_no_match():
    assert items_match([1, 2]) == 0


def test_three_items_match():
    assert items_match([1, 1, 2]) == 1


def test_two_items_match():
    assert items_match([1, 1]) == 2


def test_six_items_match():
    assert items_match([4, 4, 4, 5, 5, 4]) == 4


def test_first_and_last_items_match():
    assert items_match([4, 3, 2, 5, 1, 4]) == 1


def test_three_items_no_match():
    assert items_match([1, 2, 3]) == 0