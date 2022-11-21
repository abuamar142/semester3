from abc import ABC, abstractmethod
from pydraw import resize, clear, circle

class Drawable(ABC):
    @abstractmethod
    def draw(self, x, y): pass

class Canvas: 
    width = 400
    height = 400
    bgcolor = 'white'

    @classmethod
    def initialize(cls, width, height, bgcolor):
        cls.width = width
        cls.height = height
        cls. bgcolor = bgcolor
        resize(cls.width, cls.height)
        clear(cls.bgcolor)

    @classmethod
    def draw_object(cls, x, y, obj: Drawable):
        obj.draw(x, y)

class Circle(Drawable):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def draw(self, x, y):
        circle(x, y, self.radius, self.color)

class Smiley(Drawable):
    def __init__(self, size):
        self.size = size
    def draw(self, x, y):
        circle(x, y, self.size / 2, 'yellow', True)
        circle(x - self.size / 4, y, self.size / 10, 'black', True)
        circle(x + self.size / 4, y, self.size / 10, 'black', True)

if __name__ == '__main__':
    Canvas.initialize(400, 400, 'white')
    Canvas.draw_object(0, 0, Circle(100, 'black'))
    Canvas.draw_object(-200, -200, Circle(100, 'black'))
    Canvas.draw_object(100, -100, Circle(100, 'blue'))
    Canvas.draw_object(200, -200, Smiley(100))