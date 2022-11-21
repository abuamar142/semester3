class Person:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname
    @classmethod
    def from_fullname(cls, fullname):
        firstname, surname = fullname.split()
        return cls(firstname, surname)

jokowi = Person.from_fullname('Joko Widodo')
print(jokowi.firstname, jokowi.surname)