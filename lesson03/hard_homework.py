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

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


file_worker = open("workers.txt", "r")
file_hour = open("hours_of.txt", "r")

def counter(X):
    count = 0
    for line in X:
        count += 1
    return count

row_worker = counter(file_worker)
row_hour = counter(file_hour)

file_worker.seek(0)
file_hour.seek(0)

def reading(file, n):
    new = []
    for i in range(n):
        str = file.readline().split()
        new.append(str)
    del new[0]
    return new

lst1 = reading(file_worker, row_worker)
lst2 = reading(file_hour, row_hour)

for i in range(len(lst1)):
    del lst2[i][0]
    del lst1[i][0], lst1[i][2]

for i in lst1:
    for j in lst2:
        if i[0] == j[0]:
            i.append(j[1])

# month_salary = a[i][1], needed_hours = a[i][2], worked_hours = a[i][3]
salary = []

for i in lst1:
    if int(i[3]) <= int(i[2]):
        sal = int(int(i[1])/ int(i[2]) * int(i[3]))
    else:
        sal = int(int(i[1]) + int(i[1]) / int(i[2]) * 2 * (int(i[3])-int(i[2])))
    print('Заработная плата', i[0], sal)

file_worker.close()
file_hour.close()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

f = open("fruits.txt", "r")
alphabet = list(map(chr, range(ord('А'), ord('Я')+1)))

def new_file(f):
    for line in f:
        for j in alphabet:   # считываем файл построчно
            name = 'fruits_' + j + '.txt'
            if j in line:                # пока не найдем нужную информацию
                file = open(name, 'a')
                file.write(line)
            else:
                pass

new_file(f)


