# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#number = 123.4563712

def roundit(number, n):
    number = str(number)
    a = number.find(".")
    if int(number[a+n+1]) >= 5:
        number = number[0:n+a] + str(int(number[a+n]) +1)
    else:
        number = number[0:n+a+1]
    print(number)

answer = input("Введите число, которое хотите округлить - ")
n = int(input("Введите нужное число знаков после запятой - "))
roundit(answer, n)