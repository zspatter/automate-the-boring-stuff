#! /usr/bin/env python3
# table_printer.py - formats lists of string into a tabular format


def build_table(data):
    """
    Formats and builds a table from a nested list of strings.
    Each individual element of the list represents a column

    :param list data: list of strings
    :return: str formatted for tabular representation
    """
    column_widths = []
    output = ''

    # list comprehension adds the largest length within the nested list
    # to the column_widths list (with + 1 for buffer)
    for col in data:
        column_widths.append(max([len(element) for element in col]) + 1)

    # uses indices to shift the table (data[0] is column, not row)
    for col in enumerate(data[0]):
        for row in enumerate(data):
            output += '{}'.format(data[row[0]][col[0]].rjust(column_widths[row[0]]))
        output += '\n'

    return output


if __name__ == "__main__":
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print(build_table(table_data))
