from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class Form(FlaskForm):
    email = StringField("", validators=[InputRequired('Email harus diisi!'), Email('Email tidak ditulis dengan benar!')])
    password = PasswordField("", validators=[InputRequired('Password harus diisi..!!'), Length(min=8, message='Password minimal 8 karakter.')])
    login = SubmitField('Login')