#! /usr/bin/env python3
# umbrella_reminder.py - checks the chance of precipitation, and if the
#                       chance is above the given threshold, a SMS message
#                       is sent to notify the recipient

from notifications import text_myself

import requests
from bs4 import BeautifulSoup


def rain_check(url, threshold=35):
    """
    Queries today's weather to check if the chance of precipitation is
    above the threshold. If the precip_chance is, it is returned.

    :param str url: url for query to scrape forecast (this should point
            to a specified location on weather.com)
    :param int threshold: bound for notifications. Any precip value above
            this variable will be returned
    """
    # CSS selector for precipitation chance
    selector = '#daypart-0 > div > div.today-daypart-precip > span.precip-val > span'

    try:
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        precipitation_element = soup.select(selector)
        precipitation_chance = int(precipitation_element[0].get_text()[:-1])

        if precipitation_chance >= threshold:
            return precipitation_chance

    except requests.exceptions.HTTPError as e:
        print(f'Error downloading the weather report - {e}')


if __name__ == '__main__':
    query_url = 'https://weather.com/weather/today/l/Kokomo+IN+USIN0331:1:US'
    precipitation = rain_check(url=query_url)
    if precipitation:
        text_myself(message=f"Rain alert! The chance of precipitation today is "
                            f"{precipitation}% - don't forget to take an umbrella!")
