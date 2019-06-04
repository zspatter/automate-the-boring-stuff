#! /usr/bin/env python3

import bs4
import requests


def verify_links(url):
    """
    Verifies all links within the page at the provided url. Broken links are
    printed and counted.

    :param str url: address to website to verify links
    """
    result = requests.get(url)

    try:
        result.raise_for_status()
    # if url cannot be accessed, exit
    except requests.exceptions.HTTPError as e:
        print(f'There was a problem with the provided URL: \n\t{e}')
        exit()

    # builds soup and filters for http links
    soup = bs4.BeautifulSoup(result.content, features='lxml')
    links = [link.get('href') for link in soup.select('a') if link.get('href')]
    http_links = list(filter(lambda x: (x.startswith('http')), links))

    broken_links = 0
    not_found = 0

    # iterates through collected http links
    for link in http_links:
        result = requests.get(link)

        try:
            result.raise_for_status()
        # if there's an HTTP error, print the link and increment counters
        except requests.exceptions.HTTPError as e:
            if result.status_code == 404:
                not_found += 1

            print(f'{e}')
            broken_links += 1

    # summary of link verification
    print(f"\nOf the {len(http_links)} links found at {url}, {broken_links}"
          f" links could not be accessed."
          f"\n\tOf the inaccessible links, {not_found} had a "
          f"'HTTP 404 Not Found' status code.")


if __name__ == '__main__':
    verify_links('https://nostarch.com')
