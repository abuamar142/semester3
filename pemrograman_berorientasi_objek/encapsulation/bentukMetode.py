# bentuk metode
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def get_area(self):
        return 1/2 * self.base * self.height
        
x = Triangle(3, 4)
print(x.base, x.height, x.get_area())
x.base = 6
print(x.base, x.height, x.get_area())