from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    a = 20
    b = 30
    c = 20

    # mengirimkan nilai ke template
    return render_template('index.html', a = a, b = b, c = c)

if __name__ == '__main__':
    application.run(debug=True)