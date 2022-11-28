from flask import Flask, render_template, request, redirect, url_for, session
from models import MPengguna

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890'

@application.route('/')
def index():
    if 'username' in session:
        username = session['username']
        password = session['password']
        pengguna = MPengguna()
        data = pengguna.getDatabase(username, password)
        nama = data[1]
        role = data[4]
        if role == 'admin':
            data = pengguna.getDatabaseUser()
            return render_template('welcome.html', nama=nama, role=role, admin=True, data=data)
        else:
            return render_template('welcome.html', nama=nama, role=role)
            
    return render_template('index.html')

@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        data = (nama, username, password, role)
        if nama != '' and username != '' and password != '' and role != '':
            pengguna = MPengguna()
            pengguna.insertData(data)
            return render_template('index.html', berhasil=True, nama=nama)
        else:
            return render_template('register.html', kurang=True)
    else:
        return render_template('register.html')

@application.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        username = session['username']
        password = session['password']
        pengguna = MPengguna()
        data = pengguna.getDatabase(username, password)
        nama = data[1]
        role = data[4]
        if role == 'admin':
            data = pengguna.getDatabaseUser()
            return render_template('welcome.html', nama=nama, role=role, admin=True, data=data)
        else:
            return render_template('welcome.html', nama=nama, role=role)
           
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != '' and password != '':
            pengguna = MPengguna()
            data = pengguna.getDatabase(username, password)
            if pengguna.authenticate(username, password):
                session['username'] = username
                session['password'] = password
                nama = data[1]
                role = data[4]
                if role == 'admin':
                    data = pengguna.getDatabaseUser()
                    return render_template('welcome.html', nama=nama, role=role, admin=True, data=data)
                else:
                    return render_template('welcome.html', nama=nama, role=role)
            else:
                return render_template('login.html', tidak_ada=True)
        else:
            return render_template('login.html', kurang=True)
    return render_template('login.html')

@application.route('/logout')
def logout():
    session.pop('username')
    session.pop('password')
    return redirect(url_for('index'))

@application.route('/delete/<no>')
def delete(no):
    pengguna = MPengguna()
    pengguna.deleteDatabase(no)
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)