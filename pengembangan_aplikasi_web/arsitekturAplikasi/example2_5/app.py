from flask import Flask, render_template
from models import model22

application = Flask(__name__)

content = 'Ini adalah berita baru, akan tetapi dari orang lama'

@application.route('/')
def index():
    # membuat objek dari kelas model22
    model = model22()

    # mengisi nilai ke dalam model
    model.setTitle('Berita Terkini!')
    model.setDate('18 Agustus 2022')
    model.setContent(content)

    # mengirimkan nilai ke view
    return render_template('berita.html', 
                            judul=model.getTitle(), 
                            tanggal=model.getDate(), 
                            isi=model.getContent()
                            )

if __name__ == '__main__':
    application.run(debug=True)
