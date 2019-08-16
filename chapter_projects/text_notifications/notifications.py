#! /usr/bin/env python3
# notifications.py - defines text_myself() that texts a message passed as string

from os import environ

from twilio.rest import Client

ACCOUNT_SID = environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = environ.get('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = environ.get('TWILIO_NUMBER')
MY_NUMBER = environ.get('MY_NUMBER')


def text_myself(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)
