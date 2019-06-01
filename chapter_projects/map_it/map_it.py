#! /usr/bin/env python3
# map_it.py - Launches a map in the browser using an address from the command line or clipboard

import sys
import webbrowser

import pyperclip

if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = ' '.join(sys.argv[1:])
    else:
        address = pyperclip.paste()

    webbrowser.open(f'https://www.google.com/maps/place/{address}')
