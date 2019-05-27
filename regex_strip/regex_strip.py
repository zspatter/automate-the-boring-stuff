#! /usr/bin/env python3
# regex_strip.py - an implementation of string's strip() method using regex
import re


def regex_strip(text, remove=None):
    if not remove:
        return re.compile(r'^\s*|\s*$').sub('', text)
    else:
        return re.compile(str(remove)).sub('', text)


if __name__ == "__main__":
    print(regex_strip(text='     test     '))
    print(regex_strip(text='123home123', remove='123'))
