from flask import Flask, render_template, request
from models import Form

application = Flask(__name__)
application.config['SECRET_KEY'] = '@#123456&*()'

@application.route('/', methods=['GET', 'POST'])
def index():
    form = Form()
    email = form.email.data
    password = form.password.data
    if request.method == 'POST':
        return render_template('response.html')
        # if form.validate():
        #     if email == 'admin@gmail.com' and password == 'adminaja':
        #         return render_template('response.html')
        #     else:
        #         return render_template('form.html',form=form , salah=True)
        # else:
        #     errors = form.errors.items()
        #     return render_template('form.html', form=form, errors=errors)
    
    return render_template('form.html', form=form)

if __name__ == '__main__':
    application.run(debug=True)