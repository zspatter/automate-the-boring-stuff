#! /usr/bin/env python3
# stopwatch.py - a simple stopwatch program

import time


def print_instructions():
    input("Press ENTER to begin."
          "\nAfterwards, press enter to 'click' the stopwatch."
          "\nPress Ctrl + C to quit.\n")
    print('Starting.\n')


def start_stopwatch():
    global start, previous_time, lap_num
    start = time.time()
    previous_time = start
    lap_num = 1
    print(f"{'-' * 55}"
          f"\n|{'Lap #':^12} | "
          f"{'Total time':^19}| "
          f"{'Lap time':^17}|"
          f"\n{'-' * 55}", end='')


def stopwatch_loop():
    global lap_num, previous_time
    spacer = '  |  '
    try:
        while True:
            input()
            lap_time = f'{round(time.time() - previous_time, 2):.2f} s'
            total_time = f'{round(time.time() - start, 2):,.2f} s'
            print(f"|  Lap #{lap_num:<4}{spacer}"
                  f"{total_time:>16}{spacer}"
                  f"{lap_time:>14}  |", end='')
            lap_num += 1
            previous_time = time.time()
    except KeyboardInterrupt:
        print(f"{'-' * 55}"
              f"\n\nDone.")


if __name__ == '__main__':
    print_instructions()
    start_stopwatch()
    stopwatch_loop()
