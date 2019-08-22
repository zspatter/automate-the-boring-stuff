#! /usr/bin/env python3
# looking_busy.py - simple script that simulates user input to keep IM status active

import random
from datetime import datetime, time, timedelta
from time import sleep

import pyautogui


def simulated_input(interval):
    x = random.randint(a=-10, b=10)
    y = random.randint(a=-10, b=10)

    pyautogui.moveRel(xOffset=x, yOffset=y, duration=random.uniform(a=0.1, b=0.5))
    pyautogui.moveRel(xOffset=-x, yOffset=-y, duration=random.uniform(a=0.1, b=0.5))
    pyautogui.press(f'f{random.randint(15, 24)}')

    sleep(random.randint(a=interval // 2, b=interval))


def look_busy(interval=60):
    """
    Nudges the mouse by random x and y values (-10 to 10), then returns
    the mouse to it's original position. The duration of these moves is
    a random time value between 0.1 and 0.5 seconds.

    A function key bound to no action is chosen at random to simulate keyboard input

    :param float interval: max interval between mouse nudges
    """
    print('Press CTRL-C to quit.\n')
    try:
        while True:
            simulated_input(interval=interval)

    except KeyboardInterrupt:
        print('Process quit.')


def look_busy_until(interval=60, until=time(hour=10, minute=15)):
    try:
        while datetime.now().time() < until:
            simulated_input(interval=interval)

        pyautogui.hotkey('win', 'l')
    except KeyboardInterrupt:
        print('Process quit.')


def look_busy_for(interval=60, duration=timedelta(hours=1, minutes=30)):
    end = datetime.now() + duration

    try:
        while datetime.now() < end:
            simulated_input(interval=interval)

        pyautogui.hotkey('win', 'l')
    except KeyboardInterrupt:
        print('Process quit.')


if __name__ == '__main__':
    look_busy_until(until=time(hour=11))
    # look_busy_for(duration=timedelta(minutes=5))
    # look_busy(interval=5 * 60)
