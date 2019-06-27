#! /usr/bin/env python3
# countdown.py - a simple countdown script

import time
import subprocess


def countdown(seconds=60):
    for x in range(seconds, 0, -1):
        print(f'\r{x} seconds', end='')
        time.sleep(1)

    print(f'\rAlarm')
    subprocess.Popen(['start', 'alarm.wav'], shell=True)


if __name__ == '__main__':
    countdown()
