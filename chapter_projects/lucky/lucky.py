#! /usr/bin/env python3
# lucky.py - Opens several Google search results
# Usage - arguments passed are used as search terms - if no arguments are
#       provided, clipboard contents are used instead

import sys
import webbrowser

import bs4
import pyperclip
import requests

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search = " ".join(sys.argv[1:])
    else:
        search = pyperclip.paste()

    # searches for keywords
    print('Googling...')
    res = requests.get('http://google.com/search?q=' + search)
    res.raise_for_status()

    # creates soup from search results
    google_soup = bs4.BeautifulSoup(res.content, features='html.parser')
    results = google_soup.select('div a', class_='r', href=True)

    # list of valid link results
    links = []
    for result in results:
        # filters for href
        link_href = result.get('href')
        # ensures links are search results
        if "/url?q=" in link_href and "webcache" not in link_href:
            # ensures links are unique
            if not any(link_href[:50] in previous for previous in links) \
                    and 'accounts.google' not in link_href:
                links.append(link_href)

    # opens x results
    page_count = min(5, len(links))
    print(f'Opening {page_count} tabs with search results.')
    for x in range(page_count):
        webbrowser.open('https://google.com' + links[x])
