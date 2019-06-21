#! /usr/bin/env python3
# weather_forecast.py - prints the weather for a location from the command line

import json
import sys

import requests
import pprint
# http://api.openweathermap.org/data/2.5/forecast?q=London,uk&APPID=11e927016e40363a91708daf37fcccc4


def request_url(query: str = 'San Fransisco, CA', api_key='11e927016e40363a91708daf37fcccc4'):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={query}&units=imperial&appid={api_key}'
    response = requests.get(url)
    response.raise_for_status()
    return response


def print_forecast(forecast_data, query):
    forecast_details = forecast_data['list']
    print(f"Current weather in {query}:"
           f"\n\t{'Description:':<14}{forecast_details[0]['weather'][0]['main']} - "
          f"{forecast_details[0]['weather'][0]['description']}"
          f"\n\t{'Temperature:':<14}{forecast_details[0]['main']['temp_min']}°F - "
          f"{forecast_details[0]['main']['temp_max']}°F"
          f"\n\t{'Humidity:':<14}{forecast_details[0]['main']['humidity']}%"
          f""f"\n\t{'Windspeed:':<14}{forecast_details[0]['wind']['speed']} mph")

    print(f"\nTomorrow:"
           f"\n\t{'Description:':<14}{forecast_details[1]['weather'][0]['main']} - "
          f"{forecast_details[1]['weather'][0]['description']}"
          f"\n\t{'Temperature:':<14}{forecast_details[1]['main']['temp_min']}°F - "
          f"{forecast_details[1]['main']['temp_max']}°F"
          f"\n\t{'Humidity:':<14}{forecast_details[1]['main']['humidity']}%"
          f""f"\n\t{'Windspeed:':<14}{forecast_details[1]['wind']['speed']} mph")

    print(f"\nDay after tomorrow:"
          f"\n\t{'Description:':<14}{forecast_details[2]['weather'][0]['main']} - "
          f"{forecast_details[2]['weather'][0]['description']}"
          f"\n\t{'Temperature:':<14}{forecast_details[2]['main']['temp_min']}°F - "
          f"{forecast_details[2]['main']['temp_max']}°F"
          f"\n\t{'Humidity:':<14}{forecast_details[2]['main']['humidity']}%"
          f""f"\n\t{'Windspeed:':<14}{forecast_details[2]['wind']['speed']} mph")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: weather_forecast.py [location]')
        sys.exit(1)

    location = ' '.join(sys.argv[1:])
    result = request_url(query=location)
    weather_data = json.loads(result.text)
    print_forecast(forecast_data=weather_data, query=location)
