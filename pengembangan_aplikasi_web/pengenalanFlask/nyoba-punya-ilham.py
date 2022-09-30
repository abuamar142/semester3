from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    html = """
    <style>
        * {
            font-family: 'Times New Roman', Times, serif;
    }
    th, td {
      border: 1px solid black;
      padding: 8px;  
    }
    </style>
    <h2 style="margin: 0 auto; text-align: center;">Pemain Top Klasemen Liga Indonesia</h2>
    <br/>
    <div style="margin: 0 auto; width: 80%">
    <table style="width: 100%; border-collapse: collapse;">
        <tr>
            <th>Nama</th>
            <th>Profil</th>
            <th>Klub</th>
        </tr>
        <tr>
            <th>Matheus Pato</th>
            <th>Matheus Antonio Souza dos Santos, <a href="/pemain/matheus">selengkapnya.</a></th>
            <th><a href="/klub/borneo">Borneo FC</a></th>
        </tr>
        <tr>
            <th>David da Silva</th>
            <th>David Aparecido da Silva, <a href="/pemain/david">selegkapnya.</a></th>
            <th><a href="/klub/persib">Persib Bandung</a></th>
        </tr>
        <tr>
            <th>Lulinha</th>
            <th>Luiz Marcelo Morais dos Reis, <a href="/pemain/lulinha">selengkapnya.</a></th>
            <th><a href="/klub/madura">Madura United</a></th>
        </tr>
    </table>
    </div>
    """
    return html

@application.route('/pemain/<nama>')
def profile(nama):
    if nama == 'matheus':
        judul = "Matheus Pato"
        deskripsi = "Matheus Antonio Souza dos Santos (lahir 8 Juni 1995), umumnya dikenal sebagai Matheus Pato , adalah pemain sepak bola profesional Brasil yang bermain sebagai penyerang untuk klub Liga 1 Borneo Samarinda."
        klub = 'borneo'
    elif nama == 'david':
        judul = "David da Silva"
        deskripsi = "David Aparecido da Silva (lahir 12 November 1989), umumnya dikenal sebagai David da Silva , adalah pemain sepak bola profesional Brasil yang bermain sebagai striker untuk klub Liga 1 Persib Bandung."
        klub = 'persib'
    elif nama == 'lulinha':
        judul = "Lulinha"
        deskripsi = "Luiz Marcelo Morais dos Reis (lahir 10 April 1990), dikenal sebagai Lulinha , adalah pemain sepak bola profesional Brasil yang bermain sebagai gelandang serang atau pemain sayap untuk klub Indonesia Madura United."
        klub = 'madura'
    else:
        return '<p>Klub tidak ditemukan.</p>'
    html = f"""
    <h3>{judul}</h3>
    <p>{deskripsi}</p>
    <p><a href="/">Kembali</a> | <a href="/klub/{klub}">Klub</a></p>
    """
    return html

@application.route('/klub/<nama>')
def klub(nama):
    if nama == 'borneo':
        judul = "Borneo FC"
        deskripsi = "Borneo Football Club Samarinda (umumnya dikenal sebagai Borneo Samarinda) adalah sebuah klub sepak bola Indonesia yang berbasis di Samarinda, Kalimantan Timur, Indonesia. Mereka saat ini berlaga di Liga 1. Julukan mereka adalah Pesut Etam (Lumba-lumba Kita)."
        profil = 'matheus'
    elif nama == 'persib':
        judul = "Persib Bandung"
        deskripsi = "Persatuan Sepakbola Indonesia Bandung (secara harfiah berarti Persatuan Sepak Bola Indonesia Bandung), biasa disebut Persib Bandung, atau hanya Persib, adalah klub sepak bola profesional yang berbasis di Bandung, Jawa Barat, yang berkompetisi di Liga 1, kasta teratas sepak bola Indonesia. Didirikan pada tahun 1923 sebagai Bandoeng Inlandsche Voetbal Bond (BIVB), itu mengadopsi nama saat ini pada tahun 1933. Persib adalah salah satu klub paling sukses di Indonesia, setelah memenangkan lima gelar Perserikatan dan dua gelar Liga Indonesia. Pangkalan tim berada di Stadion Gelora Bandung Lautan Api dengan kapasitas lebih dari 38.000. Julukan tim termasuk Maung Bandung (Harimau Bandung) dan Pangeran Biru (Pangeran Biru)."
        profil = 'david'
    elif nama == 'madura':
        judul = "Madura United"
        deskripsi = "Madura United Football Club adalah sebuah klub sepak bola profesional Indonesia. Klub ini berbasis di Pamekasan, Madura, Jawa Timur. Mereka saat ini bermain di Liga 1. Berdiri pada 10 Januari 2016, Madura United FC merupakan salah satu dari sedikit klub profesional yang berhasil mendapatkan lisensi dari AFC (Konfederasi Sepak Bola Asia) selama dua tahun berturut-turut. Madura United FC saat ini bermain di dua stadion; Stadion Gelora Bangkalan dan Stadion Gelora Ratu Pamelangan."
        profil = 'lulinha'
    else:
        return '<p>Pemain tidak ditemukan.</p>'
    html = f"""
    <h3>{judul}</h3>
    <p>{deskripsi}</p>
    <p><a href="/">Kembali</a> | <a href="/pemain/{profil}">Profil</a></p>
    """
    return html

if __name__ == '__main__':
    application.run(debug=True)