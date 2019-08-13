import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


def make_seating_cards(guest_list_path, directory):
    """
    Creates a custom seating card for each guest on the guest list
    using a random image from the given directory as the background

    :param Path guest_list_path: path to guest list
    :param Path directory: path to directory containing invitation images
    """
    output_root = Path(guest_list_path.parent / 'seating_cards')
    output_root.mkdir(exist_ok=True)

    images = get_images(directory=directory)
    guests = guest_list_path.read_text().strip().split('\n')

    for guest in guests:
        print(f'Creating custom seating card for {guest}...')
        # add flower background
        flower = resize_image(filename=random.choice(images))
        card = Image.new(mode='RGBA', size=(360, 288), color='white')
        card.paste(im=flower, box=(0, 0))

        # adds exterior border and text
        border = Image.new(mode='RGBA', size=(366, 294), color='black')
        border.paste(im=card, box=(3, 3))
        card = draw_text(image=border, text=guest)

        # saves final image
        formatted_guest = guest.lower().replace(" ", "_").replace(".", "")
        output_path = output_root / f'{formatted_guest}_card.png'
        print(f'Saving custom seating card for {guest} as {output_path}...\n')
        card.save(output_path)


def get_images(directory):
    """
    Gets all PNG, JPG, GIF, and BMP format files at path

    :param Path directory: location to search for image files
    """
    files = []
    patterns = ('*.png', '*.jpg', '*.gif', '*.bmp')
    for pattern in patterns:
        files.extend(directory.glob(pattern))

    return files


def resize_image(filename):
    """
    Opens the image corresponding with the given filename and explicitly
    resizes the image to 360x288 (5"x4"). This function assumes the source
    image has the correct aspect ratio.

    :param Path filename: path to source image
    """
    image = Image.open(filename)
    width, height = image.size
    width_factor = width / 360
    height_factor = height / 288

    return image.resize((int(width / width_factor),
                         int(height / height_factor)))


def draw_text(image, text):
    """
    Draws the specified text on the given image. The text itself is
    centered on the image and a halo effect (border) is added to the text.

    :param Image.Image image: source image to add text to
    :param str text: text to add to the image
    """
    card_font = ImageFont.truetype('arial.ttf', 36)
    width, height = image.size
    text_width, text_height = get_text_size(image_size=image.size,
                                            text=text,
                                            font=card_font)

    text_position = (int((width - text_width) / 2),
                     int((height - text_height) / 2))

    return draw_text_with_halo(image=image,
                               position=text_position,
                               text=text,
                               font=card_font,
                               halo_color='black',
                               color='white')


def get_text_size(image_size, text, font):
    """
    Gets size of text to be added to an image (this is used to center text)

    :param tuple image_size: (width, height) of image text will be added to
    :param str text: text to be added to image
    :param ImageFont.FreeTypeFont font: font type/size for text
    """
    image = Image.new(mode='RGBA', size=image_size, color='white')
    draw = ImageDraw.Draw(image)
    return draw.textsize(text=text, font=font)


def draw_text_with_halo(image, position, text, font, halo_color, color):
    """
    Draws specified text on provided image at the given position. The text
    itself is given a halo effect (border) using the given color values

    :param Image.Image image: source image to add text to
    :param tuple position: (width, height) to position text
    :param str text: text to be added
    :param ImageFont.FreeTypeFont font: font face/point to be used
    :param str halo_color: color of exterior halo effect
    :param str color: color of interior of halo effect
    """
    halo = Image.new(mode='RGBA', size=image.size, color=(0, 0, 0, 0))
    ImageDraw.Draw(halo).text(xy=position,
                              text=text,
                              font=font,
                              fill=halo_color)

    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(xy=position,
                                      text=text,
                                      font=font,
                                      fill=color)

    return Image.composite(image1=image,
                           image2=blurred_halo,
                           mask=ImageChops.invert(blurred_halo))


if __name__ == '__main__':
    guest_path = Path('./guests.txt')
    flower_dir = Path('./flower_images/')
    make_seating_cards(guest_list_path=guest_path, directory=flower_dir)
