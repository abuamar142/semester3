from flask import Flask, render_template, request
from models import Kontak, Manage

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'

@application.route('/', methods=['GET', 'POST'])
def index():
    form = Kontak()
    atur = Manage
    if request.method == 'POST':
        if form.validate():
            nama = form.nama.data
            nomor_telepon = form.nomor_telepon.data
            email = form.email.data
            alamat = form.alamat.data
            data = [nama, nomor_telepon, email, alamat]
            atur.tambah_kontak(data)
            tampil_kontak = enumerate(atur.tampil_kontak())
            return render_template('response.html', tampil_kontak=tampil_kontak)

        else:
            # mengambil daftar kesalahan yang muncul pada saat proses validasi
            errors = form.errors.items()
            return render_template('form.html', form=form, errors=errors)

    return render_template('form.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)