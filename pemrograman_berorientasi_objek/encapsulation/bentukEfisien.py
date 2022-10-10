# bentuk efisien
class Triangle:
    def __init__(self, base, height):
        self.__base = base
        self.__height = height
        self.__recalc()

    def __recalc(self):
        self.__area = 1/2 * self.__base * self.__height

    @property
    def base(self):
        return self.__base

    @property
    def height(self):
        return self.__height

    @property
    def area(self):
        return self.__area

    @base.setter
    def base(self, base):
        self.__base = base
        self.__recalc()

    @height.setter
    def height(self, height):
        self.__height = height
        self.__recalc()
        
x = Triangle(3, 4)
print(x.base, x.height, x.area)
x.base = 6
print(x.base, x.height, x.area)