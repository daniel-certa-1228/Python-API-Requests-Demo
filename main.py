import weather_app
import email_wx
from datetime import datetime, timedelta
import os

weather = weather_app.recursiveFlatten(weather_app.getWeather())
utcOffset = timedelta(hours=5)

string = ""
string += f"**{weather.get('name')} Weather**\n"
string += f"Date: {(datetime.fromtimestamp(weather.get('dt')) - utcOffset).strftime('%m-%d-%Y')}\n"
string += f"Time: {(datetime.fromtimestamp(weather.get('dt')) - utcOffset).strftime('%H:%M')}\n"
string += f"Skies: {weather.get('main')}\n"
string += f"Current Temp: {round(weather.get('temp'))}°F\n"
string += f"Humidity: {weather.get('humidity')}%\n"
string += f"Sunrise: {(datetime.fromtimestamp(weather.get('sunrise')) - utcOffset).strftime('%H:%M')}\n"
string += f"Sunset: {(datetime.fromtimestamp(weather.get('sunset')) - utcOffset).strftime('%H:%M')}\n"

print(string)

email_wx.sendMail(string)