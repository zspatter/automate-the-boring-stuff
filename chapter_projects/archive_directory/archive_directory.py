#! /usr/bin/env python3
# archive_directory.py - Copies an entire directory and its contents into a
#       ZIP file whose filename increments

import os
import zipfile


def archive_directory(directory):
    """
    Compresses the passed directory and all of it's contents to a zip.
    This function takes special care to ignore the preceding absolute path.

    :param str directory: path to directory to compress
    """
    # gathers absolute path and determines length of path to parent directory
    directory = os.path.abspath(directory)
    path_length = len(os.path.dirname(directory))
    filename = os.path.basename(directory) + '.zip'

    # if filename already exists, increment the filename
    if os.path.exists(filename):
        increment = 1
        basename = os.path.basename(directory)

        while True:
            check_name = basename + '_' + str(increment) + '.zip'
            if not os.path.exists(check_name):
                break
            increment += 1

        filename = check_name

    # creates a .zip with the same name as the directory
    print(f'Creating {filename}\n')
    archive = zipfile.ZipFile(filename, 'w')

    # walks entire tree
    for root, _, files in os.walk(directory):
        # add current directory to zip
        print(f'Adding files in {root}\n')

        # add all the files in this directory to the zip (truncates absolute path)
        for file in files:
            # excludes previous zips of same directory from archive
            if file.startswith(os.path.basename(directory)):
                continue

            # writes contents to .zip
            filepath = os.path.join(root, file)
            archive.write(filepath, filepath[path_length:])

    archive.close()
    print('Done.')


if __name__ == "__main__":
    archive_directory(directory='..')
