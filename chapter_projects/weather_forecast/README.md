# Fetching Current Weather Data

Checking the weather seems fairly trivial: Open your web browser, click the address bar, type the URL to a weather website (or search for one and then click the link), wait for the page to load, look past all the ads, and so on.

Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed it as plaintext. This program uses the `requests` module from Chapter 11 to download data from the Web.

Overall, the program does the following:
- Reads the requested location from the command line
- Downloads JSON weather data from OpenWeatherMap.org
- Converts the string of JSON data to a Python data structure
- Prints the weather for today and the next two days

## Sample Output
<p align=center>
  <img src=./sample_output.png alt=sample console output>
</p>

Ideas for Similar Programs
-
Accessing weather data can form the basis for many types of programs. You can create similar programs to do the following:
- Collect weather forecasts for several campsites or hiking trails to see which one will have the best weather
- Schedule a program to regularly check the weather and send you a frost alert if you need to move your plants indoors
- Pull weather data from multiple sites to show all at once, or calculate and show the average of the multiple weather predictions
