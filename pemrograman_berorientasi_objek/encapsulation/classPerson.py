class Person:
    def __init__(self, firstname, surname, front_titles=[], back_titles=[]):
        self.firstname = firstname
        self.surname = surname
        self.front_titles = front_titles
        self.back_titles = back_titles
        self.fullname = f'{self.firstname} {self.surname}'
        if len(front_titles) > 0:
            titles = ''
            for title in front_titles:
                titles += f'{title} '
            self.fullname = f'{titles}{self.fullname}'
        if len(back_titles) > 0:
            titles = ''
            for title in back_titles:
                titles += f', {title}'
            self.fullname = f'{self.fullname}{titles}'

jokowi = Person('Joko', 'Widodo', ['Dr.', 'Ir.'], ['S.T.'])
print(jokowi.fullname)