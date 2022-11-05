# jarang digunakan
# ketika pada kita menggunakan python untuk buka file, koneksi database
# nah destructor itu untuk menutup file, koneksi diputus walaupun di python akan dilakukan otomatis

class Student():
    def __init__(self, npm, name, height):
        self.npm = npm
        self.name = name
        self.height = height

    def __repr__(self):
        print(f'A student, nama = {self.name}, npm = {self.npm}')

    def __del__(self):
        print(f'A student {self.name} destructor dipanggil')

    def __len__(self):
        return self.height

tono = Student('2121001', 'Tono Wiyono', 166)
print(len(tono))