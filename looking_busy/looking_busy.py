#! /usr/bin/env python3
# looking_busy.py - simple script that simulates user input to keep IM status active

import ctypes
import random
from datetime import datetime, time, timedelta
from time import sleep

import pyautogui


def simulate_input(interval):
    """
    Nudges the mouse by random x and y values (-10 to 10), then returns
    the mouse to it's original position. The duration of these moves is
    a random time value between 0.1 and 0.5 seconds.

    A function key bound to no action is chosen at random to simulate keyboard input

    :param float interval: max interval between mouse nudges
    """
    x = random.randint(a=-10, b=10)
    y = random.randint(a=-10, b=10)

    pyautogui.moveRel(xOffset=x, yOffset=y, duration=random.uniform(a=0.1, b=0.5))
    pyautogui.moveRel(xOffset=-x, yOffset=-y, duration=random.uniform(a=0.1, b=0.5))

    sleep(random.uniform(a=3.5, b=interval % 120 + 1))
    pyautogui.press(f'f{random.randint(15, 24)}')

    sleep(random.uniform(a=interval // 2, b=interval))


def look_busy(interval=60):
    """
    Continues to simulate mouse/keyboard input until the process is
    explicitly interrupted

    :param float interval: max interval between mouse nudges
    """
    try:
        print('Press CTRL-C to quit.\n')

        while True:
            simulate_input(interval=interval)

    except KeyboardInterrupt:
        print('Process quit.')


def look_busy_until(interval=60, until=time(hour=10, minute=15)):
    """
    Simulates mouse/keyboard input until the specified time

    :param float interval: max interval between mouse nudges
    :param datetime.time until: time to stop input
    """
    try:
        print('Press CTRL-C to quit.\n')

        while datetime.now().time() < until:
            simulate_input(interval=interval)

        ctypes.windll.user32.LockWorkStation()

    except KeyboardInterrupt:
        print('Process quit.')


def look_busy_for(interval=60, duration=timedelta(hours=1, minutes=30)):
    """
    Simulates mouse/keyboard input for a given duration

    :param float interval: max interval between mouse nudges
    :param datetime.timedelta duration: duration to simulate input for
    """
    end = datetime.now() + duration

    try:
        print('Press CTRL-C to quit.\n')
        while datetime.now() < end:
            simulate_input(interval=interval)

        ctypes.windll.user32.LockWorkStation()

    except KeyboardInterrupt:
        print('Process quit.')


if __name__ == '__main__':
    # look_busy_until(interval=5 * 60, until=time(hour=10, minute=20))
    look_busy_for(interval=5 * 60, duration=timedelta(hours=1, minutes=30))
    # look_busy(interval=5 * 60)
