from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    today = datetime.datetime
    return render_template('dashboard.html', today = today)

if __name__ == '__main__':
    app.run(debug=True)