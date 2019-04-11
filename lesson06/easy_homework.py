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


lst = [[2, 2], [9, 4], [3, 4], [10, 2]]
print("Даны точки с координатами", lst)
#координаты по Х в один список, координаты по Y - во второй
#основания трапеции из математики - a,b, боковые стороны - c,d, диагонали - d1,d2.

class equal_barrel:
    def __init__(self, points):
        self.points = points
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.d1 = 0
        self.d2 = 0
        self.x = 0
        self.s = 0
        self.h = 0
        self.sides = []

    def dif_sides(self):
        # вычисление сторон трапеции и диагоналей AA = math.sqrt((X1 - X2)**2 + (Y1-Y2)**2). Функция не зависит от порядка введения точекю
        i = 0
        while i < len(self.points):
            for z in range(i + 1, len(self.points)):
                self.x = float(math.sqrt((self.points[i][0] - self.points[z][0]) ** 2 + (self.points[i][1] - self.points[z][1]) ** 2))
                self.sides.append(self.x)
            i = i + 1
        return self.sides


    def cheking_barrel(self):
        # сравнение диагоналей и боковых сторон, в зависимости от порядка точек
        if (
                self.sides[0] == self.sides[5] and self.sides[1] == self.sides[4] or
                self.sides[0] == self.sides[5] and self.sides[2] == self.sides[3] or
                self.sides[2] == self.sides[3] and self.sides[1] == self.sides[4]
        ):
            return 'четырехугольник по точкам является трапецией'
        else:
            return 'четырехугольник по точкам не является трапецией'

    def sorted_sides(self):
        #сортировка сторон по условиям: основания - a,b, боковые стороны - c,d, диагонали - d1,d2. Причем c = d, d1 = d2.

        self.d1 = max([i for i in self.sides if self.sides.count(i) > 1])
        self.d2 = self.d1
        self.c = min([i for i in self.sides if self.sides.count(i) > 1])
        self.d = self.c
        for i in [self.d1, self.d2, self.c, self.d]:
            self.sides.remove(i)
        self.a = max(self.sides)
        self.b = min(self.sides)
        return f'основания {self.a, self.b}, боковые стороны - {self.c, self.d}'

    def perimeter(self):
        sum_sides = self.a + self.b + self.c + self.d
        return sum_sides

    def square(self):
        # S = (a + b)/4 * math.sqrt(4*c**2 - (a-b)**2)
        self.s = ((self.a+self.b)/4) * math.sqrt(4*(self.c**2) - (self.a-self.b)**2)
        return self.s, self.h



barrel = equal_barrel(lst)
print(barrel.dif_sides())
print(barrel.cheking_barrel())
print(barrel.sorted_sides())
print(barrel.perimeter())
print(barrel.square())









