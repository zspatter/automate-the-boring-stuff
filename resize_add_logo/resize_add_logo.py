#! /usr/bin/env python3
# resize_add_logo.py -

from pathlib import Path

from PIL import Image


def resize_and_add_logos(path, logo_path, scaling_factor):
    """
    Gathers all image files at path's location, resizes the images and
    adds a logo (as long as the logo is smaller) and saves the new images
    under a new name within a new subdirectory of path.

    :param Path path: path to images
    :param Path logo_path: logo image to add to all images
    :param float scaling_factor: scaling factor for resizing logo image
    """
    files = get_image_files(path)
    files.remove(logo_path)
    logo = resize_logo(logo=Image.open(logo_path), scaling_factor=scaling_factor)
    Path(path / 'with_logo').mkdir(exist_ok=True)

    for file in files:
        image = Image.open(file)
        filepath = Path(image.filename)
        image = resize_image(image=image)

        new_path = Path(f'{filepath.parent}/with_logo/{filepath.stem}_with_logo{filepath.suffix}')
        add_logo(image=image, logo=logo, save_as=new_path)


def get_image_files(path):
    """
    Gets all PNG, JPG, GIF, and BMP format files at path

    :param Path path: location to search for image files
    """
    files = []
    patterns = ('*.png', '*.jpg', '*.gif', '*.bmp')
    for pattern in patterns:
        files.extend(path.glob(pattern))

    return files


def resize_logo(logo, scaling_factor):
    """
    Scales the logo image according to the scaling factor

    :param Image.Image logo: image for the logo
    :param float scaling_factor: scaling factor for resizing logo image
    """
    width, height = logo.size
    return logo.resize((int(width * scaling_factor), int(height * scaling_factor)))


def resize_image(image):
    """
    Resizes image according to SQUARE_FIT_SIZE value (if required)

    :param Image.Image image: image to resize
    """
    width, height = image.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            width = SQUARE_FIT_SIZE
            height = int((SQUARE_FIT_SIZE / width) * height)
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print(f'Resizing "{image.filename}"...')
        image = image.resize((width, height))
    return image


def add_logo(image, logo, save_as):
    """
    Adds logo to bottom right corner of image and saves result as save_as

    :param Image.Image image: image to add logo to
    :param Path save_as: path of desired output
    """
    width, height = image.size
    logo_width, logo_height = logo.size
    if width >= logo_width * 2 and height >= logo_height * 2:
        image.paste(logo, (width - logo_width, height - logo_height), logo)
        print(f'Saving resulting image as "{save_as}"...')
        image.save(save_as)
    else:
        print(f'The logo is too large in comparison to "{save_as.name}", so it will be skipped.')


if __name__ == '__main__':
    SQUARE_FIT_SIZE = 500
    LOGO_FILENAME = Path('./images/catlogo.png')

    resize_and_add_logos(path=Path('./images'), logo_path=LOGO_FILENAME, scaling_factor=.2)
