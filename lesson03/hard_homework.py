# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

st = '-2/3 - -2'

# Функция разлаживает строку на 4 члена в списокБ где 1 и 3 челоя часть дроби и числитель,
# а 2 и 4 знаменатель
def conter(srt, x):
    a = srt.split(x)
    for i in range(2):
        if len(a[i]) < 3:
            a[i] = a[i] + ' 0/1'
    new = []
    for i in a:
        for j in i.split('/'):
            new.append(j)
    return new


# Функция вычисляет действие над дробью
def moving(srt):
    x = 0
    if ' + ' in srt:
        x = ' + '
    elif ' - ' in srt:
        x = ' - '
    else:
        pass
    return x

# Функция находящая целую часть в дроби  и собирающая целую часть в знаменатель
def natur(lst):
    new = []
    for i in range(0, 4, 2):
        if ' ' in lst[i]:
            x = lst[i].find(' ')
            a = lst[i]
            if '-' in a:
                number = -(int(a[1:x]) * int(lst[1]) * int(lst[3]) + int(a[x:]))
            else:
                number = int(a[0:x]) * int(lst[1]) * int(lst[3]) + int(a[x:])
            new.append(number)
        else:
            new.append(int(int(lst[i]) * (int(lst[1]) * int(lst[3]) / int(lst[i+1]))))
    new.append(int(lst[1]) * int(lst[3]))
    return new


#Функция вычисления результата
def result(lst, x):
    if x == ' + ':
        rest = lst[0] + lst[1]
    else:
        rest = lst[0] - lst[1]
    whole_number = 0

    if abs(rest) >= lst[2]:
        whole_number = (abs(rest) // lst[2])
        if rest < 0:
            whole_number = -whole_number
        rest = abs(rest) % lst[2]
        if rest == 0:
            return whole_number
    elif rest == 0:
        return 0
    else:
        whole_number = ''

    for i in range(1, 9):
        if rest % i == 0 and lst[2] % i == 0:
            rest = int(rest / i)
            lst[2] = int(lst[2] / i)
        else:
            pass
    return str(whole_number) + ' ' + str(rest) + '/' + str(lst[2])



sign = moving(st)
lst_conter = conter(st, sign)
lst_natur = natur(lst_conter)
integ = result(lst_natur, sign)

print(integ)


"""Fin = open("workers.txt", "r")

str1 = Fin.readline() # str1 = 1
str2 = Fin.readline() # str2 = 2

str = Fin.readline().split()
print(str1)
print(str[0])
print(str[1])
  # работа с файлами

Fin.close()"""
