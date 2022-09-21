from flask import Flask, render_template
from models import model22

application = Flask(__name__)

@application.route('/')
def index():
    # membuat objek dari kelas model22
    model = model22()

    # mengirimkan model ke view
    return render_template('hello.html', model = model)

if __name__ == '__main__':
    application.run(debug=True)