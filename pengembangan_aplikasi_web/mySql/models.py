import pymysql
import config

database = cursor = None

class BukuTelepon:
    def __init__(self, no=None, nama=None, no_telepon=None):
        self.no = no
        self.nama = nama
        self.no_telepon = no_telepon

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
        for no, nama, no_telepon in cursor.fetchall():
            container.append((no, nama, no_telepon))
        self.closeDatabase()
        return container

    def insertDatabase(self, data):
        self.openDatabase()
        cursor.execute("INSERT INTO buku_telepon (nama, no_telepon) VALUES ('%s', '%s')" % data)
        database.commit()
        self.closeDatabase()

    def getDatabasebyNo(self, no):
        self.openDatabase()
        cursor.execute("SELECT * FROM buku_telepon WHERE no='%s'" % no)
        data = cursor.fetchone()
        return data

    def updateDatabase(self, data):
        self.openDatabase()
        cursor.execute("UPDATE buku_telepon SET nama='%s', no_telepon='%s' WHERE no='%s'" % data)
        database.commit()
        self.closeDatabase()

    def deleteDatabase(self, no):
        self.openDatabase()
        cursor.execute("DELETE FROM buku_telepon WHERE no='%s'" % no)
        database.commit()
        self.closeDatabase()