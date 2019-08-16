#! /usr/bin/env python3
# play_2048.py - simple blind bot that plays 2048 online

import random
from itertools import cycle

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def play_2048(random_input=False):
    """
    This function launches and plays a game of 2048 with either seqential
    (up, right, down, left) or random inputs. Once the game is over,
    the browser exits and the final score is displayed
    """
    # loads 2048
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 1000)
    browser.set_window_position(0, 0)
    browser.get('https://play2048.co/')

    # web elements for game play
    game_status = browser.find_element_by_css_selector('.game-container p')
    html_element = browser.find_element_by_css_selector('html')

    # if input should be random, change game_input alias to call random.choice
    if random_input:
        sequence = KEY_INPUTS
        game_input = random.choice
    # otherwise cycle possible inputs
    else:
        sequence = cycle(KEY_INPUTS)
        game_input = next

    # while game isn't over, either give random or sequential input
    while game_status.text != 'Game over!':
        html_element.send_keys(game_input(sequence))
        game_status = browser.find_element_by_css_selector('.game-container p')

    # gather and print final score
    score = int(browser.find_element_by_css_selector('.score-container').text)
    print(f"{'Randomized' if random_input else 'Sequential':<10} input:"
          f"\tGame over - your score: {score:6,d}!")
    browser.quit()


if __name__ == '__main__':
    KEY_INPUTS = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    for _ in range(10):
        play_2048()
        play_2048(random_input=True)
        print()
