import pymysql
import config

database = cursor = None

class Postingan:
    def setup(self):
        self.createTableUser()
        self.createTablePost()
        self.createRelation()

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

    def createTableUser(self):
        self.openDatabase()
        try:
            cursor.execute(
                """
                    CREATE TABLE USER (
                        USER_ID INT AUTO_INCREMENT PRIMARY KEY,
                        NAMA VARCHAR(30),
                        USERNAME VARCHAR(10),
                        PASSWORD TEXT
                    )
                """
            )
            print("Berhasil membuat table user")
        except pymysql.Error as error:
            print(str(error))
        self.closeDatabase()

    def createTablePost(self):
        self.openDatabase()
        try:
            cursor.execute(
                """
                    CREATE TABLE POST (
                        POST_ID INT AUTO_INCREMENT PRIMARY KEY,
                        USER_ID INT,
                        PUBLISH_DATE DATE,
                        CAPTION TEXT,
                        IMAGE TEXT
                    )
                """
            )
            print("Berhasil membuat table post")
        except pymysql.Error as error:
            print(error)
        self.closeDatabase()

    def createRelation(self):
        self.openDatabase()
        try:
            cursor.execute(
                """
                    ALTER TABLE POST
                    ADD FOREIGN KEY (USER_ID)
                    REFERENCES USER(USER_ID)
                """
            )
            print("Berhasil membuat relasi table user dan post")
        except:
            print("Relasi gagal dibuat")
        self.closeDatabase()

    def insertUser(self, data_user):
        self.openDatabase()
        cursor.execute(
            "INSERT INTO USER (NAMA, USERNAME, PASSWORD) VALUES('%s', '%s', MD5('%s'))" % data_user
        )
        print(f'User dengan nama = {data_user[0]} berhasil ditambahkan ke database.')
        database.commit()
        self.closeDatabase()

    def insertPost(self, data):
        self.openDatabase()
        cursor.execute(
            "INSERT INTO POST (USER_ID, PUBLISH_DATE, CAPTION, IMAGE) VALUES('%s', '%s', '%s', '%s')" % data
        )
        print(f'Postingan dari user id = {data[0]} berhasil ditambahkan ke database.')
        database.commit()
        self.closeDatabase()

    def getAllDataUser(self):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM USER"
        )
        data = cursor.fetchall()
        self.closeDatabase()
        return data

    def getAllDataPost(self):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM POST"
        )
        data = cursor.fetchall()
        self.closeDatabase()
        return data

    def getImageName(self, user_id):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM POST WHERE USER_ID = '%s' ORDER BY POST_ID DESC LIMIT 4" % user_id
        )
        data = cursor.fetchall()
        self.closeDatabase()
        return data

    def getUserbyUsernameandPassword(self, data_user):
        self.openDatabase()
        cursor.execute(
            "SELECT * FROM USER WHERE USERNAME = '%s' AND PASSWORD = MD5('%s')" % data_user
        )
        data = cursor.fetchone()
        self.closeDatabase()
        return data

    def getCountPostIdinDatabase(self):
        self.openDatabase()
        cursor.execute(
            "SELECT COUNT(POST_ID) FROM POST"
        )
        jumlah_data_di_database = cursor.fetchone()
        self.closeDatabase()
        return jumlah_data_di_database[0] + 1