#! /usr/bin/env python3
# mcb.py - Saves and loads pieces of text to the clipboard
# Usage: mcb.py save <keyword> - Saves clipboard to keyword
#        mcb.py <keyword> - Loads keyword to clipboard
#        mcb.py list - Loads all keywords to clipboard
#        mcb.py delete <keyword> - Deletes entry associated with keyword
#        mcb.py delete - Deletes all saved entries

import shelve
import sys

import pyperclip


def save_entry(shelf, entry):
    shelf[entry] = pyperclip.paste()
    pyperclip.copy(shelf[entry])


def list_entries(shelf):
    if len(shelf.keys()) > 0:
        pyperclip.copy(str(list(shelf.keys())))
    else:
        pyperclip.copy('Error: the multi-clipboard is empty!')


def get_entry(shelf, entry):
    if entry in shelf:
        pyperclip.copy(shelf[entry])
    else:
        pyperclip.copy(f'Error: "{entry}" not found in multi-clipboard')


def delete_entry(shelf, entry):
    if entry in shelf:
        del shelf[entry]
        pyperclip.copy(f'"{entry}" deleted from the multi-clipboard')
    else:
        pyperclip.copy(f'Error: deletion failed as there is no saved entry that matches "{entry}"')


def delete_all_entries(shelf):
    shelf.clear()


if __name__ == '__main__':
    mcb_shelve = shelve.open('mcb')

    if len(sys.argv) == 3:
        # save new entry
        if sys.argv[1].lower() == 'save':
            save_entry(mcb_shelve, sys.argv[2])
        # delete entry
        elif sys.argv[1].lower() == 'delete':
            delete_entry(mcb_shelve, sys.argv[2])

    elif len(sys.argv) == 2:
        # list stored entries
        if sys.argv[1].lower() == 'list':
            list_entries(mcb_shelve)
        # delete all entries
        elif sys.argv[1].lower() == 'delete':
            delete_all_entries(mcb_shelve)
        # copy value associated with key
        else:
            get_entry(mcb_shelve, sys.argv[1])

    mcb_shelve.close()
