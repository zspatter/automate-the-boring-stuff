#! /usr/bin/env python3

import imaplib
import subprocess
from notifications import text_myself
from os import environ
from pathlib import Path

from imapclient import IMAPClient
from pyzmail import PyzMessage


def check_for_torrents(imap_domain, email_address, email_password, verification):
    """
    Logs into the specified email address with the given credentials. Then
    gathers all unique ids for emails in the inbox that include "download"
    the subject line AND are sent from the address specified in the
    verification structure.

    :param str imap_domain: email provider's IMAP server domain name
    :param str email_address: user email
    :param str email_password: email password
    :param dict verification: structure including 2 entries - an email
                address corresponding to the sender and a passphrase
                included in the message body
    """
    imaplib._MAXLINE = 10_000_000
    imap = IMAPClient(imap_domain, ssl=True)
    imap.login(email_address, email_password)
    imap.select_folder('INBOX')
    unique_ids = imap.search(['FROM', verification['email'], 'SUBJECT', 'download'])

    if unique_ids:
        links, remove_ids = check_emails(imap, unique_ids, verification)
        delete_instruction_emails(imap=imap, remove_ids=remove_ids)
        return links


def check_emails(imap, unique_ids, verification):
    """
    Check the email body for all unique ids searching for the passphrase
    stored in the verification variable. If the message contains the passphrase,
    the body of the message and unique id are added to respective collections
    (and returned)

    :param IMAPClient imap: session with user logged in
    :param list unique_ids: unique ids corresponding with search matches
    :param dict verification: structure including 2 entries - an email
                address corresponding to the sender and a passphrase
                included in the message body
    """
    instructions, remove_ids = [], []

    for unique_id in unique_ids:
        raw_messages = imap.fetch([unique_id], ['BODY[]'])
        message = PyzMessage.factory(raw_messages[unique_id][b'BODY[]'])
        text = message.text_part.get_payload().decode('ascii')

        if verification['passphrase'] in text:
            if message.html_part:
                body = message.html_part.get_payload().decode(message.html_part.charset)
            if message.text_part:
                body = message.text_part.get_payload().decode(message.text_part.charset)

            instructions.append(body)
            remove_ids.append(unique_id)

    return instructions, remove_ids


def delete_instruction_emails(imap, remove_ids):
    """
    Deletes all emails that matched the search AND contained the expected passphrase

    :param IMAPClient imap: session with user logged in
    :param list remove_ids: unique ids corresponding with valid instructional emails
    """
    if remove_ids:
        imap.delete_messages(remove_ids)
        imap.expunge()

    imap.logout()


def parse_email_body(email_body, client_path):
    """
    Parses email body to extract magnet link. Once the link is found,
    the torrent client is launched and begins downloading the torrent.
    After the download completes, a confirmation SMS message is sent.

    :param str email_body: body of the email
    :param Path client_path: path to torrent client
    """
    lines = email_body.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            torrent_process = subprocess.Popen([client_path, line])
            torrent_process.wait()
            # removes trackers with torrent info from shared magnet link
            text_myself(message=f'Finished downloading the following torrent: '
                                f'\n\n{line[0:line.find("&")]}')


if __name__ == '__main__':
    TORRENT_CLIENT = Path('/Applications/qbittorrent.app/Contents/MacOS/qbittorrent')
    EMAIL = environ.get('AUTO_EMAIL')
    PASSWORD = environ.get('EMAIL_CREDENTIALS')
    BOT_VERIFICATION = {'email':      environ.get('TORRENT_EMAIL'),
                        'passphrase': environ.get('TORRENT_PASSPHRASE')}

    instruction_emails = check_for_torrents(imap_domain='imap.gmail.com',
                                            email_address=EMAIL,
                                            email_password=PASSWORD,
                                            verification=BOT_VERIFICATION)
    if instruction_emails:
        for instruction_email in instruction_emails:
            parse_email_body(email_body=instruction_email,
                             client_path=TORRENT_CLIENT)
