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

    @property
    def count(self) -> int:
        return len(self.__shapes)

    def __len__(self) -> int:
        return len(self.__shapes)

    def __getitem__(self, index: int) -> Shape:
        return self.get_shape(index)

    def __iter__(self):
        return iter(self.__shapes)