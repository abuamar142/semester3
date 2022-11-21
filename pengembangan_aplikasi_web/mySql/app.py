from flask import Flask, render_template, request, redirect, url_for
from models import BukuTelepon

application = Flask(__name__)

@application.route('/')
def index():
    model = BukuTelepon()
    container = []
    container = model.selectDatabase()
    return render_template('index.html', container=enumerate(container))

@application.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        nama = request.form['nama']
        no_telp = request.form['no_telp']
        if len(nama) <= 3:
            return render_template('insert_form.html', errorNama=True)
        elif len(no_telp) <= 11:
            return render_template('insert_form.html', errorNo=True)
        else:
            data = (nama, no_telp)
            model = BukuTelepon()
            model.insertDatabase(data)
            return redirect(url_for('index'))
    else:
        return render_template('insert_form.html')

@application.route('/update/<no>')
def update(no):
    model = BukuTelepon()
    data = model.getDatabasebyNo(no)
    return render_template('update_form.html', data=data)

@application.route('/update_process', methods=['GET', 'POST'])
def update_process():
    no = request.form['no']
    nama = request.form['nama']
    no_telp = request.form['no_telp']
    model = BukuTelepon()
    data = model.getDatabasebyNo(no)
    if len(nama) <= 3:
        return render_template('update_form.html', data=data, errorNama=True)
    elif len(no_telp) <= 11:
        return render_template('update_form.html', data=data, errorNo=True)
    else:
        data = (nama, no_telp, no)
        model = BukuTelepon()
        model.updateDatabase(data)
        return redirect(url_for('index'))

@application.route('/delete/<no>')
def delete(no):
    model = BukuTelepon()
    model.deleteDatabase(no)
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)