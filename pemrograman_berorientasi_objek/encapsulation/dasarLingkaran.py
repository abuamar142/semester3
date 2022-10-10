from math import pi

# biasakan untuk method internal ditaruh paling atas
# kalo gak gitu bisa setelah method init
# kemudian selanjutnya bisa getter setter selang seling tergantung preferensi
class Circle:
    # untuk recalc dikasi 2 undescore didepan variable karena ini merupakan internal method, yaitu sebuah method yang dapat dijalankan didalam class ini saja.
    def __recalc(self):
        self.__diameter = 2 * self.__radius
        self.__area = pi * self.__radius ** 2
        self.__circumference = 2 * pi * self.__radius

    def __init__(self, radius):
        self.__radius = radius
        self.__recalc()

    @property
    def radius(self):
        return self.__radius
    
    @property
    def diameter(self):
        return self.__diameter

    @property
    def area(self):
        return self.__area

    @property
    def circumference(self):
        return self.__circumference

    @radius.setter
    def radius(self, radius):
        self.__radius = radius
        self.__recalc()

if __name__ == '__main__':
    c = Circle(10)
    print(c.radius, c.diameter, c.area, c.circumference)

    c.radius = 15
    print(c.radius, c.diameter, c.area, c.circumference)