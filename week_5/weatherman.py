# weatherman.py
# 
# Provides the current forecast for the weather in Berkeley, California

from urllib.request import urlopen
import json


def get_report():
    """
    Returns the current forecast of Berkeley right now
    """
    # url = 'http://api.openweathermap.org/data/2.5/weather?q=Berkeley,ca'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Berkeley,ca&APPID=25e24b4207d7309fccfcce627731f0a1'
    response = urlopen(url)
    raw_weather_data = response.read().decode("utf-8")
    weather_data = json.loads(raw_weather_data)
    forecast = "Berkeley, CA Forecast: " + weather_data["weather"][0]["main"]
    return forecast
