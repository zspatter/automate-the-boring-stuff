#! /usr/bin/env python3
# xkcd_downloader.py - Downloads every single XKCD comic

import os

import bs4
import requests

ANSI_RED = '\033[31;m'
ANSI_RESET = '\033[0m'

if __name__ == '__main__':
    # store comics in ./xkcd_comics/
    url, comic_url = 'http://xkcd.com', ''
    os.makedirs('xkcd_comics', exist_ok=True)

    # while there is a previous comic/link
    while not url.endswith('#'):
        # download webpage
        print(f"{'Downloading page:':<19} {url}...")
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.content, features='lxml')
        comic_element = soup.select('#comic img')

        # find the URL of the comic image
        if not comic_element:
            print(f'\n{ANSI_RED}Could not find comic image.{ANSI_RESET}\n')
        else:
            try:
                # download the image
                comic_url = f'http:{comic_element[0].get("src")}'
                print(f"{'Downloading image:':<19} {comic_url}...")
                res = requests.get(comic_url)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                # skip this comic
                print(f'\n{ANSI_RED}An error occurred while downloading the image at {comic_url}'
                      f'\n\tThis comic is being skipping and will not be downloaded{ANSI_RESET}\n')
                prev_link = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prev_link.get('href')
                continue

        # save the image locally
        with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image:
            for chunk in res.iter_content(100_000):
                image.write(chunk)

        # generate link for previous comic
        prev_link = soup.select('a[rel="prev"]')[0]
        url = f'http://xkcd.com{prev_link.get("href")}'

    print('Done.')
