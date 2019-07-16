#! /usr/bin/env python3
# text_myself.py - defines text_myself() that texts a message passed as string
from twilio.rest import Client

file = open('credentials.txt', 'r')
credentials = file.readlines()
ACCOUNT_SID, AUTH_TOKEN, twilio_number, my_cell = [item.strip() for item in credentials]


def text_myself(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(body=message, from_=twilio_number, to=my_cell)
