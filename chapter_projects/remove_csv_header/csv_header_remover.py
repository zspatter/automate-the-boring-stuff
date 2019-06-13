#! /usr/bin/env python3
# csv_header_remover.py - removes the header from all CSV files in the read path's directory

import csv
import os
from os.path import abspath, join


def remove_headers(input_path='.', output_path='.'):
    """
    Finds all CSV files directly in the input_path and removes the header row.
    The results are saved under the same name in the output path. If the two
    paths are identical, it will overwrite the original file.

    :param str input_path: path to directory to search
    :param str output_path: path to directory for results
    """
    # ensures paths are absolute and creates output directory if it doesn't exist
    input_path, output_path = abspath(input_path), abspath(output_path)
    os.makedirs(output_path, exist_ok=True)

    csv_list = [file for file in os.listdir(input_path) if file.lower().endswith('.csv')]

    for csv_file in csv_list:
        print(f"Removing header from '{csv_file}'...")

        # gather all lines but header row
        reader = csv.reader(open(join(input_path, csv_file), 'r'))
        lines = [line for line in reader if reader.line_num != 1]

        # write headless content
        writer = csv.writer(open(join(output_path, csv_file), 'w'))
        writer.writerows(lines)


if __name__ == '__main__':
    read_path = join(abspath('.'), 'sample_files')
    write_path = join(abspath('.'), 'headless')
    remove_headers(input_path=read_path, output_path=write_path)
