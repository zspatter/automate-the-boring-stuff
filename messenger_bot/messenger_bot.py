from time import sleep

import pyautogui


def send_notifications(recipients, notification):
    print('5 seconds to navigate to Slack.')
    sleep(5)

    for recipient in recipients:
        send_notification(recipient=recipient, notification=notification)
        sleep(2)

    print('Done.')


def send_notification(recipient, notification):
    try:
        pyautogui.hotkey('command', 'k')
        pyautogui.typewrite(recipient)
        pyautogui.press('enter')

        if not pyautogui.locateOnScreen('active_identifier.png'):
            print(f'{recipient} is not active - message not sent.')
            return

        pyautogui.typewrite(f'{notification}\n')
        print(f'Message successfully sent to {recipient}.')

    except KeyboardInterrupt:
        print('Process quit.')


if __name__ == '__main__':
    pyautogui.PAUSE = 1

    contacts = input('Enter recipient contacts delimitted by commas: ').split(', ')
    message = input('Enter the notification message you wish to distribute: ')

    send_notifications(recipients=contacts, notification=message)
