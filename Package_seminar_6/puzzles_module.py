'''Задайте модуль с функцией внутри. Функция получает загадку, список с отгадками и 
количество попыток. Возвращает номер попытки, с которой была отгадана 
и 0, если попытки исчерпаны.'''

'''Добавьте сюда функцию, которая хранит словарь списков.
 Ключ - загадка, значение - список отгадок. 
 Функция в цикле вызывает загадывающую функцию, чтобы  передать ей 
 все загадки'''

'''Добавьте в модуль с загадками функцию, которая принимает на вход
строку: текст загадки и число - номер попытки, которой она отгадана
 и формирует словарь с результататми. Надо использовать защищенный
 словарь. Надо написать функцию, которая выводит результаты угадывания.'''


__all__= ['puzzles', 'puzzle_storage']


def puzzles(puzzle: str, answers:list[str], counter:int=3) -> int:
    print('Отгадай загадку')
    print(f'{puzzle}')
    for i in range(counter):
        answer = input('Введите ответ: ').lower()
        if answer in answers:
            print(f'Поздравляем, вы угадали с попытки {i + 1}')
            return i + 1
    print('К сожалению вы не угадали. Попытки исчерпаны.')
    return 0

def puzzle_storage():
    storage = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'елка'],
        'Не лает, не кусает, домой не пускает': ['замок', 'затвор', 'щеколда'],
        'Красна девица сидит в темнице, а коса на улицу': ['морковка', 'морковь']
    }

    for k, v in storage.items():
        result = puzzles(k, v)
        save_results(k, result)
        print('Не угадал' if not result else f'Поздравляем, вы угадали с попытки {result}')

_data = {}

def save_results(text:str, num:int):
    _data[text] = num

def show_results(data:dict):
    res = (f'Загадку {k} не угадали' if not v
           else f'Поздравляем, вы угадали загадку {k} с {v} попытки'
    for k, v in data.items())
    print(*res, sep='\n')

if __name__ == '__main__':
    # puzzles(puzzle='Зимой и летом одним цветом', answers=['ель', 'ёлка', 'елка'])
    puzzle_storage()
    show_results(_data)