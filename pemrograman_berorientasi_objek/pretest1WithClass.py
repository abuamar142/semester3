class Building:
    def __init__(self):
        self.ruangan = []

    def append(self, ruang):
        hasil = ruang.panjang * ruang.lebar
        self.ruangan.append(hasil)

    def area(self):
        hasil = 0
        for a in self.ruangan:
            hasil += a
            
        return hasil

class Ruang:
    def __init__(self, sisi1, sisi2):
        self.panjang = sisi1
        self.lebar = sisi2

building = Building()

building.append(Ruang(3,4))
building.append(Ruang(3,4))
building.append(Ruang(3,4))
building.append(Ruang(8,5))
building.append(Ruang(3,4))
building.append(Ruang(3,4))
building.append(Ruang(4,4))
building.append(Ruang(4,4))
building.append(Ruang(4,4))

print(f"Total luas ruangan: {building.area()} m^2")