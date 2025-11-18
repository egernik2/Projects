from time import sleep


class Pidor:
    def __init__(self, name):
        """
        Инициализирует объект Pidor с заданным именем.

        Аргументы:
            name (str): Имя для инициализации объекта.
        """
        self.name = name

    def get_info(self):
        """
        Возвращает имя объекта Pidor.

        Возвращает:
            str: Имя объекта.
        """
        return self.name
    
    def call_pidor(self):
        """
        Публичный метод, который выводит в консоль текст, называющий объект Pidor пидором.

        Возвращает:
            bool: True, если метод вызван успешно.
        """
        print(f'{self.name} - ты пидор!')
        return True
    

def main():
    """
    Главная функция программы. Создает список объектов Pidor c именами,
    заданными в списке names. Затем в бесконечном цикле вызывает
    метод call_pidor() каждого объекта, выводя в консоль текст,
    называющий объект пидором. Между вызовами метода call_pidor()
    делает паузу в 0.5 секунды.
    """
    names = ['Влад', 'Жора', 'Рома', 'Кирилл', 'Никита', 'Жаник', 'Илья', 'Стас']
    classes_list = [Pidor(name) for name in names]
    while True:
        for cls in classes_list:
            cls.call_pidor()
            sleep(0.5)


if __name__ == '__main__':
    main()