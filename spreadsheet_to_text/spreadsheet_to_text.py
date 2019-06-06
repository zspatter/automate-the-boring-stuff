#! /usr/bin/env python3

import os
from os.path import join, abspath

import openpyxl


def spreadsheet_to_text(filename: str):
    """
    Writes column data in worksheet to text files. The filenames are
    in the first row of each column. Each subsequent row represents an
    individual line of text.

    :param str filename: name of spreadsheet
    """
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb.active

    for column in sheet.columns:
        with open(f'{column[0].value}', 'w') as text:
            lines = [cell.value for cell in column[1:] if cell.value]
            for line in lines:
                text.write(line)


if __name__ == '__main__':
    os.chdir(join(abspath('.'), 'sample_files'))
    spreadsheet_to_text('text_to_sheet.xlsx')

