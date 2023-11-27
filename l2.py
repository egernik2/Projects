# red = int(input('Красных: '))
# green = int(input('Зелёных: '))
# blue = int(input('Синих: '))
# aa = (red * 10) + (green * 5) + (blue * 3)
# print ('Древней адены:', aa)
# money = aa * 13
# print ('Денег:', money)

from flask import Flask

app = Flask(__name__)

from flask import Flask
from l2 import main

app = Flask(__name__)

@app.route('/')
def index():
    return main()