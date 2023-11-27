# Скрипт формирования графика, его сохранения локально и в интернет-репозиторий api.imgbb.com

import matplotlib.pyplot as plt
from libdatabase import Connection
from datetime import datetime
import matplotlib.ticker as ticker
import base64
import requests

PATH_TO_BD = '/root/Ivan/weather_novosibirsk.db'
key = 'c70e0d6c2991cafd74de018624189af7'

conn = Connection(PATH_TO_BD)

data = conn.select_all()

def upload_plot(filename):
    with open(filename, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key,
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        print(res)

x = []
y = []

for item in data:
    x.append(item[2])
    y.append(item[1])

plt.plot(x, y)
plt.yticks([min(y), max(y)])
plt.xticks([min(x), max(x)])
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:}"))
plt.legend(['Погода в Новосибирске'])
plt.xlabel('Время')
plt.ylabel('Градусы Цельсия')
plt.title('График погоды в Новосибирске')
filename = '/root/Iven/pngs/weather_{}'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
plt.savefig(filename)
#upload_plot('{}.png'.format(filename))