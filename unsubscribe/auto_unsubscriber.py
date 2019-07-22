#! /usr/bin/env python3
import imaplib
import webbrowser
from os import environ

import pyzmail
from bs4 import BeautifulSoup
from imapclient import IMAPClient


def get_unsubscribe_links(imap_domain, email_address, email_password):
    imaplib._MAXLINE = 10_000_000
    imap = IMAPClient(imap_domain, ssl=True)
    imap.login(email_address, email_password)
    imap.select_folder('INBOX', readonly=True)

    unique_ids = imap.search(['ALL'])
    links = []

    for unique_id in unique_ids:
        raw_messages = imap.fetch([unique_id], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_messages[unique_id][b'BODY[]'])

        if message.html_part:
            links.extend(search_html_part(message))

    return links


def search_html_part(message):
    html = message.html_part.get_payload().decode(message.html_part.charset)
    soup = BeautifulSoup(html, 'html.parser')

    link_elems = soup.select('a')
    unsubscribe_links = []

    for link in link_elems:
        if 'unsubscribe' in link.text.lower():
            unsubscribe_links.append(link.get('href'))

    return unsubscribe_links


def open_links(links):
    for link in links:
        print(f'Opening link: {link}')
        webbrowser.open(link)


if __name__ == '__main__':
    email = environ.get('AUTO_EMAIL')
    password = environ.get('EMAIL_CREDENTIALS')

    unsub_links = get_unsubscribe_links(imap_domain='imap.gmail.com',
                                        email_address=email,
                                        email_password=password)
    open_links(links=unsub_links)
