class item():
    def __init__(self, nama=None, nim=None, prodi=None):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

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