from collections import Counter

from table_printer import table_printer


def test_build_table():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    # removes final new line escape character
    tabular_str = table_printer.build_table(table_data).rstrip()
    lines = tabular_str.split('\n')
    line_length = len(lines[0])
    counter = Counter(tabular_str)

    # checks for expected number of rows (decreased expected due to rstrip())
    assert counter['\n'] == len(table_data[0]) - 1

    # checks each row is of equal length
    for line in lines:
        assert len(line) == line_length
