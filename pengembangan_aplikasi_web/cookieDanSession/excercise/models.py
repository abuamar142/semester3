import pymysql
import config

database = cursor = None

class MPengguna():
    def __init__(self, nama=None, username=None, password=None, role=None):
        self.nama = nama
        self.username = username
        self.password = password
        self.role = role
    
    def openDatabase(self):
        global database, cursor
        database = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        cursor = database.cursor()

    def getDatabase(self, username, password):
        self.openDatabase()
        cursor.execute("SELECT * FROM DATA_PENGGUNA WHERE USERNAME = '%s' AND PASSWORD = '%s'" % (username, password))
        data = cursor.fetchone()
        self.closeDatabase()
        return data

    def deleteDatabase(self, id):
        self.openDatabase()
        cursor.execute("DELETE FROM DATA_PENGGUNA WHERE ID = '%s'" % (id))
        database.commit()
        self.closeDatabase()

    def getDatabaseUser(self):
        self.openDatabase()
        cursor.execute("SELECT * FROM DATA_PENGGUNA WHERE ROLE='user'")
        data = cursor.fetchall()
        self.closeDatabase()
        return data

    def closeDatabase(self):
        global database, cursor
        database.close()

    def insertData(self, data):
        self.openDatabase()
        cursor.execute(
            "INSERT INTO DATA_PENGGUNA (NAMA, USERNAME, PASSWORD, ROLE) VALUES('%s','%s','%s','%s')" % (data)
        )
        database.commit()
        print(f'Data {data[0]} berhasil ditambahkan ke dalam database.')
        self.closeDatabase()

    def authenticate(self, username, password):
        self.openDatabase()
        cursor.execute(
            "SELECT COUNT(*) FROM DATA_PENGGUNA WHERE USERNAME = '%s' AND PASSWORD = '%s'" % (username, password)
        )
        jumlah_akun = (cursor.fetchone())[0]
        self.closeDatabase()
        return True if jumlah_akun > 0 else False