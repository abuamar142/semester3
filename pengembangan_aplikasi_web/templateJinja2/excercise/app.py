from flask import Flask, render_template
from models import Transaksi

transaksi = Transaksi

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/add')
def tambah():
    return render_template('tambah.html')

if __name__ == '__main__':
    application.run(debug=True)