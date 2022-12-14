from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class Kontak(FlaskForm):
    nama = StringField('Nama ', validators=[InputRequired('Nama harus diisi..!!'), length(max=25)])
    nomor_telepon = IntegerField('Nomor Handphone: ', validators=[input_required('Nomor Handphone tidak boleh kosong')])
    email = StringField('Email ', validators=[InputRequired('Email harus diisi..!!'), Email('Email tidak ditulis dengan benar')])
    alamat = TextAreaField('Alamat ', validators=[InputRequired('Tulis alamat dengan benar.')])
    simpan = SubmitField('Simpan')

semua_kontak = []

class Manage:
    def tambah_kontak(data):
        semua_kontak.append(data)

    def tampil_kontak():
        return semua_kontak