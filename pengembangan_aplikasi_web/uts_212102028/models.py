import pymysql
import config

database = cursor = None

class TabelProduk:
    def __init__(self, id_produk=None, nama_produk=None, deskripsi=None, harga=None, available=None):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.deskripsi = deskripsi
        self.harga = harga
        self.available = available

    def openDatabase(self):
        global database, cursor
        database = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        cursor = database.cursor()

    def closeDatabase(self):
        global database, cursor
        database.close()

    def tampilProduk(self):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM TABEL_PRODUK"
        )
        container = []
        for id_produk, nama_produk, deskripsi, harga, available in cursor.fetchall():
            container.append((id_produk, nama_produk, deskripsi, harga, available))
        self.closeDatabase()
        return container