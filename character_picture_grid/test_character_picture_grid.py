from character_picture_grid import character_picture_grid

simple_grid = [[1, 2],
               [3, 4]]


def test_rotate_grid():
    result = character_picture_grid.rotate_grid(simple_grid)
    assert result == [(3, 1),
                      (4, 2)]


def test_format_grid():
    assert character_picture_grid.format_grid(simple_grid) == '1 2\n3 4\n'
