import math
from shapes.base import Shape

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__("Круг", color)
        self.__radius = radius

    def calculate_area(self):
        return math.pi * math.pow(self.__radius, 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

    def display_info(self):
        super().display_info()
        print(f"Радиус: {self.__radius}")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, rad):
        if rad <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.__radius = rad