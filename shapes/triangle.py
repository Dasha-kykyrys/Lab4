import math
from abc import ABC
from shapes.base import Shape

class Triangle(Shape, ABC):
    def __init__(self, side_a, side_b, side_c, color):
        super().__init__("Треугольник", color)
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def validate_side(self):
        if (self.__side_a + self.__side_b > self.__side_c
                and self.__side_a + self.__side_c > self.__side_b
                and self.__side_b + self.__side_c > self.__side_a):
            print("Треугольник с такими сторонами существует")
        else:
            print("Треугольника не существует")

    def calculate_area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        s = math.sqrt(p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c))
        return s

    def calculate_perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c

    def get_triangle_type(self):
        if self.__side_a == self.__side_b == self.__side_c:
            return "Треугольник равносторонний"
        if self.__side_a != self.__side_b != self.__side_c:
            return "Треугольник разносторонний"
        if (self.__side_a == self.__side_b != self.__side_c
                or self.__side_a == self.__side_c != self.__side_b
                or self.__side_b == self.__side_c != self.__side_a):
            return "Треугольник равнобедренный"

    def display_info(self):
        super().display_info()
        print(f"Стороны треугольника:{self.__side_a}, {self.__side_b}, {self.__side_c}")

    @property
    def side_a(self):
        return self.__side_a

    @property
    def side_b(self):
        return self.__side_b

    @property
    def side_c(self):
        return self.__side_c

    @side_a.setter
    def side_a(self, side_a):
        if side_a <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__side_a = side_a

    @side_b.setter
    def side_b(self, side_b):
        if side_b <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__side_b = side_b

    @side_c.setter
    def side_c(self, side_c):
        if side_c <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__side_a = side_c


