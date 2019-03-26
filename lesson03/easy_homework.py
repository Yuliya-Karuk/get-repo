# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#a - индекс, где находится точка. x - в каком знаке меняется число, если окрглять нужно 9

def my_round(number, n):
    number = str(number)
    a = number.find(".")
    if int(number[a+n+1]) >= 5:
        x = n
        while number[a + x] == "9":
            x = x - 1
        if x == 0:
            number = str(int(number[0:a]) + 1) + "." + "0" * n
        else:
            number = number[0:a+x] + str(int(number[a+x]) + 1) + "0"*(n-x)
    else:
        number = number[0:n+a+1]
    return number

answer = input("Введите число, которое хотите округлить - ")
n = int(input("Введите нужное число знаков после запятой - "))
print(my_round(answer, n))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    a,b = 0,0
    for i in ticket_number[0:3]:
        a = a + int(i)
    for i in ticket_number[3:]:
        b = b + int(i)
    if a == b:
        return "Билет счастливый"
    else:
        return "Билет несчастливый"



print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))