'''Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске
8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.

Программа получает на вход восемь пар чисел, каждое число от 1 до 8 -
координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел
для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.'''

from random import randint

__all__= ['eight_queens', 'generate_position', 'find_position']

def eight_queens(q1:list[int], q2:list[int],q3:list[int],q4:list[int],q5:list[int],q6:list[int],q7:list[int],q8:list[int]) -> bool:
    all_positions = [q1, q2, q3, q4, q5, q6, q7, q8]

    for i in range(len(all_positions)):
        for j in range(i+1, len(all_positions)):
            if all_positions[i][0] + all_positions[i][1] == all_positions[j][0] + all_positions[j][1] \
                    or all_positions[i][0] - all_positions[i][1] == all_positions[j][0] - all_positions[j][1] \
                    or all_positions[i][0] == all_positions[j][0] \
                    or all_positions[i][1] == all_positions[j][1]:
                return False
    return True

def generate_position()-> list[list[int]]:
        all_positions = []
        while len(all_positions) < 8:
            position = [randint(1, 8), randint(1, 8)]
            if position not in all_positions:
                all_positions.append(position)
        return all_positions

def find_position():
    new_positions = generate_position()
    while not eight_queens(*new_positions):
        new_positions = generate_position()
    return (new_positions)


if __name__ == '__main__':
    # print(eight_queens([1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]))
    # print(eight_queens([1, 2], [2, 4], [3, 6], [4, 8], [5, 3], [6, 1], [7, 7], [8, 5]))

    print(find_position())

