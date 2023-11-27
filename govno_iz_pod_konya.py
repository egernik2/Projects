from datetime import datetime


def logger(message):
	f = open('prog.log', 'a')
	data = str(datetime.now()) + ": " + message
	f.write(data)
	f.write("\n")
	f.close()


def parser(stroka):
	first, second = stroka.split('/')
	data = f'[+][INFO] При парсинге строки {stroka} получены следующие значения: {first}, {second}'
	logger(data)
	return int(first), int(second)


def delenie(first, second):
	result = first / second
	data = f'[+][INFO] Результат от деления {first} на {second}: {result}'
	logger(data)
	return result


def percent(char):
	result = str(char * 100) + '%'
	data = f'[+][INFO] При переводе числа {char} в процентный вид дал результат: {result}'
	logger(data)
	return result


def rounder(char):
	result = round(char, 5)
	data = f'[+][INFO] При округлении числа {char} получен результат: {result}'
	logger(data)
	return result


def main():
	stroka = input('Введите вероятность чего нужно посчитать: ')
	first, second = parser(stroka)
	result_delenie = delenie(first, second)
	rounded_result = rounder(result_delenie)
	result = percent(rounded_result)
	print ('Результат: ', result)


if __name__ == "__main__":
	main()
