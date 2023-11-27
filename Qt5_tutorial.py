#pyuic5 -x viewer.ui -o viewer.py # Преобразование файла стиля в python файл
from PyQt5 import QtWidgets # Импорт виджетов
from PyQt5.QtWidgets import QApplication, QMainWindow # Импорт приложение я окна
import sys # Импорт sys

resolution_x = 1920 # Разрешение экрана x
resolution_y = 1080 # Разрешение экрана y
height = 350 # Размер окна x
width = 200 # Размер окна y

class Window(QMainWindow): # Создание класса формы, наследуемся от родительского класса
    def __init__(self): # Конструктор класса
        super(Window, self).__init__() # Вызываем конструктор класса родительского класса
        self.setWindowTitle('Изменятор текста') # Задание заголовка окна
        self.setGeometry((resolution_x//2)-(height//2), (resolution_y//2)-(width//2), height, width) # Задание смещение окна и его размеров (1-2 - смещение x и y, 3-4 - размер x и y)

        self.main_text = QtWidgets.QLabel(self) # Создание надписи. В скобках указывается окно, которой он принадлежит
        self.main_text.setText("Добро пожаловать") # Наполнение текстом
        self.main_text.move(100, 100) # Смещение
        self.main_text.adjustSize() # Автоподбор ширины под содержимое

        self.btn = QtWidgets.QPushButton(self) # Создание кнопки. В скобках указывается окно, которому она пренадлежит
        self.btn.move(100, 150) # Смещение кнопки
        self.btn.setText('Нажми меня') # Текст кнопки
        self.btn.adjustSize() # Автоподбор ширины под сорержимое
        self.btn.clicked.connect(self.add_label) # А вот тут сложно. Создаём событие clicked, с помощью connect присоединяем функцию, которая будет выполняться при нажатии на кнопку

        self.new_label = QtWidgets.QLabel(self) # Создаём надпись, которая не видна, так как не содержит текста

    def add_label(self): # Функция, которая вызывается при нажатии на кнопку (название может быть произвольным)
        self.new_label.setText ('Ты нажал на кнопку') # Добавляет текст в надпись и она становится видна
        self.new_label.adjustSize() # Автоподбор ширины под сордержимое после добавления текста

def application(): # Объявляем главную функцию приложения
    app = QApplication(sys.argv) # Объявляем экземпляр класса приложения, передавая с помощью sys.argv параметры ОС для кросплатфоменности
    window = Window() # Объявляем экзмепляр класса окна


    window.show() # Показ окна
    sys.exit(app.exec_()) # Корректный выход из программы

if __name__ == '__main__':
    application()