# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.c = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)

    def perimeter(self):
        p1 = self.a + self.b + self.c
        return round(p1,2)

    def area(self):#площадь считаем через полупериметр треугольника
        p0 = self.perimeter()/2 #полупериметр
        area1 = math.sqrt((p0)*(p0-self.a)*(p0-self.b)*(p0-self.c))
        return round(area1,2)

    def altitude(self):
        h1 = round(2 * self.area() / self.a,2)
        h2 = round(2 * self.area() / self.b,2)
        h3 = round(2 * self.area() / self.c,2)
        return [h1, h2, h3]
triangle1 = triangle(-1,0,3,0,0,3) #тестовый треугольник
print('Площадь {}, Высоты {}, Периметр {}'.format(triangle1.area(),triangle1.altitude(),triangle1.perimeter()))



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezoid:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = float(x1)
        self.y1 = float(y1)
        self.x2 = float(x2)
        self.y2 = float(y2)
        self.x3 = float(x3)
        self.y3 = float(y3)
        self.x4 = float(x4)
        self.y4 = float(y4)

    def sides(self):
        a = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) #сторона а - нижнее основание трапеции
        b = math.sqrt(((self.x3 - self.x2) ** 2) + ((self.y3 - self.y2) ** 2))
        c = math.sqrt(((self.x4 - self.x3) ** 2) + ((self.y4 - self.y3) ** 2))
        d = math.sqrt(((self.x4 - self.x1) ** 2) + ((self.y4 - self.y1) ** 2))
        return [a, b, c, d]

    def is_trap(self):
        if self.sides([1]) == self.sides([3]):
            return 'Трапеция является равнобедренной'
        else:
            return 'Трапеция не является равнобедренной'

    def perimeter(self):
        per = sum(self.sides())
        return per

    def area(self):#площадь трапеции считаем по 4 сторонам
        a = Trapezoid.sides([0])
        b = Trapezoid.sides([1])
        c = Trapezoid.sides([2])
        d = Trapezoid.sides([3])
        S = ((a + b) / 2) * math.sqrt((d ** 2) - ((((a - c) ** 2) + (d ** 2) - (b ** 2) / (2 * (a - c)))))
        return S
trap1 = Trapezoid (0,0,6,0,4,4,2,4)
print('Длины сторон {}, периметр {}, площадь [}'.format(trap1.sides(), trap1.perimeter(), trap1.area()))