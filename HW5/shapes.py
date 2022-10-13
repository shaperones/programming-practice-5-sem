""" Реализовать структуру наследования классов геометрических фигур. Каждый класс должен обладать
методами .area() и .perimeter(). Среди обязательных для реализации структур: круг, треугольник, прямоугольник,
квадрат, ромб. Для простоты можно конструировать фигуры из точек, передающихся в порядке обхода по часовой
стрелке."""


class Point:
    def __init__(self, x=0, y=0):
        self._x = int(x)
        self._y = int(y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return str("(" + str(self._x) + ", " + str(self._y) + ")")


def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5


""" На вход фигуры принимают список из Point() объектов в обходе по часовой стрелке. Я почти не 
занимаюсь защитой от дурака, просто вежливо указываю типы и ругаюсь на все неадекватное. Еще мне 
не хочется делать геттеры и сеттеры :("""


class MyError(Exception):
    pass


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)

    def perimeter(self):
        return None

    def area(self):
        return None


class Circle(Shape):
    def __init__(self, center: Point, radius: int, type='Circle'):
        super().__init__(type)
        self._center = center
        self._radius = radius

    def __str__(self):
        return " ".join([super().__str__(), self._center.__str__(), self._radius.__str__()])

    def perimeter(self):
        return 2 * 3.1415 * self._radius

    def area(self):
        return 3.1415 * self._radius ** 2


class Polygon(Shape):
    def __init__(self, points: list, type="Polygon"):
        super().__init__(type)
        self._points = points

    def __str__(self):
        return " ".join([super().__str__(), " ".join([point.__str__() for point in self._points])])

    def perimeter(self):
        perimeter = 0
        prev_point = self._points[-1]
        for i in range(len(self._points)):
            next_point = self._points[i]
            perimeter += dist(prev_point, next_point)
            prev_point = next_point
        return perimeter

    def area(self):  # разбиваем многоугольник на треугольники и считаем площадь треугольников по точкам
        area = 0
        st = self._points[0]
        p1 = self._points[1]
        for i in range(2, len(self._points)):
            p2 = self._points[i]
            area += 0.5 * abs(p1.get_x() * (p2.get_y() - st.get_y()) -
                              p2.get_x() * (st.get_y() - p1.get_y()) -
                              st.get_x() * (p1.get_y() - p2.get_y())
                              )
            p1 = p2
        return area


class Triangle(Polygon):
    def __init__(self, points: list, type="Triangle"):
        if len(points) == 3:
            super().__init__(points, type)
        else:
            raise MyError('нужно три точки')

    def __str__(self):
        return super().__str__()

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()


class Rhombus(Polygon):
    def __init__(self, points: list, type="Rhombus"):
        if (len(points) == 4 and
                dist(points[0], points[1]) ==
                dist(points[2], points[3]) ==
                dist(points[1], points[2]) ==
                dist(points[0], points[3])):
            super().__init__(points, type)
        else:
            raise MyError('ты вводишь даже не ромб')

    def __str__(self):
        return super().__str__()

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()


class Rectangle(Polygon):
    def __init__(self, points: list, type="Rectangle"):
        x01 = points[1].get_x() - points[0].get_x()
        x03 = points[3].get_x() - points[0].get_x()
        y01 = points[1].get_y() - points[0].get_y()
        y03 = points[3].get_y() - points[0].get_y()
        x21 = points[1].get_x() - points[2].get_x()
        x23 = points[3].get_x() - points[2].get_x()
        y21 = points[1].get_y() - points[2].get_y()
        y23 = points[3].get_y() - points[2].get_y()
        if (len(points) == 4 and
            (x01 * x03 + y01 * y03) == 0 and
                (x21 * x23 + y21 * y23) == 0):
            super().__init__(points, type)
        else:
            raise MyError('ты вводишь даже не прямоугольник')

    def __str__(self):
        return super().__str__()

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()


class Square(Rectangle, Rhombus):
    def __init__(self, points: list, type="Square"):
        if (len(points) == 4 and
                dist(points[0], points[1]) == dist(points[1], points[2])):
            super().__init__(points, type)
        else:
            raise MyError('ты вводишь даже не квадрат')

    def __str__(self):
        return super().__str__()

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()


a = Polygon([Point(), Point(1, 1), Point(3, 2)])
print(a, a.area(), a.perimeter())
b = Triangle([Point(), Point(1, 1), Point(3, 2)])
print(b, b.area(), b.perimeter())
c = Circle(Point(), 1)
print(c, c.area(), c.perimeter())
d = Rectangle([Point(), Point(0, 1), Point(1, 1), Point(1, 0)])
print(d, d.area(), d.perimeter())
try:
    m = Rhombus([Point(), Point(1, 1), Point(3, 2)])
except MyError:
    print('error works')
try:
    m = Rhombus([Point('word', 'word'), Point(1, 1), Point(3, 2)])
except ValueError:
    print('error works')




