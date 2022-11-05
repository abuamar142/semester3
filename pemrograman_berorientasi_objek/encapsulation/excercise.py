class Person:
    def __init__(self, firstname, surname, front_titles=[], back_titles=[]):
        self.__firstname = firstname
        self.__surname = surname
        self.__front_titles = front_titles
        self.__back_titles = back_titles
        self.__gabung()

    def __gabung(self):
        self.__fullname = f'{self.__firstname} {self.__surname}'
        if len(self.__front_titles) > 0:
            __titles = ''
            for title in self.__front_titles:
                __titles += f'{title} '
            self.__fullname = f'{__titles}{self.__fullname}'
        if len(self.__back_titles) > 0:
            __titles = ''
            for title in self.__back_titles:
                __titles += f', {title}'
            self.__fullname = f'{self.__fullname}{__titles}'

    @property
    def firstname(self):
        return self.__firstname

    @property
    def surname(self):
        return self.__surname

    @property
    def front_titles(self):
        return self.__front_titles

    @property
    def back_titles(self):
        return self.__back_titles

    @property
    def fullname(self):
        return self.__fullname

    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname
        self.__gabung()
    
    @surname.setter
    def surname(self, surname):
        self.__surname = surname
        self.__gabung()
    
    @front_titles.setter
    def front_titles(self, front_titles):
        self.__front_titles = front_titles
        self.__gabung()
    
    @back_titles.setter
    def back_titles(self, back_titles):
        self.__back_titles = back_titles
        self.__gabung()

jokowi = Person('Joko', 'Widodo', ['Dr.', 'Ir.'], ['S.T.'])
print(jokowi.fullname) 

jokowi.back_titles = ['M.Eng.']
print(jokowi.fullname)