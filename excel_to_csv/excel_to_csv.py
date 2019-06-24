#! /usr/bin/env python3

import csv
import os
from os.path import abspath, join

import openpyxl


def excel_to_csv(path='.', save_directory='csv_output'):
    """
    Converts all .xlsx files in the provided path to CSVs. The resulting
    files are saved to a subdirectory of the path 'csv_output'.

    :param str path: path to directory to search for excel files
    :param str save_directory: name of folder where output will be saved
    """
    output_path = join(abspath(path), save_directory)
    os.makedirs(output_path, exist_ok=True)

    for sheet, workbook in worksheet_generator(root=abspath(path)):
        # creates filename in the form [workbook]_[worksheet].csv
        csv_filename = f"{workbook[:-5]}_{sheet.title}.csv".replace(' ', '_')
        print(f"Converting '{sheet.title}' in '{workbook}' to {csv_filename}...")

        # writes content of the worksheet to a CSV
        sheet_content = [[cell.value for cell in row] for row in sheet.rows]
        writer = csv.writer(open(join(output_path, csv_filename), 'w'))
        writer.writerows(sheet_content)


def worksheet_generator(root):
    """
    Generates worksheet objects in alphabetical order. After all
    worksheets within a workbook have been returned, the generator
    will start on the next workbook in the directory.

    :param str root: path to directory to search for .xlsx files
    """
    workbooks = sorted([file for file in os.listdir(path=root) if file.endswith('.xlsx')])

    for workbook in workbooks:
        wb = openpyxl.load_workbook(filename=join(root, workbook))
        for worksheet in sorted(wb.sheetnames):
            yield wb[worksheet], workbook


if __name__ == '__main__':
    excel_to_csv(path=join('.', 'sample_files'))
