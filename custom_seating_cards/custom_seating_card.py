import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont


def make_seating_cards(guest_list_path, directory):
    output_path = Path(guest_list_path.parent / 'seating_cards')
    output_path.mkdir(exist_ok=True)

    images = get_images(directory=directory)
    guests = guest_list_path.read_text().strip().split('\n')

    for guest in guests:
        print(f'Creating custom seating card for {guest}...')
        # add flower background
        flower = resize_image(filename=random.choice(images))
        card = Image.new('RGBA', (360, 288), 'white')
        card.paste(flower, (0, 0))

        # adds exterior border
        border = Image.new('RGBA', (364, 292), 'black')
        border.paste(card, (2, 2))

        # adds centered text and saves final image
        card = draw_text(border, guest)
        formatted_guest = guest.lower().replace(" ", "_").replace(".", "")
        card.save(output_path / f'{formatted_guest}_card.png')


def get_images(directory):
    files = []
    patterns = ('*.png', '*.jpg', '*.gif', '*.bmp')
    for pattern in patterns:
        files.extend(directory.glob(pattern))

    return files


def resize_image(filename):
    image = Image.open(filename)
    width, height = image.size
    width_factor = width / 360
    height_factor = height / 288
    return image.resize((int(width / width_factor), int(height / height_factor)))


def draw_text(image, text):
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
    image = Image.new('RGBA', image_size, 'white')
    draw = ImageDraw.Draw(image)
    return draw.textsize(text=text, font=font)


def draw_text_with_halo(image, position, text, font, halo_color, color):
    halo = Image.new('RGBA', image.size, (0, 0, 0, 0))
    ImageDraw.Draw(halo).text(position, text, font=font, fill=halo_color)
    blurred_halo = halo.filter(ImageFilter.BLUR)
    ImageDraw.Draw(blurred_halo).text(position, text=text, font=font, fill=color)
    return Image.composite(image, blurred_halo, ImageChops.invert(blurred_halo))


if __name__ == '__main__':
    guest_path = Path('./guests.txt')
    flower_dir = Path('./flower_images/')
    make_seating_cards(guest_list_path=guest_path, directory=flower_dir)
