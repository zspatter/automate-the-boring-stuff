from time import sleep

import pyautogui


def send_notifications(recipients, notification):
    """
    Distributes notification to each recipient individually

    :param list recipients: all recipients to receive notification
    :param str notification: message to distribute via IM
    """
    print('5 seconds to navigate to Slack.')
    sleep(5)

    for recipient in recipients:
        send_notification(recipient=recipient, notification=notification)
        sleep(2)

    print('Done.')


def send_notification(recipient, notification):
    """
    Distributes notification to individual recipient by first searching
    for recipient, then checking recipient's status (availability).
    Assuming the recipient is available the message is sent.

    :param str recipient: recipient username
    :param str notification: message to distribute via IM
    """
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
