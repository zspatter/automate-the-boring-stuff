#! /usr/bin/env python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.py save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.py <keyword> - Loads keyword to clipboard.
#        py.exe mcb.py list - Loads all keywords to clipboard.

import shelve
import sys

import pyperclip

mcb_shelve = shelve.open('mcb')

# save new entry
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list stored entries
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelve.keys())))
    # copy value associated with key
    elif sys.argv[1] in mcb_shelve:
        pyperclip.copy(mcb_shelve[sys.argv[1]])

mcb_shelve.close()
