#! /usr/bin/env python3
# selective_copy.py - TODO generator?

import os
import re
import shutil


def selective_copy(source, destination_path, extension):
    directory = os.path.abspath(destination_path)

    # if destination doesn't exist, it's created
    if not os.path.exists(directory):
        os.makedirs(directory)

    # walks entire tree from source directory
    for root, _, files in os.walk(os.path.abspath(source)):
        print(f'\nSearching in {root}')

        # iterates over each file
        for filename in files:
            # if it matches desired extension
            if filename.endswith(extension):
                filepath = os.path.join(root, filename)
                destination_path = directory

                # skip if source of file is destination
                if os.path.dirname(filepath) == directory:
                    continue

                # if file of this name exists in destination
                if os.path.exists(os.path.join(destination_path, filename)):
                    regex = re.compile(f'(.*)(_\\d+)?({extension})')

                    increment = 1
                    check_name = os.path.join(directory,
                                              f'{regex.search(filename).group(1)}'
                                              f'_{increment}{extension}')

                    # increment filename until name is unique
                    while os.path.exists(check_name):
                        check_name = os.path.join(directory,
                                                  f'{regex.search(filename).group(1)}'
                                                  f'_{increment}{extension}')
                        increment += 1

                    destination_path = check_name

                # move file to destination
                shutil.copy(filepath, destination_path)
                print(
                    f'\tCopied {os.path.basename(filepath)} to {os.path.abspath(destination_path)}')


if __name__ == '__main__':
    selective_copy(source='..', destination_path='./matches/', extension='.txt')
