from abc import ABC
from shapes.base import Shape

class Rectangle(Shape, ABC):
    def __init__(self, color, width, height):
        super().__init__("Квадрат", color)
        self.__width = width
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return 2 * self.__width + 2 * self.__height

    def display_info(self):
        super().display_info()
        print(f"Ширина:{self.__width}")
        print(f"Высота:{self.__height}")

    def is_square(self):
        return self.__width == self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w <= 0:
            raise ValueError("Ширина должна быть положительной")
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h <= 0:
            raise ValueError("Высота должна быть положительной")
        self.__height = h