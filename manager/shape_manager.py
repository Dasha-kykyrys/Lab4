from shapes.base import Shape

class ShapeManager:
    def __init__(self):
        self.__shapes = []

    def add_shape(self, shape: Shape) -> None:
        if isinstance(shape, Shape):
            self.__shapes.append(shape)
        else:
            raise TypeError("Можно добавлять только объекты типа Shape")

    def remove_shape(self, index: int) -> bool:
        if 0 <= index < len(self.__shapes):
            del self.__shapes[index]
            return True
        return False

    def get_shape(self, index: int) -> Shape:
        if 0 <= index < len(self.__shapes):
            return self.__shapes[index]
        raise IndexError("Индекс вне диапазона")

    def get_all_shapes(self) -> list[Shape]:
        return self.__shapes.copy()

    def clear_all(self) -> None:
        self.__shapes.clear()

    def calculate_total_area(self):
        total = 0.0
        for shape in self.__shapes:
            total += shape.calculate_area()
        return total

    def calculate_total_perimetr(self):
        total = 0.0
        for shape in self.__shapes:
            total += shape.calculate_perimeter()
        return total

    def get_average_area(self):
        if len(self.__shapes) == 0:
            return 0.0
        total_area = self.calculate_total_area()
        return total_area / len(self.__shapes)

    def find_by_name(self, name):
        return [shape for shape in self.__shapes if shape.name.lower() == name.lower()]

    def find_by_color(self, color):
        return [shape for shape in self.__shapes if shape.color.lower() == color.lower()]

    def find_largest_shape(self) -> Shape:
        if not self.__shapes:
            raise ValueError("Список фигур пуст")
        return max(self.__shapes, key=lambda shape: shape.calculate_area())

    def find_smallest_shape(self) -> Shape:
        if not self.__shapes:
            raise ValueError("Список фигур пуст")
        return min(self.__shapes, key=lambda shape: shape.calculate_area())

    def filter_by_min_area(self, min_area: float) -> list[Shape]:
        return [shape for shape in self.__shapes if shape.calculate_area() >= min_area]

    @property
    def count(self) -> int:
        return len(self.__shapes)

    def __len__(self) -> int:
        return len(self.__shapes)

    def __getitem__(self, index: int) -> Shape:
        return self.get_shape(index)

    def __iter__(self):
        return iter(self.__shapes)