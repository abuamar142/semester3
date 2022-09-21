class item():
    def __init__(self, nama=None, nim=None, prodi=None, gender=None):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.gender = gender

    def setNama(self, nama):
        self.nama = nama

    def getNama(self):
        return self.nama

    def setNim(self, nim):
        self.nim = nim

    def getNim(self):
        return self.nim

    def setProdi(self, prodi):
        self.prodi = prodi

    def getProdi(self):
        return self.prodi

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender
