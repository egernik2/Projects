from libdatabase import Connection
import requests
import time

db = Connection('for_ivan/weather.db')


key = '13d44774766c17c27eab5da3d2411510'
lat = '55.018803'
lon = '82.933952'
link = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

def get_data():
    result = requests.get(link).json()
    if result:
        temp = round((float(result.get('main').get('temp')) - 273,15)[0], 2)
        db.insert_data(temp)

while True:
    get_data()
    time.sleep(1800)