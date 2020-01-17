#! /usr/bin/env python3
# regex_strip.py - an implementation of string's strip() method using regex

import re


def regex_strip(text, remove=None):
    """
    Takes a string and performs the same operation as str.strip()
    This function defaults to removing whitespace, but if the optional
    remove argument is supplied, the remove value is removed from the text

    :param str text: source string
    :param str remove: optional value to remove from source string
    """
    if not remove:
        return re.compile(r'^\s*|\s*$').sub('', text)
    else:
        return re.compile(f'^({remove})+|({remove})+$').sub('', text)


if __name__ == "__main__":
    print(f"'     test     ' \t->\t '{regex_strip(text='     test     ')}'")
    print(f"'123home123' \t\t->\t "
          f"'{regex_strip(text='123home123', remove='123')}'")
    print(f"'123home123home123' \t\t->\t "
          f"'{regex_strip(text='123home123home123', remove='123')}'")
    print(f"'123123home123home123123' \t\t->\t "
          f"'{regex_strip(text='123123home123home123123', remove='123')}'")
