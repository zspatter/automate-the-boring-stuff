#! /usr/bin/env python3
# selective_copy.py - selectively copies a specific filetype's matched
#                   files to a destination directory (renaming as needed)

import os
import re
import shutil
from pathlib import Path


def selective_copy(source, destination_path, extension):
    """
    Selectively copies files of the extension's type from the source
    path to the destination path renaming the files as needed (sequentially)

    :param str source: path to directory to search (recursively)
    :param str destination_path: path to output directory
    :param str extension: desired filetype's extension
    """
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
                    regex = re.compile(f'(.*?)(_\\d+)?({extension})')

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


def simple_selective_copy(source, destination, extension):
    """
    Selectively copies files of the extension's type from the source
    path to the destination path renaming the files as needed (sequentially)

    :param Path source: path to directory to search (recursively)
    :param Path destination: path to output directory
    :param str extension: desired filetype's extension
    """
    matches = list(source.rglob(pattern=f'*{extension}'))
    destination.mkdir(exist_ok=True)

    for match in matches:
        new_path = destination / match.name

        if match.parent.resolve() == destination.resolve():
            continue

        if new_path.exists():
            regex = re.compile(f'(.*?)(_\\d+)?({extension})', re.IGNORECASE)
            regex_match = regex.search(new_path.name)
            increment = int(regex_match.group(2)) + 1 if regex_match.group(2) else 1

            while new_path.exists():
                new_path = destination / f'{regex_match.group(1)}_{increment}{new_path.suffix}'
                increment += 1

        shutil.copy(src=f'{match}', dst=f'{new_path}')
        print(f'Copied "{match}" to "{new_path}"')


if __name__ == '__main__':
    # selective_copy(source='.', destination_path='./matches/', extension='.txt')
    simple_selective_copy(source=Path('.'), destination=Path('./matches/'), extension='.txt')
