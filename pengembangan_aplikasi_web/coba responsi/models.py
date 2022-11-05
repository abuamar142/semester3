from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class Form(FlaskForm):
    nama = StringField('Nama ', validators=[InputRequired('Nama harus diisi..!!'), length(max=25)])
    nomor_telepon = IntegerField('Nomor Handphone: ', validators=[input_required('Nomor Handphone tidak boleh kosong')])
    email = StringField('Email ', validators=[InputRequired('Email harus diisi..!!'), Email('Email tidak ditulis dengan benar')])
    password = PasswordField('Password ', validators=[InputRequired('Tulis alamat dengan benar.')])
    simpan = SubmitField('Simpan')

class Form(FlaskForm):
    email = StringField("Email ", validators=[InputRequired('Email harus diisi!'), Email('Email tidak ditulis dengan benar!')])
    password = PasswordField("", validators=[InputRequired('Password harus diisi..!!'), Length(min=8, message='Password minimal 8 karakter.')])
    login = SubmitField('Login')

semua_kontak = []

class Manage:
    def tambah_kontak(data):
        semua_kontak.append(data)

    def tampil_kontak():
        return semua_kontak