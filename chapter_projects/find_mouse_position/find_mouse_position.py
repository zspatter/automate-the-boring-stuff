#! /usr/bin/env python3
# find_mouse_position.py -

import pyautogui


def get_mouse_position():
    print('Press Ctrl-C to quit.\n')
    backspace = '\b'

    try:
        while True:
            x, y = pyautogui.position()
            rgb = pyautogui.screenshot().getpixel((x, y))
            position = f'X: {x:>6,d}\tY: {y:>5,d}\t' \
                       f'RGB: ({rgb[0]:>3d}, {rgb[1]:>3d}, {rgb[2]:>3d})'
            print(f'{backspace * len(position)}{position}', end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone')


if __name__ == '__main__':
    get_mouse_position()
