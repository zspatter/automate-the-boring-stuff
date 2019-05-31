import logging
import random
from pathlib import Path


def get_input():
    """
    Loops until input is a valid selection

    :return: valid guess
    """
    in_value = ''
    while in_value not in ('heads', 'tails'):
        in_value = input('Guess the coin toss! Enter heads or tails: ').strip().lower()
        s = 'valid input of:'
        logging.debug(f'{"in" + s if not in_value in ("heads", "tails") else s:17s}'
                      f' \'{in_value}\'')

    return in_value


def coin_toss():
    """
    Simulated coin toss

    :return:
    """
    guess = get_input()
    toss = random.choice(('heads', 'tails'))
    logging.debug(f'guess = \'{guess}\'')
    logging.debug(f'toss = \'{toss}\'')

    if toss == guess:
        print('You got it!')
        logging.debug(f'toss == guess = \'{toss}\'')
    else:
        print('Nope! Guess again!')
        guess = get_input()
        if toss == guess:
            print('You got it!')
            logging.debug(f'toss == guess = \'{toss}\'')
        else:
            print('Nope. You are really bad at this game.')
            logging.debug(f'toss = \'{toss}\'  != guess = \'{guess}\'')


if __name__ == '__main__':
    logging.basicConfig(filename=f'{Path(__file__).stem}.log',
                        level=logging.DEBUG,
                        format=' %(asctime)s.%(msecs)03d - %(levelname)s - '
                               '<%(funcName)s>: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.disable(logging.CRITICAL)

    logging.debug('start of script')
    coin_toss()
    logging.debug('end of script')
