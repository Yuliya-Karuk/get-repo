# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

lst_beg = [random.randint(-10, 10) for i in range(5)]
lst_last = [(lambda i: i*i)(i) for i in lst_beg]
print('Начальный список - ', lst_beg, 'Конечный список - ', lst_last)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits = ["яблоко", "банан", "киви", "арбуз", "клубника", "слива", "черешня", "инжир", "хурма"]
exotic_fruit = ["инжир", "маракуйа", "ананас", "хурма"]
print('Список фруктов - ', fruits, '\nСписок экзотических фруктов - ', exotic_fruit)

inter = [i for i in fruits if i in exotic_fruit]
print('Фрукты в обоих списках', inter)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

original = [random.randint(-100, 100) for i in range(10)]
last = [i for i in original if i >= 0 and i % 3 == 0 and i % 4 != 0]
print('Начальный список', original, '\nКонечный список', last)