from time import sleep

def correct():
    print('\tДобро пожаловать в программу FizzBuzz!\n')
    is_correct = False
    while is_correct == False:
        try:
            n = int(input('Пожалуйста, введите число n больше 1: '))
        except:
            print('\nПожалуйста, введите число, а не символы!\n')
            continue
        print(f'Вы ввели: {n}')
        if n > 1:
            is_correct = True
            print('\n\tПрограмма начинает выполнение...\n')
            func(n)
        else:
            print('\nВведите число больше 1!\n')

def func(n):
    for item in range(n):
        if (item % 2) != 0:
            s = ''
            a = item % 3
            b = item % 5
            if a == 0:
                s += f'Solo'
            if b == 0:
                s += f'Learn'
            if a != 0 and b != 0:
                print(f"Вывод: {item}")
                sleep(0.3)
                continue
            s += f' (Число: {item})'
            print (f'Вывод: {s}')
            sleep(0.3)
        else:
            continue
    print('\n\tПрограмма завершила выполнение...')
    exit()

if __name__ == '__main__':
    correct()