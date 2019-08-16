#! /usr/bin/env python3
# date_converter - Renames files with MM-DD-YYYY dates to YYYY-MM-DD

import re
from pathlib import Path

date_regex = re.compile(r"""^(.*?)      # all text before the date
       ((0|1)?\d)                       # one or two digits for the month
       (-|_|\.| )                       # separators
       ((0|1|2|3)?\d)                   # one or two digits for the day
       (-|_|\.| )                       # separators
       ((19|20)\d\d)                    # four digits for the year
       (.*?)$                           # all text after the date
     """, re.VERBOSE)


def convert_dates(path):
    """
    This function converts all files with recognized date patterns
    in their filename to ISO 8601 format (MM-DD-YYYY to YYYY-MM-DD).

    :param Path path: path to directory for analysis
    """
    path = path.resolve()
    # iterates over all files at given path
    for filepath in path.iterdir():
        match_object = date_regex.search(filepath.name)

        # only continues if there is a regex match
        if match_object:
            # breaks apart date parts and converts to ISO 8601 format
            prefix = match_object.group(1)
            year = match_object.group(8)
            month = match_object.group(2)
            day = match_object.group(5)
            suffix = match_object.group(10)
            new_name = f'{prefix}{year}.{month}.{day}{suffix}'

            # determines path for new filenames
            new_path = path.joinpath(new_name)

            # renames applicable files
            print(f"Renaming '{filepath.name}' "
                  f"to '{new_path.name}'...")
            filepath.replace(target=new_path)


if __name__ == '__main__':
    convert_dates(path=Path('./sample_files'))
