# Задача: Классы Triangle и Square

**Ответственный:** Алина
**Статус:** 
**Срок:** 

## Описание
Реализовать классы для треугольника и квадрата

## Требования
### Triangle
- [ ] Создать класс `Triangle` в файлах `Triangle.h` и `Triangle.cpp`
- [ ] Наследование от `Shape`
- [ ] Приватные поля: `sideA`, `sideB`, `sideC` (double)
- [ ] Реализация `calculateArea()` по формуле Герона
- [ ] Реализация `calculatePerimeter()` (sum of sides)
- [ ] Валидация: проверка существования треугольника (a+b>c, a+c>b, b+c>a)
- [ ] Конструктор: `Triangle(double a, double b, double c, string color)`

### Square
- [ ] Создать класс `Square` в файлах `Square.h` и `Square.cpp`
- [ ] Наследование от `Rectangle`
- [ ] Конструктор с одним параметром: `Square(double side, string color)`
- [ ] Автоматическая установка width = height = side

