from flask import Flask, url_for, render_template, request, session

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        session.user_logged_in = True
        return 'Validating a login! U:{} P:{}'.format(request.form['username'], request.form['password'])
    return render_template('login.html', error=error)
