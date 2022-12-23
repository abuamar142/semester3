from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from datetime import datetime
from models import Postingan
import os

model = Postingan()

application = Flask(__name__)
application.config['SECRET_KEY'] = "1234567890!@#$%^&*()"
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/uploads'
application.config['MAX_CONTENT_PATH'] = 10000000

def check_session():
    if 'name' not in session:
        return redirect(url_for('login'))

def session_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

@application.before_request
def before_request():
    check_session()

@application.route('/')
@application.before_request
def index():
    nama = session['nama']
    data = model.getImageName(session['user_id'])
    if session.get('pesan') == 'postBerhasil':
        session.pop('pesan', '')
        return render_template('index.html', nama=nama, data=data, berhasil=True)
    return render_template('index.html', nama=nama, data=data)

@application.route('/login', methods=['GET', 'POST'])
@application.before_request
def login():
    if 'nama' in session:
        nama = session['nama']
        return render_template('index.html', nama=nama)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != "" and password != "":
            try:
                data = (username, password)
                data = model.getUserbyUsernameandPassword(data)
                nama = data[1]
                user_id = data[0]
                session['nama'] = nama
                session['user_id'] = user_id
                return redirect(url_for('index'))
            except:
                flash('Password atau username yang anda masukkan salah', category='danger')
        else:
            flash('Form tidak boleh kosong',category='warning')
    if session.get('pesan') == 'registerBerhasil':
        session.pop('pesan', '')
        flash('Register berhasil', category='success')
    return render_template('login.html')

@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']
        if nama != "" and username != "" and password != "":
            if len(nama) > 3 and len(username) > 3 and len(password) > 3:
                data = (username, password)
                if model.getUserbyUsernameandPassword(data) == None:
                    data = (nama, username, password)
                    model.insertUser(data)
                    session['pesan'] = 'registerBerhasil'
                    return redirect(url_for('index'))
                return render_template('register.html', sudahAda=True)
            else:
                return render_template('register.html', kurang=True)
        else:
            return render_template('register.html', kosong=True)


    return render_template('register.html')

@application.route('/logout')
def logout():
    session.pop('nama', '')
    session.pop('user_id', '')
    return redirect(url_for('login'))

@application.route('/add_status', methods=['GET', 'POST'])
def add_status():
    if 'nama' in session:
        if request.method == 'POST':
            user_id = session['user_id']
            today = datetime.now().strftime('%Y-%m-%d')
            caption = request.form['caption']
            file = request.files['file_photo']
            jumlah_post_id = model.getCountPostIdinDatabase()
            filename = application.config['UPLOAD_FOLDER'] + '/feed_' + str(jumlah_post_id)
            if caption != "":
                try:
                    file.save(filename)
                    filename = 'feed_' + str(jumlah_post_id)
                    data = (user_id, today, caption, filename)
                    model.insertPost(data)
                    session['pesan'] = 'postBerhasil'
                    return redirect(url_for('index'))
                except:
                    return render_template('add_status.html', gagal=True)
            else:
                return render_template('add_status.html', kosong=True)    
        return render_template('add_status.html')    
    return redirect(url_for('login'))

if __name__ == '__main__':
    application.run(debug=True)
