import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def play_2048(random_input=False):
    """
    This function launches and plays a game of 2048 with random inputs.
    Once the game is over, the browser exits and the final score is displayed
    """
    # loads 2048
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    driver.get('https://play2048.co/')

    # web elements for game play
    game_status = driver.find_element_by_css_selector('.game-container p')
    html_element = driver.find_element_by_css_selector('html')

    # possible input keys for game play
    input_keys = (Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT)

    if not random_input:
        # loop while game isn't over
        while game_status.text != 'Game over!':
            html_element.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
            game_status = driver.find_element_by_css_selector('.game-container p')
    else:
        while game_status.text != 'Game over!':
            html_element.send_keys(random.choice(input_keys))
            game_status = driver.find_element_by_css_selector('.game-container p')

    # print score
    score = driver.find_element_by_css_selector('.score-container').text
    print(f'Game over - your score: {score}!')


if __name__ == '__main__':
    play_2048()
    play_2048(random_input=True)
