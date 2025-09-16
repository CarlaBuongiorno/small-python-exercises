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