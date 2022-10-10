from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, \
    RadioField, SelectField, BooleanField, SubmitField

class PersonalForm(FlaskForm):
    nama = StringField('Nama: ')
    alamat = TextAreaField('Alamat: ')
    jenisKelamin = RadioField('Jenis Kelamin: ',
        choices=[("p", "Pria"), ("w", "Wanita")]
        )
    agama = SelectField('Agama: ',
        choices=[
            (1, "Islam"),
            (2, "Protestan"),
            (3, "Katolik"),
            (4, "Hindu"),
            (5, "Budha"),
        ])
    hobi1 = BooleanField('Olahraga')
    hobi2 = BooleanField('Membaca')
    hobi3 = BooleanField('Jalan-jalan')
    submit = SubmitField('Kirim')