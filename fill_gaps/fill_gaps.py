#! /usr/bin/env python3

import os
import re
import shutil


def get_matching_files(root, regex):
    return sorted([file for file in os.listdir(root) if regex.match(file)])


def fill_sequence_gaps(root, prefix, extension):
    # ensures path is absolute
    root = os.path.abspath(root)

    # ensures the '.' in the extension is optional in the formal parameter
    if extension.startswith('.'):
        extension = extension[1:]

    # builds regex with given prefix and extension to find pattern matches
    regex = re.compile('(^' + prefix + r')(\d+)(.*)?(\.' + extension + '$)')
    matches = get_matching_files(root, regex)

    # where sequence begins
    start = int(regex.search(matches[0]).group(2))
    expected = start
    max_length = len(regex.search(matches[-1]).group(2))

    for match in matches:
        match_object = regex.search(match)  # match object to extract regex groups
        sequence_num = int(match_object.group(2))  # number of current file

        if sequence_num != expected:
            # if file number isn't expected, build new filename
            filename = f"{prefix}" \
                f"{'0' * (max_length - len(str(sequence_num)))}" \
                f"{expected}" \
                f"{match_object.group(3)}" \
                f"{match_object.group(4)}"

            # rename file
            shutil.move(os.path.join(root, match), os.path.join(root, filename))
            print(f'Renaming {match} to {filename}')

        # increment expected count
        expected += 1


if __name__ == '__main__':
    path = os.path.abspath('./demo_files/')
    if os.path.exists(path):
        shutil.rmtree(path)

    os.makedirs(path)

    # creates files with only odd numbers spam00<x>.txt
    for x in range(1, 10, 2):
        with open(os.path.join(path, f'spam00{x}.txt'), 'w') as spam:
            spam.write(f'spam00{x}')

    fill_sequence_gaps(path, 'spam', '.txt')
