#! /usr/bin/env python3
# stopwatch.py - a simple stopwatch program

import time


def print_instructions():
    input("Press ENTER to begin."
          "\nAfterwards, press ENTER to 'click' the stopwatch."
          "\nPress Ctrl + C to quit.\n")
    print('Starting.\n')


def stopwatch():
    start = time.time()
    previous_time = start
    lap_num = 1
    column_spacer = '  ║  '

    # print table header
    print(f"{build_table_separator(outer_left='╔', inner='═', outer_right='╗')}"
          f"\n║{'Super Stopwatch':^54}║"
          f"\n{build_table_separator(inner='╦')}"
          f"\n║{'Lap Number':^14}║ "
          f"{'Total time':^19}║ "
          f"{'Lap Time':^17}║"
          f"\n{build_table_separator()}", end='')

    try:
        while True:
            input()
            lap_time = f'{time.time() - previous_time:,.2f} s'
            total_time = f'{time.time() - start:,.2f} s'

            # prints results of current stopwatch
            print(f"║  Lap #{lap_num:<5}{column_spacer}"
                  f"{total_time:>16}{column_spacer}"
                  f"{lap_time:>14}  ║", end='')

            lap_num += 1
            previous_time = time.time()
    except KeyboardInterrupt:
        # closes the stopwatch table
        print(f"\n{build_table_separator(outer_left='╚', inner='╩', outer_right='╝')}"
              f"\n\nDone.")


def build_table_separator(outer_left='╠', inner='╬', outer_right='╣'):
    return f"{outer_left}{'═' * 14}{inner}{'═' * 20}{inner}{'═' * 18}{outer_right}"


if __name__ == '__main__':
    print_instructions()
    stopwatch()
