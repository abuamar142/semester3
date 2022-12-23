from flask import Flask, render_template, request
from datetime import datetime
from models import Cashflow
import os

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/uploads'
# satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000

model = Cashflow()

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keterangan = request.form['keterangan']
        nominal = request.form['nominal']
        file = request.files['file']
        print(keterangan, nominal, file)
        if keterangan != '' and nominal != '':
            try:
                nominal = int(nominal)
                filename = application.config['UPLOAD_FOLDER'] + '/' + 'file_terunggah_' + str(model.getCountDatainDatabase())
                try:
                    file.save(filename)
                    nama_file = 'file_terunggah' +  str(model.getCountDatainDatabase())
                    model.insertPengeluaran(nama_file)
                    data = model.getAllDatainDatabase()
                    return render_template('upload_sukses.html', data=data)
                except:
                    return render_template('upload_gagal.html')
            except:
                return render_template('form.html', bukan_angka=True)
        else:
            return render_template('form.html', kosong=True)
    return render_template('form.html')

if __name__ == '__main__':
    application.run(debug=True)