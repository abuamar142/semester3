from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length

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

class FormData(FlaskForm):
    global keterangan, nominal
    keterangan = StringField('Keterangan', validators=[InputRequired('Keterangan harus diisi...!!!'), Length(max=100)])
    nominal = StringField('Nominal', validators=[InputRequired('Nominal harus diisi...!!!'), Length(min=4)])