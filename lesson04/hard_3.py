# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


def is_correct_position(coords: list):
    """
    Проверяет возможность нахождения 8ми ферзей на одной доске 8х8.
    Фактически, проверяет что на каждой строке и столбце одновременно находится лишь одна фигура
    :param coords: Список списков из двух целых
    :return: 'NO' Если ферзи не бьют друг друга, иначе 'YES', 'ERROR' если входные параметры некорректны
    """

    # Попарно сравниваем координаты каждого ферзя
    for i in range(8):
        for j in range(i+1, 8):
            # Если входные параметры некорректны то возвращаем ошибку
            try:
                # Если совподают оси Х, Y или диагонали то значит ферзи бьют друг друга
                if coords[i][0] == coords[j][0] \
                        or coords[i][1] == coords[j][1] \
                        or abs(coords[i][0] - coords[j][0]) == abs(coords[i][1] - coords[j][1]):
                    return 'YES'
            except:
                return 'ERROR'
    # Ферзи не бют друг друга
    return 'NO'


# Проверка результатов
coords = [
    [1, 0],
    [6, 1],
    [4, 2],
    [7, 3],
    [0, 4],
    [3, 5],
    [5, 6],
    [2, 7]
]  # Корректная расстановка
print(is_correct_position(coords))  # NO

from random import randint
random_coords = [[randint(0, 7), randint(0, 7)] for _ in range(8)]
print(is_correct_position(random_coords))  # YES

print(is_correct_position([]))  # ERROR