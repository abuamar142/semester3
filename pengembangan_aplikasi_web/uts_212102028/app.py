from flask import Flask, render_template
from models import TabelProduk

application = Flask(__name__)

@application.route('/')
def index():
    model = TabelProduk()
    container = []
    container = model.tampilProduk()
    return render_template('tampil_produk.html', container=container)

if __name__ == '__main__':
    application.run(debug=True)