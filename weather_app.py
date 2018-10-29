import json
import requests
import time
import os

cityId = "4644585"
units = "imperial"
apiKey = os.environ.get('OPENWEATHERAPIKEY')
url = f'https://api.openweathermap.org/data/2.5/weather?&id={cityId}&units={units}&APPID={apiKey}'

weatherFlat = {}

def getWeather():
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def recursiveFlatten(object):
    if object is not None:
        for k, v in object.items():
            if isinstance(v, dict):
                recursiveFlatten(v)
            elif isinstance(v, list):
                for val in v:
                    recursiveFlatten(val)    
            else: 
              weatherFlat[k]=v
    return weatherFlat

weather = recursiveFlatten(getWeather())

string = ""
string += f"{weather.get('name')} Weather\n"
string += f"Date: {time.strftime('%m-%d-%Y', time.localtime(weather.get('dt')))}\n"
string += f"Time: {time.strftime('%H:%M:%S', time.localtime(weather.get('dt')))}\n"
string += f"Skies: {weather.get('main')}:\n"
string += f"Current Temp: {weather.get('temp')}°F\n"
string += f"Humidity: {weather.get('humidity')}%\n"
string += f"High: {weather.get('temp_max')}°F\n"
string += f"Low: {weather.get('temp_min')}°F\n"
string += f"Sunrise: {time.strftime('%H:%M:%S', time.localtime(weather.get('sunrise')))}\n"
string += f"Sunset: {time.strftime('%H:%M:%S', time.localtime(weather.get('sunset')))}\n"

print(string)
