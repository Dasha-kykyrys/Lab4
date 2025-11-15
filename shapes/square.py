from abc import ABC
from shapes.base import Shape

class Square(Shape, ABC):
    def __init__(self, color, side):
        super().__init__("Квадрат", color)
        self.__side = side

    def calculate_area(self):
        return self.__side * self.__side

    def calculate_perimeter(self):
        return 4 * self.__side

    def display_info(self):
        super().display_info()
        print(f"Ширина:{self.__side}")
        print(f"Высота:{self.__side}")

    @property
    def width(self):
        return self.__side

    @width.setter
    def width(self, w):
        if w <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__side = w

    @property
    def height(self):
        return self.__side

    @height.setter
    def height(self, h):
        if h <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__side = h