__author__ = "Карук Ю.А"

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number = input("Введите любое число: ")
i = 0
while i < len(number):
    print(number[i])
    i = i + 1


