class MyList(list):
    def double(self):
        for index, x in enumerate(self):
            self.__setitem__(index, 2*x)
    def sum(self):
        total = 0
        for a in self:
            total += a
        return total
    def average(self):
        return self.sum() / len(self)

a = MyList([12])
print(a)

a.append(10)
a.append(20)
print(a)

a.double()
print(a)

print(a.average())
