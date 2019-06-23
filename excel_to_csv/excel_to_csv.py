#! /usr/bin/env python3

import csv
import os
from os.path import abspath, join

import openpyxl


def excel_to_csv(path='.'):
    """
    Converts all .xlsx files in the provided path to CSVs. The resulting
    files are saved to a subdirectory of the path 'csv_output'.

    :param path:
    """
    output_path = join(abspath(path), 'csv_output')
    os.makedirs(output_path, exist_ok=True)

    for workbook, sheet in worksheet_generator(root=abspath(path)):
        # creates filename in the form [workbook]_[worksheet].csv
        csv_filename = f"{workbook[:-5].replace(' ', '_')}_{sheet.title}.csv"
        writer = csv.writer(open(join(output_path, csv_filename), 'w'))

        sheet_content = [[cell.value for cell in row] for row in sheet.rows]
        writer.writerows(sheet_content)


def worksheet_generator(root):
    """
    Generates worksheet objects

    :param root:
    """
    workbooks = sorted([file for file in os.listdir(path=root) if file.endswith('.xlsx')])

    for workbook in workbooks:
        wb = openpyxl.load_workbook(filename=join(root, workbook))

        for worksheet in wb.sheetnames:
            yield workbook, wb[worksheet]


if __name__ == '__main__':
    excel_to_csv(path=join('.', 'sample_files'))
