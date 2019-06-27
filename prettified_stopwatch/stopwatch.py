#! /usr/bin/env python3
# stopwatch.py - a simple stopwatch program

import time

import pyperclip


def print_instructions():
    """
    Prints instructions for using the stopwatch
    """
    input("Press ENTER to begin."
          "\nAfterwards, press ENTER to 'click' the stopwatch."
          "\nPress Ctrl + C to quit.\n")
    print('Starting.\n')


def stopwatch():
    """
    Creates an interactive stopwatch that displays details in the console.
    CTRL + C will cause the stopwatch to terminate - before doing so, the
    stopwatch table is copied to the clipboard.
    """
    print_instructions()

    # initializes stopwatch variables
    start, previous_time = time.time(), time.time()
    lap_num = 1

    # print table header
    output = build_header()
    print(output, end='')

    try:
        while True:
            input()

            # builds results of current lap
            lap_time = f'{time.time() - previous_time:,.2f} s'
            total_time = f'{time.time() - start:,.2f} s'
            row_content = build_row(lap_num, lap_time, total_time)

            # increments stopwatch variables
            lap_num += 1
            previous_time = time.time()

            # saves and prints current results
            output += f'\n{row_content}'
            print(row_content, end='')
            
    except KeyboardInterrupt:
        # closes the stopwatch table and copies the table to clipboard
        close_table = f"\n{build_table_border(outer_left='╚', inner='╩', outer_right='╝')}"
        output += close_table
        print(f"{close_table}\n\nDone.\nStopwatch content copied to clipboard.")
        pyperclip.copy(output)


def build_header():
    """
    Builds formatted header for the stopwatch unicode table.

    :return: formatted unicode header
    """
    return f"{build_table_border(outer_left='╔', inner='═', outer_right='╗')}" \
        f"\n║{'Stopwatch':^54}║" \
        f"\n{build_table_border(inner='╦')}" \
        f"\n{'║':<3}{'Lap Number':^10}{column_spacer}" \
        f"{'Lap Time':^14}{column_spacer}{'Total Time':^16}{'║':>3}" \
        f"\n{build_table_border()}"


def build_table_border(outer_left='╠', inner='╬', outer_right='╣'):
    """
    Builds formatted table border for stopwatch unicode table. Default
    values create the inner borders.

    :param str outer_left: unicode char corresponding to outer left intersection
    :param str inner: unicode char corresponding to inner intersections
    :param str outer_right: unicode char corresponding to outer right intersection
    :return: formatted unicode table border
    """
    return f"{outer_left}{'═' * 14}{inner}{'═' * 18}{inner}{'═' * 20}{outer_right}"


def build_row(lap_num, lap_time, total_time):
    """
    Builds formatted row with details about the lap/total time.

    :param int lap_num: lap number
    :param str lap_time: formatted string representing lap time in seconds
    :param str total_time: formatted string representing total time in seconds
    :return: formatted unicode string representing an individual table row
    """
    return f"{'║':<3}Lap #{lap_num:<5,}{column_spacer}" \
        f"{lap_time:>14}{column_spacer}{total_time:>16}{'║':>3}"


if __name__ == '__main__':
    column_spacer = '  ║  '
    stopwatch()
