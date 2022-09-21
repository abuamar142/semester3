from flask import Flask, render_template, url_for, request, redirect
from models import item

app = Flask(__name__)

nama = ""
nim = ""
prodi = ""

# membuat objek dari class item
model = item()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        prodi = request.form['prodi']

        if nama != "" and nim != "" and prodi != "":

            # mengisi nilai kedalam model
            model.setNama(nama)
            model.setNim(nim)
            model.setProdi(prodi)

            return redirect('/card')

    return render_template('form.html')

@app.route('/card')
def index():
    # mengirim nilai ke view
    return render_template('index.html',
                            nama = model.getNama(),
                            nim = model.getNim(),
                            prodi = model.getProdi()
                            )

if __name__ == '__main__':
    app.run(debug=True)