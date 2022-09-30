from flask import Flask, render_template, url_for, request, redirect, flash
from models import item

app = Flask(__name__)

# membuat objek dari class item
model = item()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        prodi = request.form['prodi']
        gender = request.form['gridRadios']

        if nama != "" and nim != "" and prodi != "":

            # mengisi nilai kedalam model
            model.setNama(nama)
            model.setNim(nim)
            model.setProdi(prodi)
            model.setGender(gender)

            return redirect('/card')
        else:
            return render_template('form.html', warning = True)

    return render_template('form.html')

@app.route('/card')
def card():
    # mengirim nilai ke view
    return render_template('card.html',
                            nama = model.getNama(),
                            nim = model.getNim(),
                            prodi = model.getProdi(),
                            gender = model.getGender()
                            )

if __name__ == '__main__':
    app.run(debug=True)