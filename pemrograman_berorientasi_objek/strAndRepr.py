# class Employee:
#     def __new__(cls):
#         print ("__new__ magic method is called")
#         inst = object.__new__(cls)
#         print(inst)
#         return inst
#     def __init__(self):
#         print ("__init__ magic method is called")
#         self.name='Satya'

# dayat = Employee()

class Student():
    def __init__(self, npm, name):
        self.npm = npm
        self.name = name

    def __str__(self):
        return f'This is a student, nama = {self.name}, npm = {self.npm}'

tono = Student('2121001', 'Tono Wiyono')

# class Student():
#     def __init__(self, npm, name):
#         self.npm = npm
#         self.name = name

#     def __repr__(self):
#         return f'A student, nama = {self.name}, npm = {self.npm}'

# tono = Student('2121001', 'Tono Wiyono')

# cara menggunakannya yaitu dengan masuk ke console python
# kemudian import nama filenya 'import strAndRepr as student'
# kemudian tuliskan 'student.tono'