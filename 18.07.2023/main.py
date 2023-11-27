from pprint import pprint
import json

class JsonLoader(object): # Класс для работы с файлом
    def __init__(self, filename): # Функция инициализации
        self.filename = filename # Получаем имя файла

    def load_data(self): # Функция загрузки данных из файла
        with open(self.filename, 'r', encoding='CP866') as f: # Открываем файл с данными в кодировке для Windows 10
            return json.load(f) # Возвращаем данные из файла
        
    def save_data(self, data): # Функция записи данных в файл
        with open(self.filename, 'w', encoding='CP866') as f: # Открываем файл для записи в кодировке для Windows 10
            json.dump(data, f, ensure_ascii=False, indent=2) # Записываем данные в виде словаря или списка словарей в файл с отступом в 2 пробела
        print('Файл успешно сохранён')
        
def get_data(json_loader): # Функция получения данных
    return json_loader.load_data() # Получаем данные из файла в виде словаря или списка словарей, используя метод нашего класса

def update_data(json_loader, data): # Функция сохранения данных
    json_loader.save_data(data) # Вызываем метод класса, передавая data в качестве аргумента для сохранения

def seacrh(data, stroka):
    for item in data:
        if stroka in item['name']:
            print(item)
            break
    print('Не найдено')

def main(): # Главная функция
    json_loader = JsonLoader('18.07.2023/persons.json') # Создаём экземпляп класса, задавая имя файла с данными в формате json
    data = get_data(json_loader) # Получаем данные из файла с помощью функции, передавая экземпляр класса в качестве аргумента
    a = input('Введите строку для поиска: ')
    seacrh(data, a)

    

if __name__ == '__main__':
    main()