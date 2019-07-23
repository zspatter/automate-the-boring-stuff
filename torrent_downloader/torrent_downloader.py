#! /usr/bin/env python3

import imaplib
import json
import subprocess
from os import environ

from imapclient import IMAPClient
from notifications import text_myself
from pyzmail import PyzMessage


def check_for_torrents(imap_domain, email_address, email_password, verification):
    imaplib._MAXLINE = 10_000_000
    imap = IMAPClient(imap_domain, ssl=True)
    imap.login(email_address, email_password)
    imap.select_folder('INBOX')
    unique_ids = imap.search(['SUBJECT', 'download', 'FROM', verification['email']])

    if unique_ids:
        links, remove_ids = check_emails(imap, unique_ids, verification)
        delete_instruction_emails(imap=imap, remove_ids=remove_ids)
        return links


def check_emails(imap, unique_ids, verification):
    instructions, remove_ids = [], []

    for unique_id in unique_ids:
        raw_messages = imap.fetch([unique_id], ['BODY[]'])
        message = PyzMessage.factory(raw_messages[unique_id][b'BODY[]'])
        text = message.text_part.get_payload().decode(message.text_part.charset)

        if verification['verification'] in text:
            if message.html_part:
                body = message.html_part.get_payload().decode(message.html_part.charset)
            if message.text_part:
                body = message.text_part.get_payload().decode(message.text_part.charset)

            instructions.append(body)
            remove_ids.append(unique_id)

    return instructions, remove_ids


def delete_instruction_emails(imap, remove_ids):
    if remove_ids:
        imap.delete_messages(remove_ids)
        imap.expunge()

    imap.logout()


def parse_email_body(email_body, torrent_client):
    lines = email_body.split('\n')
    for line in lines:
        if line.startswith('magnet:?'):
            print(line)
            subprocess.Popen(f'{torrent_client} {line}')
            text_myself(message=f'Downloading magnet link: {line}')


if __name__ == '__main__':
    TORRENT_CLIENT = 'path'
    EMAIL = environ.get('AUTO_EMAIL')
    PASSWORD = environ.get('EMAIL_CREDENTIALS')
    TORRENT_VERIFICATION = json.loads(environ.get('TORRENT_VERIFICATION'))

    instruction_emails = check_for_torrents(imap_domain='imap.gmail.com',
                                            email_address=EMAIL,
                                            email_password=PASSWORD,
                                            verification=TORRENT_VERIFICATION)
    for instruction_email in instruction_emails:
        parse_email_body(email_body=instruction_email,
                         torrent_client=TORRENT_CLIENT)
