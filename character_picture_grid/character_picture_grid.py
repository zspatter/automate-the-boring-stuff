#! /usr/bin/env python3
# character_picture_grid.py - takes a nested list input, rotates and formats the data


def rotate_grid(grid):
    """
    Rotates the input 90 degrees clockwise

    :param list grid: input with nested lists to format
    """
    return list(zip(*grid[::-1]))


def format_grid(grid):
    """
    Formats each row to represent list value delimited by spaces

    :param list grid: input with nested lists to format
    """
    formatted_grid = ''
    for row in grid:
        # list comprehension used to explicitly cast items to str
        # this allows for the grid param to consist of non-str variables
        formatted_grid += ' '.join([str(item) for item in row]) + '\n'
    return formatted_grid


if __name__ == '__main__':
    input_ = [['.', '.', '.', '.', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['.', 'O', 'O', 'O', 'O', 'O'],
              ['O', 'O', 'O', 'O', 'O', '.'],
              ['O', 'O', 'O', 'O', '.', '.'],
              ['.', 'O', 'O', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.']]
    print(format_grid(rotate_grid(input_)))
