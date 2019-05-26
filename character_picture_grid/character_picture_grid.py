#! /usr/bin/env python3


def rotate_grid(grid):
    return list(zip(*grid[::-1]))


def format_grid(grid):
    formatted_grid = ''
    for row in grid:
        # list comprehension used to explicitly cast items to str.
        # str() converts slice to list of chars
        # this allows for the grid param to consist of non-str variables
        formatted_grid += ' '.join([str(item) for item in row]) + '\n'
    return formatted_grid


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
    print(format_grid(rotate_grid(grid)))
