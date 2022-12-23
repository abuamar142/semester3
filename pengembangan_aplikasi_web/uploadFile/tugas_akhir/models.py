from datetime import datetime
import pymysql
import config

database = cursor = None

class Cashflow:
    def __init__(self):
        pass

    def openDatabase(self):
        global database, cursor
        database = pymysql.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME,
        )
        cursor = database.cursor()

    def closeDatabase(self):
        global database, cursor
        database.close()

    def insertPengeluaran(self, nama_file):
        self.openDatabase()
        # today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO TRANSAKSI (TRANSAKSI_ID, NAMA_USER, JENIS_TRANSAKSI, KETERANGAN, NOMINAL, NAMA_NOTA, TANGGAL) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (nama_file)
        )
        print(f'Data {nama_file} berhasil ditambahkan ke database.')
        database.commit()
        self.closeDatabase()

    def getCountDatainDatabase(self):
        self.openDatabase()
        cursor.execute(
            "SELECT COUNT(TRANSAKSI_ID) FROM TRANSAKSI"
        )
        jumlah_data_di_database = cursor.fetchone()
        self.closeDatabase()
        return jumlah_data_di_database[0] + 1

    def getAllDatainDatabase(self):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM TRANSAKSI"
        )
        data = cursor.fetchall()
        self.closeDatabase()
        return data

# model = Cashflow()
# # model.getCountDatainDatabase()

# data = model.getAllDatainDatabase()
# for a in data:
#     print(a[2])
#     format_tanggal = a[2].strftime('%d %B, %Y')
#     print(format_tanggal)