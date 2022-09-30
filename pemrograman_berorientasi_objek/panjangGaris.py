from math import sqrt

class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Garis:
    def __init__(self, awal, akhir):
        self.awal = awal
        self.akhir = akhir
        x1, y1 = awal.x, awal.y
        x2, y2 = akhir.x, akhir.y
        self.panjang = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
class Rute:
    def __init__(self, daftar_ruas):
        self.daftar_ruas = daftar_ruas
        self.panjang = 0
        for ruas in daftar_ruas:
            self.panjang += ruas.panjang
        
A = Titik(1, 14)
B = Titik(13, 12)
C = Titik(4, 9)
D = Titik(1, 6)
E = Titik(12, 8)
F = Titik(14, 1)
G = Titik(5, 4)
H = Titik(2, 2)
 
jalur = Rute([
    Garis(A, B),
    Garis(B, C),
    Garis(C, D),
    Garis(D, E),
    Garis(E, F),
    Garis(F, G),
    Garis(G, H)
    ])

panjang = jalur.panjang

print(panjang)