from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    # list dengan elemen bertipe tuple
    navigasi = [
        ('/home', 'Home'),
        ('/profile', 'Profile'),
        ('/product', 'Product'),
        ('/contact', 'Contact')
    ]
    return render_template('index.html', navigasi = navigasi)

@application.route('/home')
def home():
    return '<h2>Home</h2>';

@application.route('/profile')
def profile():
    return '<h2>Profile</h2>';

@application.route('/product')
def product():
    return '<h2>Product</h2>';

@application.route('/contact')
def contact():
    return '<h2>Contact</h2>';

if __name__ == '__main__':
    application.run(debug=True)
