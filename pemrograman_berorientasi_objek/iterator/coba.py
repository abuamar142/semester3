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
# print(file.readlines())

# for i, row in enumerate(file.split(" ")):
#   for j, character in enumerate(row):
#     print("Row: {}, Column: {}, Character: {}".format(i, j, character))

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

# number = findStringinFile('a')
# for a in number:
#     print(a)

# print(file.index('dua'))

# file = open('text.txt', 'r')

# def findString(string):
#   lines = file.readlines()
#   for index, line in enumerate(lines):
#     object = line.find(string)
#     if object != -1:
#       row = object + 1
#       column = index + 1
#       return row, column

object = iter(findStringinFile('dua'))
for a in object:
  print(a)
  