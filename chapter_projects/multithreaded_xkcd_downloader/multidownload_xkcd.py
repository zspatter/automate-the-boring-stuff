#! /usr/bin/env python3
# multidownload_xkcd.py - downloads XKCD comics using multiple threads

import os
import re
import threading

import bs4
import requests

ANSI_RED = '\033[31;m'
ANSI_RESET = '\033[0m'


def scrape_xkcd(start_num, end_num):
    if start_num < 1:
        start_num = 1
    for comic_num in range(start_num, end_num - 1, -1):
        print(f"{'Downloading page:':<19} https://xkcd.com/{comic_num}...")
        try:
            res = requests.get(f'https://xkcd.com/{comic_num}')
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            continue

        soup = bs4.BeautifulSoup(res.content, features='lxml')
        comic_element = soup.select('#comic img')

        # find the URL of the comic image
        if not comic_element:
            print(f'\n{ANSI_RED}Could not find comic image.{ANSI_RESET}\n')
        else:
            download_image(comic_element)


def download_image(comic_element):
    # download the image
    comic_url = f'https:{comic_element[0].get("src")}'
    print(f"{'Downloading image:':<19} {comic_url}...")
    try:
        res = requests.get(comic_url)
        res.raise_for_status()

        # save the image locally
        with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image:
            for chunk in res.iter_content(100_000):
                image.write(chunk)
    except requests.exceptions.MissingSchema:
        # skip this comic
        print(f'\n{ANSI_RED}An error occurred while downloading the image at {comic_url}'
              f'\n\tThis comic is being skipping and will not be downloaded{ANSI_RESET}\n')


def get_latest_comic_number(comic_num=2101):
    try:
        # download homepage
        homepage = requests.get('https://xkcd.com/')
        homepage.raise_for_status()
    except requests.exceptions.HTTPError:
        return comic_num

    regex = re.compile(r'\nPermanent link to this comic: https://xkcd.com/(\d+)/')
    match = regex.search(homepage.text)
    if match:
        comic_num = int(match.group(1))

    return comic_num


def download_all_comics(output_path='xkcd_comics'):
    # create directory for output
    os.makedirs(output_path, exist_ok=True)
    threads = []

    # create threads for downloading
    for x in range(get_latest_comic_number(), 0, -100):
        download_thread = threading.Thread(target=scrape_xkcd, args=(x, x - 99))
        threads.append(download_thread)
        download_thread.start()

    # wait for all threads to end
    for thread in threads:
        thread.join()

    print(f'\nAll successfully downloaded images have been saved to the /xkcd_comics/ directory.'
          f'\nDone.')


if __name__ == '__main__':
    download_all_comics()
