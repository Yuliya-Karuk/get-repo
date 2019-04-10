# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, points):
        # points[[x1, y1], [x2, y2], [x3, y3]] координаты треугольника, a, b, c - стороны, s - площадь, h - высота
        self.points = points
        self.a = 0
        self.b = 0
        self.c = 0
        self.s = 0
        self.h = 0


    def square(self):
        # вычисление площади треугольника
        self.s = math.fabs(((self.points[1][0] - self.points[0][0])*(self.points[2][1] - self.points[0][1]) - (self.points[2][0] - self.points[0][0])*(self.points[1][1] - self.points[0][1]))/2)
        return self.s

    def perimeter(self):
        # вычисление сторон треугольника
        self.a = int(math.fabs(math.sqrt((self.points[1][0] - self.points[0][0]) ** 2 + (self.points[1][1] - self.points[0][1]) ** 2)))
        self.b = int(math.fabs(math.sqrt((self.points[2][0] - self.points[1][0]) ** 2 + (self.points[2][1] - self.points[1][1]) ** 2)))
        self.c = int(math.fabs(math.sqrt((self.points[2][0] - self.points[0][0]) ** 2 + (self.points[2][1] - self.points[0][1]) ** 2)))
        summ = self.a + self.b + self.c
        return summ

    def height(self):
        # вычисление высоты треугольника
        self.h = int(self.s * 2 / self.a)
        return self.h

points = [[-1, -3], [3, 4], [5, -5]]
trian_1 = Triangle(points)
print(f"Площадь треугольника равна: {trian_1.square()}")
print(f"Периметр треугольника равен: {trian_1.perimeter()}")
print(f"Высота треугольника равна: {trian_1.height()}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.









