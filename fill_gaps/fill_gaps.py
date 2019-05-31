#! /usr/bin/env python3

import os
import re
import shutil


def get_matching_files(root, regex):
    """
    Generates a sorted list of files that match the regex pattern at
    root's destination

    :param str root: absolute path of directory to search
    :param Pattern regex: pattern of filename
    :return: sorted list of matching filenames
    """
    return sorted([file for file in os.listdir(root) if regex.match(file)])


def fill_sequence_gap(root, prefix, extension):
    """
    This function finds all file names that start with the passed
    prefix, end with the passed extension, and include a number. All of
    these matches are searched to ensure the increment sequentially
    (no missing numbers). If not, the files are renamed with the expected
    number to close the gap.

    :param str root: path of directory to search
    :param str prefix: text the filename begins with
    :param str extension: desired extension
    """
    # ensures path is absolute
    root = os.path.abspath(root)

    # ensures the '.' in the extension is optional in the formal parameter
    if extension.startswith('.'):
        extension = extension[1:]

    # builds regex with given prefix and extension to find pattern matches
    regex = re.compile(f'(^{prefix})(\\d+)(.*)?(\\.{extension}$)')
    matches = get_matching_files(root, regex)

    # where sequence begins
    start = int(regex.search(matches[0]).group(2))
    expected_num = start
    max_length = len(regex.search(matches[-1]).group(2))

    for match in matches:
        match_object = regex.search(match)  # match object to extract regex groups
        sequence_num = int(match_object.group(2))  # number of current file

        if sequence_num != expected_num:
            # if file number isn't expected, build new filename
            filename = f"{prefix}" \
                f"{'0' * (max_length - len(str(expected_num)))}" \
                f"{expected_num}" \
                f"{match_object.group(3)}" \
                f"{match_object.group(4)}"

            # rename file
            shutil.move(os.path.join(root, match), os.path.join(root, filename))
            print(f'Renaming {match} to {filename}')

        # increment expected count
        expected_num += 1


def insert_gap(root, prefix, extension, start, stop=None):
    """
    Inserts a gap in the numbering sequence of the files at the root
    destination. The files impacted will start with the given prefix,
    include a number, and end with the given extension. This function
    assumes the files have no pre-existing gap (if so, call
    fill_sequence_gap() first).

    This will insert a gap in the numbering of the filenames starting
    at the passed start value up to the stop value (non-inclusive). The
    stop value is optional - if none is provided the gap will only be one
    number.

    :param str root: path of directory to search
    :param str prefix: text the filename begins with
    :param str extension: desired extension
    :param int start: number where gap should begin (where shift starts)
    :param int stop: number where gap ends (non-inclusive)
    """
    # ensures path is absolute
    root = os.path.abspath(root)

    # ensures the '.' in the extension is optional in the formal parameter
    if extension.startswith('.'):
        extension = extension[1:]

    # builds regex with given prefix and extension to find pattern matches
    regex = re.compile(f'(^{prefix})(\\d+)(.*)?(\\.{extension}$)')
    matches = get_matching_files(root, regex)

    max_length = len(regex.search(matches[-1]).group(2))
    start_index = int(regex.search(matches[0]).group(2))
    stop_index = int(regex.search(matches[-1]).group(2))

    if not stop:
        stop = start + 1

    if start_index <= start <= stop_index:
        for match in matches[start - start_index:][::-1]:
            match_object = regex.search(match)
            new_number = int(match_object.group(2)) + stop - start
            filename = f'{prefix}' \
                f'{"0" * (max_length - len(str(new_number)))}' \
                f'{new_number}' \
                f'{match_object.group(3)}' \
                f'{match_object.group(4)}'

            shutil.move(os.path.join(root, match),
                        os.path.join(root, filename))
            print(f'Renaming {match} to {filename}')


if __name__ == '__main__':
    path = os.path.abspath('./demo_files/')
    if os.path.exists(path):
        shutil.rmtree(path)

    os.makedirs(path)

    # creates files with only odd numbers spam00<x>.txt
    for x in range(1, 25, 2):
        with open(os.path.join(path, f'spam{x:03}.txt'), 'w') as spam:
            spam.write(f'spam{x:03}')

    fill_sequence_gap(path, 'spam', '.txt')
    print()
    insert_gap(path, 'spam', '.txt', 5, 10)
