# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.a = 0
        self.b = 0
        self.c = 0
        self.s = 0
        self.h = 0


    def square(self):
        self.s = math.fabs(((self.x2 - self.x1)*(self.y3 - self.y1) - (self.x3 - self.x1)*(self.y2 - self.y1))/2)
        return self.s

    def perimeter(self):
        points = [[self.x1, self.y1], [self.x2, self.y2], [self.x3, self.y3]]
        self.a = int(math.fabs(math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2)))
        self.b = int(math.fabs(math.sqrt((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2)))
        self.c = int(math.fabs(math.sqrt((points[2][0] - points[0][0]) ** 2 + (points[2][1] - points[0][1]) ** 2)))
        summ = self.a + self.b + self.c
        return summ

    def height(self):
        self.h = int(self.s * 2 / self.a)
        return self.h


trian_1 = Triangle(-1, 3, 5, -3, 4, -5)
print(f"Площадь треугольника равна: {trian_1.square()}")
print(f"Периметр треугольника равен: {trian_1.perimeter()}")
print(f"Высота треугольника равна: {trian_1.height()}")




