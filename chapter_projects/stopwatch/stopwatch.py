#! /usr/bin/env python3
# stopwatch.py - a simple stopwatch program

import time


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
    start = time.time()
    previous_time = start
    lap_num = 1
    column_spacer = '  ║  '

    # print table header
    print(f"{build_table_separator(outer_left='╔', inner='═', outer_right='╗')}"
          f"\n║{'Stopwatch':^54}║"
          f"\n{build_table_separator(inner='╦')}"
          f"\n{'║':<3}{'Lap Number':^10}{column_spacer}"
          f"{'Lap Time':^14}{column_spacer}"
          f"{'Total Time':^16}{'║':>3}"
          f"\n{build_table_separator()}", end='')

    try:
        while True:
            input()
            lap_time = f'{time.time() - previous_time:,.2f} s'
            total_time = f'{time.time() - start:,.2f} s'

            # prints results of current stopwatch
            print(f"{'║':<3}Lap #{lap_num:<5,}{column_spacer}"
                  f"{lap_time:>14}{column_spacer}"
                  f"{total_time:>16}{'║':>3}", end='')

            lap_num += 1
            previous_time = time.time()
    except KeyboardInterrupt:
        # closes the stopwatch table
        print(f"\n{build_table_separator(outer_left='╚', inner='╩', outer_right='╝')}"
              f"\n\nDone.")


def build_table_separator(outer_left='╠', inner='╬', outer_right='╣'):
    """
    Builds formatted unicode header for the stopwatch table.

    :return: formatted unicode header
    """
    return f"{outer_left}{'═' * 14}{inner}{'═' * 18}{inner}{'═' * 20}{outer_right}"


if __name__ == '__main__':
    print_instructions()
    stopwatch()
