#! /usr/bin/env python3
# spreadsheet_to_text.py - converts spreadsheet (.XLSX) to text (.TXT)

import os
from os.path import join, abspath

import openpyxl


def spreadsheet_to_text(filename):
    """
    Writes column data in worksheet to text files. The filenames are
    in the first row of each column. Each subsequent row represents an
    individual line of text.

    :param str filename: name of spreadsheet
    """
    print(f'Reading {filename}...')
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb.active

    for column in sheet.columns:
        # opens the value of the item in first row
        print(f"Opening '{column[0].value}' to write data...")
        with open(f'{column[0].value}', 'w') as writer:
            lines = [cell.value for cell in column[1:] if cell.value]

            # writes each cell with a value to text file
            for line in lines:
                writer.write(line)


if __name__ == '__main__':
    os.chdir(join(abspath('.'), 'sample_files'))
    spreadsheet_to_text(filename='text_to_sheet.xlsx')
