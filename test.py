import numpy as np
import matplotlib.pyplot as plt
import random

# def processedY(x):
#     y = x * 2 - 10
#     y = round(y, 1)
#     return y

# for i in range(10):
#     x = random.uniform(0, 10)
#     x = round(x, 1)
#     y = processedY(x)
#     print (f'{x}: {y}')


fig, ax = plt.subplots()

data = { #Набор точек
    7.1: 4.2,
    8.3: 6.6,
    4.8: -0.4,
    1.9: -6.2,
    5.8: 1.6,
    1.9: -6.2,
    4.5: -1.0,
    3.9: -2.2,
    4.6: -0.8,
    6.2: 2.4
    }

for x in data:
    ax.scatter(x, data[x])

ax.set(title='Посмотри что ты наделал...')

plt.show()
