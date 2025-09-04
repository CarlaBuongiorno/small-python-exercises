from zero_to_end import zero_to_end


def test_zero_to_end_exists():
    assert zero_to_end


def test_empty_list():
    assert zero_to_end([]) == []


def test_one_item():
    assert zero_to_end([0]) == [0]


def test_two_items_zero_to_end():
    assert zero_to_end([0, 1]) == [1, 0]


def test_three_items_zero_to_end():
    assert zero_to_end([0, 1, 2]) == [1, 2, 0]


def test_four_items_zero_to_end():
    assert zero_to_end([0, 2, 0, 1]) == [2, 1, 0, 0]


def test_five_items_zero_to_end():
    assert zero_to_end([0, 2, [0], 1]) == [2, [0], 1,0]


def test_five_items_zero_to_end():
    assert zero_to_end([0, 2, [0], 1, "bob"]) == [2, [0], 1, "bob", 0]
