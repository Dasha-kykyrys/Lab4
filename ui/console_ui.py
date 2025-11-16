from manager.shape_manager import ShapeManager
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
import json
import os

class ConsoleUI:
    def __init__(self, shape_manager: ShapeManager):
        self.shape_manager = shape_manager

    def run(self):
        while True:
            self.show_main_menu()
            choice = input("Выберите пункт меню: ").strip()

            if choice == "1":
                self.handle_add_shape()
            elif choice == "2":
                self.handle_remove_shape()
            elif choice == "3":
                self.handle_show_all()
            elif choice == "4":
                self.handle_show_statistics()
            elif choice == "5":
                self.handle_find_shapes()
            elif choice == "6":
                self.handle_save_load_menu()
            elif choice == "7":
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def show_main_menu(self):
        print("Главное меню")
        print("1. Добавить фигуру")
        print("2. Удалить фигуру")
        print("3. Показать все фигуры")
        print("4. Показать статистику")
        print("5. Найти фигуры")
        print("6. Сохранить/загрузить отчет")
        print("7. Выход")

    def handle_add_shape(self):
        print("Добавление фигуры")
        print("1. Круг")
        print("2. Прямоугольник")
        print("3. Квадрат")
        print("4. Треугольник")
        print("5. Назад")

        choice = input("Выберите тип фигуры: ").strip()

        if choice == "1":
            self.add_circle()
        elif choice == "2":
            self.add_rectangle()
        elif choice == "3":
            self.add_square()
        elif choice == "4":
            self.add_triangle()
        elif choice == "5":
            return
        else:
            print("Неверный выбор.")

    def add_circle(self):
        try:
            color = input("Введите цвет круга: ").strip()
            radius = float(input("Введите радиус круга: ").strip())

            if radius <= 0:
                print("Радиус должен быть положительным числом!")
                return

            circle = Circle(color, radius)
            self.shape_manager.add_shape(circle)
            print("Круг успешно добавлен!")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def add_rectangle(self):
        try:
            color = input("Введите цвет прямоугольника: ").strip()
            width = float(input("Введите ширину прямоугольника: ").strip())
            height = float(input("Введите высоту прямоугольника: ").strip())

            if width <= 0 or height <= 0:
                print("Ширина и высота должны быть положительными числами!")
                return

            rectangle = Rectangle(color, width, height)
            self.shape_manager.add_shape(rectangle)
            print("Прямоугольник успешно добавлен!")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def add_square(self):
        try:
            color = input("Введите цвет квадрата: ").strip()
            side = float(input("Введите длину стороны квадрата: ").strip())

            if side <= 0:
                print("Сторона должна быть положительным числом!")
                return

            square = Square(color, side)
            self.shape_manager.add_shape(square)
            print("Квадрат успешно добавлен!")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def add_triangle(self):
        try:
            color = input("Введите цвет треугольника: ").strip()
            side_a = float(input("Введите длину стороны A: ").strip())
            side_b = float(input("Введите длину стороны B: ").strip())
            side_c = float(input("Введите длину стороны C: ").strip())

            if side_a <= 0 or side_b <= 0 or side_c <= 0:
                print("Все стороны должны быть положительными числами!")
                return

            triangle = Triangle(side_a, side_b, side_c, color)
            triangle.validate_side()

            if (side_a + side_b <= side_c or
                    side_a + side_c <= side_b or
                    side_b + side_c <= side_a):
                print("Треугольник с такими сторонами не существует!")
                return

            self.shape_manager.add_shape(triangle)
            print("Треугольник успешно добавлен!")

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def handle_remove_shape(self):
        if self.shape_manager.count == 0:
            print("Список фигур пуст!")
            return

        self.handle_show_all()

        try:
            index = int(input("Введите индекс фигуры для удаления: ").strip())
            if self.shape_manager.remove_shape(index):
                print("Фигура успешно удалена!")
            else:
                print("Неверный индекс!")
        except ValueError:
            print("Введите корректный номер!")

    def handle_show_all(self):
        if self.shape_manager.count == 0:
            print("Список фигур пуст!")
            return

        print("Все фигуры")

        for i, shape in enumerate(self.shape_manager):
            print(f"\n Фигура #{i} ")
            shape.display_info()
            print("-" * 30)

    def handle_show_statistics(self):
        if self.shape_manager.count == 0:
            print("Список фигур пуст!")
            return

        print("Статистика")

        try:
            print(f"Общее количество фигур: {self.shape_manager.count}")
            print(f"Общая площадь: {self.shape_manager.calculate_total_area():.2f}")
            print(f"Общий периметр: {self.shape_manager.calculate_total_perimetr():.2f}")
            print(f"Средняя площадь: {self.shape_manager.get_average_area():.2f}")

            largest = self.shape_manager.find_largest_shape()
            smallest = self.shape_manager.find_smallest_shape()

            print(f"\nСамая большая фигура:")
            largest.display_info()

            print(f"\nСамая маленькая фигура:")
            smallest.display_info()

        except Exception as e:
            print(f"Ошибка при расчете статистики: {e}")

    def handle_find_shapes(self):
        if self.shape_manager.count == 0:
            print("Список фигур пуст!")
            return

        print("Поиск фигур")
        print("1. По имени")
        print("2. По цвету")
        print("3. По минимальной площади")
        print("4. Назад")

        choice = input("Выберите тип поиска: ").strip()

        if choice == "1":
            name = input("Введите имя фигуры: ").strip()
            results = self.shape_manager.find_by_name(name)
            self.display_search_results(results, f"фигуры с именем '{name}'")

        elif choice == "2":
            color = input("Введите цвет: ").strip()
            results = self.shape_manager.find_by_color(color)
            self.display_search_results(results, f"фигуры цвета '{color}'")

        elif choice == "3":
            try:
                min_area = float(input("Введите минимальную площадь: ").strip())
                results = self.shape_manager.filter_by_min_area(min_area)
                self.display_search_results(results, f"фигуры с площадью >= {min_area}")
            except ValueError:
                print("Введите корректное число!")

        elif choice == "4":
            return
        else:
            print("Неверный выбор.")

    def display_search_results(self, results, search_description):
        if not results:
            print(f"Фигуры по запросу '{search_description}' не найдены.")
            return

        print(f"\nРезультаты поиска ({search_description}):")
        print("=" * 50)

        for i, shape in enumerate(results):
            print(f"\n--- Результат #{i} ---")
            shape.display_info()
            print("-" * 30)

    def handle_save_load_menu(self):
        print("Отчёты")
        print("1. Сохранить отчет в файл")
        print("2. Загрузить отчет из файла")
        print("3. Назад")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            self.save_report()
        elif choice == "2":
            self.load_report()
        elif choice == "3":
            return
        else:
            print("Неверный выбор.")

    def save_report(self):
        if self.shape_manager.count == 0:
            print("Нет данных для сохранения!")
            return

        try:
            filename = input("Введите имя файла (без расширения): ").strip()
            if not filename:
                print("Имя файла не может быть пустым!")
                return

            filename = f"{filename}.json"

            report_data = {
                "total_shapes": self.shape_manager.count,
                "total_area": self.shape_manager.calculate_total_area(),
                "total_perimeter": self.shape_manager.calculate_total_perimetr(),
                "average_area": self.shape_manager.get_average_area(),
                "shapes": []
            }

            for shape in self.shape_manager:
                shape_data = {
                    "type": shape.name,
                    "color": shape.color,
                    "area": shape.calculate_area(),
                    "perimeter": shape.calculate_perimeter()
                }

                if isinstance(shape, Circle):
                    shape_data["radius"] = shape.radius
                elif isinstance(shape, Rectangle):
                    shape_data["width"] = shape.width
                    shape_data["height"] = shape.height
                    shape_data["is_square"] = shape.is_square()
                elif isinstance(shape, Square):
                    shape_data["side"] = shape.width
                elif isinstance(shape, Triangle):
                    shape_data["side_a"] = shape.side_a
                    shape_data["side_b"] = shape.side_b
                    shape_data["side_c"] = shape.side_c
                    shape_data["triangle_type"] = shape.get_triangle_type()

                report_data["shapes"].append(shape_data)

            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, ensure_ascii=False, indent=2)

            print(f"Отчет успешно сохранен в файл: {filename}")

        except Exception as e:
            print(f"Ошибка при сохранении отчета: {e}")

    def load_report(self):
        try:
            filename = input("Введите имя файла (без расширения): ").strip()
            if not filename:
                print("Имя файла не может быть пустым!")
                return

            filename = f"{filename}.json"

            if not os.path.exists(filename):
                print(f"Файл {filename} не существует!")
                return

            with open(filename, 'r', encoding='utf-8') as f:
                report_data = json.load(f)

            print("Загруженный отчёт")
            print(f"Общее количество фигур: {report_data['total_shapes']}")
            print(f"Общая площадь: {report_data['total_area']:.2f}")
            print(f"Общий периметр: {report_data['total_perimeter']:.2f}")
            print(f"Средняя площадь: {report_data['average_area']:.2f}")

            print("\nДетали по фигурам:")
            for i, shape_data in enumerate(report_data['shapes']):
                print(f"\n Фигура #{i} ")
                print(f"Тип: {shape_data['type']}")
                print(f"Цвет: {shape_data['color']}")
                print(f"Площадь: {shape_data['area']:.2f}")
                print(f"Периметр: {shape_data['perimeter']:.2f}")

                for key, value in shape_data.items():
                    if key not in ['type', 'color', 'area', 'perimeter']:
                        print(f"{key}: {value}")
                print("-" * 30)

        except Exception as e:
            print(f"Ошибка при загрузке отчета: {e}")


def main():
    shape_manager = ShapeManager()
    ui = ConsoleUI(shape_manager)
    ui.run()


if __name__ == "__main__":
    main()