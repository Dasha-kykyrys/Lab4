from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def display_info(self):
        print(f"Название: {self.__name}")
        print(f"Цвет: {self.__color}")
        print(f"Площадь: {self.calculate_area()}")
        print(f"Периметр: {self.calculate_perimeter()}")

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color