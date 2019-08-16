#! /usr/bin/env python3
# find_photo_folders.py - finds all folders that contain >50% image files

from pathlib import Path

from PIL import Image


def find_photo_folders(root):
    """
    Finds all folders containing more image files that non-image files
    and prints the corresponding absolute paths.

    Image files are only considered an image if they are PNG, JPG, GIF, or BMP
    format and at least 500x500 in size

    :param Path root: root of the path to search recursively
    """
    directories = get_subdirectories(path=root)
    print(f'Searching for photo folders recursively in: {root.resolve()}...\n')

    for directory in directories:
        file_count = len([file for file in directory.iterdir() if file.is_file()])
        images = get_images(path=directory)

        for filename in images:
            try:
                image = Image.open(filename)
            except OSError:
                continue

            width, height = image.size

            if width < 500 or height < 500:
                images.remove(filename)

        image_count = len(images)
        if image_count > file_count - image_count:
            print(directory.resolve())


def get_subdirectories(path):
    """
    Gets list of all directories contained within path recursively
    (including root)

    :param Path path: path to search
    """
    return list(path.rglob('./'))


def get_images(path):
    """
    Gets list of all images within the directory at path

    :param Path path: path to search
    """
    files = []
    patterns = ('*.png', '*.jpg', '*.gif', '*.bmp')
    for pattern in patterns:
        files.extend(path.glob(pattern))

    return files


if __name__ == '__main__':
    find_photo_folders(root=Path('../..'))
