#! /usr/bin/env python3
# auto_unsubscriber.py - navigates to the unsubscribe link associated
#                       with any emails in the inbox

import imaplib
import webbrowser
from os import environ

import pyzmail
from bs4 import BeautifulSoup
from imapclient import IMAPClient


def get_unsubscribe_links(imap_domain, email_address, email_password):
    """
    Logs into the IMAP server with the specified credentials. After
    logging in, all messages in the inbox are searched. This function
    returns a list of links to unsubscribe from email newsletters

    :param str imap_domain: email provider's IMAP server domain name
    :param str email_address: user
    :param str email_password: password
    """
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
            links.extend(search_html_part(message=message))

    return links


def search_html_part(message):
    """
    Parses the html message using BeautifulSoup and searches for all href
    references. Any links that contain the word 'unsubscribe' are added
    to a list of unsubscribe_links along with sender names and returned

    :param PyzMessage message: email message in html
    """
    html = message.html_part.get_payload().decode(message.html_part.charset)
    soup = BeautifulSoup(html, 'html.parser')

    link_elems = soup.select('a')
    unsubscribe_links = []

    for link in link_elems:
        if 'unsubscribe' in link.text.lower():
            unsubscribe_links.append((link.get('href'),
                                      message.get_address('from')[0]))

    return unsubscribe_links


def open_links(links):
    """
    Opens all of the collected unsubscribe links individually in the browser.

    :param list links: unsubscribe links and sender names
    """
    for link, sender in links:
        print(f"Unsubscribing from: '{sender}'")
        webbrowser.open(link)


if __name__ == '__main__':
    email = environ.get('AUTO_EMAIL')
    password = environ.get('EMAIL_CREDENTIALS')

    unsub_links = get_unsubscribe_links(imap_domain='imap.gmail.com',
                                        email_address=email,
                                        email_password=password)
    open_links(links=unsub_links)
