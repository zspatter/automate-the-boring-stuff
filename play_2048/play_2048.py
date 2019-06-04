import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def play_2048(random_input=False):
    """
    This function launches and plays a game of 2048 with either seqential
    (up, right, down, left) or random inputs. Once the game is over,
    the browser exits and the final score is displayed
    """
    # loads 2048
    browser = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    browser.get('https://play2048.co/')

    # web elements for game play
    game_status = browser.find_element_by_css_selector('.game-container p')
    html_element = browser.find_element_by_css_selector('html')

    # possible input keys for game play
    input_keys = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
    game_input = lambda x: x

    # if input should be random, change game_input alias to call random.choice
    if random_input:
        game_input = random.choice

    # while game isn't over, either give random or sequential input
    while game_status.text != 'Game over!':
        html_element.send_keys(game_input(input_keys))
        game_status = browser.find_element_by_css_selector('.game-container p')

    # gather and print final score
    score = int(browser.find_element_by_css_selector('.score-container').text)
    print(f"{'Randomized' if random_input else 'Sequential':<10} input:"
          f"\tGame over - your score: {score:6,d}!")
    browser.quit()


if __name__ == '__main__':
    for _ in range(10):
        play_2048()
        play_2048(random_input=True)
        print()
