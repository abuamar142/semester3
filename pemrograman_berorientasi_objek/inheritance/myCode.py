class MyCode(int):
    def __repr__(self):
        return '%04d' % self

code = MyCode(10)
print(code)