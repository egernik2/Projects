import requests
import sqlite3


key = '13d44774766c17c27eab5da3d2411510'
lat = '55.018803'
lon = '82.933952'
link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

result = requests.get(link).json()
if result:
    temp = float(result.get('main').get('temp')) - 273,15
    print(f"Температура: {round(temp[0], 2)}")