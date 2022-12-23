'''
Buat class iterator beserta generator yang bisa menjalankan fungsi berikut:
1. Mengiterasi bilangan bulat dari n menuju ke nol (terbalik)
2. Mengiterasi bilangan prima di antara 2 bilangan bulat a dan b
3. Mengiterasi lokasi (baris, kolom) dari suatu string di dalam file
'''

'''
Jawaban nomor 1
'''
# iterator
class reversedNumber:
    def __init__(self, number):
        self.current = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        current = self.current
        self.current -= 1
        return current

number = reversedNumber(9)
for a in number:
    print(a)

# generator
def reversed_number(n):
  current_number = n
  while current_number >= 0:
    yield current_number
    current_number -= 1

object = iter(reversed_number(9))
for a in object:
    print(a)

'''
Jawaban nomor 2
'''
# iterator
class PrimeNumberBetween:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.current = self.a

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.b:
            raise StopIteration
        while not self.prime(self.current):
            self.current += 1
            if self.current >= self.b:
                raise StopIteration
        current = self.current
        self.current += 1
        return current
            

    def prime(self, n):
        if n < 2:
            return False
        for number in range(2, n):
            if n % number == 0:
                return False
        return True

for prime in PrimeNumberBetween(2,15):
    print(prime)

# generator
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_numbers_between(a, b):
    for n in range(a, b+1):
        if check_prime(n):
            yield n

# buat generator objek
prime_numbers = iter(prime_numbers_between(2, 15))

# print hasil
print(next(prime_numbers))
print(next(prime_numbers))
print(next(prime_numbers))

'''
Jawaban nomor 3
'''
file = open('text.txt', 'r')

# iterator
class findStringinFile:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return self

    def __next__(self):
        lines = file.readlines()
        for index, line in enumerate(lines):
          object = line.find(self.string)
          if object != -1:
            row = object + 1
            column = index + 1
            return row, column
        raise StopIteration