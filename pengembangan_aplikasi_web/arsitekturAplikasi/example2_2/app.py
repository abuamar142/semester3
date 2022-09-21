from flask import Flask
from models import model22

application = Flask(__name__)

@application.route('/')
def index():
    # membuat objek dari model22
    model = model22()

    # mengembalikan nilai yang diambil dari model
    return model.getText()

if __name__ == '__main__':
    application.run(debug=True)