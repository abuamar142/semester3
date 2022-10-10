class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

class Penilaian:
    def __init__(self, mata_kuliah, nilai):
        self.__mata_kuliah = mata_kuliah
        self.__nilai = nilai
        self.__hitung_skor()

    def __hitung_skor(self):
        sks = self.mata_kuliah.sks
        self.__skor = sks * {
            'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0
        }.get(self.__nilai, 0)

    @property
    def mata_kuliah(self):
        return self.__mata_kuliah

    @property
    def nilai(self):
        return self.__nilai

    @property
    def skor(self):
        return self.__skor

    @mata_kuliah.setter
    def mata_kuliah(self, mata_kuliah):
        self.__mata_kuliah = mata_kuliah
        self.__hitung_skor()

    @nilai.setter
    def nilai(self, nilai):
        self.__nilai = nilai
        self.__hitung_skor()


class Mahasiswa:
    def __init__(self, npm, nama, hasil_studi):
        self.npm = npm
        self.nama = nama
        self.__hasil_studi = hasil_studi
        self.__hitung_ipk()

    def __hitung_ipk(self):
        total_skor = total_sks = 0
        for penilaian in self.__hasil_studi:
            total_sks += penilaian.mata_kuliah.sks
            total_skor += penilaian.skor

        self.__ipk = total_skor / total_sks

    @property
    def hasil_studi(self):
        return self.__hasil_studi
    
    @property
    def ipk(self):
        return self.__ipk

    @hasil_studi.setter
    def hasil_studi(self, hasil_studi):
        self.__hasil_studi = hasil_studi
        self.__hitung_ipk()

if __name__ == '__main__':
    inf001 = MataKuliah('INF001', 'Konsep Pemrograman', 4)
    inf002 = MataKuliah('INF002', 'Pengantar Teknologi Informasi', 2)

    mahasiswa = Mahasiswa('2121002', 'Joko Winarko', [
        Penilaian(inf001, 'A'),
        Penilaian(inf002, 'B'),
    ])

    print(mahasiswa.ipk)
    