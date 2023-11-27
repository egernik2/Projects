from rich.console import Console
from rich.table import Table
from os import system
from time import sleep

console = Console()
table = Table(title="Количество букв в словах", show_lines=True)
sys = system

def StartApp():
    print ("Добро пожаловать в обработчик предложений")
    print ("Данная программа принимает на вход предложение и возвращает самое длинное слово")
    print ("Загрузка модулей программы...")
    sleep(2)

def EnterSentence():
    sentence = input("\nВведите предложение для обработки: ")
    console.print("[green][+][/green] Предложение успешно получено")
    return sentence

def Checker(word):
    list = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
    for s in word:
        if s not in list:
            word = word.replace(s, '', 1)
    return word

def HandlerSentence(sentence):
    console.print('[green][+][/green] Запущена обработка предложения[white]...[/white]')
    sleep(1)
    l = list()
    l1 = list()
    l1 = sentence.split(" ")
    for word in l1:
        word = Checker(word)
        if word != '':
            l.append(word)
    count = len(l)
    console.print("[green][+][/green] Предложение успешно обработано. Количество слов:", count)
    return l

def CountWordLen(list):
    count = 0
    longestword = ""
    for word in list:
        countTest = len(word)
        console.print (f"[green][+][/green] Количество букв в слове \"{word}\": {countTest}")
        if countTest > count:
            count = countTest
            longestword = word
    return count, longestword

def CountWordLenTable(list):
    count = 0
    longestword = ""
    table.add_column('Слово')
    table.add_column('Количество букв', justify="right")
    for word in list:
        countTest = len(word)
        table.add_row(word, str(countTest))
        if countTest > count:
            count = countTest
            longestword = word
    return count, longestword, table

def Choice():
    print ("\nВ каком виде хотите получить ответ?")
    print ("1. Список")
    print ("2. Таблица")
    ask = input("Выбор: ")
    if ask != "1" and ask != "2":
        Choice()
    else:
        return ask

def main():
    sys('cls')
    StartApp()
    sentence = EnterSentence()
    listofwords = HandlerSentence(sentence)
    ask = Choice()
    if ask == "1":
        sys('cls')
        count, longestword = CountWordLen(listofwords)
        console.print (f"\nСамое длинное слово: \"{longestword}\"")
        console.print (f"Количество букв: {count}")
    else:
        sys('cls')
        count, longestword, table = CountWordLenTable(listofwords)
        console.print('\n', table)
        console.print (f"\nСамое длинное слово: \"{longestword}\"")
        console.print (f"Количество букв: {count}")

if __name__ == "__main__":
    main()