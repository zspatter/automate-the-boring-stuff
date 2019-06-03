#! /usr/bin/env python3

import getpass
import re
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def emailer(sender, password, recipient, subject, message):
    email_regex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+      # username
            @                      # @ symbol
            [a-zA-Z0-9.-]+         # domain name
            (\.[a-zA-Z]{2,4})      # dot-something
            )''', re.VERBOSE)

    if not email_regex.match(recipient):
        print("**Invalid Email Address Provided**")
    else:
        browser = webdriver.Chrome()
        browser.set_window_size(1200, 1000)
        browser.set_window_position(0, 0)
        browser.get('https://mail.google.com')
        # browser.maximize_window()
        email_elem = browser.find_element_by_id('identifierId')
        email_elem.send_keys(sender)
        email_elem.send_keys(Keys.ENTER)
        time.sleep(3)

        # Password Login
        pass_elem = browser.find_element_by_name('password')
        pass_elem.send_keys(password)
        pass_elem.send_keys(Keys.ENTER)
        time.sleep(5)

        # click compose
        browser.find_element_by_class_name('z0').click()
        # html_elem.send_keys('C')
        time.sleep(3)

        # recipient
        to_elem = browser.find_element_by_name('to')
        to_elem.send_keys(recipient)
        time.sleep(1)

        # subject
        subject_elem = browser.find_element_by_name('subjectbox')
        subject_elem.send_keys(subject)
        time.sleep(1)

        # Message
        subject_elem.send_keys(Keys.TAB, message)
        time.sleep(1)
        subject_elem.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        time.sleep(2)
        browser.quit()


if __name__ == '__main__':
    if len(sys.argv) > 3:
        session_recipient = sys.argv[1]
        session_subject = sys.argv[2]
        session_message = ' '.join(sys.argv[3:])

        session_sender = input('Enter your gmail email: ')
        session_password = getpass.getpass('Enter your email password: ')

        emailer(session_sender,
                session_password,
                session_recipient,
                session_subject,
                session_message)
    else:
        print("Usage: command_line_emailer.py [recipient] [subject] [message]")
