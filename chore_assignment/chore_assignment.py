#! /usr/bin/env python3

import random
import smtplib
from os import environ


def allocate_chores(chores, emails):
    chore_assignments = dict()

    for email in email_generator(emails):
        if not chores:
            break
        chore_assignment = random.choice(chores)
        chores.remove(chore_assignment)
        chore_assignments.setdefault(email, [])
        chore_assignments[email].append(chore_assignment)

    email_assigned_chores(chore_assignments)


def email_generator(emails):
    while True:
        random.shuffle(emails)
        yield from emails
        print()


def email_assigned_chores(chore_assignments):
    email = environ.get('AUTO_EMAIL')
    password = environ.get('EMAIL_CREDENTIALS')

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password)

    for recipient, chores in chore_assignments.items():
        message = f'Subject: Chore Assignments' \
            f'\nGreetings,' \
            f'\n\nYour assigned chores are: {format_chores(chores)}.'

        sendmail_status = smtp.sendmail(email, recipient, message)

        if sendmail_status != {}:
            print(f'There was a problem sending an email to {recipient} - {sendmail_status}')

    smtp.quit()


def format_chores(chores):
    if len(chores) == 1:
        return f'{chores[0]}'
    elif len(chores) == 2:
        return f'{chores[0]} and {chores[1]}'
    else:
        chores[-1] = 'and ' + chores[-1]
        return f"{', '.join(chores)}"


if __name__ == '__main__':
    chore_list = ['wash dishes', 'clean bathroom', 'vacuum', 'walk the dog',
                  'take out the trash', 'take out the recycling' 'get the mail',
                  'clean the fish tank', 'cook dinner', 'set the table']
    email_list = ['resident01@example.com', 'resident02@example.com',
                  'resident03@example.com', 'resident04@example.com']
    
    allocate_chores(chores=chore_list, emails=email_list)
