'''Создать модуль с функцией внутри. Функцияпринимает на
вход три целых числа: верхний и нижний пределы и число попыток.
Внутри генерируется сулчайное число, пользователь
должен его угадать.'''

'''Добавьте возможность запуска функции из модуля в 
командной строке терминала. Строка должна принимать три аргумента.
Для преобразования строки в число использовать генераторное выражение.
'''

from random import randint
from sys import argv

__all__ = ['guess_number']

def guess_number(low:int=0, up:int=100, counter:int=10) -> bool:
    guess = randint(low, up)
    for _ in range(counter):
        number = int(input('Введите число: '))
        if number < guess:
            print('Загаданное число больше')
        elif number > guess:
            print('Загаданное число меньше')
        else:
            print('Поздравляю, вы угадали')
            return True
    print('Увы, вы не угадали. Попытки кончились.')
    return False

if __name__ == '__main__':
    param = argv[1:]
    guess_number(*(int(item) for item in param))

