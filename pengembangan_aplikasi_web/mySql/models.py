import pymysql
import config

database = cursor = None

class BukuTelepon:
    def __init__(self, no=None, nama=None, no_telp=None):
        self.no = no
        self.nama = nama
        self.no_telp = no_telp

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

    def selectDatabase(self):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM buku_telepon"
        )
        container = []
        for no, nama, no_telp in cursor.fetchall():
            container.append((no, nama, no_telp))
        self.closeDatabase()
        return container
