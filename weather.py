#! python3
# weather.py - weather() is a function to get the current weather info (temperature, humidity, wind speed) via OpenWeather API
# Last update: 20230731
# Author: Andre Cheung
# Organizaton: RoboticsCats.com
import re, requests

def weather(lat, long, key):
    # define the regexes
    temperature = re.compile(r'("temp":)(\d?\d?\d.\d?\d?)')
    humidity = re.compile(r'("humidity":)(\d?\d?\d)')
    wind_speed = re.compile(r'("wind_speed":)(\d?\d?\d.\d?\d?)')
    
    url = 'https://api.openweathermap.org/data/3.0/onecall?lat=' + str(round(lat,4)) + '&lon=' + str(round(long,4)) + '&exclude=minutely,hourly,daily&units=metric&appid=' + str(key)

    try:
        # call the OpenWeather API to get current weather
        current = requests.get(url)

        if current.status_code == 200:
            t = temperature.search(current.text)
            h = humidity.search(current.text)
            w = wind_speed.search(current.text)
            
            info = str(round(float(t.group(2)),1)) + chr(176) + 'C | ' + h.group(2) +' % | ' + w.group(2) + ' km/h'
            return info

    except Exception as e:
        print(f"Error: {e}")
        return('')


latitude = 50.88
longitude = 119.89
apikey = ''

print(weather(latitude, longitude, apikey))
