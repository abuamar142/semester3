from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def _get_area(self): pass
    @abstractmethod
    def _get_perimeter(self): pass
    @property
    def area(self):
        return self._get_area()
    @property
    def perimeter(self):
        return self._get_perimeter()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def _get_area(self):
        return pi * self.radius ** 2
    def _get_perimeter(self):
        return 2 * pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def _get_area(self):
        return self.side ** 2
    def _get_perimeter(self):
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def _get_area(self):
        return self.width * self.height
    def _get_perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def _get_area(self):
        return 0.5 * self.base * self.height
    def _get_perimeter(self):
        return None

if __name__ == '__main__':
    c = Circle(10)
    print(c.area, c.perimeter)
    s = Square(10)
    print(s.area, s.perimeter)
    r = Rectangle(10, 6)
    print(r.area, r.perimeter)
    t = Triangle(4, 5)
    print(t.area, t.perimeter)