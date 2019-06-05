import sys

import openpyxl


def insert_blank_rows(index: int, filename: str, offset: int = 1):
    """
    Inserts a blank row at the passed index. If an offset is provided,
    multiple blank rows are inserted.

    :param int index: row number where blank row starts
    :param int offset: number of blank rows
    :param str filename: name of file (including ext)
    """
    wb = openpyxl.load_workbook(filename=filename)
    sheet = wb.active
    rows = tuple(sheet.rows)
    print('Inserting blank rows...')

    # traverses rows in reverse
    for row in rows[::-1]:
        for cell in row:
            row = cell.row
            column = cell.column

            # moves contents and replaces previous cell with blank value
            if index <= row < index + offset:
                sheet.cell(row=row + offset, column=column).value = cell.value
                sheet.cell(row=row, column=column).value = ''
            # moves contents
            elif row >= index + offset:
                sheet.cell(row=row + offset, column=column).value = cell.value

    wb.save('result_' + filename)
    print(f"Resulting file saved as 'result_{filename}'")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: blank_row_inserter.py [index] [offset] [filename]')
    else:
        start = int(sys.argv[1])
        blank_number = int(sys.argv[2])
        file = sys.argv[3]

        insert_blank_rows(index=start, offset=blank_number, filename=file)

    insert_blank_rows(5, 'multiplication_table.xlsx')
