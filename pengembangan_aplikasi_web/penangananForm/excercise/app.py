from flask import Flask, render_template, request, redirect
from models import Transaksi, FormData

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'

@application.route('/', methods=['GET', 'POST'])
def index():
    transaksi = Transaksi()
    saldo = 0
    for uang in transaksi.getData():
        if uang['jenis'] == 'masuk':
            saldo += uang['nominal']
        elif uang['jenis'] == 'keluar':
            saldo -= uang['nominal']

    if request.method == 'POST':
        print('satu')
        return render_template('index.html', transaksi=enumerate(transaksi.getData()), saldo=saldo, edit=True)
    else:
        print('dua')
        return render_template('index.html', transaksi=enumerate(transaksi.getData()), saldo=saldo)

@application.route('/add', methods=['GET', 'POST'])
def tambah():
    form = FormData()

    if request.method  == 'POST':
        if form.validate():
            keterangan = form.keterangan.data
            nominal = form.nominal.data
            tanggal = request.form['tanggal']
            jenis = request.form['jenisTransaksi']

            if keterangan != "" and nominal != "" and tanggal != "" and jenis != "":
                try:
                    nominal = int(request.form['nominal'])
                except:
                    return render_template('tambah.html', form=form, integer = True)

                transaksi = Transaksi(keterangan, nominal, tanggal, jenis)
                transaksi.addTransaksi()
                return redirect('/')
                
            else:
                return render_template('tambah.html', form=form, empty = True)
        else:
            errors = form.errors.items()
            return render_template('tambah.html', form=form, errors=errors)

    return render_template('tambah.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)