# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** ndigits) + 0.41
    number = number // 1
    return number / (10 ** ndigits)

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func,lst):
    for i in lst:
        if func(i) == False:
            lst.remove(i)
    return lst

#Пример любой функции
def kvadr(x):
    z = x**2 + 4
    return z

numbers = [1, 3, 4]
print(my_filter(kvadr, numbers))