#! /usr/bin/env python3

import os

import bs4
import requests


def downloader(query, quantity=100, output_path=os.path.join('.', 'imgur')):
    # create output path if it doesn't already exist
    path = os.path.abspath(output_path)
    os.makedirs(path, exist_ok=True)

    # creates and downloads query url
    query_url = f'https://imgur.com/search?q={query}'
    print(f'Downloading page: {query_url}...')
    result = requests.get(query_url)
    result.raise_for_status()

    # parses result.content with bs4 to image_element
    imgur_soup = bs4.BeautifulSoup(result.content)
    image_element = imgur_soup.select('.post .image-list-link img')

    # sets quantity and generates links
    quantity = min(quantity, len(image_element))
    links = [f'https:{img.get("src")}' for img in image_element[:quantity]]

    for x, link in enumerate(links):
        # generates and downloads image urls
        image_url = f"https:{image_element[x].get('src')}"
        print(f'Downloading image: {image_url:<32}...')
        result = requests.get(image_url)
        result.raise_for_status()

        # saves images to path
        with open(os.path.join(output_path, os.path.basename(image_url)), 'wb') as image:
            for chunk in result.iter_content(1_000_000):
                image.write(chunk)

    print(f'{quantity} images downloaded successfully.')


if __name__ == '__main__':
    downloader('monday')
