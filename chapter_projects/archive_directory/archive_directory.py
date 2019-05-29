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
    :return:
    """
    # gathers absolute path and determines length of path to parent directory
    directory = os.path.abspath(directory)
    path_length = len(os.path.dirname(directory))
    filename = os.path.basename(directory) + '.zip'

    # creates a .zip with the same name as the directory
    print(f'Creating {filename}\n')
    archive = zipfile.ZipFile(filename, 'w')

    # walks entire tree
    for dir_name, sub_dirs, filenames in os.walk(directory):
        # add current directory to zip
        print(f'Adding files in {dir_name}\n')

        # add all the files in this directory to the zip (truncates absolute path)
        for filename in filenames:
            filepath = os.path.join(dir_name, filename)
            archive.write(filepath, filepath[path_length:])

    archive.close()
    print('Done.')


if __name__ == "__main__":
    archive_directory('..')
