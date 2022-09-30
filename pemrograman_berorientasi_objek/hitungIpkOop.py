class Kelas:
    def __init__(self, peserta):
        self.peserta = peserta
        total_ipk = 0
        for mahasiswa in self.peserta:
            total_ipk += mahasiswa.ipk
        self.rata2_ipk = total_ipk / len(peserta)

class Mahasiswa:
    def __init__(self, npm, nama, hasil_studi):
        self.npm = npm
        self.nama = nama
        self.hasil_studi = hasil_studi
        total_sks = 0
        total_skor = 0
        for nilai in self.hasil_studi:
            total_sks += nilai.mata_kuliah.sks
            total_skor += nilai.skor
        self.ipk = total_skor / total_sks

class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai
        self.skor = self.mata_kuliah.sks * {
            'A': 4, 'A-': 3.75, 'AB': 3.5, 'B+': 3.25,
            'B': 3, 'B-': 2.75, 'BC': 2.5, 'C+': 2.25,
            'C': 2,
            'D': 1,
    }.get(self.nilai, 0)

mk_Inf001 = MataKuliah('INF001', 'Konsep Pemrograman', 4)
mk_Inf002 = MataKuliah('INF002', 'Pengantar Teknologi Informasi', 2)

kelas = Kelas([
    Mahasiswa('2121001', 'Naruto Saifudin', [
        Nilai(mk_Inf001, 'A'),
        Nilai(mk_Inf002, 'A-'),
    ]),
    Mahasiswa('2121002', 'Saitama Gundul', [
        Nilai(mk_Inf001, 'B'),
        Nilai(mk_Inf002, 'B+'),
    ]),
])

rata2_ipk = kelas.rata2_ipk

print(rata2_ipk)