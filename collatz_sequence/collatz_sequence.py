#! /usr/bin/env python3


def collatz(number: int) -> int:
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


if __name__ == '__main__':
    try:
        result = int(input("Enter number: "))
        while result != 1:
            result = collatz(result)
    except ValueError:
        print('Error: input must be an integer')
