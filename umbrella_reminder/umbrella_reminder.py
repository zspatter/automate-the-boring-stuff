import requests
from bs4 import BeautifulSoup
from notifications import text_myself


def rain_check(threshold=35):
    """
    Quarries today's weather to check if the chance of precipitation is
    above the threshold. If the precip_chance is, it is returned.

    :param threshold:
    :return:
    """
    url = 'https://weather.com/weather/today/l/Kokomo+IN+USIN0331:1:US'
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
    precipitation = rain_check(threshold=85)
    if precipitation:
        text_myself(message=f'Rain alert! The chance of precipitation today is '
        f'{precipitation}% - don\'t forget to take an umbrella!')
