from flask import Flask, render_template
from models import BukuTelepon

application = Flask(__name__)

@application.route('/')
def index():
    model = BukuTelepon()
    container = []
    container = model.selectDatabase()
    return render_template('index.html', container=container)

if __name__ == '__main__':
    application.run(debug=True)