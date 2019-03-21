# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
print("Список фруктов")
n = 1
for x in fruits:
    print(n, " {:>10}".format(x))
    n += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits = ["яблоко", "банан", "киви", "арбуз", "клубника", "слива", "черешня", "инжир", "хурма"]
exotic_fruit = ["инжир", "маракуйа", "ананас", "хурма"]
print(fruits)
print(exotic_fruit)

for fruit in exotic_fruit:
    if fruit in fruits:
        fruits.remove(fruit)

print(fruits)
print(exotic_fruit)

fruits = ["яблоко", "банан", "киви", "арбуз", "клубника", "слива", "черешня", "инжир", "хурма"]
exotic_fruit = ["инжир", "маракуйа", "ананас", "хурма"]
print(fruits)
print(exotic_fruit)
new = []

for item in set(fruits).difference(exotic_fruit):
    new.append(item)

fruits = new
print(fruits)
print(exotic_fruit)





