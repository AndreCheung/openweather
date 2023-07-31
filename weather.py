#! python3
# weather.py - Get the current weather info (at Sun Peaks) via OpenWeather API
# Last update: 20230730
# Author: Andre Cheung
# Organizaton: RoboticsCats
import re, requests

# global constants
OWurl = 'https://api.openweathermap.org/data/3.0/onecall?lat=50.88&lon=-119.89&exclude=minutely,hourly,daily&units=metric&appid={API key}'

def weather(url):
    # define the regexes
    temperature = re.compile(r'("temp":)(\d?\d?\d.\d?\d?)')
    humidity = re.compile(r'("humidity":)(\d?\d?\d)')
    wind_speed = re.compile(r'("wind_speed":)(\d?\d?\d.\d?\d?)')
    
    try:
        # call the OpenWeather API to get current weather
        current = requests.get(url)

        if current.status_code == 200:
            t = temperature.search(current.text)
            h = humidity.search(current.text)
            w = wind_speed.search(current.text)
                      
            info = t.group(2) +' C | ' + h.group(2) +' % | ' + w.group(2) + ' km/h'
            return info

    except Exception as e:
        print(f"Error: {e}")
        
print(weather(OWurl))
