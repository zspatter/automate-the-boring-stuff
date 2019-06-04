import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def play_2048():
    # loads 2048
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    driver.get('https://play2048.co/')

    # webelements for gameplay
    game_status = driver.find_element_by_css_selector('.game-container p')
    html_element = driver.find_element_by_css_selector('html')

    # possible input keys for gameplay
    input_keys = (Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT)

    # loop while game isn't over
    while game_status.text != 'Game over!':
        html_element.send_keys(random.choice(input_keys))
        game_status = driver.find_element_by_css_selector('.game-container p')

    # print score
    score = driver.find_element_by_css_selector('.score-container').text
    print(f'Game over! You scored: {score}!')


if __name__ == '__main__':
    play_2048()
