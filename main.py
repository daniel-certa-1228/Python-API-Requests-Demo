import weather_app
import email_wx
import time
import os

weather = weather_app.recursiveFlatten(weather_app.getWeather())

string = ""
string += f"{weather.get('name')} Weather\n"
string += f"Date: {time.strftime('%m-%d-%Y', time.localtime(weather.get('dt')))}\n"
string += f"Time: {time.strftime('%H:%M:%S', time.localtime(weather.get('dt')))}\n"
string += f"Skies: {weather.get('main')}\n"
string += f"Current Temp: {weather.get('temp')}°F\n"
string += f"Humidity: {weather.get('humidity')}%\n"
string += f"High: {weather.get('temp_max')}°F\n"
string += f"Low: {weather.get('temp_min')}°F\n"
string += f"Sunrise: {time.strftime('%H:%M:%S', time.localtime(weather.get('sunrise')))}\n"
string += f"Sunset: {time.strftime('%H:%M:%S', time.localtime(weather.get('sunset')))}\n"

print(string)

email_wx.sendMail(string)