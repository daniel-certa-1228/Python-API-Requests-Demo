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


