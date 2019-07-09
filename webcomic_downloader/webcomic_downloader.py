#! /usr/bin/env python3

import os
import shelve
from os.path import abspath, join, basename

import bs4
import requests


def check_buttersafe(root=join(abspath('.'), 'webcomics'), previous_date=None):
    """
    Checks buttersafe's home page for current comic. If A previous date
    is provided, all comics with a different date will be downloaded. If
    no previous date is provided, the most recent comic is downloaded.

    :param str root: path to save images to
    :param str previous_date: most recently downloaded comic's upload date
    :return: date of most recent comic
    """
    os.makedirs(root, exist_ok=True)

    try:
        res = requests.get('https://www.buttersafe.com', headers=headers)
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('Error downloading webpage https://www.buttersafe.com/')
        print(e)
        return previous_date

    soup = bs4.BeautifulSoup(res.text, features='lxml')
    date_elem = soup.select('#headernav-date')
    latest_date = date_elem[0].text.strip()
    current_date = latest_date

    if not previous_date:
        print('First ever request')
        download_buttersafe_comic(soup, root)
        print(f'\nThe most recent buttersafe comic has been saved to:'
              f'\n\t{join(basename(root), "[filename]")}')
    else:
        print('Starting chron check...')
        if previous_date == current_date:
            print('No updates available for buttersafe...')
            return latest_date
        else:
            while current_date != previous_date:
                download_buttersafe_comic(soup, root)
                current_date, soup = get_previous_butterface(soup)
            print(f'\nAll buttersafe comics published after {previous_date} '
                  f'have been saved to: {join(basename(root), "[filename]")}')

    return latest_date


def get_previous_butterface(soup):
    """
    Downloads previous page and extracts date of upload

    :param BeautifulSoup soup: parsed html webpage
    :return: date and soup of previous page
    """
    prev_link = soup.select('#headernav > a')[0]
    url = prev_link.get('href')
    print(f'Downloading webpage {url}...')
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, features='lxml')
        date_elem = soup.select('#headernav-date')
        date = date_elem[0].text.strip()
        return date, soup
    except requests.exceptions.HTTPError:
        print(f'Error downloading webpage {url}')


def download_buttersafe_comic(soup, root):
    """
    Extracts image url from site parsed with BeautifulSoup. This image
    is downloaded and saved to root

    :param BeautifulSoup soup: parsed html webpage
    :param str root: path to save image to
    """
    image_url = soup.select('#comic > img')[0].get('src')
    print(f'Downloading image {image_url}...')
    try:
        res = requests.get(image_url, headers=headers)
        res.raise_for_status()
        with open(join(root, basename(image_url)), 'wb') as image:
            for chunk in res.iter_content(100_000):
                image.write(chunk)
    except requests.exceptions.HTTPError:
        print(f'Error downloading image {image_url}')


def check_comics():
    """
    Wrapper function used to check for recently published items. This
    function is included to allow other comic downloaders to be added
    to the script in the future.
    """
    shelf = shelve.open('previous_dates')

    if 'butterface' not in shelf:
        shelf['butterface'] = check_buttersafe()
    else:
        shelf['butterface'] = check_buttersafe(previous_date=shelf['butterface'])


if __name__ == '__main__':
    headers = {'User-Agent': 'Custom user agent'}
    check_comics()
