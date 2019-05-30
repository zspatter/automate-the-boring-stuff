#! /usr/bin/env python3

import os


def find_large_files(path, threshold):
    """
    Finds all files whose size is greater than or equal to threshold and
    prints their absolute path and size to the console

    :param str path: path to directory to search
    :param int threshold: size threshold in bytes
    """
    path = os.path.abspath(path)
    print(f'Searching for contents above the size: {threshold / 1_000_000:,.3f} MB'
          f'\n\tSearching {path}\n')

    for content in os.listdir(path):
        filepath = os.path.join(path, content)

        if os.path.isdir(filepath):
            size = get_dir_size(filepath)
        else:
            size = os.path.getsize(filepath)

        if size >= threshold:
            print(f'{filepath}: {size / 1_000_000:,.3f} MB')


def get_dir_size(path):
    """
    Get's the cumulative size of a directory and all of it's contents

    :param str path: absolute path to directory
    :return: int cumulative size of directroy
    """
    size = 0
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            size += os.path.getsize(filepath)

    return size


if __name__ == '__main__':
    find_large_files(os.path.join('..', '..', '..'), 1_000_000)
