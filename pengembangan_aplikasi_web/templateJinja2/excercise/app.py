import re
from flask import Flask, render_template, request, redirect
from models import Transaksi
import datetime

now = datetime.datetime.now()
today = now.strftime("%A, %d %B %Y")

application = Flask(__name__)

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
    if request.method  == 'POST':
        keterangan = request.form['keterangan']
        nominal = request.form['nominal']
        tanggal = request.form['tanggal']
        jenis = request.form['jenisTransaksi']

        if keterangan != "" and nominal != "" and tanggal != "" and jenis != "":
            try:
                nominal = int(request.form['nominal'])
            except:
                return render_template('tambah.html', integer = True)

            transaksi = Transaksi(keterangan, nominal, tanggal, jenis)
            transaksi.addTransaksi()
            return redirect('/')
            
        else:
            return render_template('tambah.html', empty = True)

    return render_template('tambah.html')

if __name__ == '__main__':
    application.run(debug=True)