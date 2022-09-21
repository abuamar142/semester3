from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return "<h2>Hello Guys!</h2><a href='/profile'>Profile</a><p><a href='/coba'>Coba</a></p>";

@application.route('/profile')
def profile():
    return "<h2>Ini adalah Halaman Profil</h2><table><tr><td>Nama</td><td>M. Abu Amar Al Badawi</td></tr><tr><td>NIM</td><td>212102028</td></tr></table><br><a href='/'>Home</a><br><a href='/pengertian-flask'>Pengertian Flask</a>";

@application.route('/pengertian-flask')
def name():
    return "<h2>Penjelasan mengenai <b>Flask</b></h2><p>Flask adalah kerangka kerja aplikasi web bersifat kerangka kerja mikro yang ditulis dalam bahasa pemrograman Python dan menggunakan dependensi Werkzeug dan Jinja2. Aplikasi yang menggunakan Flask antara lain adalah Pinterest, LinkedIn, dan halaman web komunitas situs Flask itu sendiri. Flask disebut kerangka kerja mikro karena tidak membutuhkan alat-alat tertentu atau pustaka. Flask mendukung ekstensi yang dapat menambahkan fitur aplikasi seolah-olah mereka diimplementasikan dalam Flask itu sendiri. Ekstensi yang ada seperti pemetaan objek-relasional, validasi form, penanganan unggahan, berbagai teknologi otentikasi terbuka, lapisan abstraksi basisdata, validasi form, atau komponen lain.<p><br><a href='/'>Home</a><br><a href='/profile'>Profile</a>";

@application.route('/coba')
def coba():
    return render_template('coba.html')

if __name__ == '__main__':
    application.run(debug=True)