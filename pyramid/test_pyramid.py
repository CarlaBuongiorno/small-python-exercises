from pyramid import pyramid_grid


def test_pyramid_exists():
    assert pyramid_grid


def test_one():
    assert pyramid_grid(1) == [[1]]


def test_three():
    assert pyramid_grid(3) == [
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]


def test_five():
    assert pyramid_grid(5) == [
        [1, 1, 1, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1],
    ]


def test_seven():
    assert pyramid_grid(7) == [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 2, 3, 3, 3, 2, 1],
        [1, 2, 3, 4, 3, 2, 1],
        [1, 2, 3, 3, 3, 2, 1],
        [1, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ]