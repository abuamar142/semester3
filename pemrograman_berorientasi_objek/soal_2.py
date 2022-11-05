class Person:
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def __repr__(self):
        return f'{self.fullname}'
        
    @classmethod
    def from_fullname(cls, firstname, surname):
        fullname = firstname + surname
        return cls(fullname)

jokowi = Person.from_fullname('Joko', 'Widodo')
print(jokowi)