import os
import re


def regex_search(regex, path):
    if not os.path.isdir(path):
        print('The file path must be to a directory.')
        return

    regex = re.compile(regex)
    matches = ''

    generator = (file for file in os.listdir(path=path) if file.endswith('.txt'))
    for file in generator:
        with open(path + file) as document:
            match_gen = (line for line in document if regex.search(line))
            for line in match_gen:
                matches += line

    return matches


if __name__ == '__main__':
    email_regex = re.compile(r'''(
         [a-zA-Z0-9._%+-]+      # username
         @                      # @ symbol
         [a-zA-Z0-9.-]+         # domain name
         (\.[a-zA-Z]{2,4})      # dot-something
         )''', re.VERBOSE)

    print(''.join(regex_search(email_regex, './sample_data/')))
