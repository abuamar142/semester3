import pymysql
import config

database = cursor = None

class MPengguna():
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

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

    def authenticate(self):
        self.openDatabase()
        cursor.execute("SELECT COUNT(*) FROM pengguna WHERE username = '%s' AND password = MD5('%s') " % (self.username, self.password))
        count_account = (cursor.fetchone())[0]
        self.closeDatabase()
        return True if count_account>0 else False