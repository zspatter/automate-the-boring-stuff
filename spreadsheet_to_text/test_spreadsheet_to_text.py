import os
from os.path import join, abspath

import openpyxl

from spreadsheet_to_text import spreadsheet_to_text

original_wd = abspath(os.getcwd())
test_wd = join(abspath('.'), 'spreadsheet_to_text', 'test_files')


def test_spreadsheet_to_text():
    setup_directory()
    spreadsheet_to_text.spreadsheet_to_text('test_text_to_sheet.xlsx')

    result_files = [file for file in os.listdir() if file.lower().endswith('.txt')]
    wb = openpyxl.load_workbook('test_text_to_sheet.xlsx')
    sheet = wb.active

    assert sheet.max_column == len(result_files)

    for column in sheet.columns:
        with open(f'{column[0].value}', 'r') as read:
            lines = [cell.value for cell in column[1:] if cell.value]
            for line in lines:
                assert line == read.readline()

    revert_directory()


def setup_directory():
    os.chdir(test_wd)


def revert_directory():
    result_files = [file for file in os.listdir() if file.lower().endswith('.txt')]
    for file in result_files:
        os.remove(file)

    os.chdir(original_wd)
