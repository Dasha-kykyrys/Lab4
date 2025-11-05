# Задача: Система подсчета площади и поиска фигур

**Ответственный:** @alina
**Статус:** 
**Срок:**

## Описание
Реализовать функционал для подсчета общей площади и поиска фигур по характеристикам

## Требования
### Подсчет общей площади
- [ ] Создать функцию `double calculateTotalArea(const vector<Shape*>& shapes)`
- [ ] Функция должна суммировать площади всех фигур в коллекции
- [ ] Обработка пустой коллекции (возврат 0)

### Поиск фигур
- [ ] Функция поиска по имени: `vector<Shape*> findShapesByName(const vector<Shape*>& shapes, const string& name)`
- [ ] Функция поиска по цвету: `vector<Shape*> findShapesByColor(const vector<Shape*>& shapes, const string& color)`
- [ ] Функция поиска фигур с площадью больше заданной: `vector<Shape*> findShapesWithAreaGreaterThan(const vector<Shape*>& shapes, double minArea)`
