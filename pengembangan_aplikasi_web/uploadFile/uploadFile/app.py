from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/uploads'

# satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = application.config['UPLOAD_FOLDER'] + '/' + secure_filename(file.filename)
        try:
            file.save(filename)
            return render_template('upload_sukses.html', filename=secure_filename(file.filename))
        except:
            return render_template('upload_gagal.html')
    return render_template('form.html')

if __name__ == '__main__':
    application.run(debug=True)