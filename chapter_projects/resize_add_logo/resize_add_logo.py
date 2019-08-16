#! /usr/bin/env python3
# resize_add_logo.py - takes in images, resizes all to predefined size, then adds logo

from pathlib import Path

from PIL import Image


def get_images(path):
    """
    Gets all image files and iterates over the matches

    :param Path path: path to search for source images
    """
    files = list(path.glob('*.[pP][nN][gG]')) + list(path.glob('*.[jJ][pP][gG]'))
    files.remove(LOGO_FILENAME)

    for file in files:
        image = Image.open(file)
        filepath = Path(image.filename)
        image = resize_image(image=image)

        new_path = Path(f'{filepath.parent}/{filepath.stem}_with_logo{filepath.suffix}')
        add_logo(image=image, save_as=new_path)


def resize_image(image):
    """
    Resizes image according to SQUARE_FIT_SIZE value (if required)

    :param Image image: image to resize
    """
    width, height = image.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            width = SQUARE_FIT_SIZE
            height = int((SQUARE_FIT_SIZE / width) * height)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print(f'Resizing {image.filename}...')
        image = image.resize((width, height))
    return image


def add_logo(image, save_as):
    """
    Adds logo to bottom right corner of image and saves result as save_as

    :param Image image: image to add logo to
    :param Path save_as: path of desired output
    """
    width, height = image.size
    image.paste(logo_image, (width - logo_width, height - logo_height), logo_image)
    print(f'Saving resulting image as {save_as}')
    image.save(save_as)


if __name__ == '__main__':
    SQUARE_FIT_SIZE = 500
    LOGO_FILENAME = Path('./images/catlogo.png')

    logo_image = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_image.size
    logo_image = logo_image.resize((int(logo_width / 5), int(logo_height / 5)))
    logo_width, logo_height = logo_image.size

    get_images(path=Path('./images'))
