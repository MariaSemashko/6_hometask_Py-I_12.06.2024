'''Создайте модуль и напишите в нем функцию, которая
на вход принимает дату в формате DD.MM.YYYY
Функция возвращает истину, если такая дата может существовать,
и ложь - если нет.
Весь период 1 января 1 года - 31 декабря 9999 года.
Проверку на високосность вынести в отдельную функцию'''

from sys import argv

__all__ = ['date_is_true']

def _is_leap(year:int) -> bool:
    return year%4 == 0 and year%100 != 0 or year%400 == 0


def date_is_true(data:str) -> bool:
    day, month, year = list(map(int, data.split('.')))
    check_days = {
        1:31,
        2:29 if _is_leap(year) else 28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    }
    max_day = check_days.get(month)
    if not max_day or (9999 < year or year < 1) or (max_day < day or day < 1):
        return False
    else:
        return True

if __name__ == '__main__':
    user_date = argv[1]
    print(date_is_true(user_date))


    # print(date_is_true('01.13.2024'))
    # print(date_is_true('01.12.2024'))
    # print(date_is_true('01.12.12024'))

