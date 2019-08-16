#! /usr/bin/env python3
# regex_search.py -

import re
from pathlib import Path


def regex_search(regex, path):
    path = path.resolve()
    if not path.is_dir():
        print('The file path must be to a directory.')
        return

    regex = re.compile(regex)
    matches = []
    generator = (file for file in path.iterdir() if file.suffix == '.txt')

    for file in generator:
        text = file.read_text().split('\n')
        match_gen = (line for line in text if regex.search(line))

        for line in match_gen:
            matches.append(line)

    return matches


if __name__ == '__main__':
    email_regex = re.compile(r'''(
         [a-zA-Z0-9._%+-]+      # username
         @                      # @ symbol
         [a-zA-Z0-9.-]+         # domain name
         (\.[a-zA-Z]{2,4})      # dot-something
         )''', re.VERBOSE)

    print('\n'.join(regex_search(email_regex, Path('./sample_data'))))
