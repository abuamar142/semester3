data = []

class Transaksi:
    def __init__(self, keterangan="", nominal="", tanggal="", jenis=""):
        self.keterangan = keterangan
        self.nominal = nominal
        self.tanggal = tanggal
        self.jenis = jenis

    def getData(self):
        return data

    def addTransaksi(self):
        transaksi = {
            'keterangan' : self.keterangan,
            'nominal' : self.nominal,
            'jenis' : self.jenis,
            'tanggal' : self.tanggal,
        }

        data.append(transaksi)

    def removeTransaksi(self):
        transaksi = {
            'keterangan' : self.keterangan,
            'nominal' : self.nominal,
            'jenis' : self.jenis,
            'tanggal' : self.tanggal,
        }

        data.remove(transaksi)