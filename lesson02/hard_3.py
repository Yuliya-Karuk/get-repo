# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3


# x - номер комнаты
# z - размер этажа
# floo - номер этажа

x = 1
z = 1
tower = []
while x < 100:
    for i in range(z):
        new = []
        for i in range(z):
            new.append(x)
            x = x + 1
        tower.append(new)
    z = z + 1

print(tower)

# пусть number = 40. Вычисление размерности этажа. Размерность = n
user_number = int(input("Введите номер комнаты - "))
n = 1
number = user_number
while number > 0:
    number = number - n**2
    if number <= 0:
        number = number + n**2
        break
    else:
        n = n + 1


# пусть number = 40. Вычисление номера массива из массивов одинаковой размерности. Номер массива = m
m = 1
while number > 0:
    number = number - n
    if number <= 0:
        break
    m = m + 1

#теперь мы знаем размерность массива и номер массива с определенной размерность. Можно узнать номер этаж - это номер массива из tower.
# количество этажей с другой размерность до нужной размерности = k. Нужный этаж = k + m

k = 0
for i in range(n):
    k = k + i
floo = k + m
print("Этаж заданной комнаты - ", floo)

# комнаты с этажа добавим в отдельный список, чтобы узнать порядковый номер комнаты слева - floo_number
lst = tower[floo-1]
floo_number = lst.index(user_number) + 1
print("Порядковый номер комнаты слева -", floo_number)