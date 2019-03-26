# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    new = []
    for i in range(len(origin_list)):
        new.append(min(origin_list))
        origin_list.remove(min(origin_list))
    return new


a = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func,lst):
    new = []
    for i in lst:
        a = func(i)
        new.append(a)
    return new

#Пример любой функции
def kvadr(x):
    z = x**2 + 4
    return z

numbers = [1, 3, 4]
print(my_filter(kvadr, numbers))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

points = [[2, 2], [4, 6], [14, 6], [12, 2]]
print("Даны точки с координатами", points)
#координаты по Х в один список, координаты по Y - во второй
x = []
y = []
for i in points:
    x.append(i[0])
    y.append(i[1])

#Решать задачу будем с условием, что 2 стороны параллелограмма попарно раны.
#Сторону параллелограмма можно найти по формуле AA = math.sqrt((X1 - X2)**2 + (Y1-Y2)**2)
#Функция qvadr находит (Z1 - Z2)**2 - 6 возможных вариантов и помещает их список

def qvadr(lst):
    new = []
    i = 0
    while i < len(lst):
        for z in range(i+1,len(lst)):
            a = (lst[i] - lst[z])**2
            new.append(a)
        i= i + 1
    return new

a = qvadr(x)
b = qvadr(y)

#Находим 6 возможных отрезков
new_list = list(map(lambda x,y : math.sqrt(x+y), a, b))

#Сравнение сторон параллелограмма
if new_list[0] == new_list[5]:
    if new_list[2] == new_list[3] or new_list[1] == new_list[4]:
        print("Фигура из данных 4 точек является параллелограммом")
    else:
        print("Фигура из данных 4 точек не является параллелограммом")