# Задача: Базовый класс Shape

**Ответственный:** Даша
**Статус:** 
**Срок:** 

## Описание
Создать абстрактный базовый класс для всех геометрических фигур с виртуальными методами

## Требования
- [ ] Создать класс `Shape` 
- [ ] Добавить защищенные поля: `name` (string) и `color` (string)
- [ ] Реализовать виртуальные методы:
  - [ ] `virtual double calculateArea() const = 0`
  - [ ] `virtual double calculatePerimeter() const = 0`
  - [ ] `virtual void displayInfo() const`
- [ ] Сделать деструктор виртуальным: `virtual ~Shape()`
- [ ] Добавить геттеры для name и color
