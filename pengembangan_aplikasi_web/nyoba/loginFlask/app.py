from flask import Flask, request

application = Flask(__name__)

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Amar" and password == "123":
            return "<h2>Login berhasil</h2>"
        else:
            return "<h2>Login Failed</h2>"

    else:
        return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        '''

if __name__ == '__main__':
    application.run(debug=True)